from db.connect import conn, cur

class user_service:
    def create(self):
        cur.execute("select* from department;")
        res = cur.fetchone()
        print(res)
        # conn.e
        pass

    def update(self, user):
        pass

    def delete(self, user):
        pass

    def get_all(self):
        pass

    def get_by_id(self, id):
        pass

    def get_by_name(self, name):
        pass

    def get_by_department(self, department):
        pass