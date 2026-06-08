from tkinter import *

# ==========================================
# Tkinter Calculator
#
# My first calculator project using Tkinter.
#
# Things I practiced:
# - Entry Widget
# - Button Widget
# - Functions
# - Global Variables
# - Lambda Functions
# - Exception Handling
#
# Notes:
# - Built while learning Tkinter basics.
# - Code structure, comments, and organization
#   were refined with help from AI tools.
# ==========================================

# Main Window
window = Tk()

window.title("Tkinter Calculator")
window.geometry("900x800")
window.resizable(True, True)

# ------------------------------------------
# Variables
# ------------------------------------------
# first_number stores the first value entered
# operation remembers which operator was clicked

first_number = 0
operation = ""

# ------------------------------------------
# Entry Box
# ------------------------------------------
# This box shows numbers and answers

Input = Entry(
    width=18,
    borderwidth=5,
    font=("Arial", 29),
    justify="right"      # looks more like a real calculator
)

Input.place(x=50, y=20)

# ------------------------------------------
# Button Positions
# ------------------------------------------
# Keeping positions in variables makes
# it easier to adjust the layout later

x1 = 80
x2 = 260
x3 = 440
x4 = 620

y1 = 130
y2 = 260
y3 = 390
y4 = 520
y5 = 650

# Common button size
w = 5
h = 2

button_font = ("Arial", 17, "bold")

# ==========================================
# Number Buttons
# ==========================================
""" Example: -- Current value = 12
                Click 5
                New value = 125"""


def click(num):

    current_value = Input.get()

    Input.delete(0, END)

    Input.insert(
        0,
        str(current_value) + str(num)
    )

# ==========================================
# Decimal Button
# ==========================================
# Prevents:
# 12.5.7
#
# Allows:
# 12.57

def decimal():

    current_value = Input.get()

    if "." not in current_value:
        Input.insert(END, ".")

# ==========================================
# Operator Buttons
# ==========================================
# Save first number
# Remember selected operation
# Clear entry so user can enter second number

def add():

    global first_number
    global operation

    first_number = float(Input.get())

    operation = "addition"

    Input.delete(0, END)


def sub():

    global first_number
    global operation

    first_number = float(Input.get())

    operation = "subtraction"

    Input.delete(0, END)


def mult():

    global first_number
    global operation

    first_number = float(Input.get())

    operation = "multiplication"

    Input.delete(0, END)


def div():

    global first_number
    global operation

    first_number = float(Input.get())

    operation = "division"

    Input.delete(0, END)


def percent():

    global first_number
    global operation

    first_number = float(Input.get())

    operation = "percentage"

    Input.delete(0, END)

# ==========================================
# Equal Button
# ==========================================
# Calculation based on the operator selected earlier

def equal():

    global first_number
    global operation

    try:

        second_number = float(Input.get())

        Input.delete(0, END)

        if operation == "addition":

            answer = first_number + second_number

        elif operation == "subtraction":

            answer = first_number - second_number

        elif operation == "multiplication":

            answer = first_number * second_number

        elif operation == "division":

            # Prevent program crash
            if second_number == 0:

                Input.insert(0, "Error")

                return

            answer = first_number / second_number

        elif operation == "percentage":

            # Example:
            # 200 % 10 = 20
            answer = (first_number * second_number) / 100

        else:

            Input.insert(0, "Error")

            return

        # Show final answer
        Input.insert(0, answer)

    except:

        # If something unexpected happens
        # show Error instead of crashing
        Input.delete(0, END)

        Input.insert(0, "Error")

# ==========================================
# Clear Button
# ==========================================
# Remove everything from Entry Box

def clear():

    Input.delete(0, END)

# ==========================================
# Row 1
# ==========================================

Button(
    window,
    text="C",
    width=w,
    height=h,
    font=button_font,
    command=clear
).place(x=x1, y=y1)

Button(
    window,
    text="%",
    width=w,
    height=h,
    font=button_font,
    command=percent
).place(x=x2, y=y1)

Button(
    window,
    text="÷",
    width=w,
    height=h,
    font=button_font,
    command=div
).place(x=x3, y=y1)

Button(
    window,
    text="×",
    width=w,
    height=h,
    font=button_font,
    command=mult
).place(x=x4, y=y1)

# ==========================================
# Row 2
# ==========================================

Button(
    window,
    text="7",
    width=w,
    height=h,
    font=button_font,
    command=lambda: click(7)
).place(x=x1, y=y2)

Button(
    window,
    text="8",
    width=w,
    height=h,
    font=button_font,
    command=lambda: click(8)
).place(x=x2, y=y2)

Button(
    window,
    text="9",
    width=w,
    height=h,
    font=button_font,
    command=lambda: click(9)
).place(x=x3, y=y2)

Button(
    window,
    text="-",
    width=w,
    height=h,
    font=button_font,
    command=sub
).place(x=x4, y=y2)

# ==========================================
# Row 3
# ==========================================

Button(
    window,
    text="4",
    width=w,
    height=h,
    font=button_font,
    command=lambda: click(4)
).place(x=x1, y=y3)

Button(
    window,
    text="5",
    width=w,
    height=h,
    font=button_font,
    command=lambda: click(5)
).place(x=x2, y=y3)

Button(
    window,
    text="6",
    width=w,
    height=h,
    font=button_font,
    command=lambda: click(6)
).place(x=x3, y=y3)

Button(
    window,
    text="+",
    width=w,
    height=h,
    font=button_font,
    command=add
).place(x=x4, y=y3)

# ==========================================
# Row 4
# ==========================================

Button(
    window,
    text="1",
    width=w,
    height=h,
    font=button_font,
    command=lambda: click(1)
).place(x=x1, y=y4)

Button(
    window,
    text="2",
    width=w,
    height=h,
    font=button_font,
    command=lambda: click(2)
).place(x=x2, y=y4)

Button(
    window,
    text="3",
    width=w,
    height=h,
    font=button_font,
    command=lambda: click(3)
).place(x=x3, y=y4)

# ==========================================
# Row 5
# ==========================================

Button(
    window,
    text="0",
    width=12,
    height=h,
    font=button_font,
    command=lambda: click(0)
).place(x=x1, y=y5)

Button(
    window,
    text=".",
    width=w,
    height=h,
    font=button_font,
    command=decimal
).place(x=x3, y=y5)

# ==========================================
# Equal Button
# ==========================================

Button(
    window,
    text="=",
    width=w,
    height=5,
    font=("Arial", 16, "bold"),
    command=equal
).place(x=x4, y=y4)

# Start Program
window.mainloop()