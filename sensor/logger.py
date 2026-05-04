import logging
import os
from datetime import datetime
import os


LOG_FILE_NAME=f"{datetime.now().strftime('%m%d%Y__%H%M_%S')}.log"

LOG_FILE_DIR=os.path.join(os.getcwd(),"logs")
