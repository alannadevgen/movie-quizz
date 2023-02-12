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

# def get_actors_movie(movie_id):
#     db = create_engine(db_string)
#     query = "SELECT actors.id FROM actors JOIN play ON actors.id = play.actor_id\
#         JOIN movies ON play.movie_id = movies.movie_id\
#         WHERE movies.movie_id = %s ;"%(movie_id)
#     with db.connect() as conn:
#         res = conn.execute(text(query)).fetchall()
#         if len(res):
#             id = list(res)
#         else:
#             id = None
#     return id

# def get_directors_movie(movie_id):
#     db = create_engine(db_string)
#     query = "SELECT directors.id FROM directors JOIN manage ON directors.id = manage.director_id\
#         JOIN movies ON manage.movie_id = movies.movie_id\
#         WHERE movies.movie_id = %s ;"%(movie_id)
#     with db.connect() as conn:
#         res = conn.execute(text(query)).fetchall()
#         if len(res):
#             id = list(res)
#         else:
#             id = None
#     return id

# def get_countries_movie(movie_id):
#     db = create_engine(db_string)
#     query = "SELECT countries.id FROM countries JOIN come_from ON countries.id = come_from.country_id\
#         JOIN movies ON come_from.movie_id = movies.movie_id\
#         WHERE movies.movie_id = %s ;"%(movie_id)
#     with db.connect() as conn:
#         res = conn.execute(text(query)).fetchall()
#         if len(res):
#             id = list(res)
#         else:
#             id = None
#     return id

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