class Logger:
    __instance = None
    __count = 0

    @staticmethod
    def getInstance():
        if Logger.__instance is None:
            Logger.__instance = Logger()
        return Logger.__instance

    def log(self, message):
        self.__count += 1
        print(f"{message} (Log count: {self.__count})")
        

if __name__ == "__main__":
    logger = Logger.getInstance()
    logger.log("First log message.")
    another_logger = Logger.getInstance()
    another_logger.log("Second log message.")