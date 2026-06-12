from flask import Flask, jsonify
from datetime import datetime
import psycopg2

app = Flask(__name__)

def get_db_connection():
    return psycopg2.connect(
        host="db",
        database="testdb",
        user="postgres",
        password="postgres"
    )

@app.route('/api')
def home():
    conn = None
    db_info = "Not connected"

    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT version();")
        db_info = cur.fetchone()[0]
        cur.close()
        conn.close()
    except Exception as e:
        db_info = str(e)

    return jsonify({
        "message": "Hello from Flask Backend 🚀",
        "time": datetime.utcnow().isoformat(),
        "database": db_info
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)