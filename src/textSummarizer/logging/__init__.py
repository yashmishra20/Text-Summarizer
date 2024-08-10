import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"
log_dir = "logs"
log_filepath = os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir, exist_ok=True)



logging.basicConfig(
    level= logging.INFO,
    format= logging_str,

    handlers=[
        logging.FileHandler(log_filepath),  #It will make an file for the logging.
        logging.StreamHandler(sys.stdout)   #It will show the log in the terminal.
    ]
)

logger = logging.getLogger("textSummarizerLogger")