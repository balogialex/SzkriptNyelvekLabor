import tkinter as tk
from tkinter import scrolledtext
import threading
import pyautogui
import time
#import cv2

# Define the main application
class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Automation App")
        self.is_running = False
        self.thread = None

        # Create Start, Stop buttons and Log section
        self.start_button = tk.Button(root, text="Start", command=self.start_script)
        self.start_button.grid(row=0, column=0, padx=10, pady=10)

        self.stop_button = tk.Button(root, text="Stop", command=self.stop_script, state=tk.DISABLED)
        self.stop_button.grid(row=0, column=1, padx=10, pady=10)

        self.log_text = scrolledtext.ScrolledText(root, width=100, height=30)
        self.log_text.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

    # Start script method
    def start_script(self):
        self.is_running = True
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.log_message("Script started...")
        self.thread = threading.Thread(target=self.run_script)
        self.thread.start()

    # Stop script method
    def stop_script(self):
        self.is_running = False
        self.log_message("Script stopped.")
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)

    # Add messages to the log
    def log_message(self, message):
        self.log_text.insert(tk.END, f"{message}\n")
        self.log_text.yview(tk.END)

    # Script logic for locating and clicking images
    def run_script(self):
        while self.is_running:
            try:
                # Path to the image to locate (replace with your own image)
                image_path = "proba.png"

                # Locate the image on the screen
                location = pyautogui.locateOnScreen(image_path, confidence=0.8)

                if location:
                    pyautogui.click(location)
                    self.log_message(f"Clicked on {image_path} at {location}")
                else:
                    self.log_message(f"Image not found on the screen.")

                time.sleep(20)  # Wait for a while before next attempt

            except Exception as e:
                self.log_message(f"Error: {str(e)}")
                break

# Create the main window
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
