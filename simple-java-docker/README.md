# Install Docker 
sudo apt-get update
sudo apt-get install docker.io

# Create Image From Dockerfile
**Go to the directory where the Dockerfile is located.**

docker build -t java-app .

# Create Container From Docker Image
docker run java-app