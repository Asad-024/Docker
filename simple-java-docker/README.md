# Install Docker 
sudo apt-get update <br>
sudo apt-get install docker.io

# Create Image From Dockerfile
**Go to the directory where the Dockerfile is located.**
```bash
docker build -t java-app .
```

# Create Container From Docker Image
```bash
docker run java-app
```