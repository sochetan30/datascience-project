from src.datascience.config.configuration import ConfiguarationManager
from src.datascience.components.data_ingestion import DataIngestion
from src.datascience import logger

STAGE_NAME='Data Ingestion Stage'

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def intiate_data_ingestion(self):
        config=ConfiguarationManager()
        data_ingestion_config=config.get_data_igestion_config()
        data_ingestion=DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()


if __name__=='__main__':
    try:
        logger.info(f'>>>>>> stage {STAGE_NAME} started <<<<<<')
        obj= DataIngestionTrainingPipeline()
        obj.intiate_data_ingestion()
        logger.info(f'>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx=================x')
    except Exception as e:
        logger.exception(e)
        raise e

