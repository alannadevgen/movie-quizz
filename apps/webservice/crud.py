from sqlalchemy import create_engine, text
import os
import dotenv
from typing import List, Dict

# information for connecting to the database
dotenv.load_dotenv(override=True)

db_user = os.getenv('POSTGRES_USER')
db_pass = os.getenv('POSTGRES_PASSWORD')
db_name = 'database'
db_host = 'db'
db_port = '5432'
db_string = 'postgresql://{}:{}@{}:{}/{}'.format(db_user, db_pass, db_host, db_port, db_name)
############################################

def new_id(table: str, id_col: str) -> int:
    '''
    Create a new ID

    Parameters
    ----------
    table : str
        name of the table where to create the new ID
    id_col: str
        name of the ID column in the table

    Returns
    -------
    int
        new ID
    '''
    db = create_engine(db_string)
    # create a new ID just after the last ID in the DB
    query = "SELECT max(%s) AS max FROM %s;"%(id_col, table)
    with db.connect() as conn:
        res = conn.execute(text(query)).fetchall()
        new_id = int(res[0]['max']) + 1
    return new_id


def get_id(table: str, id_col: str, name_col: str, value: str) -> int:
    '''
    Get the ID of a value from its name

    Parameters
    ----------
    table : str
        name of the table where to create the new ID
    id_col: str
        name of the id column in the table
    name_col: str
        name of the name column in the table
    value: str
        value for the name column

    Returns
    -------
    int
        ID
    '''
    db = create_engine(db_string)
    query = "SELECT %s FROM %s WHERE lower(%s) LIKE lower('%s');"%(id_col, table, name_col, value.replace("'", "''"))
    with db.connect() as conn:
        res = conn.execute(text(query)).fetchall()
        # check the name value is in the table
        if len(res):
            id = int(res[0][id_col])
        else:
            id = None
    return id

def get_ids(table: str, id_col: str, name_col: str, value: str) -> List:
    '''
    Get all IDs of a value from its name

    Parameters
    ----------
    table : str
        name of the table where to create the new ID
    id_col: str
        name of the ID column in the table
    name_col: str
        name of the name column in the table
    value: str
        value for the name column

    Returns
    -------
    list(int)
        ID
    '''
    db = create_engine(db_string)
    query = "SELECT %s FROM %s WHERE lower(%s) LIKE lower('%s');"%(id_col, table, name_col, value.replace("'", "''"))
    with db.connect() as conn:
        res = conn.execute(text(query)).fetchall()
        ids = []
        # check the name value is in the table
        if len(res):
            # if True, add each ID in a list
            for id in res:
                ids.append(int(id[id_col]))
    return ids

def get_name(table: str, id_col: str, name_col: str, value: int) -> str:
    '''
    Get name of a value from its ID

    Parameters
    ----------
    table : str
        name of the table where to create the new id
    id_col: str
        name of the ID column in the table
    name_col: str
        name of the name column in the table
    value: int
        value for the ID column

    Returns
    -------
    list(int)
        ID
    '''
    db = create_engine(db_string)
    query = "SELECT %s FROM %s WHERE %s=%s;"%(name_col, table, id_col, value)
    with db.connect() as conn:
        res = conn.execute(text(query)).fetchall()
        if len(res):
            # check the name value is in the table
            name = res[0][name_col]
        else:
            name = None
    return name

def get_info_movies_name(title: str) -> Dict:
    '''
    Get information about a movie from its name

    Parameters
    ----------
    title: str
        value for the title column

    Returns
    -------
    dict
        information about the movie
    '''
    db = create_engine(db_string)
    # query to select all information about movies
    query = "SELECT movies.movie_id AS movie_id,title,year,genre,duration,actors.name AS actor, directors.name AS director, countries.name AS country\
         FROM actors\
            JOIN play ON actors.id = play.actor_id \
            JOIN movies ON play.movie_id = movies.movie_id\
            JOIN manage ON movies.movie_id = manage.movie_id\
            JOIN directors ON manage.director_id = directors.id\
            JOIN come_from ON movies.movie_id = come_from.movie_id\
            JOIN countries ON come_from.country_id = countries.id\
            WHERE lower(title) LIKE lower('%s');"%(title.replace("'", "''"))
    
    with db.connect() as conn:
        res = conn.execute(text(query)).fetchall()
        final = {}
        if len(res):
            final['actors'] = []
            final['directors'] = []
            final['countries'] = []
            final['ids']=[]

            # add results directly when the field must contain only one element
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

                if elem['movie_id'] not in final['ids']:
                    final['ids'].append(elem['movie_id'])
            
    return final

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
            JOIN play ON actors.id = play.actor_id \
            JOIN movies ON play.movie_id = movies.movie_id\
            JOIN manage ON movies.movie_id = manage.movie_id\
            JOIN directors ON manage.director_id = directors.id\
            JOIN come_from ON movies.movie_id = come_from.movie_id\
            JOIN countries ON come_from.country_id = countries.id\
            WHERE movies.movie_id=%s;"%(id)
    
    with db.connect() as conn:
        res = conn.execute(text(query)).fetchall()
        final = {}
        if len(res):
            final['actors'] = []
            final['directors'] = []
            final['countries'] = []

            # add results directly when the field must contain only one element
            final['id']=res[0]['movie_id']
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

def insert_table_id_name(table: str, id: str, name: str, value_id: int, value_name: str) -> None:
    '''
    Insert values in a table containing only an ID column and a name column

    Parameters
    ----------
    table : str
        name of the table where to insert values
    id: str
        name of the ID column in the table
    name: str
        name of the name column in the table
    value_id: int
        value for the ID column
    value_name: str
        value for the name column
    '''
    db = create_engine(db_string)
    query = "INSERT INTO %s (%s, %s) VALUES \
                        (%s,  '%s');"%(table, id, name, value_id, value_name.replace("'", "''"))
    with db.connect() as conn:
        conn.execute(text(query))

def insert_table_id_id(table: str, id1: str, id2: str, value1: int, value2: int) -> None:
    '''
    Insert values in a table containing two ID columns

    Parameters
    ----------
    table : str
        name of the table where to insert values
    id1: str
        name of the first ID column in the table
    id2: str
        name of the second ID column in the table
    value1: int
        value for the first ID column
    value1: int
        value for the second ID column
    '''
    db = create_engine(db_string)
    query = "INSERT INTO %s (%s,%s) VALUES \
                        (%s,  %s);"%(table, id1, id2, value1, value2)
    with db.connect() as conn:
        conn.execute(text(query))


def insert_movies(id: int, title: str, year: int, genre: str, duration: int) -> None:
    '''
    Insert values into movies table

    Parameters
    ----------
    id: int
        movie ID
    title: str
        movie title
    year: int
        year of the film's release
    genre: str
        genre of the movie
    duration: int
        duration of the movie (number of minutes)
    '''
    db = create_engine(db_string)
    query = "INSERT INTO movies (movie_id,title,year,genre,duration,avg_vote,critics_vote,public_vote,total_votes) \
            VALUES (%s,  '%s', %s, '%s', %s, null, null, null, null);\
            "%(id, title.replace("'", "''"), year, genre.replace("'", "''"), duration)
    with db.connect() as conn:
        conn.execute(text(query))

def delete_values_table_id(table: str, id: str, value_id: int) -> None:
    '''
    Delete all values in a table for a given ID

    Parameters
    ----------
    table: str
        name of the table
    id: str
        name of the ID column
    value_id: int
        ID of rows to detele
    '''
    db = create_engine(db_string)
    query = "DELETE FROM %s WHERE %s = %s;"%(table, id, value_id)
    with db.connect() as conn:
        conn.execute(text(query))

def update_movies(id: int, title: str, year: int, genre: str, duration: int) -> None:
    '''
    Update values for movies table

    Parameters
    ----------
    id: int
        movie ID
    title: str
        movie title
    year: int
        year of the film's release
    genre: str
        genre of the movie
    duration: int
        duration of the movie (number of minutes)
    '''
    db = create_engine(db_string)
    query = "UPDATE movies\
        SET title = '%s',\
        year = %s,\
        genre = '%s',\
        duration = %s\
        WHERE movie_id = %s;"%(title.replace("'", "''"), year, genre.replace("'", "''"), duration, id)
    with db.connect() as conn:
        conn.execute(text(query))