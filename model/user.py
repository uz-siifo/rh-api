from .model import model as BaseModel

class User(BaseModel):
    def __init__(self, name, nickname, email, passwd, access_level, updated_at=None) -> None:
        super().__init__()
        self.name = name
        self.nickname = nickname
        self.email = email
        self.passwd = passwd
        self.access_level = access_level
        self.updated_at = updated_at

    def to_json(self):
        return {
            "name": self.name,
            "nickname": self.nickname,
            "email": self.email,
            "passwd": self.passwd,
            "access_level": self.access_level,
            "updated_at": self.updated_at
        }

    @classmethod
    def from_json(cls, user_data):
        try:
            return cls(
                user_data.get("name"),
                user_data.get("nickname"),
                user_data.get("email"),
                user_data.get("passwd"),
                user_data.get("access_level"),
                user_data.get("updated_at")
            )
        except Exception as e:
            print(f"Error: {e}")
