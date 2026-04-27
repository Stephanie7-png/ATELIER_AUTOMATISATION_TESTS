import sqlite3
import json
from datetime import datetime

DB_NAME = "runs.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS runs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            created_at TEXT,
            total INTEGER,
            passed INTEGER,
            failed INTEGER,
            success_rate REAL,
            avg_latency REAL,
            p95_latency REAL,
            results TEXT
        )
    """)

    conn.commit()
    conn.close()

def save_run(run):
    init_db()

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO runs (
            created_at, total, passed, failed,
            success_rate, avg_latency, p95_latency, results
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        run["total"],
        run["passed"],
        run["failed"],
        run["success_rate"],
        run["avg_latency"],
        run["p95_latency"],
        json.dumps(run["results"])
    ))

    conn.commit()
    conn.close()

def list_runs():
    init_db()

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, created_at, total, passed, failed,
               success_rate, avg_latency, p95_latency
        FROM runs
        ORDER BY id DESC
    """)

    rows = cursor.fetchall()
    conn.close()

    return rows
