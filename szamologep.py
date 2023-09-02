import tkinter as tk
import webbrowser

def on_number_click(number):
    current_text = entry_result.get()
    entry_result.delete(0, tk.END)
    entry_result.insert(tk.END, current_text + str(number))

def on_operator_click(operator):
    current_text = entry_result.get()
    if current_text and current_text[-1].isdigit():
        entry_result.insert(tk.END, operator)

def on_backspace_click():
    current_text = entry_result.get()
    entry_result.delete(0, tk.END)
    entry_result.insert(tk.END, current_text[:-1])

def on_backspace_click_ac():
    entry_result.delete(0, tk.END)


def calculate():
    try:
        expression = entry_result.get()
        if expression == '69':
            entry_result.delete(0, tk.END)
            entry_result.insert(tk.END, "sus")
        else:
            result = eval(expression)
            entry_result.delete(0, tk.END)
            entry_result.insert(tk.END, result)
    except:
        entry_result.delete(0, tk.END)
        entry_result.insert(tk.END, "Érvénytelen kifejezés!")

def open_channel():
    webbrowser.open("https://www.youtube.com/@craftolok")

app = tk.Tk()
app.title("Számológép")
app.configure(bg="#e6f7ff")  # Kékebb háttérszín

entry_result = tk.Entry(app, font=('Arial', 36))
entry_result.grid(row=0, column=0, columnspan=4, padx=20, pady=20)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('0', 4, 1),
]

for (text, row, col) in buttons:
    button = tk.Button(app, text=text, font=('Arial', 24), command=lambda t=text: on_number_click(t))
    button.grid(row=row, column=col, padx=10, pady=10)

operator_buttons = [
    ('+', 1, 3), ('-', 2, 3), ('*', 3, 3), ('/', 4, 3),
    ('C', 4, 0),
]

for (text, row, col) in operator_buttons:
    button = tk.Button(app, text=text, font=('Arial', 24), command=lambda t=text: on_operator_click(t) if t != 'C' else on_backspace_click())
    button.grid(row=row, column=col, padx=10, pady=10)

calculate_button = tk.Button(app, text="=", font=('Arial', 24), command=calculate)
calculate_button.grid(row=4, column=2, columnspan=1, padx=10, pady=10)

backspace_button = tk.Button(app, text="AC", font=('Arial', 18), command=on_backspace_click_ac)
backspace_button.grid(row=6, column=0, columnspan=1, padx=10, pady=10)

version_label = tk.Label(app, text="Version: 1.7.2", font=('Arial', 18))
version_label.grid(row=7, column=1, columnspan=2, padx=10, pady=10)

channel_button = tk.Button(app, text="Channel", font=('Arial', 18), command=open_channel)
channel_button.grid(row=7, column=2, columnspan=2, padx=10, pady=10, sticky='E')

app.mainloop()
