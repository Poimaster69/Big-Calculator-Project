from tkinter import *
from calculator_logic import buttonClick, buttonClear, buttonBackspace, buttonEqual

def create_rounded_button(parent, text, command, x, y, width, height, bg, fg, font):
    canvas = Canvas(parent, width=width, height=height, bg='black', highlightthickness=0)
    canvas.grid(row=y, column=x, padx=5, pady=5, sticky='nsew')
    
    # Draw the rounded rectangle
    radius = height // 4
    canvas.create_arc(0, 0, 2 * radius, 2 * radius, start=90, extent=90, fill=bg, outline=bg)  # Top-left corner
    canvas.create_arc(width - 2 * radius, 0, width, 2 * radius, start=0, extent=90, fill=bg, outline=bg)  # Top-right corner
    canvas.create_arc(0, height - 2 * radius, 2 * radius, height, start=180, extent=90, fill=bg, outline=bg)  # Bottom-left corner
    canvas.create_arc(width - 2 * radius, height - 2 * radius, width, height, start=270, extent=90, fill=bg, outline=bg)  # Bottom-right corner
    canvas.create_rectangle(radius, 0, width - radius, height, fill=bg, outline=bg)  # Top rectangle
    canvas.create_rectangle(0, radius, width, height - radius, fill=bg, outline=bg)  # Left and right rectangles
    
    # Create the button overlay
    button = Button(parent, text=text, font=font, bg=bg, fg=fg, command=command,
                    relief='flat', borderwidth=0, width=2, height=2)
    button_window = canvas.create_window(width // 2, height // 2, window=button)
    
    return canvas

def create_calculator_frame(parent, display_text, page_name):
    frame = Frame(parent, bg="black")
    frame.grid(row=1, column=0, sticky='nsew')

    # Configure grid rows and columns to expand properly
    for i in range(6):
        frame.grid_rowconfigure(i, weight=1)
    for i in range(5):
        frame.grid_columnconfigure(i, weight=1)

    # Common button size and font
    button_font = ("Helvetica", 18, "bold")
    button_width = 80
    button_height = 80

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
            create_rounded_button(frame, text, lambda: buttonEqual(display_text), col, row, button_width, button_height, "#FF8C00", "white", button_font)
        elif text == "C":
            create_rounded_button(frame, text, lambda: buttonClear(display_text), col, row, button_width, button_height, "#FF3B30", "white", button_font)
        elif text == "⌫":
            create_rounded_button(frame, text, lambda: buttonBackspace(display_text), col, row, button_width, button_height, "#FF3B30", "white", button_font)
        else:
            create_rounded_button(frame, text, lambda t=text: buttonClick(display_text, t), col, row, button_width, button_height, "white", "black", button_font)

    return frame

def switch_frame(frame):
    frame.tkraise()

def main():
    global basic_frame
    global advanced_frame
    global current_mode

    main_window = Tk()
    main_window.title("Rounded Edge Calculator")
    main_window.geometry("360x600")
    main_window.configure(bg="black")

    # Configure the main window grid
    main_window.grid_rowconfigure(0, weight=1)
    main_window.grid_rowconfigure(1, weight=5)
    main_window.grid_columnconfigure(0, weight=1)
    main_window.grid_columnconfigure(1, weight=1)

    # Create the display text entry with enhanced styling
    display_text = Entry(main_window, font=("Helvetica", 40, "bold"), bd=0, bg="#333", fg="#FFF",
                         justify=RIGHT, insertbackground='white', highlightthickness=0)
    display_text.grid(row=0, column=0, columnspan=2, padx=10, pady=20, sticky='nsew')

    # Create a StringVar to manage the current mode
    current_mode = StringVar()
    current_mode.set("basic")  # Start with the basic mode

    # Create frames for each page
    basic_frame = create_calculator_frame(main_window, display_text, "basic")
    advanced_frame = create_calculator_frame(main_window, display_text, "advanced")

    # Start with the basic frame
    switch_frame(basic_frame)

    main_window.mainloop()

if __name__ == "__main__":
    main()
