import math
from tkinter import INSERT, END

def buttonClick(display_text, value):
    current_text = display_text.get()
    str_value = str(value)

    if str_value.isdigit() or str_value in "+-*/.%²()":
        if current_text == "" and str_value in "+*/.%²)":
            return
        if current_text and current_text[-1] in "+-*/.%²(" and str_value in "+-*/.%²)":
            return

        pos = display_text.index(INSERT)
        display_text.insert(pos, str_value)
    
    elif str_value == '√':
        if current_text == "" or current_text[-1] in "+-*/.":
            pos = display_text.index(INSERT)
            display_text.insert(pos, '√()')
        else:
            pos = display_text.index(INSERT)
            display_text.insert(pos, '*√()')

def buttonClear(display_text):
    display_text.delete(0, END)

def buttonBackspace(display_text):
    current_text = display_text.get()
    if current_text:
        pos = display_text.index(INSERT)
        if pos > 0:
            display_text.delete(pos - 1)

def buttonEqual(display_text):
    expression = display_text.get()

    try:
        # Convert '√' to 'math.sqrt(' and '²' to '**2'
        expression = expression.replace('√()', 'math.sqrt(')
        expression = expression.replace('²', '**2')

        # Handle unmatched parentheses
        open_parentheses = expression.count('(')
        close_parentheses = expression.count(')')
        close_parens_needed = open_parentheses - close_parentheses
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

def keyPress(event, display_text):
    key = event.char
    if key.isdigit() or key in "+-*/.%()":
        buttonClick(display_text, key)
    elif key == "\r":
        buttonEqual(display_text)
    elif key == "\x08":
        buttonBackspace(display_text)
