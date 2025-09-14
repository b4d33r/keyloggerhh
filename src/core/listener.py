from pynput import keyboard
class Keystrokelistener:
    def __init__(self,on_press_callback):
        self.on_press_callback=on_press_callback
        self.listener=keyboard.Listener(on_press=self._on_press)
    def _on_press(self,key):
        try:
            key=key.char
        except AttributeError:
            key=str(key)
        self.on_press_callback(key)
    def start(self):
        self.listener.start()
    def join(self):
        self.listener.join()
    def stop(self):
        self.listener.stop()