import tkinter as tk
import pymysql as mysql
import random as rd
from sql_connect import sql


class HardMode:
    class Memory:
        window = tk.Tk()
        points = tk.StringVar()

        itWas = []
        fakewords_list = []

        points_var = 0
        mistakes = 0
        round_n = 1

        pl = ""; ang = ""; img = ""

        odp1 = ""; odp2 = ""; odp3 = ""; odp4 = ""; odp5 = ""; odp6 = ""


    def Play():
        HardMode.Memory.window.eval('tk::PlaceWindow . center')
        HardMode.Memory.window.resizable(False,False)
        HardMode.Memory.window.title("")

        appwidth = 1920; screenwidth = HardMode.Memory.window.winfo_screenwidth(); x = (screenwidth / 2) - (appwidth / 2)
        appheight = 1080; screenheight = HardMode.Memory.window.winfo_screenheight(); y = (screenheight / 2) - (appheight / 2)

        HardMode.Memory.window.geometry(f'{appwidth}x{appheight}+{int(x)}+{int(y)}')

        pl = tk.StringVar(); pl.set(HardMode.Memory.pl)

        odp1 = tk.StringVar(); odp1.set(HardMode.Memory.odp1)
        odp2 = tk.StringVar(); odp2.set(HardMode.Memory.odp2)
        odp3 = tk.StringVar(); odp3.set(HardMode.Memory.odp3)
        odp4 = tk.StringVar(); odp4.set(HardMode.Memory.odp4)
        odp5 = tk.StringVar(); odp5.set(HardMode.Memory.odp5)
        odp6 = tk.StringVar(); odp6.set(HardMode.Memory.odp6)
        
        tk.Label(image=photos[photosAsStr.index(HardMode.Memory.img)], height=500, width=900
                    ).place(x=500, y=20)
        tk.Label(textvariable=pl, width=10, height=2
                    ).place(x=910,y=600)
        tk.Label(textvariable=HardMode.Memory.points, width=2, height=2
                    ).place(x=20, y=20)

        tk.Button(textvariable=odp1, width=40, height=2, command=lambda: HardMode.IsCorectOdp(HardMode.Memory.odp1)
                            ).place(x=500, y=700)
        tk.Button(textvariable=odp2, width=40, height=2, command=lambda: HardMode.IsCorectOdp(HardMode.Memory.odp2)
                            ).place(x=800, y=700)
        tk.Button(textvariable=odp3, width=40, height=2, command=lambda: HardMode.IsCorectOdp(HardMode.Memory.odp3)
                            ).place(x=1100, y=700)
        tk.Button(textvariable=odp4, width=40, height=2, command=lambda: HardMode.IsCorectOdp(HardMode.Memory.odp4)
                            ).place(x=500, y=750)
        tk.Button(textvariable=odp5, width=40, height=2, command=lambda: HardMode.IsCorectOdp(HardMode.Memory.odp5)
                            ).place(x=800, y=750)
        tk.Button(textvariable=odp6, width=40, height=2, command=lambda: HardMode.IsCorectOdp(HardMode.Memory.odp6)
                            ).place(x=1100, y=750)

        HardMode.Memory.window.mainloop()


    def RandomWord():
        r_num = rd.randrange(0,len(sql.hard_words)-1)
        r_word = str(sql.hard_words[r_num])

        r_word = r_word.replace("'",""); r_word = r_word.replace(")",""); r_word = r_word.replace("(",""); r_word = r_word.split(", ")
        
        id = r_word[0]
        pl = r_word[1]
        HardMode.Memory.ang = r_word[2]
        img = r_word[3]

        img = img.replace(".png","")
        HardMode.Memory.img = img

        if (id in HardMode.Memory.itWas):
            HardMode.RandomWord()
        else: 
            HardMode.Memory.itWas.append(id)
            HardMode.Memory.pl = pl

        fakewords = str(sql.fakewords)
        fakewords = fakewords.replace("'",""); fakewords = fakewords.replace(")",""); fakewords = fakewords.replace("(","")
        fakewords = fakewords.replace("]",""); fakewords = fakewords.replace("[",""); fakewords = fakewords.split(", ")
        
        for x in range(0,len(fakewords)):
            if (x%2 != 0):
                HardMode.Memory.fakewords_list.append(fakewords[x])

        fw1 = HardMode.Memory.fakewords_list[rd.randrange(len(HardMode.Memory.fakewords_list))]
        fw2 = HardMode.Memory.fakewords_list[rd.randrange(len(HardMode.Memory.fakewords_list))]
        fw3 = HardMode.Memory.fakewords_list[rd.randrange(len(HardMode.Memory.fakewords_list))]
        fw4 = HardMode.Memory.fakewords_list[rd.randrange(len(HardMode.Memory.fakewords_list))]
        fw5 = HardMode.Memory.fakewords_list[rd.randrange(len(HardMode.Memory.fakewords_list))]

        whichButton = rd.randrange(1,7)
        
        if (whichButton == 1):
            HardMode.Memory.odp1 = HardMode.Memory.ang
            HardMode.Memory.odp2 = fw1
            HardMode.Memory.odp3 = fw2
            HardMode.Memory.odp4 = fw3
            HardMode.Memory.odp5 = fw4
            HardMode.Memory.odp6 = fw5
        if (whichButton == 2):
            HardMode.Memory.odp1 = fw1
            HardMode.Memory.odp2 = HardMode.Memory.ang
            HardMode.Memory.odp3 = fw2
            HardMode.Memory.odp4 = fw3
            HardMode.Memory.odp5 = fw4
            HardMode.Memory.odp6 = fw5
        if (whichButton == 3):
            HardMode.Memory.odp1 = fw2
            HardMode.Memory.odp2 = fw1
            HardMode.Memory.odp3 = HardMode.Memory.ang
            HardMode.Memory.odp4 = fw3
            HardMode.Memory.odp5 = fw4
            HardMode.Memory.odp6 = fw5
        if (whichButton == 4):
            HardMode.Memory.odp1 = fw3
            HardMode.Memory.odp2 = fw1
            HardMode.Memory.odp3 = fw2
            HardMode.Memory.odp4 = HardMode.Memory.ang
            HardMode.Memory.odp5 = fw4
            HardMode.Memory.odp6 = fw5
        if (whichButton == 5):
            HardMode.Memory.odp1 = fw4
            HardMode.Memory.odp2 = fw1
            HardMode.Memory.odp3 = fw2
            HardMode.Memory.odp4 = fw3
            HardMode.Memory.odp5 = HardMode.Memory.ang
            HardMode.Memory.odp6 = fw5
        if (whichButton == 6):
            HardMode.Memory.odp1 = fw5
            HardMode.Memory.odp2 = fw1
            HardMode.Memory.odp3 = fw2
            HardMode.Memory.odp4 = fw3
            HardMode.Memory.odp5 = fw4
            HardMode.Memory.odp6 = HardMode.Memory.ang


    def IsCorectOdp(x):
        if HardMode.Memory.round_n <= 20:
            HardMode.Memory.round_n += 1

            if x == HardMode.Memory.ang:
                HardMode.Memory.points_var += 1
                HardMode.Memory.points.set(HardMode.Memory.points_var)
            else:
                HardMode.Memory.mistakes += 1
                if HardMode.Memory.mistakes == 3:
                    HardMode.Memory.round_n = 21

            HardMode.RandomWord()

            # Update the window with new content
            HardMode.update_window()
        else:
            HardMode.End()

    def update_window():
        # Destroy all widgets in the current window
        for widget in HardMode.Memory.window.winfo_children():
            widget.destroy()

        # Re-create and place the necessary widgets
        pl = tk.StringVar()
        pl.set(HardMode.Memory.pl)
        
        odp1 = tk.StringVar(); odp1.set(HardMode.Memory.odp1)
        odp2 = tk.StringVar(); odp2.set(HardMode.Memory.odp2)
        odp3 = tk.StringVar(); odp3.set(HardMode.Memory.odp3)
        odp4 = tk.StringVar(); odp4.set(HardMode.Memory.odp4)
        odp5 = tk.StringVar(); odp5.set(HardMode.Memory.odp5)
        odp6 = tk.StringVar(); odp6.set(HardMode.Memory.odp6)
        
        tk.Label(image=photos[photosAsStr.index(HardMode.Memory.img)], height=500, width=900
                    ).place(x=500, y=20)
        tk.Label(textvariable=pl, width=10, height=2
                    ).place(x=910,y=600)
        tk.Label(textvariable=HardMode.Memory.points, width=2, height=2
                    ).place(x=20, y=20)

        tk.Button(textvariable=odp1, width=40, height=2, command=lambda: HardMode.IsCorectOdp(HardMode.Memory.odp1)
                            ).place(x=500, y=700)
        tk.Button(textvariable=odp2, width=40, height=2, command=lambda: HardMode.IsCorectOdp(HardMode.Memory.odp2)
                            ).place(x=800, y=700)
        tk.Button(textvariable=odp3, width=40, height=2, command=lambda: HardMode.IsCorectOdp(HardMode.Memory.odp3)
                            ).place(x=1100, y=700)
        tk.Button(textvariable=odp4, width=40, height=2, command=lambda: HardMode.IsCorectOdp(HardMode.Memory.odp4)
                            ).place(x=500, y=750)
        tk.Button(textvariable=odp5, width=40, height=2, command=lambda: HardMode.IsCorectOdp(HardMode.Memory.odp5)
                            ).place(x=800, y=750)
        tk.Button(textvariable=odp6, width=40, height=2, command=lambda: HardMode.IsCorectOdp(HardMode.Memory.odp6)
                            ).place(x=1100, y=750)
        
        # Update the window
        HardMode.Memory.window.update_idletasks()


    def End():
        for widget in HardMode.Memory.window.winfo_children():
            widget.destroy()

        if (HardMode.Memory.points_var == 20):
            cytat = "Prawdziwy sukces to spełnienie celów, które dają nam radość i poczucie spełnienia.\nTrue success is achieving goals that give us joy and a sense of fulfillment."
        elif (HardMode.Memory.points_var >= 15):
            cytat = "Sukces to nie klucz do szczęścia. Szczęście to klucz do sukcesu. Jeśli kochasz to, co robisz, osiągniesz sukces.\nSuccess is not the key to happiness. Happiness is the key to success. If you love what you do, you will succeed."
        elif (HardMode.Memory.points_var >= 10):
            cytat = "Nie możesz zmienić kierunku wiatru, ale możesz dostosować ustawienia swoich żagli, aby dotrzeć tam, gdzie chcesz.\nYou can't change the direction of the wind, but you can adjust the settings of your sails to get where you want."
        elif (HardMode.Memory.points_var >= 5):
            cytat = "Nie ma skrótu, aby osiągnąć sukces trwający. Trzeba pracować ciężko i nie przestawać wierzyć w siebie.\nThere is no shortcut to achieving lasting success. You have to work hard and never stop believing in yourself."
        elif (HardMode.Memory.points_var < 5):
            cytat = "Szczęścia szukaj blisko siebie, bo ono jest w drobnych, codziennych radościach.\nLook for happiness close to yourself, because it is found in small, everyday joys."

        write = "Twój wynik to: "+str(HardMode.Memory.points_var)+"/20\n"+str(cytat)

        label = tk.Label(text=write).pack()

            
from em_photos import *

HardMode.RandomWord()
HardMode.Play()