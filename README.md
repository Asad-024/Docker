**Installing Docker in Ubuntu**
```bash
sudo apt-get update
```
```bash
sudo apt-get install docker.io
```
**Add user in docker group**
```bash
sudo usermod -aG docker $USER
```
**Refresh group**
#To 
```bash
sudo newgrp docker
```
