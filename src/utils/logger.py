import datetime
class Filelogger:
    def __init__(self,filename):
        self.filename=filename
    def log_keystroke(self,key):
        with open(self.filename,'a') as f:
            time=datetime.datetime.now().isoformat()
            log=f"{str(time)}:{key}\n"
            f.write(log)