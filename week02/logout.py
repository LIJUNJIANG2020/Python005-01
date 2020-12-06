#!/usr/bin/env python

import os
from datetime import datetime
import logging


now_date = datetime.strftime(datetime.now(), "%Y-%m-%d")   
dirpath = os.getcwd() + "/var/log/python-" + now_date
logfile = "logout.log" 


def logFomat(logfile):
    logging.basicConfig(filename=logfile, 
                        level="DEBUG",
                        format="%(asctime)s %(name)s %(levelname)s [line: %(lineno)d] %(message)s"
                        )


def logToFile(info, logfilename=logfile):
    logfile = os.path.join(dirpath, logfilename)
    print(dirpath)
    if not os.path.exists(dirpath):
        os.makedirs(dirpath)

    # logout()
    logFomat(logfile)
    logging.info(info)


    
if __name__ == "__main__":
    logToFile('text')