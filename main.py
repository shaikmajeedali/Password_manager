from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import json

#password generator
def gen_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_letters = [choice(letters) for _ in range(nr_letters)]
    password_symbols = [choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    # password = ""
    # for char in password_list:
    #   password += char

    password = "".join(password_list)
    # print(password)
    pass_entry.insert(0, password)






panel = Tk()
panel.title("password Manager")
panel.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(row=0, column=1)

#save pass
def save():

    website = web_entry.get()
    email = email_entry.get()
    password = pass_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Enter Data", message="please fill th data")
    else:
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            with open("data1.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
                data.update(new_data)
                with open("data.json", "w") as file:
                    json.dump(data, file, indent=4)
        finally:
                web_entry.delete(0, END)
                pass_entry.delete(0, END)

def find_password():
    website = web_entry.get()
    try:
        with open("data.json") as file:
           data = json.load(file)
    except FileNotFoundError:
            messagebox.showinfo(title="error", message="File not found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email:{email}\n password:{password}")
        else:
            messagebox.showinfo(title="error", message=f"no details for {website} exist")

#labels
web_label = Label(text="Website")
web_label.grid(row=1, column=0)
email_label = Label(text="Email/Username")
email_label.grid(row=2, column=0)
pass_label = Label(text="Password")
pass_label.grid(row=3, column=0)

#entry
web_entry = Entry(width=21)
web_entry.grid(row=1, column=1)
web_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "Abc@gmail.com")
pass_entry = Entry(width=21)
pass_entry.grid(row=3, column=1)

#button
search_button = Button(text="search", width=10, command=find_password)
search_button.grid(row=1, column=2)
gen_button = Button(text="Generate pass", command=gen_password)
gen_button.grid(row=3, column=2)
add_button = Button(text="add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

panel.mainloop()

