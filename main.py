import tkinter
from tkinter import Label
from tkinter import Button
from tkinter import Entry


window_title = 'ToDo List'
window = tkinter.Tk()
window.title(window_title)
window.geometry("400x200")
window.resizable(False, False)


class CreateLabel:
    amount = 0
    max_todos = []

    def __init__(self, todo):
        if len(todo) >= 3:
            if self.amount < 5:
                self.max_todos.append(Label(window, text=todo))
                self.max_todos[self.amount].grid(row=CreateLabel.amount, column=2)
                CreateLabel.amount += 1


def todo_amount():
    if CreateLabel.amount != 0:
        color = 'red'
    else:
        color = 'green'

    todo_length = Label(
        window,
        text=f'ToDo\'s left {CreateLabel.amount}',
        font=('JetBrains Mono', 10),
        foreground=color,
        background='black',
        highlightbackground='black')
    todo_length.grid_forget()
    todo_length.grid(row=6, column=0, sticky='SW')


def destroy_widget():
    if 5 >= len(CreateLabel.max_todos) > 0:
        CreateLabel.max_todos[CreateLabel.amount - 1].grid_forget()
        CreateLabel.max_todos.pop(CreateLabel.amount - 1)
        CreateLabel.amount -= 1
        todo_amount()


def submit_button():
    CreateLabel(text_box.get())
    text_box.delete(0, 'end')


def combine():
    submit_button()
    todo_amount()


# TextBox Button
text_box = Entry(
    window, background='light yellow', width=35, bd=2)

# Simple text on top of window
enter_text = Label(
    window, text='Please enter something ToDo', font=('JetBrains Mono', 10))

# Submit Button
submit_btn = Button(
    window, text='Submit', width=5, bd=2, activeforeground='green', command=combine)

# Quit Button
quit_btn = Button(
    window,
    text='Quit',
    width=6,
    activeforeground='red',
    command=window.destroy)

# Delete Button
delete_btn = Button(
    window,
    text='Delete',
    width=5,
    bd=2,
    activeforeground='red',
    command=destroy_widget)


enter_text.grid(row=0, column=0, columnspan=2)
text_box.grid(row=1, column=0, columnspan=2)
submit_btn.grid(row=2, column=0, columnspan=2)
delete_btn.grid(row=5, column=2, pady=5, padx=10, sticky='SE')
quit_btn.grid(row=6, column=2, pady=10, padx=10, sticky='SE')


window.grid_rowconfigure(5, weight=1)
window.columnconfigure(1, weight=1)

todo_amount()
window.mainloop()
