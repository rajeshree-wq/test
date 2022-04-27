import logging

class LogGen:
    @staticmethod
    def loggen():
        # logging.basicConfig(filename=".\\Logs",
        #                     format='%(asctime)s %(levelname)s:%(message)s', datefmt='%m%d%Y %I%M%S %P'
        #                     )
        # logging.basicConfig(filename='.\\logs\\automation.log', mode='a')
        # logger=logging.getLogger()
        # logger.setLevel(logging.INFO)
        # return logger

        logger = logging.getLogger()
        fhandler = logging.FileHandler(filename='.\\Logs\\automation.log', mode='a')
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fhandler.setFormatter(formatter)
        logger.addHandler(fhandler)
        logger.setLevel(logging.INFO)
        return logger