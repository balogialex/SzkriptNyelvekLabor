import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import threading
import time
import Modulok.BA_Modul as BAModul


class BAScriptRunner:
    def __init__(self, log_widget):
        self.running = False
        self.log_widget = log_widget
        self.script_thread = None

    def start_script(self):
        self.running = True
        self.log("Script started")
        self.script_thread = threading.Thread(target=self.run_script)
        self.script_thread.start()

    def stop_script(self):
        self.running = False
        self.log("Script stopped")

    def run_script(self):
        while self.running:
            # Here should be the image locating and clicking logic
            self.log("Clicked at a specific location.")
            time.sleep(2)  # Dummy delay for simulating script

    def log(self, message):
        self.log_widget.insert(tk.END, message + '\n')
        self.log_widget.see(tk.END)


def start():
    if not runner.running:
        runner.start_script()


def stop():
    if runner.running:
        runner.stop_script()


def create_gui():
    root = tk.Tk()
    root.title("ABC App")

    start_button = tk.Button(root, text="Start", command=start)
    start_button.pack(pady=10)

    stop_button = tk.Button(root, text="Stop", command=stop)
    stop_button.pack(pady=10)

    log_area = ScrolledText(root, wrap=tk.WORD, height=10)
    log_area.pack(padx=10, pady=10)

    return root, log_area


if __name__ == "__main__":
    root, log_area = create_gui()
    runner = BAScriptRunner(log_area)
    root.mainloop()