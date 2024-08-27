from tkinter import *
from functools import partial

def buttonClick(number):
    global operator
    operator = operator + str(number)
    input_value.set(operator)

def buttonClear():
    global operator
    operator = ""
    input_value.set("")

def buttonEqual():
    global operator
    try:
        result = str(eval(operator))
        input_value.set(result)
    except:
        input_value.set("Error")
    operator = ""

main = Tk()
main.title("Calculator")
main.geometry("420x500")
main.configure(bg="#2b2024")

operator = ""
input_value = StringVar()

# หน้าจอแสดงตัวเลข
display_text = Entry(main, font=("arial", 32, "bold"), textvariable=input_value, bd=0, bg="#fbf9fa", fg="#2b2024", justify=RIGHT)
display_text.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=10, pady=10)

# ขนาดของปุ่ม
for i in range(5):
    main.grid_rowconfigure(i, weight=1)
    main.grid_columnconfigure(i, weight=1)

# สีของตัวเลข
def style_number_button(btn, color):
    btn.config(font=("arial", 20, "bold"), relief=RAISED, bd=1, bg=color, fg="#2b2024", activebackground="#e1e0e0", activeforeground="#2b2024")

# สีของตัวคิดเลข
def style_operator_button(btn):
    btn.config(font=("arial", 20, "bold"), relief=RAISED, bd=1, bg="#fd0054", fg="white", activebackground="#e60047", activeforeground="white")

# ศูนย์รวมปุ่ม
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3, 'operator'),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3, 'operator'),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3, 'operator'),
    ('0', 4, 0), ('C', 4, 1, 'special'), ('=', 4, 2, 'special'), ('+', 4, 3, 'operator'),
]

for (text, row, column, *button_type) in buttons:
    if button_type and button_type[0] == 'operator':
        btn = Button(main, text=text, command=partial(buttonClick, text))
        style_operator_button(btn)
    elif button_type and button_type[0] == 'special':
        if text == 'C':
            btn = Button(main, text=text, command=buttonClear)
        elif text == '=':
            btn = Button(main, text=text, command=buttonEqual)
    else:
        # Alternate colors for number buttons
        color = "#fbf9fa" if text in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] else "#a80038"
        btn = Button(main, text=text, command=partial(buttonClick, text))
        style_number_button(btn, color)

    btn.grid(row=row, column=column, sticky="nsew", padx=5, pady=5)

main.mainloop()
