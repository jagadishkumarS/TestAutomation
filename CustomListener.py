from robot.api import logger
import customResult

class CustomListener:
    ROBOT_LISTENER_API_VERSION = 3

    def __init__(self):
        self.suites = 0
        self.tests = 0

    def close(self):
        logger.info(f'All suites completed. Total suites: {self.suites}')
        logger.info(f'Total tests executed: {self.tests}')
        final = str.join("",customResult.data)
        result = customResult.content1+final+customResult.content2
        # print(result)
        with open("CustomReport.html",'w') as file:
            file.write(result)

