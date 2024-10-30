# sistema-rh-api
Este repositorio vai é da api do backend, para a equipe de backend

### 1. **Instalação de Dependências**
Primeiro, é necessário instalar o **FastAPI** e o servidor **Uvicorn** para executar a aplicação.

1.1. Crie um ambiente virtual (opcional, mas recomendado para manter as dependências isoladas):
```bash
python3 -m venv venv
source venv/bin/activate  # Para Linux/MacOS
venv\Scripts\activate     # Para Windows
```

1.2. Instale o **FastAPI** e **Uvicorn** e outras mais dependências do projeto com o **pip**:
```bash
 pip install -r requirements.txt
```

### 2. **Executando o Projeto**
Com o código definido, é hora de executar o projeto utilizando o **Uvicorn**.

4.1. No terminal, dentro do diretório do projeto, execute o seguinte comando:
```bash
uvicorn app.main:app --reload
```
- O argumento `app.main:app` refere-se ao caminho do módulo. `app` é o diretório onde está o arquivo `main.py`, e `app` é a instância do FastAPI dentro deste arquivo.
- O argumento `--reload` é utilizado para recarregar o servidor automaticamente sempre que houver mudanças no código durante o desenvolvimento.

### 3. **Gerando Arquivo de Dependências**
Para manter o controle das dependências utilizadas no projeto, é recomendado gerar um arquivo `requirements.txt`.

3.1. Gere o arquivo com o seguinte comando:
```bash
pip freeze > requirements.txt
```

### 4. **Comandos Úteis**

- **Rodar o servidor FastAPI**:
```bash
uvicorn app.main:app --reload
```

- **Gerar um arquivo de dependências**:
```bash
pip freeze > requirements.txt
```
