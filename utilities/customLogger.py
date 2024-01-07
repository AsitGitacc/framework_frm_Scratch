import logging


class LogGen:
    # location of log to be generated , format of log and timestamp format

    @staticmethod
    def loggen():
        logging.basicConfig(filename=".\\Logs\\logforautomation.log",
                            format='%(asctime)s : %(levelname)s : %(message)s',
                            datefmt='%Y-%m-%d %H:%M:%S')

        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
