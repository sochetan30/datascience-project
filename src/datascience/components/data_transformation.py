from src.datascience.entity.config_entity import DataTransformationConfig
from sklearn.model_selection import train_test_split
import os
from src.datascience import logger
import pandas as pd



class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    # Data Transformation - feature Engineering, Data Cleaning

    def train_test_splitting(self):
        data= pd.read_csv(self.config.data_path)

        train, test = train_test_split(data)

        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index= False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index= False)


        logger.info("Splitting data into trainig and test sets : ")
        logger.info(train.shape)
        logger.info(test.shape)

        print(train.shape)
        print(test.shape)
