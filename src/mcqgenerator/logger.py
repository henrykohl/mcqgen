import logging
import os
from datetime import datetime


LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

log_path=os.path.join(os.getcwd(),"logs") ## current work directory + "logs"

os.makedirs(log_path,exist_ok=True) ## create the log file


LOG_FILEPATH=os.path.join(log_path,LOG_FILE)


logging.basicConfig(level=logging.INFO,  ## 注意要有 basicConfig
        filename=LOG_FILEPATH,
        format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s"
)