import os
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# Connect to an existing database 172.17.0.2, postgres, pass
default_db = "postgres"
user = os.environ['POSTGRES_USER']
password = os.environ['POSTGRES_PASSWORD']
server = os.environ['POSTGRES_SERVER']
port = os.environ['POSTGRES_PORT']

conn = psycopg2.connect(dbname=default_db, password=password, user=user, host=server, port=port)
print conn
conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
cur = conn.cursor()
cur.execute("CREATE DATABASE nfldb")
cur.close()
conn.close()
