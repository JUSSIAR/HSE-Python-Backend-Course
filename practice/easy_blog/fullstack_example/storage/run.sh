docker build -t blog .
docker run -d -p 9000:5432 --name blog blog
