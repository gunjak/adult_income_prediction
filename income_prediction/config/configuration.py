from income_prediction.entity.entity_config import TrainingPipelineConfig
from income_prediction.logger import  logging
from income_prediction.exception import IncomeException
from income_prediction.entity.entity_config import DataIngestionConfig
import os,sys
from income_prediction.constant import *
from income_prediction.util.util import  read_yaml_file

class Configuration:
    def __init__(self,config_file_path:str=CONFIG_FILE_PATH,current_time_stamp=CURRENT_TIME_STAMP)->None:
        try:
            self.config_info=read_yaml_file(file_path=config_file_path)
            self.training_pipeline_config=self.get_training_pipeline_config()
            self.current_time_stamp=current_time_stamp
        except Exception as  e:
            raise IncomeException(e,sys)from e
    def get_data_ingestion_config(self)->DataIngestionConfig:
        try:
            artifact_dir=self.training_pipeline_config.artifact_dir
            data_ingestion_artifact_dir=os.path.join(artifact_dir,
                                                    DATA_INGESTION_ARTIFACT_DIR,
                                                    self.current_time_stamp)
            data_ingestion_info=self.config_info[DATA_INGESTION_CONFIG_KEY]
            dataset_url=data_ingestion_info[DATA_INGESTION_DOWNLOAD_URL_KEY]
            raw_data_dir=os.path.join(data_ingestion_artifact_dir,
                                    data_ingestion_info[DATA_INGESTION_RAW_DATA_DIR_KEY])
            raw_data_file=os.path.join(data_ingestion_artifact_dir,raw_data_dir,
                                    data_ingestion_info[DATA_INGESTION_RAW_DATA_FILE])
            
            ingested_dir=os.path.join(data_ingestion_artifact_dir,
                                    data_ingestion_info[DATA_INGESTION_INGESTED_DIR_NAME_KEY])
            ingested_train_dir=os.path.join(ingested_dir,
                                            data_ingestion_info[DATA_INGESTION_TRAIN_DIR_KEY])
            ingested_test_dir=os.path.join(ingested_dir,data_ingestion_info[DATA_INGESTION_TEST_DIR_KEY])
            data_ingestion_config=DataIngestionConfig(dataset_url=dataset_url,
                                                    raw_dir=raw_data_dir,
                                                    raw_data_file=raw_data_file,
                                                    ingested_dir=ingested_dir,
                                                    ingested_train_dir=ingested_train_dir,
                                                    ingested_test_dir=ingested_test_dir)
            logging.info(f'Data ingestion config:{data_ingestion_config}')
            return data_ingestion_config
        except Exception as e:
            raise IncomeException(e,sys) from e           
        
    def get_training_pipeline_config(self)->TrainingPipelineConfig:
        try:
            training_pipeline_config_key=self.config_info[TRAINING_PIPELINE_CONFIG_KEY]
            artifact_dir=os.path.join(ROOT_DIR,training_pipeline_config_key[TRAINING_PIPELINE_NAME_KEY],
                                      training_pipeline_config_key[TRAINING_PIPELINE_ARTIFACT_DIR_KEY])
            training_pipeline_config=TrainingPipelineConfig(artifact_dir=artifact_dir)
            logging.info(f'taining pipeline config:{artifact_dir}')
            return training_pipeline_config
        except Exception as e:
            raise IncomeException(e,sys) from e
                  
        
