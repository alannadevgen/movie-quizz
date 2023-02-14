from flask import Flask, jsonify, request
import crud

app = Flask(__name__)


@app.route('/api/v1/actor/id/<id>', methods=['GET'])
def get_actor_id(id: int):
    '''
    Get information about an actor with with his ID

    Parameters
    ----------
    id: int
        ID of the actor

    Returns
    -------
    json
        information about the actor
    '''
    name = crud.get_name("actors", "actor_id", "name", id)
    final = {}
    if name:
        final['name'] = name
        return jsonify(status="True",
        actor = final)
    return jsonify(status="False")


@app.route('/api/v1/actor/name/<name>', methods=['GET'])
def get_actor_name(name: str):
    '''
    Get information about an actor with with his name

    Parameters
    ----------
    name: str
        name of the actor

    Returns
    -------
    json
        information about the actor
    '''
    id = crud.get_id("actors", "actor_id", "name", name)
    final = {}
    if id:
        final['id'] = id
        return jsonify(status="True",
        actor = final)
    return jsonify(status="False")

@app.route('/api/v1/movie/id/<id>', methods=['GET'])
def get_movie_id(id: int):
    '''
    Get information about a movie with its ID

    Parameters
    ----------
    id: int
        ID of the movie

    Returns
    -------
    json
        information about the movie
    '''
    infos = crud.get_info_movies_id(id)
    if infos:
        return jsonify(status="True",
        movie = infos)
    return jsonify(status="False")


@app.route('/api/v1/movie/title/<title>', methods=['GET'])
def get_movie_title(title: str):
    '''
    Get information about a movie with its title

    Parameters
    ----------
    title: str
        title of the movie

    Returns
    -------
    json
        information about the movie
    '''
    infos = crud.get_info_movies_name(title)
    if infos:
        return jsonify(status="True",
        movie = infos)
    return jsonify(status="False")

@app.route('/api/v1/movie', methods=['POST'])
def create_movie():
    '''
    Create a movie based on information given in the json body

    Example for the json body:
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

    Returns
    -------
    json
        status (indicates if the creation has been done)
    '''
    title = None
    countries_id = []
    actors_id = []
    directors_id = []

    res = request.get_json()
    if res:
        if 'countries' in list(res.keys()):
            for country in res['countries']:
                id = crud.get_id('countries', 'country_id', 'name', country)
                if not id:
                    id = crud.new_id("countries", "country_id")
                    crud.insert_table_id_name("countries", 'country_id', "name", id, country)
                countries_id.append(id)

        if 'actors' in list(res.keys()):
            for actor in res['actors']:
                id = crud.get_id('actors', 'actor_id', 'name', actor)
                if not id:
                    id = crud.new_id("actors", "actor_id")
                    crud.insert_table_id_name("actors", 'actor_id', "name", id, actor)
                actors_id.append(id)

        if 'directors' in list(res.keys()):
            for director in res['directors']:
                id = crud.get_id('directors', 'director_id', 'name', director)
                if not id:
                    id = crud.new_id("directors", "director_id")
                    crud.insert_table_id_name("directors", 'director_id', "name", id, director)
                directors_id.append(id)

        if 'movie' in list(res.keys()) and countries_id and actors_id and directors_id:
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
            ids = crud.get_ids('movies', 'movie_id', 'title', title)
            if ids:
                final['id'] = max(ids)
                final['created'] = title
            return jsonify(status="True", movie=final)
    return jsonify(status="False")


@app.route('/api/v1/movie', methods=['PUT'])
def update_movie():
    '''
    Create or update a movie based on information given in the json body

    Example for the json body:
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

    Returns
    -------
    json
        status (indicates if the creation/update has been done)
    '''
    title = None
    countries_id = []
    actors_id = []
    directors_id = []

    res = request.get_json()
    if res:
        if 'countries' in list(res.keys()):
            for country in res['countries']:
                id = crud.get_id('countries', 'country_id', 'name', country)
                if not id:
                    id = crud.new_id("countries", "country_id")
                    crud.insert_table_id_name("countries", 'country_id', "name", id, country)
                countries_id.append(id)

        if 'actors' in list(res.keys()):
            for actor in res['actors']:
                id = crud.get_id('actors', 'actor_id', 'name', actor)
                if not id:
                    id = crud.new_id("actors", "actor_id")
                    crud.insert_table_id_name("actors", 'actor_id', "name", id, actor)
                actors_id.append(id)

        if 'directors' in list(res.keys()):
            for director in res['directors']:
                id = crud.get_id('directors', 'director_id', 'name', director)
                if not id:
                    id = crud.new_id("directors", "director_id")
                    crud.insert_table_id_name("directors", 'director_id', "name", id, director)
                directors_id.append(id)

        if 'movie' in list(res.keys()) and countries_id and actors_id and directors_id:
            if 'title' in res['movie'] and 'year' in res['movie'] and 'genre'\
                in res['movie'] and 'duration' in res['movie']:
                movie = res['movie']
                title = movie['title']
                year = movie['year']
                genre = movie['genre']
                duration = movie['duration']
                
                # update the movie or create a new one if the movie does not exist (PUT)
                movie_ids = crud.get_ids("movies", "movie_id", "title", title)

                if not movie_ids:
                    # create
                    movie_id = crud.new_id("movies", "movie_id")            
                    crud.insert_movies(movie_id, title, year, genre, duration)
        
                    for id in countries_id:
                        crud.insert_table_id_id("come_from", 'movie_id', "country_id", movie_id, id)
                    
                    for id in actors_id:
                        crud.insert_table_id_id("play", 'movie_id', "actor_id", movie_id, id)

                    for id in directors_id:
                        crud.insert_table_id_id("manage", 'movie_id', "director_id", movie_id, id)
                
                else:
                    for movie_id in movie_ids:
                        # update
                        crud.update_movies(movie_id, title, year, genre, duration)

                        # delete old values for actors, directors and countries using movie_id
                        crud.delete_values_table_id("come_from", "movie_id", movie_id)
                        crud.delete_values_table_id("play", "movie_id", movie_id)
                        crud.delete_values_table_id("manage", "movie_id", movie_id)

                        # add new values for actors, directors and countries using movie_id
                        for id in countries_id:
                            crud.insert_table_id_id("come_from", 'movie_id', "country_id", movie_id, id)
                        
                        for id in actors_id:
                            crud.insert_table_id_id("play", 'movie_id', "actor_id", movie_id, id)

                        for id in directors_id:
                            crud.insert_table_id_id("manage", 'movie_id', "director_id", movie_id, id)
        
        if title:
            final = {}
            ids = crud.get_ids('movies', 'movie_id', 'title', title)
            if ids:
                final['id'] = ids
                final['updated or created'] = title
            return jsonify(status="True", movie=final)
    return jsonify(status="False")


@app.route('/api/v1/movie/<title>', methods=['DELETE'])
def delete_movie(title: str):
    '''
    Delete a movie defined by its title

    Parameters
    ----------
    title: str
        title of the movie to delete

    Returns
    -------
    json
        status (indicates if the deletion has been done)
    '''
    # retrieve all ids of a movie defined by its title
    movie_ids = crud.get_ids("movies", "movie_id", "title", title)
    if movie_ids:
        # delete movies using all the IDs associated with the movie
        for movie_id in movie_ids:
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