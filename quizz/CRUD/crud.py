from sqlalchemy import create_engine, text
import os
import dotenv

dotenv.load_dotenv(override=True)

db_user = os.getenv('POSTGRES_USER')
db_pass = os.getenv('POSTGRES_PASSWORD')
db_name = 'database'
db_host = 'db'
db_port = '5432'
db_string = 'postgresql://{}:{}@{}:{}/{}'.format(db_user, db_pass, db_host, db_port, db_name)

def new_id(table, id_col):
    db = create_engine(db_string)
    query = "SELECT max(%s) AS max FROM %s;"%(id_col, table)
    with db.connect() as conn:
        res = conn.execute(text(query)).fetchall()
        new_id = int(res[0]['max']) + 1
    return new_id

def get_id(table, id_col, name_col, value):
    db = create_engine(db_string)
    query = "SELECT %s FROM %s WHERE lower(%s) LIKE lower('%s');"%(id_col, table, name_col, value)
    with db.connect() as conn:
        res = conn.execute(text(query)).fetchall()
        if len(res):
            id = int(res[0][id_col])
        else:
            id = None
    return id

def get_ids(table, id_col, name_col, value):
    db = create_engine(db_string)
    query = "SELECT %s FROM %s WHERE lower(%s) LIKE lower('%s');"%(id_col, table, name_col, value)
    with db.connect() as conn:
        res = conn.execute(text(query)).fetchall()
        ids = []
        if len(res):
            for id in res:
                ids.append(int(id[id_col]))
    return ids

def get_name(table, id_col, name_col, value):
    db = create_engine(db_string)
    query = "SELECT %s FROM %s WHERE %s=%s;"%(name_col, table, id_col, value)
    with db.connect() as conn:
        res = conn.execute(text(query)).fetchall()
        if len(res):
            name = res[0][name_col]
        else:
            name = None
    return name

def get_info_movies_name(name_col, value):
    db = create_engine(db_string)
    query = "SELECT movies.movie_id AS movie_id,title,year,genre,duration,actors.name AS actor, directors.name AS director, countries.name AS country\
         FROM actors\
            JOIN play ON actors.id = play.actor_id \
            JOIN movies ON play.movie_id = movies.movie_id\
            JOIN manage ON movies.movie_id = manage.movie_id\
            JOIN directors ON manage.director_id = directors.id\
            JOIN come_from ON movies.movie_id = come_from.movie_id\
            JOIN countries ON come_from.country_id = countries.id\
            WHERE lower(%s) LIKE lower('%s');"%(name_col, value)
    
    with db.connect() as conn:
        res = conn.execute(text(query)).fetchall()
        final = {}
        if len(res):
            final['actors'] = []
            final['directors'] = []
            final['countries'] = []
            final['ids']=[]
            final['title']=res[0]['title']
            final['year']=res[0]['year']
            final['genre']=res[0]['genre']
            final['duration']=res[0]['duration']

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

def get_info_movies_id(id_col, value):
    db = create_engine(db_string)
    query = "SELECT movies.movie_id AS movie_id,title,year,genre,duration,actors.name AS actor, directors.name AS director, countries.name AS country\
         FROM actors\
            JOIN play ON actors.id = play.actor_id \
            JOIN movies ON play.movie_id = movies.movie_id\
            JOIN manage ON movies.movie_id = manage.movie_id\
            JOIN directors ON manage.director_id = directors.id\
            JOIN come_from ON movies.movie_id = come_from.movie_id\
            JOIN countries ON come_from.country_id = countries.id\
            WHERE movies.%s=%s;"%(id_col, value)
    
    with db.connect() as conn:
        res = conn.execute(text(query)).fetchall()
        final = {}
        if len(res):
            final['actors'] = []
            final['directors'] = []
            final['countries'] = []
            final['id']=res[0]['movie_id']
            final['title']=res[0]['title']
            final['year']=res[0]['year']
            final['genre']=res[0]['genre']
            final['duration']=res[0]['duration']

        for elem in res:
            if elem['actor'] not in final['actors']:
                final['actors'].append(elem['actor'])

            if elem['director'] not in final['directors']:
                final['directors'].append(elem['director'])

            if elem['country'] not in final['countries']:
                final['countries'].append(elem['country'])
            
    return final

# def get_info_movies_id(id_col, value):
#     db = create_engine(db_string)
#     query = "SELECT movie_id,title,year,genre,duration FROM movies WHERE %s=%s;"%(id_col, value)
#     with db.connect() as conn:
#         res = conn.execute(text(query)).fetchall()
#         final = {}
#         if len(res):
#             final['id']=res[0]['movie_id']
#             final['title']=res[0]['title']
#             final['year']=res[0]['year']
#             final['genre']=res[0]['genre']
#             final['duration']=res[0]['duration']
        
#     return final

def insert_table_id_name(table, id, name, value_id, value_name):
    db = create_engine(db_string)
    query = "INSERT INTO %s (%s,%s) VALUES \
                        (%s,  '%s');"%(table, id, name, value_id, value_name)
    with db.connect() as conn:
        conn.execute(text(query))

def insert_table_id_id(table, id1, id2, value1, value2):
    db = create_engine(db_string)
    query = "INSERT INTO %s (%s,%s) VALUES \
                        (%s,  %s);"%(table, id1, id2, value1, value2)
    with db.connect() as conn:
        conn.execute(text(query))


def insert_movies(id_value, title_value, year_value, genre_value, duration_value):
    db = create_engine(db_string)
    query = "INSERT INTO movies (movie_id,title,year,genre,duration,avg_vote,critics_vote,public_vote,total_votes) \
            VALUES (%s,  '%s', %s, '%s', %s, null, null, null, null);\
            "%(id_value, title_value, year_value, genre_value, duration_value)
    with db.connect() as conn:
        conn.execute(text(query))

def delete_values_table_id(table, id, value_id):
    db = create_engine(db_string)
    query = "DELETE FROM %s WHERE %s = %s;"%(table, id, value_id)
    with db.connect() as conn:
        conn.execute(text(query))

def update_movies(id, title, year, genre, duration):
    db = create_engine(db_string)
    query = "UPDATE movies\
        SET title = '%s',\
        year = %s,\
        genre = '%s',\
        duration = %s\
        WHERE movie_id = %s;"%(title, year, genre, duration, id)
    with db.connect() as conn:
        conn.execute(text(query))