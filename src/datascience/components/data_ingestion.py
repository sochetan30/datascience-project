import urllib.request as request
from src.datascience import logger 
import os
import zipfile
from src.datascience.entity.config_entity import DataIngestionConfig

# DataIngestion Components
class DataIngestion:
    def __init__(self,config: DataIngestionConfig):
        self.config=config

    # Downloading the zip file
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url=self.config.source_URL,
                filename=self.config.local_data_file
            )
            logger.info(f"{filename} download! with the following info: \n {headers}")
        else:
            logger.info("File already exists")


    def extract_zip_file(self):
        """Zip fil path: str
        Extract the zip file into data directory
        """
        unzip_data = self.config.unzip_dir
        os.makedirs(unzip_data, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_data)

