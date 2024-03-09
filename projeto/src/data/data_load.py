### BIBLIOS BUILT-IN PYTHON ----------------------------------------------------------
import os
import sys

## forçar a entender que a pasta src é um modulo
sys.path.append(os.path.join(os.path.dirname(__file__), "../src"))

### BIBLIOS NEED TO INSTALL IF DONT INSTALL --------------------------------------------

import pandas as pd

## biblioteca para facilitar o acompanhamento de rodagem de scripts 
import structlog

logger = structlog.getLogger()

### BIBLIOS OF PROJECT -------------------------------------------------------------------

## carrega arquivo config
from utils.utils import load_config_file


### classe que encapsula etapa de carregamento dos dados
class DataLoad:
    """Class data load"""
    
    def __init__(self) -> None:
        pass

    def data_load(self, dataset_name: str) -> pd.DataFrame:
        """Carrega os dados a partir do nome do dataset fornecido

        Args:
            dataset_name (str): O nome do dataset a ser carregado

        Returns:

        Raises:
        """
        logger.info(f"Comecando a carga dos dados com o nome: {dataset_name}")
        ### traz o nome do arquivo a ser lido de acordo com a chave passada
        dataset = load_config_file().get(dataset_name)

        try:
            dataset = load_config_file().get(dataset_name)
            
            if dataset is None: ### se dataset estiver vazio retorna um erro
                raise ValueError(
                    f"Erro: O nome do dataset fornecido e incorreto: {dataset}"
                )
            ## dataset carregado
            loaded_data = pd.read_csv(f"../data/raw/{dataset}")
            
            ### retornar dataset com as colunas a serem usadas
            return loaded_data[load_config_file().get("columns_to_use")]
        
        ### Para pegar erros adicionais
        except ValueError as ve:
            logger.error(str(ve))
        
        except Exception as e:
            logger.error(f"Erro inesperado: {str(e)}")