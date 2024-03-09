### BIBLIOS BUILT-IN PYTHON ----------------------------------------------------------
import os
import sys

## forçar a entender que a pasta src é um modulo
sys.path.append(os.path.join(os.path.dirname(__file__), "../src"))

### BIBLIOS NEED TO INSTALL IF DONT INSTALL --------------------------------------------

## biblio para manipular dados tabulares
import pandas as pd
### biblio para validação dos dados de entrada
import pandera  
from pandera import Check, Column, DataFrameSchema
## biblioteca para facilitar o acompanhamento de rodagem de scripts 
import structlog

logger = structlog.getLogger()

### BIBLIOS OF PROJECT -------------------------------------------------------------------
## carrega arquivo config
from utils.utils import load_config_file



class DataValidation:
    """Classe usada para checar/validar a conformidade do dataframe de treino na entrada"""
    def __init__(self) -> None: 
        ## recebe as colunas que devem estar contidas nos dados
        self.columns_to_use = load_config_file().get('columns_to_use') 
    
    def check_shape_data(self, dataframe: pd.DataFrame) -> bool:  
        """Verificar se contém as colunas desejadas
        Args:
            recebe um dataframe (pd.DataFrame)
        Returns: True or False
        Raises:
        """
        try:
            logger.info('Validacao iniciou')
            dataframe.columns = self.columns_to_use
            return True 
        except Exception as e:
            logger.error(f'Validacao errou: {e}')
            return False
        
    def check_columns(self, dataframe: pd.DataFrame) -> bool: 
        """Verificar coluna por coluna relativo aos tipos de dados.
           Check(lambda x: x > 0), coerce=True verifica nulos para target e para outras colunas aceita colunas 
           com nulos pois posteriormente será tratada.
        Args:
            recebe um dataframe (pd.DataFrame)
        Returns: True or False
        Raises:
        """
        schema = DataFrameSchema(
                {
                    "target": Column(int, Check.isin([0, 1]), Check(lambda x: x > 0), coerce=True),
                    "TaxaDeUtilizacaoDeLinhasNaoGarantidas": Column(float, nullable=True),
                    "Idade": Column(int, nullable=True),
                    "NumeroDeVezes30-59DiasAtrasoNaoPior": Column(int, nullable=True),
                    "TaxaDeEndividamento": Column(float, nullable=True),
                    "RendaMensal": Column(float, nullable=True),
                    "NumeroDeLinhasDeCreditoEEmprestimosAbertos": Column(int, nullable=True),
                    "NumeroDeVezes90DiasAtraso": Column(int, nullable=True),
                    "NumeroDeEmprestimosOuLinhasImobiliarias": Column(int, nullable=True),
                    "NumeroDeVezes60-89DiasAtrasoNaoPior": Column(int, nullable=True),
                    "NumeroDeDependentes": Column(float, nullable=True)
                }
            )
        try:
            schema.validate(dataframe)
            logger.info("Validation columns passed...")
            return True
        except pandera.errors.SchemaErrors as exc:
            logger.error("Validation columns failed...")
            pandera.display(exc.failure_cases)
        return False
    
    def run(self, dataframe: pd.DataFrame) -> bool:
        """Método executor da classe que irá chamar os outros métodos e orquestrar as validações
        Args:
            recebe um dataframe (pd.DataFrame)
        Returns: True or False
        Raises:
        """
        if self.check_shape_data(dataframe) and self.check_columns(dataframe):
            logger.info('Validacao com sucesso.')
            return True 
        else:
            logger.error('Validacao falhou.')
            return False