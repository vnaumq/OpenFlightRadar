import os

DB_CONFIG = {
    "host": os.getenv("PGHOST", "db"),
    "port": os.getenv("PGPORT", "5432"),
    "user": os.getenv("POSTGRES_USER", "ofr"),
    "password": os.getenv("POSTGRES_PASSWORD", "ofr"),
    "dbname": os.getenv("POSTGRES_DB", "ofr"),
}
