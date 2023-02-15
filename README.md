# Movie quizz :movie_camera:

## Description

This project implements a Python quizz about movies. The application consists of three elements: a PostgreSQL database, an API and a Python quizz. The whole application can be launched with Docker.

The data used in the application come from https://www.kaggle.com/datasets/stefanoleone992/filmtv-movies-dataset and were originally scraped from the public available website https://www.filmtv.it.

## Architecture

### Database

The following schema represents the logical model of the database (entity-relation formalism).
```mermaid
erDiagram
  movies {
    movie_id INT 
    title VARCHAR500
    year INT
    genre VARCHAR50
    duration INT
    avg_vote NUMERIC
    critics_vote NUMERIC
    public_vote NUMERIC
    total_votes INT
  }

  actors{
    actor_id INT
    name VARCHAR500
  }
  
  countries{
    country_id INT
    name VARCHAR500
  }

  directors{
    director_id INT
    name VARCHAR500
  }

  movies }|--|{ actors : "play"
  movies }|--|{ countries : "come from"
  movies }|--|{ directors : "manage"
```
There are three associations in the database: ***play***, ***come from*** and ***manage***. Tables have been created for each of these associations. For example, the table ***play*** contains both the actor ID and the movie ID in order to join the ***actors*** the ***movies*** tables. All the instructions for initialising the database (creation and filling of tables) are included in the **database/init.sql** file. The Dockerfile in the ***database** folder is used to create a Postgres container for the database. TCP port 5432 of the container is mapped to host port 5432.

### API
The API was implemented using *Flask*. Several endpoints were created in order to retrieve information about movies and actors. It is also possible to add new movies, to modify existing ones or to delete some movies from the database. The file *apps/webservice/app.py* implements the API. The functions allowing to Create, Read, Update and Delete data are coded in the *apps/webservice/crud.py*. The Dockerfile in the *webservice* folder is used to create a Python docker container for the API. TCP port 80 of the container is mapped to host port 80. This makes the API available on the localhost on port 80.

### Quizz
All the modules and classes used to implement the quizz are located in the *quizz* folder. The *quizz/object* folder contains the core of the application. The "factory" design pattern has been used to create questions for the quizz. The user is asked questions about different topics:
- countries associated with movies
- movies in which an actor has played in
- directors of a movie
- genre of a movie
- year of release of a movie

The file *quizz/object/question_factory.py* instantiates a question depending on its type.

The file *quizz/main.py* allows to start the quiz. The user has to select the number of questions he or she wants, the questions are then presented to the user randomly (the type of question is chosen randomly).

## Installation

```bash
git clone https://github.com/alannagenin/movie-quizz.git
cd movie-quizz
python3 -m venv venv
source venv/bin/activate
```
### Environment setup
The following instructions add a .env file in the *apps/quizz* and *apps/webservice* folders. Please replace *\<username\>* with a chosen username and *\<password\>* with a chosen password.

```bash
env_content="POSTGRES_USER=<username>
POSTGRES_PASSWORD=<password>"
cd apps/quizz
echo "$env_content" > .env
cd ..
cd webservice
echo "$env_content" > .env
cd ..
cd ..
```

### Application launch

The following instruction build the project and run it in daemon mode.

```bash
docker-compose up --d --build
```

### Quizz launch

Run the app-quizz container and open a bash terminal:

```bash
docker-compose exec app-quizz bash
```

Run the following command into the bash terminal:

```bash
python main.py
```

### Tests

**Test the quizz**

```bash
docker-compose exec app-quizz bash
```

Run the following command into the bash terminal:

```bash
python -m unittest
```

**Test the API**

```bash
docker-compose exec app-webservice bash
```

Run the following command into the bash terminal:

```bash
python -m pytest tests/
```

### Deinstallation

```bash
# stop and remove all containers
docker-compose rm -f -s
```

## Examples of requests to the API

###  GET (accessible from any navigator)

- Information about an actor using their ID: **http://localhost/api/v1/actor/id/1**
- Information about an actor using their name: **http://localhost/api/v1/actor/name/abe vigoda**
- Information about movie using its ID: **http://localhost/api/v1/movie/id/39520**
- Information about movie using its ID: **http://localhost/api/v1/movie/title/the godfather trilogy: 1901-1980**

### POST (with Insomnia or Postman)

Add a new movie (it will duplicate the movies if we run the request several times):

**URL: http://localhost/api/v1/movie**

**BODY (json):**
```json
{
	"movie": {
		"title": "Funny Koalas",
		"year": 2023,
		"genre": "Comedy",
		"duration": 90
	},
	"countries": ["Australia"],
	"actors": ["Alice", "Bob"],
	"directors": ["Charlie"]
    }
```

### PUT (with Insomnia or Postman)

Add or update a movie (do not duplicate the movies):

**URL: http://localhost/api/v1/movie**

**BODY (json):**
```json
{
	"movie": {
		"title": "Funny Koalas",
		"year": 2022,
		"genre": "Documentary",
		"duration": 100
	},
	"countries": ["Australia"],
	"actors": ["Smart Koalas"],
	"directors": ["Alice"]
    }
```

### DELETE (with Insomnia or Postman)

Delete a movie using its name:

**URL: http://localhost/api/v1/movie/funny koalas**

## Contributors

* Alanna DEVLIN-GENIN
* Camille LE POTIER