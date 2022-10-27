
import pyperclip
import tkinter
from tkinter import messagebox

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

import random

def generate_pass():
  label3_entry.delete(0, tkinter.END)
  letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

  nr_letters = random.randint(8, 10)
  nr_symbols = random.randint(2, 4)
  nr_numbers = random.randint(2, 4)


  password_letters = [random.choice(letters) for char in range(nr_letters)]
  password_symbols = [random.choice(symbols) for char in range(nr_symbols)]
  password_numbers = [random.choice(numbers) for c in range(nr_numbers)]

  password_list = password_letters + password_symbols + password_numbers
  random.shuffle(password_list)

  password = "".join(password_list)
  label3_entry.insert(0, password)
  pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
  web_data = label1_entry.get()
  email = label2_entry.get()
  pas = label3_entry.get()
  
  if len(web_data) == 0:
    messagebox.showinfo(title="Opps" ,  message="Website Field is blank")
    
  elif len(pas) == 0:
    messagebox.showinfo(title="Opps" ,  message="Password Field is blank")
      
    
  
  if len(web_data) and len(pas) != 0:
    is_ok = messagebox.askokcancel(title = "Disclaimer" , message = f"These are detailes entered: \nEmail: {email} \nPassword: {pas} \nIs it ok to save")
    
    if is_ok:
      with open ("pass.txt", "a") as data:
        data.write(f"{web_data} | {email} | {pas} \n")
        label1_entry.delete(0, tkinter.END)
        label3_entry.delete(0, tkinter.END)

# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Password Manger")
window.config(padx=70, pady=70)

canva = tkinter.Canvas(height=200, width=200)
img = tkinter.PhotoImage(file="logo.png")
canva.create_image(100,100 , image=img)
canva.grid(row=0, column=1)


# labels

label1 = tkinter.Label(text="Website:")
label1.grid(row=1, column=0)
label2 = tkinter.Label(text="Email/Username:")
label2.grid(row=2, column=0)
label3 = tkinter.Label(text="Password:")
label3.grid(row=3, column=0)

# enteries

label1_entry = tkinter.Entry(width=35)
label1_entry.grid(row=1, column=1, columnspan=2)
label1_entry.focus()


label2_entry = tkinter.Entry(width=35)
label2_entry.grid(row=2, column=1, columnspan=2)
label2_entry.insert(0, "yashthorat60@gmail.com")

label3_entry = tkinter.Entry(width=35)
label3_entry.grid(row=3, column=1, columnspan=2 )


# buttons

PAss_generator_bu = tkinter.Button(text="Genreate Password" ,command=generate_pass)
PAss_generator_bu.grid(row=3, column=3)

add_bu = tkinter.Button(text="Add", width=36, command=save)
add_bu.grid(row=4, column=1, columnspan=2)


window.mainloop()