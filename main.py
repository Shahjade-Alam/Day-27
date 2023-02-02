from tkinter import *


def Button_click():
    print("I got called")
    new_text = input.get()
    my_label.config(text=new_text)
    Button()


window = Tk()

window.title("My First GUI program")
window.minsize(width=500, height=300)
window.config(padx=100,pady=200)

# Label
my_label = Label(text='I am a label', font=("Arial", 24))
my_label.config(text='NEW TEXT')
my_label.grid(column=0, row=0)
my_label.config(padx=50,pady=50)
# Button
button = Button(text="Click Me", command=Button_click)
# button.pack()
button.grid(column=1, row=1)

button = Button(text="New Button", )
# button.pack()
button.grid(column=2, row=0)

# Entry
input = Entry(width=10)
# input.pack()
input.grid(column=3, row=2)
input.get()

window.mainloop()
