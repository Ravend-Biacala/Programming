import logging
import logging.config
import os, sys
# from datetime import datetime
# currTime = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

path = os.path.dirname(os.path.realpath(__file__))
mdir = False
if not os.path.exists(path+'\log'):
    os.makedirs(path+'\log')
    mdir = True
    print("Created Log directory")

logpath = path+'\log\log_test.txt'
logging.basicConfig(filename=logpath, level=logging.INFO, format='%(asctime)s : %(message)s ')

logging.info("="*10+"Start Log"+"="*10)
if mdir:
    logging.info("Created Log directory")


logging.info("test")


logging.info("="*11+"End log"+"="*11)




