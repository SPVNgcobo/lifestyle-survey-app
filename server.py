
from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

def init_db():
    conn = sqlite3.connect('survey.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS responses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fullname TEXT,
            email TEXT,
            contact TEXT,
            date TEXT,
            age INTEGER,
            food TEXT,
            eatout INTEGER,
            movies INTEGER,
            tv INTEGER,
            radio INTEGER
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    conn = sqlite3.connect('survey.db')
    c = conn.cursor()
    c.execute('''
        INSERT INTO responses (fullname, email, contact, date, age, food, eatout, movies, tv, radio)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        data['fullname'], data['email'], data['contact'], data['date'], data['age'],
        ', '.join(data['food']),
        data['eatout'], data['movies'], data['tv'], data['radio']
    ))
    conn.commit()
    conn.close()
    return jsonify({"message": "Survey submitted successfully"}), 200

@app.route('/results', methods=['GET'])
def results():
    conn = sqlite3.connect('survey.db')
    c = conn.cursor()
    c.execute('SELECT * FROM responses')
    rows = c.fetchall()
    conn.close()

    if not rows:
        return jsonify({"message": "No Surveys Available", "data": []})

    total = len(rows)
    ages = [row[5] for row in rows if isinstance(row[5], int)]
    pizza_lovers = sum(['Pizza' in row[6] for row in rows])
    eatout_avg = round(sum([row[7] for row in rows]) / total, 1)
    pizza_percent = round((pizza_lovers / total) * 100, 1)
    avg_age = round(sum(ages) / len(ages), 1) if ages else 0
    oldest = max(ages) if ages else 0
    youngest = min(ages) if ages else 0

    summary = {
        "total": total,
        "avg_age": avg_age,
        "oldest": oldest,
        "youngest": youngest,
        "pizza_percent": pizza_percent,
        "eatout_avg": eatout_avg
    }

    return jsonify(summary)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
