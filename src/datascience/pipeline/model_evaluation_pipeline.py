from src.datascience.config.configuration import ConfiguarationManager
from src.datascience.components.model_evaluation import ModelEvaluation
from src.datascience import logger

STAGE_NAME = "Model Evaluation Stage"

class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def initiate_model_evaluation(self):
        config= ConfiguarationManager()
        model_trainer_config = config.get_model_evaluation_config()
        model_trainer = ModelEvaluation(config=model_trainer_config)
        model_trainer.log_into_mlflow()

if __name__=="__main__":
    try:
        logger.info(f">>>>>>>>> stage {STAGE_NAME} <<<<<<<<<<")
        obj = ModelEvaluationPipeline()
        obj.initiate_model_evaluation()
        logger.info(f">>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<\nn\ x====================x")

    except Exception as e:
        logger.exception(e)
        raise e
    

