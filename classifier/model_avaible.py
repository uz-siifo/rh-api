import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, accuracy_score

# Carregar o dataset
df = pd.read_excel('avaliacao_colaboradores.xlsx')

# Definir características (features) e rótulo (target)
X = df.drop(columns=['id', 'is_assiduous'])  # Remover a coluna id e a coluna alvo
y = df['is_assiduous']  # Coluna alvo

# Converter colunas booleanas para inteiros (0 e 1)
X['is_collaborative'] = X['is_collaborative'].astype(int)
X['is_punctual'] = X['is_punctual'].astype(int)

# Dividir o dataset em conjunto de treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Criar o modelo
modelo = DecisionTreeClassifier(random_state=42)

# Treinar o modelo
modelo.fit(X_train, y_train)

# Fazer previsões
y_pred = modelo.predict(X_test)

# Avaliar o modelo
precisao = accuracy_score(y_test, y_pred)
relatorio_classificacao = classification_report(y_test, y_pred)

print(f'Precisão do modelo: {precisao:.2f}')
print('Relatório de Classificação:')
print(relatorio_classificacao)

