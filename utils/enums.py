import enum

class AccessLevelEnum(enum.Enum):
    admin = 'admin'
    user = 'user'
    guest = 'guest'

class PositionAtWorkEnum(enum.Enum):
    technical = 'technical'
    engineer = 'enginneer'
    secretary = 'secretary'
    other = 'other'

class FeedbackEnum(str, enum.Enum):
    bom = "bom"
    satisfatorio = "satisfatorio"
    nao_satisfatorio = "nao satisfatorio"
    excelente = "excelente"
    razoavel = "razoavel"