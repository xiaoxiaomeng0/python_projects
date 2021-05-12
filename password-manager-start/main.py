from tkinter import *
# * is all the classes.
from tkinter import messagebox
import random
import pyperclip
import json

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letter = [random.choice(letters) for i in range(nr_letters)]
    password_symbol = [random.choice(symbols) for i in range(nr_symbols)]
    password_number = [random.choice(numbers) for i in range(nr_numbers)]
    password_list = password_letter + password_symbol + password_number
    random.shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #d
def save():
    website_string = website_input.get()
    email_string = email_input.get()
    password_string = password_input.get()
    new_data = {
        website_string: {
            "email": email_string,
            "password": password_string
        }
    }

    if not website_string or not email_string or not password_string:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website_string, message=f"These are the details entered: "
                                                             f"\nEmail: {email_string} \nPassword: {password_string} \nIs it ok to save?")
        if is_ok:
            try:
                with open("my_data.json", "r") as file:
                    data = json.load(file)
                    data.update(new_data)
            except FileNotFoundError:
                with open("my_data.json", "w") as file_write:
                    json.dump(new_data, file_write, indent=4)
            else:
                with open("my_data.json", "w") as file_write:
                    json.dump(data, file_write, indent=4)
            finally:
                clear()

def clear():
    website_input.delete(0, "end")
    password_input.delete(0, "end")

def find_password():
    website_search = website_input.get()
    try:
        with open("my_data.json", "r") as file_read:
            data = json.load(file_read)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No such website found!")
    else:
        if website_search in data:
            messagebox.showinfo(title=website_search, message=f"Name: {website_search}\n "
                                                              f"Password: {data[website_search]['password']}")
        else:
            messagebox.showinfo(title="Error", message=f"{website_search} not in the system.")

# ---------------------------- UI SETUP ------------------------------- #
canvas = Canvas(window, width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

email_user_label = Label(text="Email/Username:")
email_user_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

website_input = Entry(width=21)
website_input.grid(row=1, column=1)
website_input.focus()

email_input = Entry(width=35)
email_input.grid(row=2, column=1, columnspan=2)
email_input.insert(0, "anna@gmail.com")

password_input = Entry(width=21)
password_input.grid(row=3, column=1)

button_search = Button(text="Search", command=find_password)
button_search.grid(row=1, column=2, sticky="ew")

button_pass_gen = Button(text="Generate Password", command=generate_password)
button_pass_gen.grid(row=3, column=2)

button_add = Button(text="Add", width=36, command=save)
button_add.grid(row=4, column=1, columnspan=2)


window.mainloop()