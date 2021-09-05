class Logger:
    _instance = None

    @classmethod
    def get_logger(cls, filename):
        if not Logger._instance:
            print("First time creation")
            Logger._instance = super(Logger, cls).__new__(cls)
            Logger._instance.filename = filename
        return Logger._instance


    def _write_log(self, level, msg):
        with open(file=self.filename, mode="a") as fa:
            fa.write(f"[{level.upper()}] {msg}\n")

    def error(self, msg):
        self._write_log("ERROR", msg)

    def critical(self, msg):
        self._write_log("CRITICAL", msg)

    def warning(self, msg):
        self._write_log("WARNING", msg)

    def info(self, msg):
        self._write_log("INFO", msg)

    def debug(self, msg):
        self._write_log("DEBUG", msg)


if __name__ == "__main__":
    # l = Logger("c:\\Users\\kauma\Documents\\test.log")
    # l.info("test")
    s = Logger.get_logger("c:\\Users\\kauma\Documents\\test.log")
    print("go for second")
    t = Logger.get_logger("c:\\Users\\kauma\Documents\\test.log")
    print("third")
    tr = Logger.get_logger(filename="c:\\Users\\kauma\Documents\\test.log")
    print(s, t, tr)
    s.info("helo")
    t.info("pe")
    tr.warning("final warn")