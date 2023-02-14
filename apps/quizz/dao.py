from sqlalchemy import create_engine, text
import os
import dotenv

# information for connecting to the database
dotenv.load_dotenv(override=True)

db_user = os.getenv('POSTGRES_USER')
db_pass = os.getenv('POSTGRES_PASSWORD')
db_name = 'database'
db_host = 'db'
db_port = '5432'
db_string = 'postgresql://{}:{}@{}:{}/{}'.format(db_user, db_pass, db_host, db_port, db_name)
############################################


def get_random_id(table: str, id_col: str) -> int:
    ###################################################
    # RÉCUPÉRER ID ACTEUR OU ID MOVIE ALÉATOIREMENT
    # Mettre table="movies" et id_col="movie_id" pour
    # film aléatoire
    # Mettre table="actors" et id_col="actor_id" pour
    # acteur aléatoire
    ###################################################
    '''
    Select a random ID of a table

    Parameters
    ----------
    table : str
        name of the table where to create the new ID
    id_col: str
        name of the ID column in the table

    Returns
    -------
    int
        random ID
    '''
    db = create_engine(db_string)
    
    query = "SELECT %s AS random FROM %s ORDER BY RANDOM() LIMIT 1;"%(id_col, table)
    with db.connect() as conn:
        res = conn.execute(text(query)).fetchall()
        random_id = int(res[0]['random'])
    return random_id


def get_info_movies_id(id: int) -> dict:
    ###################################################
    # RÉCUPÉRER INFO FILM À PARTIR DE SON ID
    ###################################################
    '''
    Get information about a movie from its ID

    Parameters
    ----------
    id: int
        value for the title column

    Returns
    -------
    dict
        information about the movie
    '''
    db = create_engine(db_string)
    query = "SELECT movies.movie_id AS movie_id,title,year,genre,duration,actors.name AS actor, directors.name AS director, countries.name AS country\
         FROM actors\
            JOIN play ON actors.actor_id = play.actor_id \
            JOIN movies ON play.movie_id = movies.movie_id\
            JOIN manage ON movies.movie_id = manage.movie_id\
            JOIN directors ON manage.director_id = directors.director_id\
            JOIN come_from ON movies.movie_id = come_from.movie_id\
            JOIN countries ON come_from.country_id = countries.country_id\
            WHERE movies.movie_id=%s;"%(id)
    
    with db.connect() as conn:
        res = conn.execute(text(query)).fetchall()
        final = {}
        if len(res):
            final['actors'] = []
            final['directors'] = []
            final['countries'] = []

            # add results directly when the field must contain only one element
            final['movie_id']=res[0]['movie_id']
            final['title']=res[0]['title']
            final['year']=res[0]['year']
            final['genre']=res[0]['genre']
            final['duration']=res[0]['duration']

            # add results in a list when the field can contain more than one element
            for elem in res:
                if elem['actor'] not in final['actors']:
                    final['actors'].append(elem['actor'])

                if elem['director'] not in final['directors']:
                    final['directors'].append(elem['director'])

                if elem['country'] not in final['countries']:
                    final['countries'].append(elem['country'])
            
    return final

def random_bad_answers(name_col: str, true_value: str) -> list:
    ######################################################################
    # TIRER RÉPONSES ALÉATOIRES NON ÉGALES À TRUE_VALUE
    ######################################################################
    '''
    Returns random answers different of true_value

    Parameters
    ----------
    name_col: str
        name of the movie column where select random values
    true_value: str
        true answer to the question

    Returns
    -------
    list
        bad answers
    '''
    db = create_engine(db_string)
    query = "SELECT %s FROM movies WHERE lower(%s) != lower('%s')\
        ORDER BY RANDOM() LIMIT 3;"%(name_col, name_col, true_value.replace("'", "''"))
    
    with db.connect() as conn:
        res = conn.execute(text(query)).fetchall()
        bad_answers = []
        if len(res):
            for elem in res:
                if elem[name_col] not in bad_answers:
                    bad_answers.append(elem[name_col])

    return bad_answers


def get_movies_actor_id(actor_id: int) -> dict:
    ######################################################################
    # RÉCUPÉRER FILMS DANS LESQUELS UN ACTEUR A JOUÉ (déterminé par son ID)
    ######################################################################
    '''
    Get movies where an actor has played in

    Parameters
    ----------
    actor_id: str
        ID of the actor

    Returns
    -------
    dict
        movies
    '''
    db = create_engine(db_string)
    query = "SELECT actors.actor_id AS actor_id, actors.name AS actor, movies.movie_id AS movie_id,title FROM actors \
        JOIN play ON actors.actor_id = play.actor_id \
        JOIN movies ON play.movie_id = movies.movie_id\
        WHERE actors.actor_id = %s;"%(actor_id)
    
    with db.connect() as conn:
        res = conn.execute(text(query)).fetchall()
        final = {}
        if len(res):
            final['movie_ids'] = []
            final['titles'] = []

            # add results directly when the field must contain only one element
            final['actor_id']=res[0]['actor_id']
            final['actor_name']=res[0]['actor']

            # add results in a list when the field can contain more than one element
            for elem in res:
                if elem['movie_id'] not in final['movie_ids']:
                    final['movie_ids'].append(elem['movie_id'])

                if elem['title'] not in final['titles']:
                    final['titles'].append(elem['title'])

    return final