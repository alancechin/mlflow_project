import os 
import yaml 
## biblio que salva objetos criados para serem utilizados posteriormente
import joblib

def load_config_file(): 
    """Carrega o arquivo config.yaml para ser usado em outros arquivos
    Args:
        None
    Returns: retorna o arquivo config.yaml para usar seus parâmetros
    Raises:
    """
    ### traz diretório atual
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    ### traz caminho relativo até o arquivo config.yaml
    caminho_relativo = os.path.join("..", "..", "config", "config.yaml")
    ### constroi o caminho absoluto até o arquivo config.yaml
    config_file_path = os.path.abspath(os.path.join(diretorio_atual, caminho_relativo))
    ### ler o arquvo config.yaml
    config_file = yaml.safe_load(open(config_file_path, "rb"))
    
    return config_file


def save_model(model, model_name):
    """Salvar modelo treinado na pasta destinada para tal
    Args:
        Objeto do modelo treinado e o nome do modelo a ser salvo
    Returns: None
    Raises:
    """
    ### traz diretório atual
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    ### traz caminho relativo até o endereço que desejo salvar o modelo
    caminho_relativo = os.path.join("..", "..", "models", "logs", model_name)
    ### constroi o caminho absoluto no endereço que desejo salvar o modelo
    file_path = os.path.abspath(os.path.join(diretorio_atual, caminho_relativo))
    ### escrever modelo na pasta indicada
    joblib.dump(model, file_path)
    return None