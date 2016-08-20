#!/usr/bin/python3

import tkinter as tk
import pyautogui
import threading
from pynput.keyboard import Key, Listener

def on_press(key):
    if (key == Key.f8):
        startclick()
    elif (key == Key.f9):
        stopclick()

class thread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self._stopper = threading.Event()

    def stopit(self):
        self._stopper.set()

    def stopped(self):
        return self._stopper.is_set()

    def run(self):
        self._stopper = threading.Event()
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
        self.start["command"] = startclick
        self.start.pack(side="top")

        self.stop = tk.Button(self)
        self.stop["text"] = "Stop(F9)"
        self.stop["command"] = stopclick
        self.stop.pack(side="top")

def startclick():
    if (t.isAlive() == False):
        t.start()

def stopclick():
    global t
    if (t.isAlive() == True and t.stopped() == False):
        t.stopit()
        t.join()
        t = thread()

def on_closing():
    kb.stop()
    root.destroy()

t = thread()
kb = Listener(on_press=on_press, on_release=None)
kb.start()
root = tk.Tk()
app = Application(master=root)

root.protocol("WM_DELETE_WINDOW", on_closing)
app.mainloop()
