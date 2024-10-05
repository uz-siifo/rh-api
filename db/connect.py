import psycopg2
from db.config import load_config

def connect(config):
    try:
        with psycopg2.connect(**config) as conn:
            print('Conexao estabelecida.')
            return conn
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

config = load_config()
conn = connect(config)

cur = conn.cursor()