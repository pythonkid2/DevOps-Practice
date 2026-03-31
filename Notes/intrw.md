# Interview Prep - `matthew-hpa-memory-test`

## 1) 60-second task summary (say this first)

I created a k3s troubleshooting scenario where a Deployment pod crashes due to low memory limits, and an HPA is intentionally misconfigured to use a custom metric that is not exported.  
`setup.sh` creates the broken state, `solution.sh` applies a minimal fix by increasing memory limits, and `grader.py` validates root-cause correctness with anti-gaming checks (for example, limits must still exist and HPA must not be deleted).  
Expected behavior is: after setup grader returns `0`, after solution grader returns `1`.

---

## 2) What each file does and how files are connected

- `Dockerfile`
  - Builds a container with k3s, kubectl, python3, and pydantic.
  - Copies all task scripts to `/tmp`.
  - Normalizes line endings (`sed -i 's/\r$//'`) so scripts run in Linux.
  - Starts k3s in entrypoint.

- `wait_for_k3s.sh`
  - Waits for API server and kube-system/coredns readiness before setup.
  - Prevents race conditions where setup runs before cluster is ready.

- `setup.sh`
  - Creates `autoscale-demo` namespace.
  - Creates broken Deployment `memory-hog-deployment` with too-low memory limit (`64Mi`) and memory-heavy workload.
  - Creates misconfigured HPA `memory-hog-hpa` using non-existent custom metric `custom-metric` with `AverageValue`.
  - Stores metadata in `setup-metadata` ConfigMap for traceability/anti-gaming support.

- `solution.sh`
  - Applies minimal fix: updates only container `resources` (memory request/limit increased).
  - Waits for rollout and checks pod health with bounded loop (avoids infinite waits).
  - Keeps HPA intact (as required by problem).

- `grader.py`
  - Binary scoring only: all checks pass => `1.0`, otherwise `0.0`.
  - Checks deployment exists, limits exist and are high enough, pod is stable, and HPA still exists with expected custom metric config.
  - Prevents shortcut fixes like removing limits or deleting HPA.

- `task.yaml`
  - Prompt for an AI agent.
  - Symptom-based wording (not solution-hint based), with constraints and success criteria.

- `Readme.md`
  - Exact execution order: build, run, exec, wait, setup, solve, grade.

---

## 2b) Line-by-line: each file (logic and purpose)

Below is a line-by-line walkthrough you can use in an interview when asked “what does this line do?”

### `Dockerfile`

| Line(s) | What it does | Logic / why |
|--------|----------------|-------------|
| 1 | `FROM ubuntu:22.04` | Base OS for k3s and tools inside the container. |
| 3–7 | `ARG` for versions | Pins k3s/kubectl versions so builds are reproducible. |
| 9–19 | `apt-get install …` | Installs curl, python, networking tools k3s needs (iptables, socat, etc.). |
| 21 | `pip3 install pydantic pyyaml` | `pydantic` for `GradingResult` in `grader.py`; yaml optional for future use. |
| 23 | `ENV KUBECONFIG=…` | So `kubectl` finds the cluster config without extra flags. |
| 25–30 | `curl` k3s, kubectl, kubeadm | Downloads binaries at build time; fails fast if URL wrong (`-fL`). |
| 32–34 | `COPY` + `sed` + `chmod` | Copies task scripts into `/tmp`; strips Windows `\r` so bash does not break; marks executable. |
| 36–42 | Build `/entrypoint.sh` | Starts `k3s server` in background, waits until `k3s.yaml` exists, then `tail -f` keeps the container process alive. |
| 44 | `ENTRYPOINT` | Container always starts k3s when it runs. |

---

### `wait_for_k3s.sh`

| Line(s) | What it does | Logic / why |
|--------|----------------|-------------|
| 1–2 | Shebang + `set -e` | Run under bash; exit on first error. |
| 4–5 | Loop on `kubectl cluster-info` | Blocks until API server responds. |
| 7–10 | Wait until kube-system has pods | Ensures scheduler/controller started registering pods. |
| 12–13 | `kubectl wait` coredns | Core DNS readiness is enough for this lab; `|| true` avoids hard fail if label differs. |
| 15 | Success message | Human signal that it is safe to run `setup.sh`. |

---

### `setup.sh`

| Line(s) | What it does | Logic / why |
|--------|----------------|-------------|
| 1–2 | Shebang + `set -e` | Fail fast on kubectl errors. |
| 4–6 | Echo banner | Visible section in logs. |
| 8 | `kubectl wait … node … Ready` | Cluster node must be ready before workloads. |
| 10–11 | Create `autoscale-demo` + wait SA | Namespace must exist and default SA ready for pods. |
| 13–16 | Delete old deploy/HPA/configmap | Idempotent: same broken state every run. |
| 18–57 | Heredoc → `kubectl apply` Deployment | Defines `memory-hog-deployment`: Python allocates ~200Mi then sleeps; limit `64Mi` → OOM. |
| 36–49 | Container command/args | Finite allocation loop then idle loop → stable after fix, reproducible crash before fix. |
| 50–56 | `resources` | Low `limits.memory: 64Mi` is the root cause of OOM. |
| 59–81 | Heredoc → HPA | `Pods` metric `custom-metric` + `AverageValue: 100` → metric not exported → `<unknown>/100`. |
| 83–85 | Rollout wait + sleep | Give kubelet time to kill/restart pod and show failure. |
| 87–93 | Read pod name/phase/reason | Prints evidence for debugging (OOM, CrashLoop). |
| 95 | `describe` events | Shows events section (OOMKilled, etc.). |
| 97–104 | `setup-metadata` ConfigMap | Stores UIDs/names for traceability; grader could extend anti-gaming here. |
| 106–109 | Footer | Setup finished. |

---

### `solution.sh`

| Line(s) | What it does | Logic / why |
|--------|----------------|-------------|
| 1–2 | Shebang + `set -e` | Fail fast. |
| 4–6 | Banner | Log section. |
| 8–24 | `kubectl patch --type json` | **JSON patch `add` on `containers[0].resources`** only—does not wipe `image`/`command` (merge patch would). |
| 14–21 | New requests/limits | Raises memory so workload fits; keeps limits (anti-gaming). |
| 26–27 | `rollout status` | Waits for new ReplicaSet; `|| true` so script continues even if kubectl quirk. |
| 29–54 | Loop over pods | Bounded wait: finds `app=memory-hog` pod, checks `Running`, low restarts, not `CrashLoopBackOff`. |
| 48–50 | Health condition | “Healthy enough” for automation without hanging forever. |
| 56–60 | Failure branch | If still unhealthy, print pods and `exit 1`. |
| 62–67 | Success + `kubectl get` | Shows Deployment and HPA still exist (HPA unchanged). |

---

### `grader.py`

| Line(s) | What it does | Logic / why |
|--------|----------------|-------------|
| 1–5 | Imports | `json` for API output; `subprocess` for `kubectl`; `typing` for clarity. |
| 7 | `pydantic` | `GradingResult` schema (score + feedback). |
| 10–12 | `GradingResult` | Standard return shape for automation. |
| 15–20 | `run_cmd` | Wraps `kubectl` with timeout; returns stdout/stderr/rc. |
| 23–33 | `get_resource` | `kubectl get … -o json` → dict or `None` if missing. |
| 36–40 | `check_deployment_exists` | Fails if someone deleted the Deployment. |
| 43–76 | `check_deployment_limits…` | Finds container `memory-hog`; requires `limits.memory`; parses `Mi`/`Gi`; must be ≥ 128Mi → blocks “remove limits” cheat. |
| 79–114 | `check_pod_running…` | Lists pods by label; first pod must be `Running`, restartCount ≤ 3, not `CrashLoopBackOff`. |
| 117–135 | `check_hpa_exists…` | HPA must exist; must still have `Pods` metric named `custom-metric` and `AverageValue` → cannot “fix” HPA by deleting metric. |
| 138–157 | `grade` | Runs all checks; any fail → score `0.0` + list failed names; all pass → `1.0`. |
| 160–166 | `__main__` | Optional transcript arg; prints score; exit `0` only if `1.0` (shell-friendly for CI). |

---

### `task.yaml`

| Line(s) | What it does | Logic / why |
|--------|----------------|-------------|
| 1 | `id` | Stable task identifier for agents/registry. |
| 2–22 | `prompt:` block | **Symptoms + success criteria + constraints** without naming the exact fix (increase memory). |
| 12–15 | Success bullets | Aligns with grader: Running pods, limits kept, HPA + custom metric preserved. |
| 17–22 | IMPORTANT | Anti-cheat rules for the agent (no delete, no strip limits, no renames). |
| 24–26 | `metadata` | Category and difficulty for routing. |

---

### `Readme.md`

| Line(s) | What it does | Logic / why |
|--------|----------------|-------------|
| 1 | Title `# Solution` | Matches sample style: how to run the lab. |
| 3–8 | Build / run / exec | Exact Docker commands and image name `my-k3s-hpa-memory-env`. |
| 10–20 | Code block | Order: wait → setup → solution → grade (single copy-paste path). |

---

## 3) How I reproduced the issue

I reproduced the issue by creating a Deployment whose container intentionally allocates memory quickly while having a very low memory limit (`64Mi`).  
This causes OOM kills and restart loops (`CrashLoopBackOff` behavior).  
At the same time, I attached an HPA using a non-existent custom metric (`custom-metric`), so HPA target shows `<unknown>/100` and does not scale.

Useful verification commands:

```bash
kubectl get pods -n autoscale-demo
kubectl describe pod <pod-name> -n autoscale-demo
kubectl get hpa memory-hog-hpa -n autoscale-demo
```

---

## 4) If I run `setup.sh`, what output should I expect

Typical output flow:

- Header: `Setting up HPA + memory CrashLoop scenario`
- Namespace creation/cleanup logs
- Deployment and HPA creation logs
- Pod check logs with phase/reason
- Pod events showing OOM/restarts
- Footer: `Setup complete!`

Cluster state after setup:

- Deployment exists (`memory-hog-deployment`)
- HPA exists (`memory-hog-hpa`) with `<unknown>/100`
- Pod repeatedly restarts / OOM behavior
- `python3 /tmp/grader.py` should return `Score: 0.0`

---

## 5) After breaking the cluster, how I created the solution

I used a minimal root-cause fix:

1. Keep same Deployment/HPA names (no delete-and-recreate shortcut).
2. Patch only container resource section to increase memory (`limits.memory` to `512Mi`, `requests.memory` to `128Mi`).
3. Wait for rollout and verify pod stability (`Running`, low restart count, no `CrashLoopBackOff`).
4. Run grader for deterministic pass/fail.

Why minimal fix is important:

- It directly addresses memory-caused crashes.
- It preserves task realism and prevents over-engineering.
- It aligns with prompt constraints and anti-gaming design.

---

## 6) If Docker container has no internet, how to handle

Short answer for interview:

- At **build time**, internet is required to pull base image and binaries (`k3s`, `kubectl`, `kubeadm`).
- At **runtime**, this task does not require external internet once image is built.

Practical options:

1. Use prebuilt image from internal registry.
2. Configure Docker proxy:
   - `HTTP_PROXY`, `HTTPS_PROXY`, `NO_PROXY`.
3. If corporate network blocks GitHub/K8s URLs, mirror binaries internally and update Dockerfile URLs.
4. Use offline strategy:
   - Pre-download binaries and `COPY` them into image.

One-liner response:

I’d solve it by using a prebuilt image or internal mirrors/proxy; runtime task execution itself is cluster-local.

---

## 7) If I delete a pod managed by a Deployment, what happens

The Deployment controller notices desired replicas are not met and automatically creates a new pod.

Good interview add-on:

- If old pod was unhealthy, recreating may temporarily help, but root cause remains unless Deployment spec is fixed.
- In this task, deleting pod alone will not permanently fix low-memory crashes.

---

## 8) Logic used in `grader.py`

Main grading checks:

1. Deployment exists.
2. Container memory limits exist and are above threshold (`>=128Mi`).
3. Pod is running and not repeatedly crashing.
4. HPA still exists and still uses custom metric config (anti-gaming).

Scoring model:

- Any failed check => `score=0.0`
- All checks pass => `score=1.0`

Why this is strong:

- Validates root cause fix, not superficial state.
- Detects cheating (removing limits, deleting HPA).
- Deterministic and repeatable across runs.

---

## 9) If asked: "How would you train an agent to solve this?"

I’d train with a strict troubleshooting workflow:

1. **Observe**
   - `kubectl get pods, deploy, hpa -n autoscale-demo`
   - identify crash symptoms and HPA metric status.
2. **Diagnose**
   - `kubectl describe pod` for OOM evidence.
   - check deployment resource limits.
3. **Fix minimally**
   - patch memory resources only.
4. **Validate**
   - ensure pod stable and `Running`.
   - run grader.
5. **Respect constraints**
   - do not delete HPA/deployment.
   - do not remove limits.
   - use non-interactive commands.

I would encode these rules in `task.yaml` and reinforce with grader anti-gaming checks.

---

## 10) Common interview follow-ups and short answers

- **Why `<unknown>/100` in HPA TARGETS?**  
  Current metric value is unknown because custom metric is not exported; target value is 100.

- **Do we need metrics-server here?**  
  Not for this assignment. HPA is intentionally misconfigured; required fix is memory limit correction.

- **Why keep limits instead of removing them?**  
  Removing limits is a shortcut and unsafe. The task explicitly requires limits to remain.

- **Why binary grading?**  
  It removes ambiguity and makes CI automation simple and deterministic.

---

## 11) Ready-to-say final explanation (30 seconds)

I designed this as a realistic Kubernetes troubleshooting lab: a Deployment crashes from low memory limits while HPA is intentionally tied to a non-existent custom metric.  
Setup reproducibly creates the broken state, solution applies the minimum safe patch to memory resources, and grader enforces correctness plus anti-gaming constraints.  
So we prove diagnosis, fix, and validation end-to-end with deterministic pass/fail behavior.

