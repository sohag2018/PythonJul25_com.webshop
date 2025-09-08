import logging
from datetime import datetime
from selenium import webdriver
class LogGen:
    @staticmethod
    def logGen():
        timestamp=datetime.now().strftime('%y%m%d%H%M%S')
        logging.basicConfig(
            filename=f'C:/Users/enthr/PycharmProjects/com.demoshop/Log/log_{timestamp}.log',
            filemode='w',
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            force=True,
            datefmt='%m/%d/%Y %I:%M:%S %p'
        )
        logger= logging.getLogger()
        return logger

LogGen.logGen().info("Logging started")




