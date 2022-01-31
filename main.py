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


def todo_amount(amount):
    todo_length = Label(
        window,
        text=f'ToDo\'s left {amount}',
        font=('JetBrains Mono', 10),
        foreground='red',
        background='black',
        highlightbackground='black')

    todo_length.grid_forget()
    todo_length.grid(row=6, column=0, sticky='SW')


class CreateLabel:
    amount = 0
    todo_amount(amount)
    max_todos = {0: None, 1: None, 2: None, 3: None, 4: None}

    def __init__(self, todo):
        if len(todo) >= 5 > self.amount:
            self.max_todos[self.amount] = Label(window, text=todo)
            self.max_todos[self.amount].grid(row=CreateLabel.amount, column=3)
            CreateLabel.amount += 1
            print(self.max_todos.values())
            if self.amount == 4:
                self.max_todos[2].grid_forget()
                print(self.max_todos.values())


    def destroy_widget(self):
        try:
            self.grid_forget()
            self.amount -= 1

        except:
            print('there is no object')


# Simple text on top of window
enter_text = Label(
    window, text='Please enter something ToDo', font=('JetBrains Mono', 10))


# TextBox Button
text_box = Entry(
    window, background='light yellow', width=35, bd=2)


# Submit Button
submit_btn = Button(
    window, text='Submit', width=5, bd=2, activeforeground='green', command=lambda: CreateLabel(text_box.get()))


# Quit Button
quit_btn = Button(
    window,
    text='Quit',
    width=6,
    activeforeground='red',
    command=window.destroy)

Button(
    window,
    text='Submit',
    width=5,
    bd=2,
    activeforeground='green',
    command=lambda: CreateLabel.destroy_widget()
).grid(row=5, column=2)


enter_text.grid(row=0, column=0, columnspan=2)
text_box.grid(row=1, column=0, columnspan=2)
submit_btn.grid(row=2, column=0, columnspan=2)

quit_btn.grid(row=6, column=1, columnspan=2, sticky='SE')

window.grid_rowconfigure(5, weight=1)
window.columnconfigure(1, weight=1)


window.mainloop()
