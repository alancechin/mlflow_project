### BIBLIOS BUILT-IN PYTHON ----------------------------------------------------------
import os
import sys

## forçar a entender que a pasta src é um modulo
sys.path.append(os.path.join(os.path.dirname(__file__), "../src"))

### BIBLIOS NEED TO INSTALL IF DONT INSTALL --------------------------------------------

## biblio que salva objetos criados para serem utilizados posteriormente
import joblib
## método para avaliar performance do modelo  
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import StratifiedKFold, cross_val_score
## biblioteca para facilitar o acompanhamento de rodagem de scripts 
import structlog

logger = structlog.getLogger()

### BIBLIOS OF PROJECT -------------------------------------------------------------------
## carrega arquivo config
from utils.utils import load_config_file

class ModelEvaluation:
    """Classe que contem os métodos para realizar a etapa de validação de performance dos modelos"""
    def __init__(self, model, X, y, n_splits=5):
        """Inicializa a classe e seta variáveis necessárias
        Args:
            Objeto do modelo treinado, amostra de entrada(X) e saída(y) a ser validada e quantidade splits para cross_validation
        Returns: None
        Raises:
        """
        self.model = model
        self.X = X
        self.y = y
        self.n_splits = n_splits

    def cross_val_evaluate(self):
        """Realiza a validação cruzada
        Args:
            None
        Returns: resultados de cada iteração do cross validation
        Raises:
        """
        logger.info("Iniciou a validacao cruzada...")
        skf = StratifiedKFold(
            n_splits=self.n_splits,
            shuffle=True,
            random_state=load_config_file().get("random_state"),
        )
        scores = cross_val_score(self.model, self.X, self.y, cv=skf, scoring=load_config_file().get('cross_evaluate_metric'))
        return scores

    def roc_auc_scorer(self, model, X, y):
        """Realiza as predições e calcula o roc_auc_scorer
        Args:
            Objeto do modelo treinado, amostra de entrada(X) e saída(y) a ser validada
        Returns: resultado da validação
        Raises:
        """
        y_pred = model.predict_proba(X)[:, 1]
        return roc_auc_score(y, y_pred)

    @staticmethod
    def evaluate_predictions(y_true, y_pred_proba):
        """Avalia as predições realizadas pelo modelo e compara com os dados reais a partir de uma métrica de avaliação
        Args:
            Saída real e as probabilidades estimada modelo
        Returns: resultado da predição
        Raises:
        """
        logger.info("Iniciou a validacao do modelo")
        return roc_auc_score(y_true, y_pred_proba)