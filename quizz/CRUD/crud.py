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
    query = "SELECT %s FROM %s WHERE lower(%s) LIKE lower(%s);"%(id_col, table, name_col, value)
    with db.connect() as conn:
        res = conn.execute(text(query)).fetchall()
        if len(res):
            id = int(res[0][id_col])
        else:
            id = None
    return id

def get_insert_table_two_col(table, col1, col2, value1, value2):
    db = create_engine(db_string)
    query = "INSERT INTO %s (%s,%s) VALUES \
                        (%s,  %s);", (table, col1, col2, value1, value2)
    with db.connect() as conn:
        conn.execute(text(query))


def get_insert_movies(id_value, title_value, year_value, genre_value, duration_value):
    db = create_engine(db_string)
    query = "INSERT INTO movies (movie_id,title,year,genre,duration,avg_vote,critics_vote,public_vote,total_votes) \
            VALUES (%s,  %s, %s, %s, %s, null, null, null, null);\
            ", (id_value, title_value, year_value, genre_value, duration_value)
    with db.connect() as conn:
        conn.execute(text(query))