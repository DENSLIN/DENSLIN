import random
from tkinter import *

digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z']
uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
             'V', 'W', 'X', 'Y', 'Z']
Symbols = ['!', '@', '#', '$', '%', '*', '&']


def genrate():
    mixture = digits + lowercase + uppercase + Symbols

    random_digit = random.choice(digits)
    random_lowercase = random.choice(lowercase)
    random_uppercase = random.choice(uppercase)
    random_symbol = random.choice(Symbols)

    Password = random.choice(random_digit + random_lowercase + random_uppercase + random_symbol)

    length = random.randint(8, 12)

    for x in range(length):
        Password = Password + random.choice(mixture)

    Gen_pass.delete(0, END)
    Gen_pass.insert(0, Password)


window = Tk()
window.geometry("250x200")
Gen_pass = Entry(window)
Gen_pass.grid(row=1, column=0, columnspan=2, padx=60, pady=30)
Label(window, text='Password generator').grid(row=0, column=0, columnspan=2)
# Label(window, text='click button to generate').grid(row=2, column=0)
Button(window, text='Generate', command=genrate).grid(row=2, column=0)
Button(window, text='copy').grid(row=2, column=1)
window.mainloop()
