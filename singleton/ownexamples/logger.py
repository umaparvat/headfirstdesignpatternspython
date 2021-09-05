
class Singleton(object):
    instance = None
    def __new__(cls, *args, **kwargs):
        if not Singleton.instance:
            instance = super().__new__(cls)
            Singleton.instance = instance
        return Singleton.instance

    def __getattr__(self, name):
        return getattr(self.instance, name)


class Logger(Singleton):
    def __init__(self, filename):
        self.filename = filename

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
    s = Logger("c:\\Users\\kauma\Documents\\test.log")
    t = Logger("c:\\Users\\kauma\Documents\\test.log")
    print(s,t)
    s.info("helo")
    t.debug("te")
    print(s.filename)