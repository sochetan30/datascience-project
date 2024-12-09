from src.datascience import logger
from src.datascience.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.datascience.pipeline.data_validation_pipeline import DataValidationTrainingPipeline

STAGE_NAME='Data Ingestion Stage'
#logger.info("Welcome to Custom Logging of Data Science Project")

try:
    logger.info(f'>>>>>> stage {STAGE_NAME} started <<<<<<')
    obj= DataIngestionTrainingPipeline()
    obj.intiate_data_ingestion()
    logger.info(f'>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx=================x')
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME='Data Validation Stage'
try:
    logger.info(f">>>>>>>>> stage {STAGE_NAME} <<<<<<<<<<")
    obj = DataValidationTrainingPipeline()
    obj.initiate_data_validation()
    logger.info(f">>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<\nn\ x====================x")

except Exception as e:
    logger.exception(e)
    raise e