# Movie quizz :movie_camera:

The aim of this project is to create a quizz with the following requirements: at least one design patern, a relational database model containing at least 3 databases, launch the program in a Docker container.

## Quick start

```python 
git clone https://github.com/alannagenin/movie-quizz.git
cd movie-quizz
python3 -m venv venv
source venv/bin/activate

# build and run in deamon (CRUD operations possible on the API)
docker-compose up --d --build

# launch the quizz
docker-compose exec app-quizz bash
python main.py

# stop and remove all containers
docker stop webservice
docker stop quizz
docker stop database
docker-compose rm
```

**Create a .env file in apps/quizz and apps/webservice folders containing:**
```.env
POSTGRES_USER=<my_user>
POSTGRES_PASSWORD=<my_password>
```

## Contributors

* Alanna DEVLIN-GENIN
* Camille LE POTIER