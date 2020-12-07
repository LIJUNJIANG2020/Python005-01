#!/usr/bin/env python

import os
from datetime import datetime
import logging
from pathlib import Path


now_date = datetime.strftime(datetime.now(), "%Y-%m-%d")   

# os.getcwd() 获取的不是当前脚本所在目录，而是所运行脚本的父目录
# dirpath = os.getcwd() + "/var/log/python-" + now_date
dirpath = Path(__file__).parent.parent.joinpath('var', 'log', "python-"+now_date)
# print(dirpath)
logfile = "logout.log" 


def logFomat(logfile):
    logging.basicConfig(filename=dirpath.joinpath(logfile), 
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