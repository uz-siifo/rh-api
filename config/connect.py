import psycopg2
from config import load_config

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

# # cur.execute("insert into department(name, employee_nums, min_salary, max_salary) values(%s, %s, %s, %s)", ("TI", 10, 202070.6, 1777198.66))
# cur.execute("select * from department;")
# res = cur.fetchone()

# print(res)
# conn.commit()
# print(res)