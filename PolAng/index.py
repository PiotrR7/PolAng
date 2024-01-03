import tkinter as tk
import subprocess

class Memory:
    root = ""
    chosen_level = ""

class Apk:
    def create_window():
        Memory.root = tk.Tk(); Memory.root.resizable(False,False); Memory.root.title("PolAng"); Memory.root.geometry("900x300")

        tk.Button(Memory.root, text="Easy", width=20, height=3, command=lambda: Apk.open_file("easy_mode.py")
                    ).place(x=70, y=100)
        tk.Button(Memory.root, text="Medium", width=20, height=3, command=lambda: Apk.open_file("medium_mode.py")
                    ).place(x=270, y=100)
        tk.Button(Memory.root, text="Medium Hard", width=20, height=3, command=lambda: Apk.open_file("medium_hard_mode.py")
                    ).place(x=470, y=100)
        tk.Button(Memory.root, text="Hard", width=20, height=3, command=lambda: Apk.open_file("hard_mode.py")
                    ).place(x=670, y=100)

        Memory.root.mainloop()
    
    def open_file(file_name):
        Memory.root.destroy()
        
        try:
            subprocess.run(["python", file_name], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Błąd podczas uruchamiania pliku: {e}")

Apk.create_window()