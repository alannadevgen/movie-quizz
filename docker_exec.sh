docker build -t movies-db ./
docker run --rm -d --name movies-db-container -p 5432:5432 movies-db
docker exec -it movies-db-container psql -U postgres -d movies