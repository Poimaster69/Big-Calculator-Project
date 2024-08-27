from tkinter import *
import math

def buttonClick(value):
    current_text = display_text.get()
    str_value = str(value)

    if str_value.isdigit() or str_value in "+-*/.%²()":
        if current_text == "" and str_value in "+*/.%²)":
            return
        if current_text and current_text[-1] in "+-*/.%²(" and str_value in "+-*/.%²)":
            return

        pos = display_text.index(INSERT)
        display_text.insert(pos, str_value)
    
    # Special case for square root handling
    elif str_value == '√':
        if current_text == "" or current_text[-1] in "+-*/.":
            pos = display_text.index(INSERT)
            display_text.insert(pos, '√(')
        else:
            pos = display_text.index(INSERT)
            display_text.insert(pos, '*√(')  # Implicit multiplication if square root follows a number

def buttonClear():
    display_text.delete(0, END)

def buttonBackspace():
    pos = display_text.index(INSERT)
    if pos > 0:
        display_text.delete(pos - 1)

def buttonEqual():
    expression = display_text.get()

    try:
        # Handle square roots and squares
        expression = expression.replace('√(', 'math.sqrt(')  # Translate to math.sqrt
        expression = expression.replace('²', '**2')

        # Count open parentheses after replacing square roots
        open_parentheses = expression.count('(')
        close_parentheses = expression.count(')')

        # Calculate the missing closing parentheses
        close_parens_needed = open_parentheses - close_parentheses

        # Add the required number of closing parentheses
        expression += ')' * close_parens_needed

        # Evaluate the expression safely
        result = str(eval(expression))
        display_text.delete(0, END)
        display_text.insert(0, result)

    except SyntaxError:
        display_text.delete(0, END)
        display_text.insert(0, "Syntax Error")
    except ZeroDivisionError:
        display_text.delete(0, END)
        display_text.insert(0, "Division by Zero")
    except Exception as e:
        display_text.delete(0, END)
        display_text.insert(0, "Error")

def validate_input(text):
    if text == "" or text.isdigit() or text in "+-*/.%²()":
        return True
    return False

def keyPress(event):
    key = event.char
    if key.isdigit() or key in "+-*/.%()":
        buttonClick(key)
    elif key == "\r":
        buttonEqual()
    elif key == "\x08":
        buttonBackspace()

main = Tk()
main.title("Calculator")
main.resizable(False, False)

input_value = StringVar()

# Set up validation
vcmd = main.register(validate_input)
display_text = Entry(main, font=("arial", 40, "bold"), bd=20, insertwidth=4,
                     bg="powder blue", justify=RIGHT, width=16)
display_text.grid(row=0, column=0, columnspan=5, padx=10, pady=20)

main.bind("<Key>", keyPress)

# Adjust the button size and layout
button_padx = 20
button_pady = 20
button_font = ("arial", 18, "bold")

# Row 1: %, √, x², C, Backspace
btn_percent = Button(main, padx=button_padx, pady=button_pady, bd=8, fg="black",
                     font=button_font, text="%", command=lambda: buttonClick("%"))
btn_percent.grid(row=1, column=0)

btn_sqrt = Button(main, padx=button_padx, pady=button_pady, bd=8, fg="black",
                  font=button_font, text="√", command=lambda: buttonClick("√"))
btn_sqrt.grid(row=1, column=1)

btn_square = Button(main, padx=button_padx, pady=button_pady, bd=8, fg="black",
                    font=button_font, text="x²", command=lambda: buttonClick("²"))
btn_square.grid(row=1, column=2)

btn_clear = Button(main, padx=button_padx, pady=button_pady, bd=8, fg="black",
                   font=button_font, text="C", command=buttonClear)
btn_clear.grid(row=1, column=3)

btn_backspace = Button(main, padx=button_padx, pady=button_pady, bd=8, fg="black",
                       font=button_font, text="⌫", command=buttonBackspace)
btn_backspace.grid(row=1, column=4)

# Row 2: 7, 8, 9, +, (
btn_7 = Button(main, padx=button_padx, pady=button_pady, bd=8, fg="black",
               font=button_font, text="7", command=lambda: buttonClick(7))
btn_7.grid(row=2, column=0)

btn_8 = Button(main, padx=button_padx, pady=button_pady, bd=8, fg="black",
               font=button_font, text="8", command=lambda: buttonClick(8))
btn_8.grid(row=2, column=1)

btn_9 = Button(main, padx=button_padx, pady=button_pady, bd=8, fg="black",
               font=button_font, text="9", command=lambda: buttonClick(9))
btn_9.grid(row=2, column=2)

btn_add = Button(main, padx=button_padx, pady=button_pady, bd=8, fg="black",
                 font=button_font, text="+", command=lambda: buttonClick("+"))
btn_add.grid(row=2, column=3)

btn_open_bracket = Button(main, padx=button_padx, pady=button_pady, bd=8, fg="black",
                          font=button_font, text="(", command=lambda: buttonClick("("))
btn_open_bracket.grid(row=2, column=4)

# Row 3: 4, 5, 6, -, )
btn_4 = Button(main, padx=button_padx, pady=button_pady, bd=8, fg="black",
               font=button_font, text="4", command=lambda: buttonClick(4))
btn_4.grid(row=3, column=0)

btn_5 = Button(main, padx=button_padx, pady=button_pady, bd=8, fg="black",
               font=button_font, text="5", command=lambda: buttonClick(5))
btn_5.grid(row=3, column=1)

btn_6 = Button(main, padx=button_padx, pady=button_pady, bd=8, fg="black",
               font=button_font, text="6", command=lambda: buttonClick(6))
btn_6.grid(row=3, column=2)

btn_sub = Button(main, padx=button_padx, pady=button_pady, bd=8, fg="black",
                 font=button_font, text="-", command=lambda: buttonClick("-"))
btn_sub.grid(row=3, column=3)

btn_close_bracket = Button(main, padx=button_padx, pady=button_pady, bd=8, fg="black",
                           font=button_font, text=")", command=lambda: buttonClick(")"))
btn_close_bracket.grid(row=3, column=4)

# Row 4: 1, 2, 3, *
btn_1 = Button(main, padx=button_padx, pady=button_pady, bd=8, fg="black",
               font=button_font, text="1", command=lambda: buttonClick(1))
btn_1.grid(row=4, column=0)

btn_2 = Button(main, padx=button_padx, pady=button_pady, bd=8, fg="black",
               font=button_font, text="2", command=lambda: buttonClick(2))
btn_2.grid(row=4, column=1)

btn_3 = Button(main, padx=button_padx, pady=button_pady, bd=8, fg="black",
               font=button_font, text="3", command=lambda: buttonClick(3))
btn_3.grid(row=4, column=2)

btn_mul = Button(main, padx=button_padx, pady=button_pady, bd=8, fg="black",
                 font=button_font, text="*", command=lambda: buttonClick("*"))
btn_mul.grid(row=4, column=3)

# Row 5: 0, ., =, /
btn_0 = Button(main, padx=button_padx, pady=button_pady, bd=8, fg="black",
               font=button_font, text="0", command=lambda: buttonClick(0))
btn_0.grid(row=5, column=0)

btn_dot = Button(main, padx=button_padx, pady=button_pady, bd=8, fg="black",
                 font=button_font, text=".", command=lambda: buttonClick("."))
btn_dot.grid(row=5, column=1)

btn_equal = Button(main, padx=button_padx, pady=button_pady, bd=8, fg="black",
                   font=button_font, text="=", command=buttonEqual)
btn_equal.grid(row=5, column=2)

btn_div = Button(main, padx=button_padx, pady=button_pady, bd=8, fg="black",
                 font=button_font, text="/", command=lambda: buttonClick("/"))
btn_div.grid(row=5, column=3)

main.mainloop()
