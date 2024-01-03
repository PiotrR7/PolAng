import pymysql as mysql

class sql:
    easy_words = []
    medium_words = []
    medhar_words = []
    hard_words = []

    fakewords = []

def connect():
    con = mysql.Connect(host='localhost', unix_socket='', user='root', passwd='', db='polang')
    cur = con.cursor()

    cur.execute("select * from easy_words")
    for c in cur:
        sql.easy_words.append(c)

    cur.execute("select * from medium_words")
    for c in cur:
        sql.medium_words.append(c)

    cur.execute("select * from medhar_words")
    for c in cur:
        sql.medhar_words.append(c)

    cur.execute("select * from hard_words")
    for c in cur:
        sql.hard_words.append(c)


    cur.execute("select * from fakewords")
    for c in cur:
        sql.fakewords.append(c)

    cur.close()

connect()