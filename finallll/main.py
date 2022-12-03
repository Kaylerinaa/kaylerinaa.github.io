import mysql.connector as final
from tabulate import tabulate



conn = final.connect(host = 'localhost', user = 'root', password = 'KaylaBaela8$', db = 'menagerie')
print("Connected")
cursor = conn.cursor()

def database():
    db = "show databases"
    cursor.execute(db)
    for db in cursor:
        print(db[0])


database()

def databaseTwo():
    cursor.execute('DROP DATABASE IF EXISTS menagerie')
    print('Database has been dropped')
    cursor.execute("CREATE DATABASE menagerie")
    cursor.execute("USE menagerie")


databaseTwo()

def petz():
    cursor.execute("CREATE TABLE pet (name VARCHAR(20), owner VARCHAR(20), species VARCHAR(20), sex CHAR(20), birth DATE, death DATE, age int)")


petz()

def petzTwo():
    cursor.execute("INSERT INTO pet (name,owner,species,sex,birth,death,age) VALUES \
    ('Fluffy','Harold', 'cat', 'f','1993-02-04',NULL,10),\
    ('Claws','Gwen', 'cat', 'm','1994-03-17',NULL,9),\
    ('Buffy','Harold', 'dog', 'f','1989-05-13',NULL,14),\
    ('Fang','Benny', 'dog', 'm','1990-08-27',NULL,12),\
    ('Bowser','Diane', 'dog', 'm','1979-08-31','1995-07-29',13),\
    ('Chripy','Gwen', 'bird', 'f','1998-09-11',NULL,4),\
    ('Whistler','Gwen', 'bird', NULL,'1997-12-09',NULL,5),\
    ('Slim','Benny', 'snake', 'm','1996-04-29',NULL,7),\
    ('Puffball','Diane', 'hamster', 'f','1999-03-30',NULL,4)")
    conn.commit()


petzTwo()


def databaseThree():
    cursor.execute("DESCRIBE pet")
    print(cursor.fetchall())

databaseThree()

def databaseFour():
    cursor.execute("SELECT * FROM pet")
    print(cursor.fetchall())


databaseFour()

def databaseFive():
    cursor.execute("SELECT * FROM pet WHERE sex = 'f' AND species = 'dog'")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(cursor.fetchall())


databaseFive()

def databaseSix():
    cursor.execute("SELECT name, birth FROM pet")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(cursor.fetchall())


databaseSix()

def databaseSeven():
    cursor.execute("SELECT owner, COUNT(*) FROM pet GROUP BY owner")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(cursor.fetchall())


databaseSeven()

def databaseEight():
    cursor.execute("SELECT name, birth, month(BIRTH) FROM pet")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(tabulate(cursor.fetchall(),headers = ['name', 'birth', 'month(BIRTH)'], tablefmt="psql"))


databaseEight()