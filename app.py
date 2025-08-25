from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

# Initialize DB (runs only first time)
def init_db():
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS messages (id INTEGER PRIMARY KEY, text TEXT)")
    c.execute("INSERT INTO messages (text) VALUES ('Hello from SQLite!')")
    conn.commit()
    conn.close()

@app.route("/")
def home():
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    c.execute("SELECT text FROM messages")
    messages = c.fetchall()
    conn.close()
    return render_template("index.html", messages=messages)

if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000)
