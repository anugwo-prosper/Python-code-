# import sqlite3

# prosper = sqlite3.connect("class.db") 

# myclass=prosper.cursor()
# myclass1 ="""
#     CREATE TABLE IF NOT EXISTS 
#     classTable(
#     firstName TEXT, 
#     secondname TEXT, 
#     date TEXT,
#     gender TEXT,
#     status TEXT
# )"""

# myclass.execute(myclass1)
# prosper.commit()
# prosper.close()


# MATCH CASE SIMILAR TO IF AND ELSE
def prosper(x):
    match x:
        case _ if x >=90 or x <= 100:
            print('Grade A')
        case _ if x>= 70 or x <= 89:
            print('Grade B')
        case _ :
            print('Unknown Result')

y=input("Enter your score \n")
prosper(int(y))
