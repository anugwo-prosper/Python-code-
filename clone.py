import requests
from bs4 import BeautifulSoup

url = "https://www.zoho.com//"
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
# print(soup.prettify())

with open('zoho.html', "wt", encoding="utf-8") as file:
    file.write(soup.prettify())
    file.write('\n')

# import tkinter as tk

# root = tk.Tk()

# # Create an integer variable with initial value 0
# num = tk.IntVar(root, value=0)

# # Create a label to display the value of the variable
# label = tk.Label(root, textvariable=num)
# label.pack()

# # Create a button to increment the variable by 1
# increment_button = tk.Button(root, text="Increment", command=lambda: num.set(num.get() + 1))
# increment_button.pack()

# root.mainloop()