```
mkdir monitoring
cd monitoring
```
## to download prometheus
```
https://prometheus.io/download/
```
```
wget https://github.com/prometheus/prometheus/releases/download/v2.54.0-rc.0/prometheus-2.54.0-rc.0.linux-amd64.tar.gz
```
```
tar -xvf prometheus-2.54.0-rc.0.linux-amd64.tar.gz
```
rm -rf prometheus-2.54.0-rc.0.linux-amd64.tar.gz

cd prometheus-2.54.0-rc.0.linux-amd64/

```
./prometheus &
```
http://ip:9090/

## blackbox_exporter
for website monitoring

tar -xvf blackbox_exporter-0.25.0.linux-amd64.tar.gz

go inside blackbox folder

```./blackbox_exporter &
```
edit yml file 

```vi prometheus.yml
```

go here https://github.com/prometheus/blackbox_exporter
copy paste job edit url 

```
# my global config
global:
  scrape_interval: 15s # Set the scrape interval to every 15 seconds. Default is every 1 minute.
  evaluation_interval: 15s # Evaluate rules every 15 seconds. The default is every 1 minute.
  # scrape_timeout is set to the global default (10s).

# Alertmanager configuration
alerting:
  alertmanagers:
    - static_configs:
        - targets:
          # - alertmanager:9093

# Load rules once and periodically evaluate them according to the global 'evaluation_interval'.
rule_files:
  # - "first_rules.yml"
  # - "second_rules.yml"

# A scrape configuration containing exactly one endpoint to scrape:
# Here it's Prometheus itself.
scrape_configs:
  # The job name is added as a label `job=<job_name>` to any timeseries scraped from this config.
  - job_name: "prometheus"

    # metrics_path defaults to '/metrics'
    # scheme defaults to 'http'.

    static_configs:
      - targets: ["localhost:9090"]
  - job_name: 'blackbox'
    metrics_path: /probe
    params:
      module: [http_2xx]  # Look for a HTTP 200 response.
    static_configs:
      - targets:
        - http://prometheus.io    # Target to probe with http.
        - http://18.222.225.253:30704 # Target to probe with http on port 8080.
    relabel_configs:
      - source_labels: [__address__]
        target_label: __param_target
      - source_labels: [__param_target]
        target_label: instance
      - target_label: __address__
        replacement: 3.12.104.74:9115  # The blackbox exporter's real hostname:port.
  - job_name: 'blackbox_exporter'  # collect blackbox exporter's operational metrics.
    static_configs:
      - targets: ['127.0.0.1:9115']

```



## Grafana

```https://grafana.com/grafana/download
```
```
sudo /bin/systemctl start grafana-server
```

add prometheus as data sourse inside grafana
connection -->data sourses -->Add data source --> prometheus

Connection(Prometheus server URL : http://3.12.104.74:9090

import dash board - 7587(search in google)

## System level Monitoring 

install node exportwer on node you want to monitor 

add job

restart prometheus 

ggrep promethus 

kill that id 

rerun

```
# my global config
global:
  scrape_interval: 15s # Set the scrape interval to every 15 seconds. Default is every 1 minute.
  evaluation_interval: 15s # Evaluate rules every 15 seconds. The default is every 1 minute.
  # scrape_timeout is set to the global default (10s).

# Alertmanager configuration
alerting:
  alertmanagers:
    - static_configs:
        - targets:
          # - alertmanager:9093

# Load rules once and periodically evaluate them according to the global 'evaluation_interval'.
rule_files:
  # - "first_rules.yml"
  # - "second_rules.yml"

# A scrape configuration containing exactly one endpoint to scrape:
# Here it's Prometheus itself.
scrape_configs:
  # The job name is added as a label `job=<job_name>` to any timeseries scraped from this config.
  - job_name: "prometheus"

    # metrics_path defaults to '/metrics'
    # scheme defaults to 'http'.

    static_configs:
      - targets: ["localhost:9090"]
  - job_name: 'blackbox'
    metrics_path: /probe
    params:
      module: [http_2xx]  # Look for a HTTP 200 response.
    static_configs:
      - targets:
        - http://prometheus.io    # Target to probe with http.
        - http://18.222.225.253:30704 # Target to probe with http on port 8080.
    relabel_configs:
      - source_labels: [__address__]
        target_label: __param_target
      - source_labels: [__param_target]
        target_label: instance
      - target_label: __address__
        replacement: 3.12.104.74:9115  # The blackbox exporter's real hostname:port.
  - job_name: 'blackbox_exporter'  # collect blackbox exporter's operational metrics.
    static_configs:
      - targets: ['127.0.0.1:9115']
  - job_name: 'node-exporter'  # collect blackbox exporter's operational metrics.
    static_configs:
      - targets: ['18.116.100.0:9100']

```




+++ with jenkins 

go to jenkins install prometheus matrix plugin 

restart the server




manage jenkins --> system --> prometheus



![image](https://github.com/user-attachments/assets/1b41bdfd-b7d4-44c2-94e7-6390f3f5e906)
