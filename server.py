
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
        INSERT INTO responses (fullname, email, contact, date, food, eatout, movies, tv, radio)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        data['fullname'], data['email'], data['contact'], data['date'],
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
    contacts = [int(row[3]) for row in rows if str(row[3]).isdigit()]
    pizza_lovers = sum(['Pizza' in row[5] for row in rows])
    eatout_avg = round(sum([row[6] for row in rows]) / total, 1)
    pizza_percent = round((pizza_lovers / total) * 100, 1)
    avg_contact = round(sum(contacts) / len(contacts), 1) if contacts else 0
    oldest = max(contacts) if contacts else 0
    youngest = min(contacts) if contacts else 0

    summary = {
        "total": total,
        "avg_age": avg_contact,
        "oldest": oldest,
        "youngest": youngest,
        "pizza_percent": pizza_percent,
        "eatout_avg": eatout_avg
    }

    return jsonify(summary)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
