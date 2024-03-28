from thyroid import utils
from thyroid.entity import config_entity
from thyroid.entity import artifact_entity
from thyroid.exception import ThyroidException
from thyroid.logger import logging
import os
import sys
import pandas as pd 
import numpy as np
from sklearn.model_selection import train_test_split
from thyroid.config import feature_cols, TARGET_COLUMN

class DataIngestion:
    
    def __init__(self, data_ingestion_config: config_entity.DataIngestionConfig):
        try:
            logging.info(f"{'>>'*20} Data Ingestion {'<<'*20}")
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise ThyroidException(e, sys)

    def initiate_data_ingestion(self) -> artifact_entity.DataIngestionArtifact:
        try:
            logging.info("Reading dataset file...")
            df = pd.read_csv(self.data_ingestion_config.dataset_file_path)

            logging.info("Dropping 'other' column...")
            df.drop("other", axis=1, inplace=True)

            logging.info("Renaming columns...")
            df.columns = feature_cols

            logging.info("Splitting and processing target column...")
            target = df.target
            splitted_target = target.str.split("[^a-zA-Z]+", expand=True)
            target = splitted_target[0].replace({"": 'Z'})
            df[TARGET_COLUMN] = target

            logging.info("Replacing '?' with NaN...")
            df.replace('?', np.nan, inplace=True)

            logging.info("Dropping unnecessary feature columns...")
            df.drop(['TBG_measured', 'TBG', 'T3_measured', 'TSH measured', 'TT4_measured', 'T4U_measured', 'FTI_measured'], axis=1, inplace=True)

            logging.info("Removing duplicate rows...")
            df.drop_duplicates(inplace=True)

            logging.info("Saving preprocessed dataset to file...")
            df.to_csv(path_or_buf=self.data_ingestion_config.dataset_file_path, index=False, header=True)

            # Prepare artifact
            data_ingestion_artifact = artifact_entity.DataIngestionArtifact(
                dataset_file_path=self.data_ingestion_config.dataset_file_path)

            logging.info(f"Data ingestion artifact: {data_ingestion_artifact}")
            return data_ingestion_artifact

        except Exception as e:
            raise ThyroidException(error_message=e, error_detail=sys)

