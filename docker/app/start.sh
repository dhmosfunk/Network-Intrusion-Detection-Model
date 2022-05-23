docker rmi -f $(docker images -aq)
docker build -t ids-model .
docker run -it -p 5000:5000 ids-model:latest

