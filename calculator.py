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





# Sure! Let's break down the code step by step:

# Imports:

# import tkinter as tk: This imports the Tkinter module and gives it the alias tk, which is a widely used convention.
# Function Definitions:

# button_click(symbol): This function is called whenever a button on the calculator is clicked. It takes a symbol (which represents the text displayed on the button) as input.
# If the symbol is 'C', it clears the display.
# If the symbol is 'DEL', it removes the last character from the display.
# If the symbol is '=', it evaluates the expression in the display and displays the result.
# Otherwise, it appends the symbol to the current display value.
# Create the main window:

# window = tk.Tk(): This creates the main window for the calculator.
# window.title("Calculator"): Sets the title of the window to "Calculator".
# Display Entry:

# display_var = tk.StringVar(): This creates a Tkinter variable to store the value displayed in the entry widget.
# display = tk.Entry(window, textvariable=display_var, justify="right", font=("Arial", 20)): This creates an Entry widget (a text entry field) within the window. It's linked to the display_var variable, which is set to be displayed on the right and uses a larger font.
# .grid(row=0, column=0, columnspan=4, sticky="nsew"): This places the display entry widget in the first row, spanning across all four columns, and set to expand in all directions.
# Buttons:

# buttons list: Contains the labels for all the buttons in the calculator.
# row_index and col_index: Used for placing buttons in the correct rows and columns.
# Button creation loop: Iterates through the buttons list, creating a Button widget for each button label.
# The command parameter is set to lambda function to pass the button label to the button_click() function.
# .grid() method is used to place each button in its corresponding row and column.
# Configure Rows and Columns:

# window.grid_columnconfigure(i, weight=1): This configures each column of the window to expand equally when the window is resized.
# window.grid_rowconfigure(i, weight=1): This configures each row of the window to expand equally when the window is resized.
# Run the GUI:

# window.mainloop(): This starts the Tkinter event loop, which listens for events (such as button clicks) and updates the GUI accordingly.
# Overall, this code creates a simple calculator GUI using Tkinter, with a display entry for showing calculations and buttons for inputting numbers and performing operations. The button_click() function handles button clicks and updates the display accordingly.





