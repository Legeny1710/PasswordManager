from tkinter import *
from tkinter import messagebox
import random
import json



# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_input.delete(0, END)
    char = "1234567890@%^&*()qwertyuiopasdfghjklzxcvbnm"
    password = ""
    for i in range(8):
        password += random.choice(char)

    password_input.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():


    website = website_input.get()
    username = user_name_input.get()
    password = password_input.get()

    new_data = {
        website: {
            "username": username,
            "password": password
        }
    }

    if website == "" or username == "" or password == "":
        messagebox.showwarning(title="ERROR", message="You must fill all the fields to save the password!")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)


# ---------------------------- Search/Find Password ----------------------------#
def find_password():
    website = website_input.get()
    username = user_name_input.get()
    password = password_input.get()

    try:
        with open("data.json", "r") as data:
            d = json.load(data)
    except FileNotFoundError:
        messagebox.showwarning(title="ERROR",message="No Data file Found")
    else:
        found = False
        for website_name, details in d.items():
            if website_name == website:
                found = True
                messagebox.showinfo(title="Search Result", message=f"Username: {details['username']}\n Password: {details['password']}")
            elif website_name != website:
                found = False

        if not found:
            messagebox.showwarning(title="Search Result", message="No details for this website exists")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager - YPass")
window.config(padx=40, pady=40)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo =  PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=1, columnspan=3)

#Website entry
website_text = Label(text="Website:")
website_text.grid(column=1, row=2 )

website_input = Entry(width=18)
website_input.grid(column=2, row=2)
website_input.focus()

#Email/Username entry
user_name_text = Label(text="Email/Username:")
user_name_text.grid(column=1, row=3)

user_name_input = Entry(width=35)
user_name_input.grid(column=2, row=3, columnspan=2)
user_name_input.insert(0, "xyz@gmail.com")

#Password
password_text = Label(text="Password:")
password_text.grid(column=1, row=4)

password_input = Entry(width=18)
password_input.grid(column=2, row=4)

password_generate_button = Button(text="Generate Password", width=12, command=generate_password)
password_generate_button.grid(column=3, row=4)

#Add
add_button = Button(text="Add", width=45, command=save_password)
add_button.grid(column=1, row=5, columnspan=3)

#search button
search_button = Button(text="Search", width=12, command=find_password)
search_button.grid(column=3, row=2)

























window.mainloop()