from db.connect import cur, conn
from model.department import Department
import json

class DepartmentService:
    def create(self, department):
        dept_json = json.dumps(Department.from_json(department).to_json())
        cur.execute("select *from create_department(%s);", (dept_json,))
        # cur.execute("commit;")
        conn.commit()

        res = cur.fetchone()
        print(res)

        cur.execute("select name, employee_nums, min_salary, max_salary from department;")
        res = cur.fetchall()

        for row in res:
            print(row)