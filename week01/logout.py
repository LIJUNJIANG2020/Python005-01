#!/usr/bin/env python

import os
from datetime import datetime
import logging


now_date = datetime.strftime(datetime.now(), "%Y-%m-%d")   
dirpath = os.getcwd() + "/var/log/python-" + now_date
logfile = "logout.log" 

def logToFile(logfilename=logfile):
    logfile = os.path.join(dirpath, logfilename)

    if not os.path.exists(dirpath):
        os.makedirs(dirpath)

    logging.basicConfig(filename=logfile, 
                    level="DEBUG",
                    format="%(asctime)s %(name)s %(levelname)s [line: %(lineno)d] %(message)s"
                        )
    
    logging.info("The function logToFile is called")


    
if __name__ == "__main__":
    logToFile()