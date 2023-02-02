from tkinter import *


def Button_click():
    print("I got called")
    miles = miles_input.get()
    km = int(miles) * 1.6
    km_label.config(text=f"{km}")
    km_label.grid(column=1, row=1)

    Button()


# Window
window = Tk()
window.title("Miles to Km Converter")
# window.minsize(width=300, height=200)
window.config(padx=20, pady=20)

# Button
button = Button(text="Calculate", command=Button_click)
button.grid(column=1, row=2)


# Entry
miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)
miles_input.get()

# Label
is_eq_label = Label(text='is equal too', font=("Arial", 10))
is_eq_label.grid(column=0, row=1)


km_label = Label(text='Km', font=("Arial", 10))
km_label.grid(column=2, row=1)


miles_label = Label(text='Miles', font=("Arial", 10))
miles_label.grid(column=2, row=0)


window.mainloop()
