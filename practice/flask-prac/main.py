import json
import psycopg2

from flask import Flask, request, Response


BASE_URL = '/api/v1'
app = Flask(__name__)

USERS = [
    {
        'id': 1,
        'name': 'Ivan',
        'age': 22,
        'description': 'Backend developer',
    },
    {
        'id': 2,
        'name': 'Petr',
        'age': 34,
        'description': 'Frontend developer',
    }
]


def get_db_connection():
    conn = psycopg2.connect(
        host='localhost',
        port=9000,
        database='users',
        user='jussiar',
        password='jussiar'
    )
    conn.autocommit = True
    return conn


@app.route(f'{BASE_URL}/users', methods=['GET'])
def get_all():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT id, name, age, description FROM Users;')
    all_users_list = list(map(lambda item : {
        'id': item[0],
        'name': item[1],
        'age': item[2],
        'description': item[3]
    }, cur.fetchall()))
    cur.close()
    conn.close()

    return Response(json.dumps(all_users_list))


@app.route(f'{BASE_URL}/user/<int:user_id>', methods=['GET', 'DELETE'])
def get_or_delete(user_id):
    global USERS
    if request.method == 'GET':
        filtered = list(filter(lambda user: user['id'] == user_id, USERS))
        if len(filtered) == 0:
            return Response(status=404)
        if len(filtered) > 1:
            return Response(status=500)
        return filtered[0]

    assert request.method == 'DELETE'
    filtered = list(filter(lambda user: user['id'] == user_id, USERS))
    if len(filtered) != 1:
        return Response(status=400)
    USERS = list(filter(lambda user: user['id'] != user_id, USERS))
    return Response(status=204)


@app.route(f'{BASE_URL}/user/create', methods=['POST'])
def create_user():
    global USERS
    new_user_id = max(USERS, key=lambda user: user['id'])['id'] + 1
    new_user = {
        'id': new_user_id,
        'name': request.json['name'],
        'age': request.json['age'],
        'description': request.json['description'],
    }
    USERS.append(new_user)
    return Response(json.dumps(new_user), 201)



if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5005)
