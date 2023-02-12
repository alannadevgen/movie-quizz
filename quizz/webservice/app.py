from flask import Flask, jsonify, request
from sqlalchemy import create_engine, text
from CRUD import crud
import os
import dotenv

app = Flask(__name__)

dotenv.load_dotenv(override=True)

db_user = os.getenv('POSTGRES_USER')
db_pass = os.getenv('POSTGRES_PASSWORD')
db_name = 'database'
db_host = 'db'
db_port = '5432'
db_string = 'postgresql://{}:{}@{}:{}/{}'.format(db_user, db_pass, db_host, db_port, db_name)


@app.route('/api/v1/actor/id/<id>', methods=['GET'])
def get_actor_id(id):
    name = crud.get_name("actors", "id", "name", id)
    final = {}
    if name:
        final['name'] = name
        return jsonify(status="True",
        actor = final)
    return jsonify(status="False")


@app.route('/api/v1/actor/name/<name>', methods=['GET'])
def get_actor_name(name):
    id = crud.get_id("actors", "id", "name", name)
    final = {}
    if id:
        final['id'] = id
        return jsonify(status="True",
        actor = final)
    return jsonify(status="False")

@app.route('/api/v1/movie/id/<id>', methods=['GET'])
def get_movie_id(id):
    title = crud.get_name("movies", "movie_id", "title", id)
    final = {}
    if title:
        final['title'] = title
        return jsonify(status="True",
        movie = final)
    return jsonify(status="False")


@app.route('/api/v1/movie/title/<title>', methods=['GET'])
def get_movie_title(title):
    id = crud.get_id("movies", "movie_id", "title", title)
    final = {}
    if id:
        final['id'] = id
        return jsonify(status="True",
        movie = final)
    return jsonify(status="False")

@app.route('/api/v1/movie', methods=['POST'])
def create_movie():
    '''
    POST request example (json body to put in INSOMNIA or POSTMAN)
    {
	"movie": {
		"title": "Funny koalas",
		"year": 2023,
		"genre": "Comedy",
		"duration": 90
	},
	"countries": ["Australia"],
	"actors": ["Alice", "Bob"],
	"directors": ["Charlie"]
    }
    '''
    title = None
    countries_id = []
    actors_id = []
    directors_id = []

    res = request.get_json()
    if res:
        if 'countries' in list(res.keys()):
            for country in res['countries']:
                id = crud.get_id('countries', 'id', 'name', country)
                if not id:
                    id = crud.new_id("countries", "id")
                    crud.insert_table_id_name("countries", 'id', "name", id, country)
                countries_id.append(id)

        if 'actors' in list(res.keys()):
            for actor in res['actors']:
                id = crud.get_id('actors', 'id', 'name', actor)
                if not id:
                    id = crud.new_id("actors", "id")
                    crud.insert_table_id_name("actors", 'id', "name", id, actor)
                actors_id.append(id)

        if 'directors' in list(res.keys()):
            for director in res['directors']:
                id = crud.get_id('directors', 'id', 'name', director)
                if not id:
                    id = crud.new_id("directors", "id")
                    crud.insert_table_id_name("directors", 'id', "name", id, director)
                directors_id.append(id)

        if 'movie' in list(res.keys()):
            # create a new movie even if the movie already exists (POST)
            movie_id = crud.new_id("movies", "movie_id")
            if 'title' in res['movie'] and 'year' in res['movie'] and 'genre'\
                in res['movie'] and 'duration' in res['movie']:
                movie = res['movie']
                title = movie['title']
                year = movie['year']
                genre = movie['genre']
                duration = movie['duration']
                crud.insert_movies(movie_id, title, year, genre, duration)
        
        for id in countries_id:
             crud.insert_table_id_id("come_from", 'movie_id', "country_id", movie_id, id)
        
        for id in actors_id:
             crud.insert_table_id_id("play", 'movie_id', "actor_id", movie_id, id)

        for id in directors_id:
             crud.insert_table_id_id("manage", 'movie_id', "director_id", movie_id, id)
        
        if title:
            final = {}
            id = crud.get_id('movies', 'movie_id', 'title', title)
            if id:
                final['id'] = id
                final['movie_id'] = movie_id
            return jsonify(status="True", new_movie_id=final)
    return jsonify(status="False")

@app.route('/api/v1/movie/<title>', methods=['DELETE'])
def delete_movie(title):
    '''
    '''
    movie_id = crud.get_id("movies", "movie_id", "title", title)
    if movie_id:

        # delete using movie_id
        crud.delete_values_table_id("come_from", "movie_id", movie_id)
        crud.delete_values_table_id("play", "movie_id", movie_id)
        crud.delete_values_table_id("manage", "movie_id", movie_id)
        crud.delete_values_table_id("movies", "movie_id", movie_id)

        
        movie_id = crud.get_id('movies', 'movie_id', 'title', title)
        if not movie_id:
            return jsonify(status="True")
    
    return jsonify(status="False")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)