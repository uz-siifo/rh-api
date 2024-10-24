class Service:
    """
    Classe base para servicos de manipulacao de dados.

    Atributos:
    - engine: Instancia do banco de dados utilizada para realizar as operacoes.

    Metodos:
    - create(data): Cria um novo registro no banco de dados.
    - delete(data): Remove um registro do banco de dados.
    - update(data): Atualiza um registro existente no banco de dados.
    - get_all(): Retorna todos os registros cadastrados.
    """

    def __init__(self, engine) -> None:
        """
        Inicializa o Service.

        Args:
            engine: Instancia do banco de dados.
        """
        self.engine = engine

    def create(self, data):
        """
        Cria um novo registro no banco de dados.

        Args:
            data: Dicionario com os dados a serem criados.

        Returns:
            None
        """
        pass

    def delete(self, data):
        """
        Remove um registro do banco de dados.

        Args:
            data: Dicionario com os dados do registro a ser removido.

        Returns:
            None
        """
        pass

    def update(self, data):
        """
        Atualiza um registro existente no banco de dados.

        Args:
            data: Dicionario com os dados a serem atualizados.

        Returns:
            None
        """
        pass
    
    def get_all(self):
        """
        Retorna todos os registros cadastrados.

        Returns:
            list: Lista de dicionarios com os dados dos registros.
        """
        pass
