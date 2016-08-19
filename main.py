#!/usr/bin/python3

import tkinter as tk
import pyautogui
import threading

class thread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self._stopper = threading.Event()

    def stopit(self):
        self._stopper.set()

    def stopped(self):
        return self._stopper.is_set()

    def run(self):
        while (self._stopper.is_set() == False):
            pyautogui.click()

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.start = tk.Button(self)
        self.start["text"] = "Start(F8)"
        self.start["command"] = self.say_hi
        self.start.pack(side="top")

        self.stop = tk.Button(self)
        self.stop["text"] = "Stop(F9)"
        self.stop["command"] = self.say_bye
        self.stop.pack(side="top")

    def say_hi(self):
        if (t.isAlive() == False):
            t.start()

    def say_bye(self):
        if (t.isAlive() == True and t.stopped() == False):
            t.stopit()
            t.join()

def on_closing():
    root.destroy()

t = thread()

root = tk.Tk()
app = Application(master=root)

root.protocol("WM_DELETE_WINDOW", on_closing)
app.mainloop()
