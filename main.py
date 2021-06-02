import psycopg2
from flask import Flask, render_template

def get_data_from_cloud_sql():
    # connection = psycopg2.connect(dbname='checking', user='flaskuser', password='password', host='35.200.145.113')
    connection = psycopg2.connect(dbname='checking', user='flaskuser', password='password', host='/cloudsql/flask-sql')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM simple;')
    data = [row for row in cursor]
    cursor.close()
    connection.close()
    return data

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', data=get_data_from_cloud_sql())

if __name__ == '__main__':
    app.run(debug=True, port=8080, host='127.0.0.1')