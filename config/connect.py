import psycopg2
from config import load_config

def connect(config):
    """ Connect to the PostgreSQL database server """
    try:
        # connecting to the PostgreSQL server
        with psycopg2.connect(**config) as conn:
            print('Conexao estabelecida.')
            return conn
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)


# if __name__ == '__main__':
#     config = load_config()
#     connect(config)

conn = psycopg2.connect("dbname=hr_system_sinfo user=postgres password=123456789")

cur = conn.cursor()

# cur.execute("insert into department(name, employee_nums, min_salary, max_salary) values(%s, %s, %s, %s)", ("TI", 10, 202070.6, 1777198.66))
cur.execute("select * from department;")
res = cur.fetchone()

print(res)
conn.commit()
# print(res)