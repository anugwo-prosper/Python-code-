# # pin = 1234
# # card_number= 8659036754
# # balance = 0
# # print("Welcome to Digital Fotress micro finance Bank")
# # card_pin= int(input("Enter your pin number"))
# # if card_pin == pin:
# #     print ("Welcome")
# # else:
# #      print ("Access Denial")

# # mycard_number=int(input("Enter your card nunber"))
# # if mycard_number == card_number:
# #     print ("welcome user")
# # else:
# #     print("Error")

# # user= input("Enter Your Name")
# # print(f"Welcome Mr. {user} your current balance is {balance}")



# # Handling of errors which is mostly used by try and except
# # function by parameter
# # def mynumber(num1, num2):
# #     try:
# #         return num1 + num2
# #     # ERROR TYPE
# # #     except TypeError:
# # #         return('value must be an interger')
# # # #    VARIABLE NAME ERROR
# # #     except NameError:
# # #         return('parameter does not exist')
# #     except Exception as p:
# #         return p

# # print(mynumber(10,20))
# # print(mynumber('a', 10))
# # print('success')


# # def calculator(x, y, v):
# #         if v == "A":
# #             print(f"The addition of {x} and {y} is: {x + y}")
# #         elif v == "S":
# #             print(f"The Subtraction of {x} and {y} is: {x - y}")
# #         elif v == "D":
# #             if y == 0:
# #                 print("Error: Division by zero is not allowed.")
# #             else:
# #                 print(f"The Division of {x} and {y} is: {x / y}")
# #         elif v == "M":
# #             print(f"The Multiply of {x} and {y} is: {x * y}")
# #         else:
# #             print(f'"{v}" is not an option for an Operator')

# # while True:
# #     print('''Use this calculator to Add, Subtract, Divide and Multiply:
# #         Choose "A" to Add,
# #                 "S" to Subtract,
# #                 "D" to Divide,
# #                 "M" to Multiply,
# #         your two values''')

# #     calculator(int(input("Enter your first value:\n")), int(input("Enter your second value:\n")), input("Enter your operator to calculate:\n").upper())


# # from tkinter import *
# # root= Tk()
# # root.title('GUI')
# # root.geometry('400x300')
# # label = Label(root, text="First Name")
# # label.grid(row=0, column=0)
# # entry = Entry ( root, width='60')
# # entry.grid(row=0, column=1)
# # myButton= Button(root, text='submit')
# # myButton.grid(row=1, column=0, padx='20')
# # # label.pack()
# # root.mainloop()

#  # type: ignore
# # GUI FORM ASSIGNMENT
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

# # def myclick():
# #     result = []
# #     firstName= entry1.get()
# #     secondName= entry2.get()
# #     Date= entry3.get()
# #     address=addrressEntry.get()
# #     if var1.get() or var2.get():
# #         gender = result.append(" ")
# #     if var3.get() or var4.get():
# #         status = result.append(" ")


# #     # result1= Label(root, text=firstName)
# #     # result1.pack()
# #     # result2= Label(root, text=secondName)
# #     # result2.pack()
# #     # result3=Label(root, Date)
# #     # result3.pack()
# #     # result4= Label(root, text=gender)
# #     # result4.pack()
# #     # result5= Label(root, text=address)
# #     # result5.pack()
# #     # result6= Label(root, text=status)
# #     # result6.pack()
    
# #     c1=(firstName, secondName, Date, gender, address, status)
# #     myclassinsert = """INSERT INTO classTable(firstName, secondname, date, gender, status)
# #     VALUES(?,?,?,?,?) """
    
# #     myclass.execute(myclassinsert, c1)
# #     prosper.commit()

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






# # OBJECT ORIENTED PROGRAMMING
# class Product():
# # "self" can be anything, because it is used as a paramter variable
#     def __init__(self, name, price, verion, color):
#             self.name = name
#             self.price = price
#             self.version = verion
#             self.color = color


#     def __str__(self):
#             return f"{self.name}, Price: {self.price}, {self.color}"
#     def tunde(self):
#             return f"The product is {self.name}"
            
# myproduct = Product(1000, 'Headset' , 'a.o', 'black')
# print(myproduct.tunde())

# ##INHERITING A DATABASE
# class New_product(Product):
#     def __init__(self, name, price, verion, color, size, weight):
#             super().__init__(name, price, verion, color)
#             self.size = size
#             self.weight = weight
# # __str__ is used to display on your browser / terminal for user display
#     def __str__ (self):
#             return f"{self.size} {self.weight} {self.name} {self.price} {self.color}"

# ournewProduct = New_product('xxl', '75kg', 'Samsung', 50000, 'red', 'ujj')




# POLYMORPHISM OOP
class Electronics:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

def get_name(self):
        return self.name
    
     def __str__(self):
        return f'{self.name} {self.price}'


class Gadget:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

def get_name(self):
        return self.name

    def __str__(self):
        return f'{self.name} {self.price}'
    
class Materials:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight
    
def get_name(self):
        return self.name
    
    def __str__(self):
        return f'{self.name} {self.price}'

my_electronic = Electronics ('samsung', 20000, '200kg')
my_gadget = Gadget ('apple', 60000, '20kg')
my_material = Materials ('wood', 10000, '50kg')

print(my_electronic)
print(my_gadget)
print(my_material)

# loop through 
for item in [my_electronic, my_gadget, my_material]:
      print(item)
