### BIBLIOS BUILT-IN PYTHON ----------------------------------------------------------
import os
import sys
## forçar a entender que a pasta src é um modulo
sys.path.append(os.path.join(os.path.dirname(__file__), "../src"))

### BIBLIOS NEED TO INSTALL IF DONT INSTALL --------------------------------------------

## biblio para manipular dados tabulares
import pandas as pd

## biblioteca para facilitar o acompanhamento de rodagem de scripts 
import structlog
logger = structlog.getLogger()

### BIBLIOS OF PROJECT -------------------------------------------------------------------
## carrega arquivo config
from utils.utils import load_config_file, save_model


class TrainModels:
    """Classe usada para treinar o modelo com os dados ajustados"""
    def __init__(self, dados_X: pd.DataFrame,
                       dados_y: pd.DataFrame):
        """Inicializa a classe e seta variáveis necessárias
        Args:
            Dataframe representando os dados de entrada (variáveis explicativas) e Dataframe representando variável resposta (variável dependente)
        Returns: None
        Raises:
        """
        self.dados_X = dados_X 
        self.dados_y = dados_y 
        self.model_name = load_config_file().get('model_name')
        
    def train(self, model):
        """Ajusta o modelo de acordo com os dados passados
        Args:
            Objeto que representa a instancia do modelo a ser treinado
        Returns: Modelo treinado 
        Raises:
        """
        model.fit(self.dados_X, self.dados_y)
        save_model(model, self.model_name)
        return model 
    