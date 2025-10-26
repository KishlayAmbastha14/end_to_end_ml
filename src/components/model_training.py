from src.logger import logging
import sys 
import os
from src.exception import CustomException
from dataclasses import dataclass

from catboost import CatBoostClassifier
from sklearn.ensemble import (
  AdaBoostClassifier,
  GradientBoostingClassifier,
  RandomForestClassifier
)

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix,accuracy_score,classification_report
from sklearn.tree import DecisionTreeClassifier
from xgboost import XGBClassifier

from src.utils import save_object,evaluate_model

@dataclass
class Model_Trainer_Config:
  model_trainer_file_path = os.path.join("Crops","model.pkl")


class Model_Trainer:
  def __init__(self):
    self.model_trainer_config = Model_Trainer_Config()

  def initiate_model_training(self,train_array,test_array):
    try:
      logging.info("Splitting training and test input data")
      X_train,y_train,X_test,y_test = (
        train_array[:,:-1],
        train_array[:,-1],
        test_array[:,:-1],
        test_array[:,-1]
      )

      # models = {
      #   "Logistic Regression" : LogisticRegression(max_iter=400),
      #   "Decision Tree" : DecisionTreeClassifier(),
      #   "Random Forest" : RandomForestClassifier(),
      #   "XGB Classifier" : XGBClassifier(),
      #   "Cat Boost Classifier" : CatBoostClassifier(),
      #   "Ada Boost Classifier" : AdaBoostClassifier(),
      #   "Gradient Boost Classifier" : GradientBoostingClassifier()
      # }
      models = {
    "Logistic Regression": LogisticRegression(max_iter=500),
    "Decision Tree": DecisionTreeClassifier(max_depth=6),
    "Random Forest": RandomForestClassifier(
        n_estimators=100, max_depth=8, n_jobs=-1, random_state=42
    )
  }

      model_report : dict = evaluate_model(X_train=X_train, y_train=y_train,X_test=X_test,y_test=y_test, models = models)

      # to get the best model_score from dict
      best_model_score = max(sorted(model_report.values()))

      # to get the best model name from dict
      best_model_name = list(model_report.keys())[list(model_report.values()).index(best_model_score)]

      best_model = models[best_model_name]

      if best_model_score < 0.6 :
        raise CustomException("no best model is found")
      
      logging.info(f"best model found on both training and testing dataset is {best_model}")

      save_object(
        file_path = self.model_trainer_config.model_trainer_file_path,
        obj = best_model
      )

      predicted = best_model.predict(X_test)
      score = accuracy_score(y_test,predicted)
      
      return score
    
    except Exception as e:
      raise CustomException(e,sys)
