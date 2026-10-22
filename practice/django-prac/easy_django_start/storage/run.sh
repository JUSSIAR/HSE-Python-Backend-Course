docker build -t easy_django .
docker run -d -p 9000:5432 --name easy_django easy_django
