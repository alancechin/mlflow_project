### BIBLIOS BUILT-IN PYTHON ----------------------------------------------------------
import os
import sys

## forçar a entender que a pasta src é um modulo
sys.path.append(os.path.join(os.path.dirname(__file__), "../src"))

### BIBLIOS NEED TO INSTALL IF DONT INSTALL --------------------------------------------

## biblio para manipular dados tabulares
import pandas as pd
### biblio para separação de amostras de treino e teste
from sklearn.model_selection import train_test_split


### BIBLIOS OF PROJECT -------------------------------------------------------------------
## carrega arquivo config
from utils.utils import load_config_file

### da para criar algumas funções de try and except aqui
class DataTransformation:
    def __init__(self, dataframe: pd.DataFrame):
        """Inicializa a classe e seta variáveis necessárias
        Args:
            recebe um dataframe (pd.DataFrame)
        Returns: variáveis dataframe e target_name setadas podendo serem usadas em qualquer função da classe
        Raises:
        """
        self.dataframe = dataframe 
        self.target_name = load_config_file().get('target_name') 
        
    def train_test_spliting(self): 
        """Realiza a separação dos dados de treino e teste
        Args:
            None
        Returns: arrays with X_train, X_valid, y_train, y_valid
        Raises:
        """
        X = self.dataframe.drop(self.target_name, axis=1)
        y = self.dataframe[self.target_name]
        
        X_train, X_valid, y_train, y_valid = train_test_split(X, y,
                                                               test_size= load_config_file().get('test_size') ,
                                                               random_state = load_config_file().get('random_state'), 
                                                               stratify=y)
        
        return X_train, X_valid, y_train, y_valid