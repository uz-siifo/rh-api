import enum

class AccessLevelEnum(enum.Enum):
    admin = 'admin'
    user = 'user'

    def get_value(self):
        return self.value
    
class PositionAtWorkEnum(enum.Enum):
    technical = 'technical'
    engineer = 'engineer'
    secretary = 'secretary'
    other = 'other'

    def get_value(self):
        return self.value

class FeedbackEnum(str, enum.Enum):
    bom = "bom"
    satisfatorio = "satisfatorio"
    nao_satisfatorio = "nao satisfatorio"
    excelente = "excelente"
    razoavel = "razoavel"

    def get_value(self):
        return self.value
    
class GoalStatusEnum(enum.Enum):
    not_started = "Nao iniciado"
    in_progress = "Em andamento"
    completed = "Finalizada"

    def get_value(self):
        return self.value