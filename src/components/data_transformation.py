## here we do feature enginerring , eda, feature transformation

import sys
import numpy as np
import pandas as pd
from dataclasses import dataclass
# it uses to convert the columns to any other form 
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler,OneHotEncoder,LabelEncoder

from src.exception import CustomException
from src.logger import logging
import os

from src.utils import save_object


@dataclass
class DataTransformationConfig:
  preprocessor_obj_file_path = os.path.join("Crops","preprocessor.pkl")
  label_encoder_file_path = os.path.join("Crops","label_encoder.pkl")


class DataTransformation:
  def __init__(self):
    self.data_transformation_config = DataTransformationConfig()

  def get_data_preprocessor(self):
    try:
      # numerical_cols = ['BMI', 'MentHlth', 'PhysHlth', 'Age']
      num_features = ['N','P','K','temperature','humidity','ph','rainfall']

        # 2️⃣ Binary columns (0/1) - no transformation needed
      # binary_cols = ['HighBP', 'HighChol', 'CholCheck', 'Smoker', 'Stroke',
      #                  'HeartDiseaseorAttack', 'PhysActivity', 'Fruits', 'Veggies',
      #                  'HvyAlcoholConsump', 'AnyHealthcare', 'NoDocbcCost', 'DiffWalk', 'Sex']

        # 3️⃣ Multi-class categorical columns → One-hot encode
      # categorical_cols = ['Education', 'Income', 'GenHlth']

        # Numerical Pipeline
      num_pipeline = Pipeline(
        steps=[
          ("imputer",SimpleImputer(strategy="median")),
          ("scaler",StandardScaler())
        ])

        ## categorical pipeline
      # cat_pipeline = Pipeline(
      #     steps=[
      #     ("imputer",SimpleImputer(strategy="most_frequent")),
      #     ("one_hot",OneHotEncoder(handle_unknown="ignore"))
      #   ])

      logging.info(f"numerical Columns:{num_features}")
      # logging.info(f"categorical Columns:{categorical_cols}")

        # combine piplines 
      preprocessor = ColumnTransformer([
          ("numerical", num_pipeline, num_features),
          # ("category",cat_pipeline,categorical_cols)
        ],remainder='passthrough') # like others cols like binary should be as it is

      return preprocessor
    except Exception as e:
      raise CustomException(e,sys)
      
  def data_transformation(self,train_path,test_path):
    try:
      train_df = pd.read_csv(train_path)
      test_df = pd.read_csv(test_path)

      logging.info("Read the train and test")

      logging.info("Obtaining preprocessing object")

      preprocessor = self.get_data_preprocessor()

        # separate targets on training 
      target_col = "label"
      X_train = train_df.drop(columns=[target_col],axis=1)
      y_train = train_df[target_col]
      logging.info("done with X_train and y_train ")

        # separate targets on testing 
      X_test = test_df.drop(columns=[target_col],axis=1)
      y_test = test_df[target_col]
      logging.info("done with X_test and y_test ")

      # Encoded the target Columns
      le = LabelEncoder()
      y_train_encoded = le.fit_transform(y_train)
      y_test_encoded = le.transform(y_test)

        # fit on train , tranform on train and test
      X_train_transform = preprocessor.fit_transform(X_train)
      X_test_transform = preprocessor.transform(X_test)

      train_arr = np.c_[X_train_transform,np.array(y_train_encoded)]

      test_arr = np.c_[X_test_transform,np.array(y_test_encoded)]

      logging.info("saved preprocessing objects")

      save_object(
        file_path = self.data_transformation_config.preprocessor_obj_file_path,
        obj = preprocessor
      )

      save_object(
        file_path = self.data_transformation_config.label_encoder_file_path,
        obj = le
      )
      return (
        train_arr,
        test_arr,
        self.data_transformation_config.preprocessor_obj_file_path,
        self.data_transformation_config.label_encoder_file_path
      )
    except Exception as e:
      raise CustomException(e,sys)
      
