import logging
import logging.config
import os, sys
from datetime import datetime

now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")


path = os.path.dirname(os.path.realpath(__file__))
print(path)
logpath = path+'\log_test'
#replace print statements with log statements
logging.basicConfig(filename=logpath, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s: ')
logging.basicConfig(filename=logpath, level=logging.WARNING, format='%(asctime)s - %(levelname)s - %(message)s: ')

# logger = logging.getLogger(__name__)
# logger.setLevel(logging.INFO)
# formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')
# file_handler = logging.FileHandler(logpath)

#logging.info("=================Start Log==============").setFormatter(logging.Formatter('%(asctime)s'))
# logging.info(now)

logging.info("=================Start Log==============")

# a = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# print(a)

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x ,y):
    return x * y

def divide(x, y):
    return x / y


num_1 = 10
num_2 = 5

add_result = add(num_1, num_2)
logging.info('Add: {} + {} = {}'.format(num_1, num_2, add_result))
#logging only gets string

sub_result = subtract(num_1, num_2)
logging.info('Add {} + {} = {}'.format(num_1, num_2, add_result))


logging.info("=================End Log==============")
logging.warning("=================End Log==============")