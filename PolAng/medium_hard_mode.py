import tkinter as tk
import pymysql as mysql
import random as rd
from sql_connect import sql


class MedHadMode:
    class Memory:
        window = tk.Tk()
        points = tk.StringVar()
        user_answer = tk.StringVar()

        itWas = []
        fakewords_list = []

        points_var = 0
        mistakes = 0
        round_n = 1

        pl = ""; ang = ""; img = ""


    def Play():
        MedHadMode.Memory.window.eval('tk::PlaceWindow . center')
        MedHadMode.Memory.window.resizable(False,False)
        MedHadMode.Memory.window.title("")

        appwidth = 1920; screenwidth = MedHadMode.Memory.window.winfo_screenwidth(); x = (screenwidth / 2) - (appwidth / 2)
        appheight = 1080; screenheight = MedHadMode.Memory.window.winfo_screenheight(); y = (screenheight / 2) - (appheight / 2)

        MedHadMode.Memory.window.geometry(f'{appwidth}x{appheight}+{int(x)}+{int(y)}')

        pl = tk.StringVar(); pl.set(MedHadMode.Memory.pl)
        ang = tk.StringVar(); ang.set(MedHadMode.Memory.ang)

        
        # tk.Label(image=photos[photosAsStr.index(MedHadMode.Memory.img)], height=500, width=900
        #             ).place(x=500, y=20)
        tk.Label(textvariable=pl, width=10, height=2
                    ).place(x=910,y=200)
        tk.Label(textvariable=MedHadMode.Memory.points, width=2, height=2
                    ).place(x=20, y=20)
        tk.Label(textvariable=ang, width=10, height=2
                    ).place(x=910,y=250)
        tk.Entry(textvariable=MedHadMode.Memory.user_answer
                    ).place(x=885,y=300)
        tk.Button(text="Sprawdź", command=lambda: MedHadMode.IsCorectOdp()
                    ).place(x=920,y=350)

        MedHadMode.Memory.window.mainloop()


    def RandomWord():
        r_num = rd.randrange(0,len(sql.medhar_words)-1)
        r_word = str(sql.medhar_words[r_num])

        r_word = r_word.replace("'",""); r_word = r_word.replace(")",""); r_word = r_word.replace("(",""); r_word = r_word.split(", ")
        
        id = r_word[0]
        ang = r_word[1]
        pl = r_word[2]
        img = r_word[3]

        ang = ang.replace("a", " _ ")
        ang = ang.replace("o", " _ ")
        ang = ang.replace("e", " _ ")
        ang = ang.replace("i", " _ ")
        ang = ang.replace("y", " _ ")
        ang = ang.replace("u", " _ ")

        MedHadMode.Memory.ang = ang

        img = img.replace(".png","")
        MedHadMode.Memory.img = img

        if (id in MedHadMode.Memory.itWas):
            MedHadMode.RandomWord()
        else: 
            MedHadMode.Memory.itWas.append(id)
            MedHadMode.Memory.pl = pl

        fakewords = str(sql.fakewords)
        fakewords = fakewords.replace("'",""); fakewords = fakewords.replace(")",""); fakewords = fakewords.replace("(","")
        fakewords = fakewords.replace("]",""); fakewords = fakewords.replace("[",""); fakewords = fakewords.split(", ")
        
        for x in range(0,len(fakewords)):
            if (x%2 != 0):
                MedHadMode.Memory.fakewords_list.append(fakewords[x])



    def IsCorectOdp():
        x = MedHadMode.Memory.user_answer.get()
        x= x.lower()

        if MedHadMode.Memory.round_n <= 20:
            MedHadMode.Memory.round_n += 1

            if x == MedHadMode.Memory.ang.lower():
                MedHadMode.Memory.points_var += 1
                MedHadMode.Memory.points.set(MedHadMode.Memory.points_var)
            else:
                MedHadMode.Memory.mistakes += 1
                if MedHadMode.Memory.mistakes == 3:
                    MedHadMode.Memory.round_n = 21

            MedHadMode.RandomWord()

            # Update the window with new content
            MedHadMode.update_window()
        else:
            MedHadMode.End()

    def update_window():
        # Destroy all widgets in the current window
        for widget in MedHadMode.Memory.window.winfo_children():
            widget.destroy()

        # Re-create and place the necessary widgets
        pl = tk.StringVar(); pl.set(MedHadMode.Memory.pl)
        ang = tk.StringVar(); ang.set(MedHadMode.Memory.ang)
        
        # tk.Label(image=photos[photosAsStr.index(MedHadMode.Memory.img)], height=500, width=900
        #             ).place(x=500, y=20)
        tk.Label(textvariable=pl, width=10, height=2
                    ).place(x=910,y=200)
        tk.Label(textvariable=MedHadMode.Memory.points, width=2, height=2
                    ).place(x=20, y=20)
        tk.Label(textvariable=ang, width=10, height=2
                    ).place(x=910,y=250)
        tk.Entry(textvariable=MedHadMode.Memory.user_answer
                    ).place(x=885,y=300)
        tk.Button(text="Sprawdź", command=lambda: MedHadMode.IsCorectOdp()
                    ).place(x=920,y=350)
        
        # Update the window
        MedHadMode.Memory.window.update_idletasks()


    def End():
        for widget in MedHadMode.Memory.window.winfo_children():
            widget.destroy()

        if (MedHadMode.Memory.points_var == 20):
            cytat = "Prawdziwy sukces to spełnienie celów, które dają nam radość i poczucie spełnienia.\nTrue success is achieving goals that give us joy and a sense of fulfillment."
        elif (MedHadMode.Memory.points_var >= 15):
            cytat = "Sukces to nie klucz do szczęścia. Szczęście to klucz do sukcesu. Jeśli kochasz to, co robisz, osiągniesz sukces.\nSuccess is not the key to happiness. Happiness is the key to success. If you love what you do, you will succeed."
        elif (MedHadMode.Memory.points_var >= 10):
            cytat = "Nie możesz zmienić kierunku wiatru, ale możesz dostosować ustawienia swoich żagli, aby dotrzeć tam, gdzie chcesz.\nYou can't change the direction of the wind, but you can adjust the settings of your sails to get where you want."
        elif (MedHadMode.Memory.points_var >= 5):
            cytat = "Nie ma skrótu, aby osiągnąć sukces trwający. Trzeba pracować ciężko i nie przestawać wierzyć w siebie.\nThere is no shortcut to achieving lasting success. You have to work hard and never stop believing in yourself."
        elif (MedHadMode.Memory.points_var < 5):
            cytat = "Szczęścia szukaj blisko siebie, bo ono jest w drobnych, codziennych radościach.\nLook for happiness close to yourself, because it is found in small, everyday joys."

        write = "Twój wynik to: "+str(MedHadMode.Memory.points_var)+"/20\n"+str(cytat)

        label = tk.Label(text=write).pack()

            
from em_photos import *

MedHadMode.RandomWord()
MedHadMode.Play()