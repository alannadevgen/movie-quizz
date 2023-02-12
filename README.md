# Movie quizz :movie_camera:

The aim of this project is to create a quizz with the following requirements: at least one design patern, a relational database model containing at least 3 databases, launch the program in a Docker container.

## Quick start

```python 
git clone https://github.com/alannagenin/movie-quizz.git
cd movie-quizz
python -m venv venv
source venv/bin/activate
docker-compose up --build
```

**Create a .env file in quizz folder containing:**
```.env
POSTGRES_USER=<my_user>
POSTGRES_PASSWORD=<my_password>
```

**Launch the app:**
```python 
docker-compose up --build
```

## Contributors

* Alanna DEVLIN-GENIN
* Camille LE POTIER
