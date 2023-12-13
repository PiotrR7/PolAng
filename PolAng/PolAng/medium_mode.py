import tkinter as tk
import pymysql as mysql
import random as rd
from sql_connect import sql


# wyświetla się obrazek/ user wybiera 1 z 6 odpowiedzi wylosowanych z bazy/ jak źle naciśnie wyświetla się zdjęcie tego co kliknął/ następuje 2 próba/
# przy dobrej odpowiedzi l.punktów + 1/ możliwość 4 pomyłek/ po zakończeniu wyświetla wynik i w zależności od zdobytych punktów cytat motywujący po polsku i angielsku

class MediumMode:
    class Memory:
        window = tk.Tk()
        points = tk.StringVar()
        points_var = 0
        itWas = []
        fakewords_list = []
        mistakes = 0
        round_n = 1
        pl = ""
        ang = ""
        img = ""
        odp1 = ""
        odp2 = ""
        odp3 = ""
        odp4 = ""
        odp5 = ""
        odp6 = ""

    def Play():
        MediumMode.Memory.window.eval('tk::PlaceWindow . center')
        MediumMode.Memory.window.resizable(False,False)
        MediumMode.Memory.window.title("")

        appwidth = 1920
        appheight = 1080

        screenwidth = MediumMode.Memory.window.winfo_screenwidth()
        screenheight = MediumMode.Memory.window.winfo_screenheight()
        
        x = (screenwidth / 2) - (appwidth / 2)
        y = (screenheight / 2) - (appheight / 2)

        MediumMode.Memory.window.geometry(f'{appwidth}x{appheight}+{int(x)}+{int(y)}')

        pl = tk.StringVar()
        pl.set(MediumMode.Memory.pl)
        odp1 = tk.StringVar()
        odp1.set(MediumMode.Memory.odp1)
        odp2 = tk.StringVar()
        odp2.set(MediumMode.Memory.odp2)
        odp3 = tk.StringVar()
        odp3.set(MediumMode.Memory.odp3)
        odp4 = tk.StringVar()
        odp4.set(MediumMode.Memory.odp4)
        odp5 = tk.StringVar()
        odp5.set(MediumMode.Memory.odp5)
        odp6 = tk.StringVar()
        odp6.set(MediumMode.Memory.odp6)

        image = tk.Label(image=photos[photosAsStr.index(MediumMode.Memory.img)], height=500, width=900).place(x=500, y=20)
        label = tk.Label(textvariable=pl, width=10, height=2).place(x=910,y=600)
        result = tk.Label(textvariable=MediumMode.Memory.points, width=2, height=2).place(x=20, y=20)
        button = tk.Button(textvariable=odp1, width=40, height=2, command=lambda: MediumMode.IsCorectOdp(MediumMode.Memory.odp1))
        button.place(x=500, y=700)
        button = tk.Button(textvariable=odp2, width=40, height=2, command=lambda: MediumMode.IsCorectOdp(MediumMode.Memory.odp2))
        button.place(x=800, y=700)
        button = tk.Button(textvariable=odp3, width=40, height=2, command=lambda: MediumMode.IsCorectOdp(MediumMode.Memory.odp3))
        button.place(x=1100, y=700)
        button = tk.Button(textvariable=odp4, width=40, height=2, command=lambda: MediumMode.IsCorectOdp(MediumMode.Memory.odp4))
        button.place(x=500, y=750)
        button = tk.Button(textvariable=odp5, width=40, height=2, command=lambda: MediumMode.IsCorectOdp(MediumMode.Memory.odp5))
        button.place(x=800, y=750)
        button = tk.Button(textvariable=odp6, width=40, height=2, command=lambda: MediumMode.IsCorectOdp(MediumMode.Memory.odp6))
        button.place(x=1100, y=750)

        MediumMode.Memory.window.mainloop()

    def RandomWord():
        r_num = rd.randrange(0,len(sql.words)-1)
        r_word = sql.words[r_num]
        r_word = str(r_word)
        r_word = r_word.replace("'","")
        r_word = r_word.replace(")","")
        r_word = r_word.replace("(","")
        r_word = r_word.split(", ")
        id = r_word[0]
        pl = r_word[1]
        MediumMode.Memory.ang = r_word[2]
        img = r_word[3]
        img = img.replace(".png","")
        MediumMode.Memory.img = img

        if (id in MediumMode.Memory.itWas):
            MediumMode.RandomWord()
        else: 
            MediumMode.Memory.itWas.append(id)
            MediumMode.Memory.pl = pl

        fakewords = str(sql.fakewords)
        fakewords = fakewords.replace("'","")
        fakewords = fakewords.replace(")","")
        fakewords = fakewords.replace("(","")
        fakewords = fakewords.replace("]","")
        fakewords = fakewords.replace("[","")
        fakewords = fakewords.split(", ")

        for x in range(0,len(fakewords)):
            if (x%2 != 0):
                MediumMode.Memory.fakewords_list.append(fakewords[x])

        fw1 = MediumMode.Memory.fakewords_list[rd.randrange(len(MediumMode.Memory.fakewords_list))]
        fw2 = MediumMode.Memory.fakewords_list[rd.randrange(len(MediumMode.Memory.fakewords_list))]
        fw3 = MediumMode.Memory.fakewords_list[rd.randrange(len(MediumMode.Memory.fakewords_list))]
        fw4 = MediumMode.Memory.fakewords_list[rd.randrange(len(MediumMode.Memory.fakewords_list))]
        fw5 = MediumMode.Memory.fakewords_list[rd.randrange(len(MediumMode.Memory.fakewords_list))]

        whichButton = rd.randrange(1,7)
        
        if (whichButton == 1):
            MediumMode.Memory.odp1 = MediumMode.Memory.ang
            MediumMode.Memory.odp2 = fw1
            MediumMode.Memory.odp3 = fw2
            MediumMode.Memory.odp4 = fw3
            MediumMode.Memory.odp5 = fw4
            MediumMode.Memory.odp6 = fw5
        if (whichButton == 2):
            MediumMode.Memory.odp1 = fw1
            MediumMode.Memory.odp2 = MediumMode.Memory.ang
            MediumMode.Memory.odp3 = fw2
            MediumMode.Memory.odp4 = fw3
            MediumMode.Memory.odp5 = fw4
            MediumMode.Memory.odp6 = fw5
        if (whichButton == 3):
            MediumMode.Memory.odp1 = fw2
            MediumMode.Memory.odp2 = fw1
            MediumMode.Memory.odp3 = MediumMode.Memory.ang
            MediumMode.Memory.odp4 = fw3
            MediumMode.Memory.odp5 = fw4
            MediumMode.Memory.odp6 = fw5
        if (whichButton == 4):
            MediumMode.Memory.odp1 = fw3
            MediumMode.Memory.odp2 = fw1
            MediumMode.Memory.odp3 = fw2
            MediumMode.Memory.odp4 = MediumMode.Memory.ang
            MediumMode.Memory.odp5 = fw4
            MediumMode.Memory.odp6 = fw5
        if (whichButton == 5):
            MediumMode.Memory.odp1 = fw4
            MediumMode.Memory.odp2 = fw1
            MediumMode.Memory.odp3 = fw2
            MediumMode.Memory.odp4 = fw3
            MediumMode.Memory.odp5 = MediumMode.Memory.ang
            MediumMode.Memory.odp6 = fw5
        if (whichButton == 6):
            MediumMode.Memory.odp1 = fw5
            MediumMode.Memory.odp2 = fw1
            MediumMode.Memory.odp3 = fw2
            MediumMode.Memory.odp4 = fw3
            MediumMode.Memory.odp5 = fw4
            MediumMode.Memory.odp6 = MediumMode.Memory.ang


    def IsCorectOdp(x):
        if MediumMode.Memory.round_n <= 20:
            MediumMode.Memory.round_n += 1

            if x == MediumMode.Memory.ang:
                MediumMode.Memory.points_var += 1
                MediumMode.Memory.points.set(MediumMode.Memory.points_var)
            else:
                MediumMode.Memory.mistakes += 1
                if MediumMode.Memory.mistakes == 3:
                    MediumMode.Memory.round_n = 21

            MediumMode.RandomWord()

            # Update the window with new content
            MediumMode.update_window()
        else:
            MediumMode.End()

    def update_window():
        # Destroy all widgets in the current window
        for widget in MediumMode.Memory.window.winfo_children():
            widget.destroy()

        # Re-create and place the necessary widgets
        pl = tk.StringVar()
        pl.set(MediumMode.Memory.pl)
        odp1 = tk.StringVar()
        odp1.set(MediumMode.Memory.odp1)
        odp2 = tk.StringVar()
        odp2.set(MediumMode.Memory.odp2)
        odp3 = tk.StringVar()
        odp3.set(MediumMode.Memory.odp3)
        odp4 = tk.StringVar()
        odp4.set(MediumMode.Memory.odp4)
        odp5 = tk.StringVar()
        odp5.set(MediumMode.Memory.odp5)
        odp6 = tk.StringVar()
        odp6.set(MediumMode.Memory.odp6)

        image = tk.Label(image=photos[photosAsStr.index(MediumMode.Memory.img)], height=500, width=900).place(x=500, y=20)
        label = tk.Label(textvariable=pl, width=10, height=2).place(x=910, y=600)
        result = tk.Label(textvariable=MediumMode.Memory.points, width=2, height=2).place(x=20, y=20)
        button = tk.Button(textvariable=odp1, width=40, height=2, command=lambda: MediumMode.IsCorectOdp(MediumMode.Memory.odp1))
        button.place(x=500, y=700)
        button = tk.Button(textvariable=odp2, width=40, height=2, command=lambda: MediumMode.IsCorectOdp(MediumMode.Memory.odp2))
        button.place(x=800, y=700)
        button = tk.Button(textvariable=odp3, width=40, height=2, command=lambda: MediumMode.IsCorectOdp(MediumMode.Memory.odp3))
        button.place(x=1100, y=700)
        button = tk.Button(textvariable=odp4, width=40, height=2, command=lambda: MediumMode.IsCorectOdp(MediumMode.Memory.odp4))
        button.place(x=500, y=750)
        button = tk.Button(textvariable=odp5, width=40, height=2, command=lambda: MediumMode.IsCorectOdp(MediumMode.Memory.odp5))
        button.place(x=800, y=750)
        button = tk.Button(textvariable=odp6, width=40, height=2, command=lambda: MediumMode.IsCorectOdp(MediumMode.Memory.odp6))
        button.place(x=1100, y=750)

        # Update the window
        MediumMode.Memory.window.update_idletasks()


    def End():
        for widget in MediumMode.Memory.window.winfo_children():
            widget.destroy()

        if (MediumMode.Memory.points_var == 20):
            cytat = "Prawdziwy sukces to spełnienie celów, które dają nam radość i poczucie spełnienia.\nTrue success is achieving goals that give us joy and a sense of fulfillment."
        elif (MediumMode.Memory.points_var >= 15):
            cytat = "Sukces to nie klucz do szczęścia. Szczęście to klucz do sukcesu. Jeśli kochasz to, co robisz, osiągniesz sukces.\nSuccess is not the key to happiness. Happiness is the key to success. If you love what you do, you will succeed."
        elif (MediumMode.Memory.points_var >= 10):
            cytat = "Nie możesz zmienić kierunku wiatru, ale możesz dostosować ustawienia swoich żagli, aby dotrzeć tam, gdzie chcesz.\nYou can't change the direction of the wind, but you can adjust the settings of your sails to get where you want."
        elif (MediumMode.Memory.points_var >= 5):
            cytat = "Nie ma skrótu, aby osiągnąć sukces trwający. Trzeba pracować ciężko i nie przestawać wierzyć w siebie.\nThere is no shortcut to achieving lasting success. You have to work hard and never stop believing in yourself."
        elif (MediumMode.Memory.points_var < 5):
            cytat = "Szczęścia szukaj blisko siebie, bo ono jest w drobnych, codziennych radościach.\nLook for happiness close to yourself, because it is found in small, everyday joys."

        write = "Twój wynik to: "+str(MediumMode.Memory.points_var)+"/20\n"+str(cytat)

        label = tk.Label(text=write).pack()

            
from em_photos import *