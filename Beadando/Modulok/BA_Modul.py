import pyautogui
import time

class BA_ImageProcessor:
    def __init__(self, log_callback):
        self.log_message = log_callback  # A callback to log messages to the GUI


    def find_and_click_image(self):
        time.sleep(3)
        try:
            x3, y3 = pyautogui.center(pyautogui.locateOnScreen("kepek/csillag.png", confidence=0.72))
            if x3 != None and y3 != None:
                pyautogui.click(x3, y3)
                self.log_message("Csillag elkapva")
                time.sleep(3)
        except Exception as e:
            pass

        try:
            x3, y3 = pyautogui.center(pyautogui.locateOnScreen("kepek/kagylo.png", confidence=0.85))
            if x3 != None and y3 != None:
                pyautogui.click(x3, y3)
                self.log_message("Kagyló elkapva")
                time.sleep(3)
        except Exception as e:
            pass





