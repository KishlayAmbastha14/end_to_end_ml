from dataclasses import dataclass
from src.exception import CustomException
from src.logger import logging
import os, sys
import pandas as pd
from sklearn.model_selection import train_test_split
from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig

from src.components.model_training import Model_Trainer
from src.components.model_training import Model_Trainer_Config

## iha hamne iska bataya kha safe krna data ko
@dataclass
class DataIngestionConfig:
  train_data_path : str=os.path.join("Crops","train.csv")
  test_data_path : str=os.path.join("Crops","test.csv")
  raw_data_path : str=os.path.join("Crops","data.csv")
  logging.info("created the path for train and test datas ")


class DataIngestion:
  def __init__(self):
    self.ingestion_config = DataIngestionConfig()

  
  def initiate_data_ingestion(self):
    logging.info("entered into data ingestion components")

    try:
      df = pd.read_csv("notebook\data\Crop_recommendations.csv")
      logging.info("read the dataset as df")

      # loaded the raw data
      # this next line checking that ki ye artifact folder exist krta hai ki nhi ydi nhi krta to new bna do else ok
      os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path),exist_ok=True)

      df.to_csv(self.ingestion_config.raw_data_path,index=False)
      logging.info("save the raw data")

      # ye bhi check krega ki jha train.csv save krna hai wo folder hai ki nhi if not then make this
      os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)

      logging.info("train test split started")
      train_set,test_set = train_test_split(df,test_size=0.2,random_state=42)

      train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
      test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

      logging.info("ingestions of data is completeed in train , test , df")

      return(
        self.ingestion_config.train_data_path,
        self.ingestion_config.test_data_path
      )
    except Exception as e:
      raise CustomException(e,sys)

if __name__ == "__main__":
  obj = DataIngestion()
  train_data,test_data = obj.initiate_data_ingestion()

  data_transformations = DataTransformation()
  train_arr,test_arr,preprocessor_path, label_encoder_path = data_transformations.data_transformation(train_data,test_data)

  model_train = Model_Trainer()
  print(model_train.initiate_model_training(train_arr,test_arr))
  print()

