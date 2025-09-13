from pynput import keyboard
class Keystrokelistener:
    def __init__(self,on_press_callback):
    self.on_press_callback=on_press_callback
    self.listener=pynput.keyboard.Listener