--
alertmanager:
  enabled: true
  replicaCount: 1
  statefulSet:
    enabled: true
  persistentVolume:
    enabled: true
    existingClaim: alertmanager-pvc
    accessModes:
      - ReadWriteOnce
    size: 5Gi
    storageClass: manual

server:
  replicaCount: 1
  statefulSet:
    enabled: false
  persistentVolume:
    enabled: false

pv.yml

apiVersion: v1
kind: PersistentVolume
metadata:
  name: prometheus-alertmanager-pv
spec:
  capacity:
    storage: 5Gi
  accessModes:
    - ReadWriteOnce
  persistentVolumeReclaimPolicy: Retain
  storageClassName: ""
  hostPath:
    path: "/mnt/data/prometheus-alertmanager"


    ====

sudo apt update
    2  sudo snap install aws-cli --classic
    3  aws --version
    4  aws configure
    5  sudo snap install terraform --classic
    6  mkdir eks
    7  cd eks
    8  vi main.tf
    9  vi variables.tf
   10  vi output.tf
   11  terraform init
   12  terraform plan
   13  terraform apply
   14  sudo apt-get update
   15  sudo apt-get install -y apt-transport-https ca-certificates curl gnupg
   16  curl -fsSL https://pkgs.k8s.io/core:/stable:/v1.32/deb/Release.key | sudo gpg --dearmor -o /etc/apt/keyrings/kubernetes-apt-keyring.gpg
   17  sudo chmod 644 /etc/apt/keyrings/kubernetes-apt-keyring.gpg # allow unprivileged APT programs to read this keyring
   18  echo 'deb [signed-by=/etc/apt/keyrings/kubernetes-apt-keyring.gpg] https://pkgs.k8s.io/core:/stable:/v1.32/deb/ /' | sudo tee /etc/apt/sources.list.d/kubernetes.list
   19  sudo chmod 644 /etc/apt/sources.list.d/kubernetes.list   # helps tools such as command-not-found to work correctly
   20  sudo apt-get update
   21  sudo apt-get install -y kubectl
   22  kubectl cluster-info
   23  kubectl version --client
   24  aws eks --region us-east-2 update-kubeconfig --name mega_project-cluster
   25  kubectl get pods
   26  kubectl get nodes
   27  kubectl create namespace app-1
   28  vi app-1.yml
   29  kubectl apply -f app-1.yml -n app-1
   30  kubectl get all -n app-1
   31  curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3
   32  chmod 700 get_helm.sh
   33  ./get_helm.sh
   34  helm version
   35  vi values.yml
   36  cd .. && mkdir monitor && cd monitor
   37  vi values.yml
   38  vi pv.yml
   39  kubectl create ns monitoring 
   40  kubectl apply -f pv.yml -n monitoring 
   41  vi pv.yml
   42  kubectl apply -f pv.yml -n monitoring
   43  cat pv.yml 
   44  vi pv.yml 
   45  kubectl apply -f pv.yml -n monitoring
   46  helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
   47  helm repo update
   48  helm install prometheus prometheus-community/prometheus \ 
   49  --namespace monitoring --create-namespace -f values.yml
   50  helm install prometheus prometheus-community/prometheus \ 
   51  --namespace monitoring --create-namespace -f values.yml
   52  kubects get po -n monitoring
   53  kubectl get po -n monitoring
   54  helm install prometheus prometheus-community/prometheus --namespace monitoring --dry-run -f values.yml
   55  ls
   56  helm install prometheus prometheus-community/prometheus  --namespace monitoring --create-namespace -f values.yml
   57  cd ..
   58  ls
   59  cd eks/
   60  ls
   61  terraform destroy --auto-aprove
   62  terraform destroy
   63  sudo shutdown -h now
   64  SUDO APT UPDATE 
   65  sudo apt update
   66  ls
   67  cd eks/
   68  ls
   69  terraform apply
   70  kubectl get all
   71  aws eks --region us-east-2 update-kubeconfig --name mega_project-cluster
   72  kubectl get nodes
   73  ls
   74  cd ..
   75  ls
   76  cd monitor/
   77  ls
   78  cat values.yml 
   79  helm version
   80  helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
   81  helm search repo prometheus-community
   82  kubectl create namespace prometheus
   83  kubectl create namespace monitoring
   84  helm install prometheus prometheus-community/prometheus  --namespace monitoring --create-namespace -f values.yml 
   85  ls
   86  helm install prometheus prometheus-community/prometheus  --namespace monitoring --create-namespace -f values.yml 
   87  vi values.yml 
   88  helm install prometheus prometheus-community/prometheus  --namespace monitoring --create-namespace -f values.yml 
   89  kubectl get all
   90  ls
   91  kubectl apply -f pv.yml 
   92  kubectl get all
   93  kubectl get pv
   94  kubectl apply -f pv.yml -n monitoring 
   95  kubectl get pv
   96  cat pv.yml 
   97  kubectl get pv
   98  kubectl delete pv prometheus-alertmanager-pv
   99  kubectl get pv
  100  ls
  101  cat pv.yml && cat values.yml 
  102  kubectl get deamonsets
  103  kubectl get all -n monitoring
  104  alias k = "kubectl"
  105  alias k="kubectl"
  106  k get svc -n monitoring
  107  k edit svc prometheus-server
  108  k edit svc prometheus-server -n monitoring
  109  k get svc -monitoring
  110  k get svc -n monitoring
  111  k edit svc prometheus-server
  112  k edit svc prometheus-server -n monitoring
  113  k get svc prometheus-server -n monitoring -0 yaml
  114  k get svc prometheus-server -n monitoring -o yaml
  115  k edit svc prometheus-server -n monitoring -o yaml
  116  EDITOR=vi k edit svc prometheus-server -n monitoring
  117  EDITOR=vim k edit svc prometheus-server -n monitoring
  118  EDITOR=nano k edit svc prometheus-server -n monitoring
  119  kubectl get svc -n monitoring
  120  EDITOR=nano k edit svc prometheus-server -n monitoring
  121  ls
  122  helm repo add grafana https://grafana.github.io/helm-charts
  123  helm repo update
  124  helm install grafana grafana/grafana --namespace monitoring --create-namespace --set 
  125  adminPassword=admin123
  126  helm install grafana grafana/grafana --namespace monitoring --create-namespace --set adminPassword=admin123
  127  k get svc -n monitoring 
  128  kubectl get svc -n monitoring 
  129  kubectl edit svc grafana -n monitoring
  130  kubectl get svc -n monitoring 
  131  ls
  132  cd ..
  133  ls
  134  cd ubuntu/
  135  ls
  136  cd app
  137  mkdir app
  138  cd app
  139  ls
  140  vi deplo.yml
  141  kubectl create namespace app
  142  kubectl apply -f deplo -n app
  143  kubectl apply -f deplo.yml -n app
  144  ls
  145  helm install blackbox-exporter prometheus-community/prometheus-blackbox-exporter --namespace
  146  helm install blackbox-exporter prometheus-community/prometheus-blackbox-exporter --namespace monitoring --create-namespace
  147  kubectl get svc -n monitoring
  148  kubectl edit svc blackbox-exporter-prometheus-blackbox-exporter
  149  kubectl edit svc blackbox-exporter-prometheus-blackbox-exporter -n monitoring
  150  kubectl get svc -n monitoring
  151  kubectl get pods -n monitoring
  152  kubectl get all  -n monitoring
  153  kubectl get pods -n app
  154  helm repo list
  155  kubectl get pods -n app
  156  kubectl get pods -n monitoring
  157  kubectl get pv -n monitoring
  158  kubectl delete pv prometheus-alertmanager-pv -n monitoring
  159  ls
  160  kubectl get pv -n monitoring
  161  ls
  162  cd monitor/
  163  ls
  164  cat values.yml 
  165  ls
  166  cat pv.yml 
  167  ls
  168  history
