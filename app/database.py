import sqlite3
from .config import DB_PATH
def connect():
    db=sqlite3.connect(DB_PATH,check_same_thread=False);db.row_factory=sqlite3.Row;return db
def initialize():
    with connect() as db:db.executescript("""CREATE TABLE IF NOT EXISTS workflows(workflow_id INTEGER PRIMARY KEY,title TEXT,request_description TEXT,requester TEXT,business_area TEXT,priority TEXT,created_at TEXT DEFAULT CURRENT_TIMESTAMP,status TEXT DEFAULT 'created',workflow_type TEXT,plan_json TEXT);CREATE TABLE IF NOT EXISTS audit_log(id INTEGER PRIMARY KEY,workflow_id INTEGER,action TEXT,details TEXT,reviewer_note TEXT,created_at TEXT DEFAULT CURRENT_TIMESTAMP);CREATE TABLE IF NOT EXISTS timeline(id INTEGER PRIMARY KEY,workflow_id INTEGER,status TEXT,created_at TEXT DEFAULT CURRENT_TIMESTAMP);""")
