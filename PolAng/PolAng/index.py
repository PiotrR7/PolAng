import tkinter as tk
from easy_mode import EasyMode
from medium_mode import MediumMode
from medium_hard_mode import MediumHardMode
from hard_mode import HardMode

class Memory:
    root = ""
    chosen_level = ""

class Apk:
    def root_open():
        EasyMode.Memory.window.withdraw()
        MediumMode.Memory.window.withdraw()
        MediumHardMode.Memory.window.withdraw()
        HardMode.Memory.window.withdraw()

        Memory.root = tk.Tk()
        Memory.root.resizable(False,False)
        Memory.root.title("")
        Memory.root.geometry("900x300")

        tk.Button(Memory.root, text="Easy", width=20, height=3, command=lambda: Apk.Level("easy")).place(x=70, y=100)
        tk.Button(Memory.root, text="Medium", width=20, height=3, command=lambda: Apk.Level("medium")).place(x=270, y=100)
        tk.Button(Memory.root, text="Medium Hard", width=20, height=3, command=lambda: Apk.Level("medium_hard")).place(x=470, y=100)
        tk.Button(Memory.root, text="Hard", width=20, height=3, command=lambda: Apk.Level("hard")).place(x=670, y=100)

        Memory.root.mainloop()
    
    def Level(arg):
        Memory.chosen_level = arg
        Memory.root.destroy()
        if (Memory.chosen_level == "easy"):
            EasyMode.RandomWord()
            EasyMode.Play()
        if (Memory.chosen_level == "medium"):
            MediumMode.RandomWord()
            MediumMode.Play()
        if (Memory.chosen_level == "medium_hard"):
            HardMode.RandomWord()
            HardMode.Play()
        if (Memory.chosen_level == "hard"):
            MediumHardMode.RandomWord()
            MediumHardMode.Play()

Apk.root_open()