from .model import model as BaseModel

class user(BaseModel):
    def __init__(self, name, nickname, email, passwd, contact, updated_at) -> None:
        super().__init__()
        self.name = name
        self.nickname = nickname 
        self.email = email 
        self.passwd = passwd 
        self.contact = contact
        self.updated_at = updated_at

    def to_json(self):
        return {
            "name": self.name,
            "nickname": self.nickname,
            "email": self.email,
            "passwd": self.passwd,
            "contact": self.contact,
            "updated_at": self.updated_at
        }

    def from_json(self, __user):
        try:
            return user(
                __user["name"], 
                __user["nickname"], 
                __user["email"], 
                __user["passwd"], 
                __user["contact"], 
                __user["updated_at"]
            )
        except Exception as e:
              print(e)