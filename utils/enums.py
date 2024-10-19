import enum

class AccessLevelEnum(enum.Enum):
    admin = 'admin'
    user = 'user'

class PositionAtWorkEnum(enum.Enum):
    technical = 'technical'
    engineer = 'engineer'
    secretary = 'secretary'
    other = 'other'

class FeedbackEnum(str, enum.Enum):
    bom = "bom"
    satisfatorio = "satisfatorio"
    nao_satisfatorio = "nao satisfatorio"
    excelente = "excelente"
    razoavel = "razoavel"

class GoalStatusEnum(enum.Enum):
    not_started = "Nao iniciado"
    in_progress = "Em andamento"
    completed = "Finalizada"