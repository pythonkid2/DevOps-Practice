
## 1) 60-second task summary 

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

### `setup.sh` deep dive for lines 35–56 (exact snippet)

This is the container block inside the Deployment spec. You can explain it line by line like this:

- **Line 35**: `containers:`  
  Starts the list of containers for the pod template.

- **Line 36**: `- name: memory-hog`  
  Container name. Used later by grader and patch logic to target the right container.

- **Line 37**: `image: python:3.11-slim`  
  Lightweight Python runtime image. Needed because the workload script is Python.

- **Line 38**: `command: ["python", "-c"]`  
  Tells container to execute inline Python code from args.

- **Line 39**: `args:`  
  Starts argument list for the command.

- **Line 40**: `- |`  
  YAML multiline block starts. Everything below is passed as one Python script string.

- **Line 41**: `import time`  
  Imports `time` module for sleep calls.

- **Line 42**: `data = []`  
  Initializes a list to hold allocated strings and keep memory referenced.

- **Line 43**: `# Allocate ~200Mi over time to exceed the low limit (64Mi)`  
  Comment describing intent: force OOM under low memory limit.

- **Line 44**: `for _ in range(20):`  
  Loop 20 iterations to allocate memory chunks.

- **Line 45**: `data.append("x" * 10_000_000)`  
  Appends ~10MB string each loop; roughly ~200MB total across iterations in CPython object usage context.

- **Line 46**: `time.sleep(0.1)`  
  Small delay so allocation is progressive and observable in pod lifecycle/events.

- **Line 47**: `# After initial spike, stay alive without growing further`  
  Explains why the script can become stable after limits are increased.

- **Line 48**: `while True:`  
  Infinite loop keeps the process alive once initial allocation is done.

- **Line 49**: `time.sleep(10)`  
  Long sleep avoids further memory growth and high CPU usage.

- **Line 50**: `resources:`  
  Starts Kubernetes resource requests/limits block for this container.

- **Line 51**: `requests:`  
  Requested resources for scheduler placement.

- **Line 52**: `cpu: "50m"`  
  Requests 0.05 CPU core.

- **Line 53**: `memory: "32Mi"`  
  Requests 32Mi memory (scheduling hint, not hard cap).

- **Line 54**: `limits:`  
  Hard maximum resource limits enforced by kubelet/container runtime.

- **Line 55**: `cpu: "100m"`  
  CPU hard limit at 0.1 core.

- **Line 56**: `memory: "64Mi"`  
  Hard memory cap set intentionally too low; this is the root cause of OOM/restarts.

Interview one-liner for this block:
This block intentionally creates a deterministic memory-pressure workload and sets a low memory hard limit so the pod crashes before fix, then stays stable after raising limits.

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

### `solution.sh` deep dive for lines 26–60 (rollout wait + health loop)

**Big picture:** After the memory patch, Kubernetes creates a **new** ReplicaSet and replaces pods. This block waits for that rollout, then **polls** the pod until it looks “good enough” without hanging forever like `kubectl wait --for=condition=Ready` can when the pod keeps crashing.

**Line by line:**

- **26–27** `kubectl rollout status … || true`  
  Waits until the Deployment reports the new revision is applied. `|| true` means: if `rollout status` returns non-zero (timeout, transient API glitch), the script **still continues** to the health loop instead of exiting immediately. You still get a final pass/fail from the loop below.

- **29** `echo "Waiting for a healthy pod..."`  
  Log line for humans and demos.

- **30–31** `ATTEMPTS=30` and `SLEEP_SECONDS=5`  
  Bounded polling: up to **30 × 5s ≈ 150 seconds** max wait. Prevents infinite hang.

- **33** `for i in $(seq 1 "$ATTEMPTS"); do`  
  Repeat up to 30 times.

- **34** `POD_JSON=…`  
  Fetches full pod list JSON (optional for debugging; not strictly required for logic).

- **35** `POD_NAME=… jsonpath='{.items[0].metadata.name}'`  
  Picks the **first** pod matching label `app=memory-hog`. During rollout you might briefly see zero pods or a terminating pod; this line gets whatever exists now.

- **36–40** `if [ -z "$POD_NAME" ]; then … continue`  
  If no pod exists yet (scheduler delay), sleep and retry. Avoids failing on empty selection.

- **42–44** Read `PHASE`, `RESTARTS`, `WAITING_REASON`  
  - `PHASE`: Kubernetes pod lifecycle phase (`Pending`, `Running`, etc.).  
  - `RESTARTS`: container restart counter (OOM/crash evidence).  
  - `WAITING_REASON`: if container is in `waiting` state, reason like `CrashLoopBackOff`.

- **46** Echo one line summary  
  Makes live debugging easy during interview.

- **48–51** Health condition + `break`  
  Success if:
  - `PHASE` is **`Running`**, and  
  - `RESTARTS` **≤ 3** (not stuck in endless crash loop), and  
  - `WAITING_REASON` is **not** `CrashLoopBackOff`  
  Then print “Pod is healthy.” and exit the `for` loop.

- **53** `sleep` between attempts  
  Avoid hammering API server; gives kubelet time to stabilize pod.

- **56–60** Final validation after loop  
  If after all attempts the last seen state is still bad (`PHASE` not `Running`, or too many restarts, or `CrashLoopBackOff`), print pods and **`exit 1`**. This makes automation deterministic: script fails loudly instead of hanging.

**Interview explanation (one paragraph):**  
Rollout status tells us the Deployment accepted the new spec, but the pod can still be crashing. So we use a bounded polling loop that inspects actual pod phase, restart count, and waiting reason—this is more reliable than a single `kubectl wait` when workloads were previously unhealthy.

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

### `grader.py` — deep explanation (no coding background needed)

**What this file is (one sentence):**  
It is a small Python program that runs **`kubectl` commands for you**, reads the answers Kubernetes returns, and decides **pass (1.0) or fail (0.0)** using a fixed checklist.

**Why Python + `kubectl`?**  
You could grade by hand with `kubectl get`, but a script makes grading **automatic, repeatable, and fair** for CI or batch runs.

**Flow in plain English:**

1. Start the script (`python3 /tmp/grader.py`).
2. Run **four checks in order** (deployment exists → limits OK → pod healthy → HPA OK).
3. Print `PASS` or `FAIL` for each check with a short reason.
4. If **any** check fails → final score **`0.0`** and exit code **`1`** (failure).
5. If **all** checks pass → final score **`1.0`** and exit code **`0`** (success).

**Pieces of the code (what each part means):**

- **`GradingResult` (lines 10–12)**  
  A simple “result object”: a number `score` (0.0 or 1.0) and optional text `feedback`. Think of it like a form: “score + comment”.

- **`run_cmd` (lines 15–20)**  
  Runs a shell command (here, always `kubectl …`) and captures:
  - printed output (stdout),
  - errors (stderr),
  - success/failure code (return code).  
  Has a **30 second timeout** so a stuck command does not hang forever.

- **`get_resource` (lines 23–33)**  
  Asks Kubernetes: “give me this object as JSON” (`kubectl get deployment … -o json`).  
  If the object does not exist or command fails, it returns “nothing” (`None`).  
  JSON is just a structured text format; Python turns it into a dictionary so we can read fields like memory limits.

- **Check 1 — `check_deployment_exists` (lines 36–40)**  
  Question: Does `memory-hog-deployment` exist in `autoscale-demo`?  
  If someone deleted the Deployment to cheat, this fails.

- **Check 2 — `check_deployment_limits_present_and_high_enough` (lines 43–76)**  
  Questions:
  - Does the container named `memory-hog` have **`limits.memory`** set?  
    (If limits are removed, that is an invalid “fix”.)
  - Is the limit at least **128Mi**?  
    This matches the assignment idea: memory must be raised to a **reasonable** value, not left as the broken low limit.  
  Small helper `to_mebibytes` converts strings like `512Mi` or `1Gi` into a number for comparison.

- **Check 3 — `check_pod_running_and_not_crashing` (lines 79–114)**  
  Questions:
  - Is there a pod with label `app=memory-hog`?
  - Is pod phase **`Running`**?
  - Is **restart count** not too high (≤ 3)?
  - Is it **not** stuck in **`CrashLoopBackOff`**?  
  This checks “real health”, not only that YAML exists.

- **Check 4 — `check_hpa_exists_and_uses_custom_metric` (lines 117–135)**  
  Questions:
  - Does HPA `memory-hog-hpa` still exist? (Cannot delete HPA to pass.)
  - Does it still use the **Pods** metric named **`custom-metric`** with **`AverageValue`**?  
  So the “misconfigured HPA” part of the task stays intact; you fix memory, not by deleting the HPA.

- **`grade` (lines 138–157)**  
  Runs the four checks in a list. Collects names of failed checks.  
  Returns **0.0** if any failed, **1.0** if none failed.

- **`if __name__ == "__main__"` (lines 160–166)**  
  “When you run this file directly…”  
  Calls `grade()`, prints score and feedback, and sets **process exit code**:  
  - `0` = pass (automation tools treat as success)  
  - `1` = fail  

**What to say in an interview (30 seconds):**  
The grader automates kubectl inspection: it verifies the Deployment still exists with proper memory limits, the pod is actually running and stable, and the HPA was not removed or “fixed away”. Scoring is binary so the outcome is unambiguous for pipelines.

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

---

## 12) Quick troubleshooting playbook (what to do if demo fails live)

Use this if an interviewer asks you to debug in real time:

1. Check cluster and namespace:
   - `kubectl get ns`
   - `kubectl get all -n autoscale-demo`
2. Verify pod failure reason:
   - `kubectl get pods -n autoscale-demo`
   - `kubectl describe pod <pod> -n autoscale-demo`
3. Validate deployment resources:
   - `kubectl get deploy memory-hog-deployment -n autoscale-demo -o yaml`
4. Verify HPA status:
   - `kubectl get hpa memory-hog-hpa -n autoscale-demo`
   - Explain `<unknown>/100` as missing custom metric value.
5. Re-apply deterministic flow:
   - `/tmp/setup.sh`
   - `/tmp/solution.sh`
   - `python3 /tmp/grader.py`

---

## 13) Design decisions and why they are good

- **Why Deployment instead of Pod**
  - Requirement explicitly asks pod to be part of Deployment.
  - Lets interviewer test controller behavior (replace failed/deleted pods).

- **Why custom metric in HPA**
  - Matches task requirement: misconfigured custom metric (`AverageValue`) not exported.
  - Produces realistic `TARGETS <unknown>/100`.

- **Why finite memory spike in setup workload**
  - Before fix: low limit causes deterministic OOM/restarts.
  - After fix: pod can stabilize instead of eventually crashing forever.

- **Why JSON patch in solution**
  - Touches only `resources` and avoids accidental replacement of required fields like `image`.
  - Keeps fix minimal and production-safe.

- **Why anti-gaming checks in grader**
  - Prevents fake fixes (remove limits, delete HPA, delete workload).
  - Ensures the root cause is actually addressed.

---

## 14) Common mistakes to avoid (say these proactively)

1. Do not delete HPA to hide `<unknown>` metric target.
2. Do not remove resource limits from Deployment (grader fails).
3. Do not patch whole container spec with merge patch unless all required fields are included.
4. Do not trust a single `Running` check; verify restartCount and waiting reason.
5. Do not skip `wait_for_k3s.sh`; setup can fail due to startup race conditions.

---

## 15) Rapid-fire command cheat sheet

```bash
# Cluster readiness
/tmp/wait_for_k3s.sh

# Broken state
/tmp/setup.sh
kubectl get pods -n autoscale-demo
kubectl get hpa -n autoscale-demo

# Root-cause inspection
kubectl describe pod -n autoscale-demo -l app=memory-hog
kubectl get deploy memory-hog-deployment -n autoscale-demo -o yaml

# Apply fix + validate
/tmp/solution.sh
python3 /tmp/grader.py
```

---

## 16) Final 15-second answer if interviewer asks “Why should we trust your solution?”

Because it is deterministic, minimal, and testable: setup always reproduces the same crash pattern, solution only adjusts memory resources without breaking constraints, and grader enforces root-cause correction with anti-gaming checks, yielding binary pass/fail.

