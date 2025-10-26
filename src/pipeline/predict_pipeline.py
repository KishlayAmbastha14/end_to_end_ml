import pandas as pd
import numpy as np
import pickle
import os
import sys
from src.exception import CustomException
from src.logger import logging

from src.utils import load_object

try: 
  class CropPredictionPipeline:
    def __init__(self):
      self.preprocessor_path = os.path.join("Crops","preprocessor.pkl")
      self.label_encoder_path = os.path.join("Crops","label_encoder.pkl")
      self.model_path = os.path.join("Crops","model.pkl")

      # self.preprocessor = pickle.load(open("Crops/preprocessor.pkl", "rb"))
      # self.model = pickle.load(open("Crops/model.pkl", "rb"))
      # self.label_encoder = pickle.load(open("Crops/label_encoder.pkl", "rb"))


      self.preprocessor = load_object(file_path=self.preprocessor_path)
      self.label_encoder = load_object(file_path=self.label_encoder_path)
      self.model = load_object(file_path = self.model_path)

    def predict(self,input_data:dict):
      
      logging.info("converted dict to DataFrame")
      df = pd.DataFrame([input_data])

      logging.info("apply preprocessing")
      X = self.preprocessor.transform(df)

      logging.info("model prediction has done")
      y_pred = self.model.predict(X)

      logging.info("ensure that y_pred is integer type before inverse transform")
      y_pred = np.array(y_pred).astype(int)

      logging.info("decode numeric value to actual crop name")
      label = self.label_encoder.inverse_transform(y_pred)[0]

      return label
    
except Exception as e:
  raise CustomException(e,sys)

