### classe que encapsula etapa de carregamento dos dados
class DataLoad:
    """Class data load"""
    
    def __init__(self) -> None:
        pass 
    
    def load_data(self) -> pd.DataFrame:
        """Funcao vai carregar os dados
        
        return:
            pandas DataFrame"""
            
        loaded_data = pd.read_csv('../data/raw/train.csv')
        return loaded_data