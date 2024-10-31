# promoter_worker e a funcao que classifica se um fucionario deve ou nao ser promovido
# a funcao usa um modelo de classifacao RandomForest treinado a parte, para fazer essa classificao

# employee_rating: e um dicionario que contem informacoes de avalicao de um funcionario
def promoter_worker(employee_rating: dict):
    import pickle

    with open("src/include/promotion_model.pkl", "rb") as file:
        promotion_model = pickle.load(file)
        features = [
            employee_rating["is_assiduous"], 
            employee_rating["is_collaborative"], 
            employee_rating["completed_goals"], 
            employee_rating["is_punctual"], 
            employee_rating["presences"], 
            employee_rating["absences"], 
            employee_rating["work_quality_rating"], 
            employee_rating["problem_solving_skills_rating"], 
            employee_rating["problem_solving_skills_rating"], 
            employee_rating["communication_skills_rating"], 
            employee_rating["time_management_skills_rating"], 
            employee_rating["leadership_skills_rating"]
        ]

        y = promotion_model.predict([features])
        return y
