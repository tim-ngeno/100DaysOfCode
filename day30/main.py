""" Creating a Password Manager """

import json
import pyperclip
import random
import tkinter
from tkinter import messagebox


# ---------------------------- PASSWORD GENERATOR -------------------- #

def generate_password():
    """
    Generates a super strong and randomized secure password for the user
    """
    letters = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ]
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in
                        range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in
                        range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in
                        range(nr_numbers)]
    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(char for char in password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD --------------------------#


def save_details():
    """
    Save user details in a text file when the add button is clicked
    """
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    new_data = {
        website: {
            'email': email,
            'password': password,
        },
    }

    if website and email and password:
        if messagebox.askokcancel(
                title=website,
                message=f'These are the details entered:\nEmail:'
                f'{email}\nPassword: {password}.\nIs it ok to save?'
        ):

            try:
                with open('file.json', 'r') as file:
                    data = json.load(file)
                    # Update old data with new data
                    data.update(new_data)
            except FileNotFoundError:
                with open('file.json', 'w') as file:
                    json.dump(new_data, file, indent=4)

            else:
                # Save the updated data
                with open('file.json', 'w') as file:
                    json.dump(data, file, indent=4)
            finally:
                website_entry.delete(0, tkinter.END)
                password_entry.delete(0, tkinter.END)
        messagebox.showinfo(title=website,
                            message=f'Adding {website} success!')
    else:
        return


# ------------------------ RETRIEVE PASSWORD ------------------------- #

def find_password():
    """
    Retrieves the user's password for a queried website when the
    search button is pressed
    """
    website = website_entry.get()
    try:
        with open('file.json', 'r') as file:
            data = json.load(file)
            email = data[website]['email']
            password = data[website]['password']

    except FileNotFoundError:
        messagebox.showinfo(title='Error', message='No data file found')
    except KeyError:
        messagebox.showinfo(title=website,
                            message=f'No data for {website}')
    else:
        messagebox.showinfo(title=website,
                            message=f'{email}\n{password}')


# ---------------------------- UI SETUP -------------------------------#

# Create the user window
window = tkinter.Tk()
window.title('Password Manager')
window.config(padx=20, pady=20)


# Create a canvas with the logo as the background
canvas = tkinter.Canvas(width=200, height=200)
image = tkinter.PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0)


# Add labes and entry fields
website_label = tkinter.Label(text='Website')
website_label.grid(column=0, row=1)

website_entry = tkinter.Entry(width=24)
website_entry.grid(column=1, row=1)
website_entry.focus()

search_entry = tkinter.Button(text='Search', command=find_password, width=14)
search_entry.grid(column=2, row=1)

email_label = tkinter.Label(text='Email/Username')
email_label.grid(column=0, row=2)

email_entry = tkinter.Entry(width=42)
email_entry.insert(0, 'myemail@gmail.com')
email_entry.grid(column=1, row=2, columnspan=2)

password_label = tkinter.Label(text='Password')
password_label.grid(column=0, row=3)

password_entry = tkinter.Entry(width=24)
password_entry.grid(column=1, row=3)

password_generate_button = tkinter.Button(text='Generate password',
                                          command=generate_password,
                                          width=14)
password_generate_button.grid(column=2, row=3)

save_button = tkinter.Button(text='Add', width=40, command=save_details)
save_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
