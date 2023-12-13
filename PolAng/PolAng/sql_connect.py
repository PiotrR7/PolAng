import pymysql as mysql

class sql:
    words = []
    fakewords = []

def connect():
    con = mysql.Connect(host='localhost', unix_socket='', user='root', passwd='', db='polang')
    cur = con.cursor()

    cur.execute("select * from words")
    for c in cur:
        sql.words.append(c)

    fakewords = cur.execute("select * from fakewords")
    for c in cur:
        sql.fakewords.append(c)

    cur.close()

connect()