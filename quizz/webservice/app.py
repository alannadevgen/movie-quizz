from flask import Flask, jsonify, request
from sqlalchemy import create_engine, text
import dotenv
import os

app = Flask(__name__)

# dotenv.load_dotenv(override=True)

# db_name = os.environ["POSTGRES_DB"]
# db_user = os.environ["POSTGRES_USER"]
# db_pass = os.environ["POSTGRES_PASSWORD"]
db_name = 'database'
db_user = 'username'
db_pass = 'secret'
db_host = 'db'
db_port = '5432'
db_string = 'postgresql://{}:{}@{}:{}/{}'.format(db_user, db_pass, db_host, db_port, db_name)


@app.route('/api/v1/actor/<id>', methods=['GET'])
def get_actor(id):
    db = create_engine(db_string)
    query = "SELECT * FROM actors WHERE actors.id = '%s' ;"%(id)
    with db.connect() as conn:
        res = conn.execute(text(query))
    final = {}
    if res:
        for row in res:
            final['id'] = row[0]
            final['name'] = row[1]
        return jsonify(status="True",
        actor = final)
    return jsonify(status="False")

if __name__ == '__main__':
    app.run(debug=True)