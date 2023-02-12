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


@app.route('/api/v1/actor/<id>', methods=['GET'])
def get_actor(id):
    db = create_engine(db_string)
    query = "SELECT * FROM actors WHERE actors.id = '%s' ;"%(id)
    with db.connect() as conn:
        res = conn.execute(text(query)).fetchall()
    final = {}
    if res:
        for row in res:
            final['id'] = row[0]
            final['name'] = row[1]
        return jsonify(status="True",
        actor = final)
    return jsonify(status="False")

@app.route('/api/v1/movie', methods=['POST'])
def create_movie():
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
                    crud.get_insert_table_id_name("countries", 'id', "name", id, country)
                countries_id.append(id)

        if 'actors' in list(res.keys()):
            for actor in res['actors']:
                id = crud.get_id('actors', 'id', 'name', actor)
                if not id:
                    id = crud.new_id("actors", "id")
                    crud.get_insert_table_id_name("actors", 'id', "name", id, actor)
                actors_id.append(id)

        if 'directors' in list(res.keys()):
            for director in res['directors']:
                id = crud.get_id('directors', 'id', 'name', director)
                if not id:
                    id = crud.new_id("directors", "id")
                    crud.get_insert_table_id_name("directors", 'id', "name", id, director)
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
                crud.get_insert_movies(movie_id, title, year, genre, duration)
        
        for id in countries_id:
             crud.get_insert_table_id_id("come_from", 'movie_id', "country_id", movie_id, id)
        
        for id in actors_id:
             crud.get_insert_table_id_id("play", 'movie_id', "actor_id", movie_id, id)

        for id in directors_id:
             crud.get_insert_table_id_id("manage", 'movie_id', "director_id", movie_id, id)
        
        if title:
            final = {}
            id = crud.get_id('movies', 'movie_id', 'title', title)
            if id:
                final['id'] = id
                final['movie_id'] = movie_id
            return jsonify(status="True", new_movie_id=final)
    return jsonify(status="False")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)