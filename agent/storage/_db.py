import psycopg2

from agent.config import load_config

def _load_db_config():
    db = load_config().get("database", {})
    cfg = {
        "dbname": db.get("name", "Riverse"),
        "user": db.get("user", "postgres"),
        "host": db.get("host", "localhost"),
        "options": "-c client_encoding=UTF8",
    }
    if db.get("password"):
        cfg["password"] = db["password"]
    if db.get("port"):
        cfg["port"] = db["port"]
    return cfg

DB_CONFIG = _load_db_config()

def get_db_connection():
    conn = psycopg2.connect(**DB_CONFIG)
    return conn
