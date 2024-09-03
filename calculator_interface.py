from tkinter import *
from calculator_logic import buttonClick, buttonClear, buttonBackspace, buttonEqual

def create_calculator_frame(parent, display_text, page_name):
    frame = Frame(parent, bg="#F7F7F8")
    frame.grid(row=1, column=0, sticky='nsew')

    # Configure grid rows and columns to expand properly
    for i in range(6):
        frame.grid_rowconfigure(i, weight=1)
    for i in range(5):
        frame.grid_columnconfigure(i, weight=1)

    # Common button padding and font
    button_font = ("Helvetica", 18, "bold")

    if page_name == "basic":
        buttons = [
            ("%", 1, 0), ("√", 1, 1), ("²", 1, 2), ("C", 1, 3), ("⌫", 1, 4),
            ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("+", 2, 3), ("(", 2, 4),
            ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("-", 3, 3), (")", 3, 4),
            ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("*", 4, 3),
            ("0", 5, 0), (".", 5, 1), ("=", 5, 2), ("/", 5, 3),
        ]
    elif page_name == "advanced":
        buttons = [
            ("sin", 1, 0), ("cos", 1, 1), ("tan", 1, 2), ("C", 1, 3), ("⌫", 1, 4),
            ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("+", 2, 3), ("(", 2, 4),
            ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("-", 3, 3), (")", 3, 4),
            ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("*", 4, 3),
            ("0", 5, 0), (".", 5, 1), ("=", 5, 2), ("/", 5, 3),
        ]

    for (text, row, col) in buttons:
        if text == "=":
            button = Button(frame, bg="#FF8C00", fg="white", font=button_font, text=text,
                            command=lambda: buttonEqual(display_text))
        elif text == "C":
            button = Button(frame, bg="#FF3B30", fg="white", font=button_font, text=text,
                            command=lambda: buttonClear(display_text))
        elif text == "⌫":
            button = Button(frame, bg="#FF3B30", fg="white", font=button_font, text=text,
                            command=lambda: buttonBackspace(display_text))
        else:
            button = Button(frame, bg="#F0F0F5", fg="black", font=button_font, text=text,
                            command=lambda t=text: buttonClick(display_text, t))
        button.grid(row=row, column=col, padx=5, pady=5, sticky='nsew')

    return frame

def switch_frame(frame):
    frame.tkraise()

def toggle_mode():
    if current_mode.get() == "basic":
        current_mode.set("advanced")
        switch_frame(advanced_frame)
        switch_mode_button.config(text="Switch to Basic")
    else:
        current_mode.set("basic")
        switch_frame(basic_frame)
        switch_mode_button.config(text="Switch to Advanced")

def main():
    global basic_frame
    global advanced_frame
    global switch_mode_button
    global current_mode

    main_window = Tk()
    main_window.title("Modern Calculator")
    main_window.geometry("360x600")
    main_window.configure(bg="#F7F7F8")

    # Configure the main window grid
    main_window.grid_rowconfigure(0, weight=1)
    main_window.grid_rowconfigure(1, weight=5)
    main_window.grid_columnconfigure(0, weight=1)
    main_window.grid_columnconfigure(1, weight=1)

    # Create the display text entry with enhanced styling
    display_text = Entry(main_window, font=("Helvetica", 40, "bold"), bd=2, bg="#333", fg="#FFF",
                         justify=RIGHT, insertbackground='white', highlightbackground="#555", highlightthickness=1)
    display_text.grid(row=0, column=0, columnspan=2, padx=10, pady=20, sticky='nsew')

    # Create a StringVar to manage the current mode
    current_mode = StringVar()
    current_mode.set("basic")  # Start with the basic mode

    # Create frames for each page
    basic_frame = create_calculator_frame(main_window, display_text, "basic")
    advanced_frame = create_calculator_frame(main_window, display_text, "advanced")

    # Create navigation buttons
    nav_frame = Frame(main_window, bg="#F7F7F8")
    nav_frame.grid(row=1, column=0, sticky='nsew')

    # Create a frame for the mode switch button to position it at the top right
    mode_button_frame = Frame(main_window, bg="#F7F7F8")
    mode_button_frame.grid(row=0, column=1, sticky='ne', padx=10, pady=10)

    switch_mode_button = Button(mode_button_frame, text="Switch to Advanced", command=toggle_mode,
                                bg="#007AFF", fg="white", font=("Helvetica", 14, "bold"), bd=0)
    switch_mode_button.pack()

    # Start with the basic frame
    switch_frame(basic_frame)

    main_window.mainloop()

if __name__ == "__main__":
    main()
