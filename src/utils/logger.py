import time
class Filelogger:
    def __init__(self,filename):
        self.filename=filename
    def log_keystroke(self,key):
        with open(self.filename,'a') as f:
            log=f"{str(time.time())}-{key}\n"
            f.write(log)