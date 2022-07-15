import os,sys
from income_prediction.logger import logging
from income_prediction.exception import IncomeException
from income_prediction.entity.entity_config import DataIngestionConfig
from income_prediction.component.data_ingestion import DataIngestion
from income_prediction.config.configuration import  Configuration
from income_prediction.entity.artifact_entity import DataIngestionArtifact

class Pipeline:
    
    def __init__(self,config: Configuration = Configuration()) -> None:
        try:
            self.config=config

        except Exception as e:
            raise IncomeException(e,sys) from e

    def start_data_ingestion(self)->DataIngestionArtifact:
        try:
            data_ingestion = DataIngestion(data_ingestion_config=self.config.get_data_ingestion_config())
            return data_ingestion.initiate_data_ingestion()
        except Exception as e:
            raise IncomeException(e,sys) from e   
    def run_pipeline(self):
        try:
            #data ingestion

            data_ingestion_artifact = self.start_data_ingestion()
        except Exception as e:
            raise IncomeException(e,sys) from e