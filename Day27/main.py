from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
# window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

entry = Entry(width=10)
entry.grid(row=0, column=1)

mile_label = Label(text="Miles")
mile_label.grid(row=0, column=2)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(row=1, column=0)

km_num_label = Label(text="")
km_num_label.grid(row=1, column=1)

km_label = Label(text="Km")
km_label.grid(row=1, column=2)


def convert():
    miles = float(entry.get())
    km = round(1.609 * miles, 1)
    km_num_label.config(text=str(km))


button = Button(text="Calculate", command=convert)
button.grid(row=2, column=1)

# my_label = tkinter.Label(text="I am a label")
# my_label.pack()
#
#
#
# def button_clicked():
#     my_label.config(text=input.get())
#
#
# button = tkinter.Button(text="Click Me", command=button_clicked)
# button.grid()
#
# input = tkinter.Entry(width=10)
# input.pack()
# print(input.get())


window.mainloop()
