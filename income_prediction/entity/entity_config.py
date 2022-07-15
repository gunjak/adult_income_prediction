from collections import namedtuple

DataIngestionConfig=namedtuple('DataIngestionConfig',['dataset_url','raw_dir','raw_data_file','ingested_dir',
                                                      'ingested_train_dir','ingested_test_dir'])
TrainingPipelineConfig=namedtuple('TrainingPipelineConfig',['artifact_dir'])