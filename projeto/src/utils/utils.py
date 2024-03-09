import os 
import yaml 

def load_config_file(): ### carrega o arquivo config.yaml em outros arquivos
    ### traz diretório atual
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    ### traz caminho relativo até o arquivo config.yaml
    caminho_relativo = os.path.join("..", "..", "config", "config.yaml")
    ### constroi o caminho absoluto até o arquivo config.yaml
    config_file_path = os.path.abspath(os.path.join(diretorio_atual, caminho_relativo))
    ### ler o arquvo config.yaml
    config_file = yaml.safe_load(open(config_file_path, "rb"))
    
    return config_file


def save_model(model):
    pass