from configparser import ConfigParser

# funcao para carregar as configuracoes do arquivo database.ini
# param (filename) -> nome do arquivo de configuracao
# param (section) -> e o grupo de configuracoes que estao no arquivo database.ini
def load_config(filename='config/database.ini', section='postgresql'):
    parser = ConfigParser() # permite ler os chaves e os valores em arquivos de configuracao .ini
    parser.read(filename)

    config = {} # configuracao padrao
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            config[param[0]] = param[1]
    else:
        raise Exception('Sessao: {0}, nao encrontrada em: {1} file'.format(section, filename))

    return config # configuracoes em forma de um dicionario