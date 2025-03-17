docker build -t persons .
docker run -d -p 9000:5432 --name persons persons
