docker build -t users .
docker run -d -p 9000:5432 --name users users
