#!/usr/bin/python3

import tkinter as tk
import pyautogui
import threading
from pynput.keyboard import Key, Listener

def on_press(key):
    print('{0} pressed'.format(
        key))
    if (key == Key.f8):
        print('F8!')
        say_hi()
    elif (key == Key.f9):
        print('F9!')
        say_bye()

def on_release(key):
    print('{0} release'.format(
        key))
    if key == Key.esc:
        return False

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

class kbthread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self._stopper = threading.Event()

    def stopit(self):
        self._stopper.set()

    def stopped(self):
        return self._stopper.is_set()

    def run(self):
        with Listener(
                on_press=on_press,
                on_release=on_release) as self.listener:
            self.listener.join()

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.start = tk.Button(self)
        self.start["text"] = "Start(F8)"
        self.start["command"] = say_hi
        self.start.pack(side="top")

        self.stop = tk.Button(self)
        self.stop["text"] = "Stop(F9)"
        self.stop["command"] = say_bye
        self.stop.pack(side="top")

def say_hi():
    if (t.isAlive() == False):
        t.start()

def say_bye():
    global t
    if (t.isAlive() == True and t.stopped() == False):
        t.stopit()
        t.join()
        t = thread()

def on_closing():
    kb.listener.stop()
    root.destroy()

t = thread()
kb = kbthread()
kb.start()
root = tk.Tk()
app = Application(master=root)

root.protocol("WM_DELETE_WINDOW", on_closing)
app.mainloop()
