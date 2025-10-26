# any exceutions or problem is happend we can logged in some files so that we can tracks them

import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

LOG_DIR = "crop_logs"

logs_path = os.path.join(os.getcwd(),LOG_DIR)
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
  filename=LOG_FILE_PATH,
  format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
  level=logging.INFO,

)


if __name__ == "__main__":
  logging.info("Logging has started")
  logging.warning("This is a warning log")
  logging.error("This is an error log")
  print(f"Log file created at: {LOG_FILE_PATH}")