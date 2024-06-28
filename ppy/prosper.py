# mySet = {"Blue", "Red", "Pink"}
# set2 = {"Red", "white", "purple"}

# set1= {1, 2, 3, 4}
# set2={2,3,6,8}
# print(set1)

     

# set1= {"green", "blue", "red"}
# set2= {"purple", "blue", "red"}

# difference= (set1|set2)
# print(difference)

# my_set = {1, 2, 3, 4}
# print(element_in_set(my_set, 2)) # prints True
# print(element_in_set(my_set, 5)) # prints False


# LAMBDA, ANONYMOUS FUNCTION
# X = 12
# myx = lambda y : y * y 
# print(myx(X))


# FILTER FUNCTION
# x = [10, 20, 30, 40, 75, 25, 53]
# myx = list(filter(lambda y: y % 5 == 0, x))
# print(myx)


# # MAP FUNCTION
# x = [10, 20, 30, 40, 75, 25, 53]
# myx = list(map(lambda y: y % 5 == 0, x))
# print(myx)



# DATABASE MANAGEMENT

# import sqlite3
# from tkinter import *

# prosper = sqlite3.connect("class.db") 

# myclass=prosper.cursor()
# myclass1 ="""
#     CREATE TABLE IF NOT EXISTS 
#     classTable(
#     firstName TEXT, 
#     secondname TEXT, 
#     date TEXT,
#     gender TEXT,
#     address TEXT,
#     status TEXT
# )
# """

# myclass.execute(myclass1)
# prosper.commit()
# # prosper.close()

# def myclick():
#     result = []
#     firstName= entry1.get()
#     secondName= entry2.get()
#     Date= entry3.get()
#     address=addrressEntry.get()
#     if var1.get() or var2.get():
#         gender = result.append(" ")
#     if var3.get() or var4.get():
#         status = result.append(" ")


#     # result1= Label(root, text=firstName)
#     # result1.pack()
#     # result2= Label(root, text=secondName)
#     # result2.pack()
#     # result3=Label(root, Date)
#     # result3.pack()
#     # result4= Label(root, text=gender)
#     # result4.pack()
#     # result5= Label(root, text=address)
#     # result5.pack()
#     # result6= Label(root, text=status)
#     # result6.pack()
    
#     c1=(firstName, secondName, Date, gender, address, status)
#     myclassinsert = """INSERT INTO classTable(firstName, secondname, date, gender, status)
#     VALUES(?,?,?,?,?) """
    
#     myclass.execute(myclassinsert, c1)
#     prosper.commit()

# def saveData():
#     result = []
#     result_label.config(text="Selected options: "+", ".join(result))
#     firstName= entry1.get()
#     secondName= entry2.get()
#     Date= entry3.get()
#     address=addrressEntry.get()
#     if var1.get() or var2.get():
#         gender = result.append(var1 or var2)
#     if var3.get() or var4.get():
#         status = result.append(var3 or var4)

#     c1=(firstName, secondName, Date, gender, address, status)
#     myclassinsert = """INSERT INTO classTable(firstName, secondname, date, gender, address, status)
#     VALUES(?,?,?,?,?,?) """
    
#     myclass.execute(myclassinsert, c1)
#     prosper.commit()


# root= Tk()
# root.geometry('600x400')

# root.title('DECISION CARD FORM')

# var1 = IntVar()
# var2 = IntVar()
# var3 = IntVar()
# var4 = IntVar()

# label = Label(root, text="FIRST NAME: ")
# label.grid(row=0, column=0)
# entry1 = Entry ( root, width='20')
# entry1.grid(row=0, column=1 )

# label = Label(root, text="SECOND NAME: ")
# label.grid(row=0, column=2)
# entry2 = Entry ( root, width='20')
# entry2.grid(row=0, column=3)


# date = Label(root, text='Date: ')
# date.grid(row= 2, column=0, pady='10' )
# entry3 = Entry ( root, width='30')
# entry3.grid(row=2, column=1 )

# gender = Label(root, text='Gender:')
# gender.grid(row=3, column=0)
# gender = Checkbutton(text='MALE', variable=var1)
# gender.grid(row=3, column=1, )
# gender = Checkbutton(text='FEMALE', variable=var2)
# gender.grid(row=3, column=2, )

# address = Label(root, text="HOME ADDRESS: ")
# address.grid(row=4, column=0, pady='10')
# addrressEntry = Entry ( root, width='40')
# addrressEntry.grid(row=4, column=1)

# maritalStatus = Label(root, text='Marital Status:')
# maritalStatus.grid(row=5, column=0)
# maritalStatus = Checkbutton(text='Married', variable=var3)
# maritalStatus.grid(row=5, column=1, )
# maritalStatus = Checkbutton(text='Single', variable=var4)
# maritalStatus.grid(row=5, column=2, )

# myButton= Button(root, text='submit', command=saveData)
# myButton.grid(row=6, column=0, padx=20, )
# result_label=Label(root, text="")
# result_label.grid(row=6, column=0)

# # label.pack()
# root.mainloop()


# VOICE GREETING
# import tkinter as tk
# from gtts import gTTS
# import os

# def welcome_user():
#     name = name_entry.get()
#     if name:
#         welcome_message = f"Welcome, {name}!"
#         tts = gTTS(text=welcome_message, lang='en')
#         tts.save("welcome.mp3")
#         os.system("mpg321 welcome.mp3")
#         label.config(text=welcome_message)

# root = tk.Tk()
# root.title("Welcome App")

# label = tk.Label(root, text="", font=("Helvetica", 24))
# label.pack()

# name_label = tk.Label(root, text="Enter your name:")
# name_label.pack()

# name_entry = tk.Entry(root, width=30)
# name_entry.pack()

# button = tk.Button(root, text="Submit", command=welcome_user)
# button.pack()

# root.mainloop()

# #voice greeting
# import tkinter as tk
# import pygame
# from gtts import gTTS
# import os

# def welcome_user():
#     name = name_entry.get()
#     if name:
#         welcome_message = f"Welcome, {name}!"
#         label.config(text=welcome_message)
#         create_audio(welcome_message)

# def create_audio(message):
#     tts = gTTS(text=message, lang='en')
#     tts.save("welcome.mp3")
#     play_audio()

# def play_audio():
#     pygame.mixer.init()  # Initialize pygame.mixer first
#     pygame.mixer.music.load("welcome.mp3")
#     pygame.mixer.music.play()

# root = tk.Tk()
# root.title("Welcome App")

# label = tk.Label(root, text="", font=("Helvetica", 24))
# label.pack()

# name_label = tk.Label(root, text="Enter your name:")
# name_label.pack()

# name_entry = tk.Entry(root, width=30)
# name_entry.pack()

# button = tk.Button(root, text="Submit", command=welcome_user)
# button.pack()

# root.mainloop()



# CALCULATOR
import tkinter as tk

def button_click(symbol):
    current = display_var.get()
    if symbol == 'C':
        display_var.set('')
    elif symbol == 'DEL':
        display_var.set(current[:-1])
    elif symbol == '=':
        try:
            result = eval(current)
            display_var.set(str(result))
        except:
            display_var.set("Error")
    else:
        display_var.set(current + symbol)


window = tk.Tk()
window.title("Calculator")


display_var = tk.StringVar()
display = tk.Entry(window, textvariable=display_var, justify="right", font=("Arial", 20))
display.grid(row=0, column=0, columnspan=4, sticky="nsew")


buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    'C', 'DEL'
]

row_index = 1
col_index = 0
for button in buttons:
    tk.Button(window, text=button, width=5, height=2, command=lambda b=button: button_click(b)).grid(row=row_index, column=col_index, sticky="nsew")
    col_index += 1
    if col_index > 3:
        col_index = 0
        row_index += 1

for i in range(4):
    window.grid_columnconfigure(i, weight=1)
for i in range(6):
    window.grid_rowconfigure(i, weight=1)


window.mainloop()
