from income_prediction.pipeline.pipeline import Pipeline
from income_prediction.exception import IncomeException
from  income_prediction.logger import logging
from  income_prediction.config.configuration import Configuration
def main():
    try:
        pipeline = Pipeline()
        pipeline.run_pipeline()
    except Exception as e:
        logging.error(f"{e}")
        print(e)



if __name__=="__main__":
    main()