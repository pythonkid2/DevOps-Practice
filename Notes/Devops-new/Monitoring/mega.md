```
mkdir monitoring
cd monitoring
```
## to download prometheus

https://prometheus.io/download/
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

go inside prometheus folder

edit yml file 
```vi prometheus.yml
```



