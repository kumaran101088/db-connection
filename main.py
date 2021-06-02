import psycopg2
from flask import Flask, render_template, request

unix_socket = f'/cloudsql/second-flask-run:asia-south1:flask-sql'

# def get_data_from_cloud_sql():
    # connection = psycopg2.connect(dbname='checking', user='flaskuser', password='password', host='35.200.145.113')
    # connection = psycopg2.connect(dbname='checking', user='flaskuser', password='password', host='/cloudsql/flask-sql/.s.PGSQL.5432')
    # connection = psycopg2.connect(dbname='checking', user='flaskuser', password='password', host=unix_socket)
    # cursor = connection.cursor()
    # cursor.execute('SELECT * FROM simple;')
    # data = [row for row in cursor]
    # cursor.close()
    # connection.close()
    # return data

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/data', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        # connection = psycopg2.connect(dbname='checking', user='flaskuser', password='password', host='35.200.145.113')
        connection = psycopg2.connect(dbname='checking', user='flaskuser', password='password', host='/cloudsql/second-flask-run:asia-south1:flask-sql')
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM simple;')
        data = [row for row in cursor]
        cursor.close()
        connection.close()
        return render_template('index.html', data=data)
    
    given_name = request.form.get('name')
    # connection = psycopg2.connect(dbname='checking', user='flaskuser', password='password', host='35.200.145.113')
    connection = psycopg2.connect(dbname='checking', user='flaskuser', password='password', host='/cloudsql/second-flask-run:asia-south1:flask-sql')
    cursor = connection.cursor()
    cursor.execute(f"INSERT INTO simple (name) VALUES ('{given_name}')")
    connection.commit()
    cursor.execute('SELECT * FROM simple;')
    data = [row for row in cursor]
    cursor.close()
    connection.close()
    return render_template('index.html', data=data)

    

if __name__ == '__main__':
    app.run(debug=True, port=8080, host='127.0.0.1')