from src.datascience.config.configuration import ConfiguarationManager
from src.datascience.components.data_transformation import DataTransformation
from src.datascience import logger
from pathlib import Path


SATGE_NAME = "Data Transformation Stage"


class DataTransformationTrainingPipeline:

    def __init__(self):
        pass

    def intiate_data_transformation(self):

        try:
            with open(Path("artifacts/data_validation/status.txt"),'r') as f:
                status=f.read().split(" ")[-1]
            
            if status=='True':

                config= ConfiguarationManager()
                data_transfromation_config= config.get_data_transformation_config()
                data_transfromation= DataTransformation(config=data_transfromation_config)
                data_transfromation.train_test_splitting()
            else:
                raise Exception("Your Data Schema is not valid!!")
        except Exception as e:
            logger.exception(e)
            raise e


if __name__=="__main__":
    try:
        logger.info(f">>>>>>>>> stage {STAGE_NAME} <<<<<<<<<<")
        obj = DataTransformationTrainingPipeline()
        obj.intiate_data_transformation()
        logger.info(f">>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<\nn\ x====================x")

    except Exception as e:
        logger.exception(e)
        raise e
    
