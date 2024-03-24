## biblio para manipular dados tabulares
import pandas as pd
### método que auxilia no processo do fluxo de tratamento dos dados de treino e teste sem enviesar os dados
from sklearn.pipeline import Pipeline
## biblioteca para facilitar o acompanhamento de rodagem de scripts 
import structlog

logger = structlog.getLogger()


class DataPreprocess: 
     """Classe usada para realizar o preprocessamento da amostra de dados"""
     def __init__(self,  pipe: Pipeline):
        """Inicializa a classe e seta variáveis necessárias
        Args:
            um objeto instanciado Pipeline
        Returns: objetos Pipe podendo serem usadas em qualquer função da classe
        Raises:
        """
        self.pipe = pipe 
        self.trained_pipe = None
        
     def train(self, dataframe: pd.DataFrame):
        """Calcula os parâmetros de preprocessamento baseado nos dados de treino
        Args:
            variável do tipo DataFrame
        Returns: objeto Pipe ajustado com parâmetros para entrada dos dados no algoritmo
        Raises:
        """
        logger.info("Preprocessamento iniciou...")
        self.trained_pipe = self.pipe.fit(dataframe)
     def transform(self, dataframe: pd.DataFrame):
        """Aplica os parâmetros de preprocessamento baseado nos dados de treino em qualquer dataframe
        Args:
            variável do tipo DataFrame
        Returns: um DataFrame preprocessado com os parâmetros setados
        Raises:
        """
        if self.trained_pipe is None:
            raise ValueError("Pipeline nao foi treinado.")
        logger.info("Transformacao dos dados com preprocessador iniciou...")
        data_processed = self.trained_pipe.transform(dataframe)
        
        return data_processed