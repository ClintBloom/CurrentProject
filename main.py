import tkinter
from tkinter import Label
from tkinter import Button
from tkinter import Entry
from time import sleep


window_title = 'ToDo List'

window = tkinter.Tk()
window.title(window_title)
window.geometry("400x200")
window.resizable(False, False)


class LabelUpdate:
    def __init__(self):
        self.common = Label(window, text='hello')

    def common_command(self):
        self.common.grid(row=0, column=3)


def destroy_object(widget):
    try:
        widget.grid_forget()
    except:
        print('there is no object')


hello_maker = Label(
    window,
    text='hello'
)


# Simple text on top of window
enter_text = Label(
    window,
    text='Please enter something ToDo',
    font=('JetBrains Mono', 10),
)


# TextBox Button
text_box = Entry(
    window,
    background='light yellow',
    width=35,
    bd=2,
)


# Submit Button
begin = LabelUpdate()
start = begin.common_command
submit_btn = Button(
    window,
    text='Submit',
    width=5,
    bd=2,
    activeforeground='green',
    command=start
)


# Number of ToDo Lists
todo_number = 0
todo_length = Label(
    window,
    text=f'ToDo\'s left {todo_number}',
    font=('JetBrains Mono', 10),
    foreground='red',
    background='black',
    highlightbackground='black'
)


# Quit Button
quit_btn = Button(
    window,
    text='Quit',
    width=6,
    activeforeground='red',
    command=window.destroy
)

Button(
    window,
    text='Submit',
    width=5,
    bd=2,
    activeforeground='green',
    command=lambda: destroy_object(begin.common)
).grid(row=5, column=2)


enter_text.grid(row=0, column=1, columnspan=2)
text_box.grid(row=1, column=1, columnspan=2)
submit_btn.grid(row=2, column=1, columnspan=2)
todo_length.grid(row=6, column=2, padx=10)
quit_btn.grid(row=6, column=1, columnspan=2)
window.grid_rowconfigure(5, weight=1)
window.columnconfigure(1, weight=1)


window.mainloop()
