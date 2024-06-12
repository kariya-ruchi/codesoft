from tkinter import *
from math import *
import tkinter as tk
import random
import string

root = tk.Tk()
root.title("Password Generator")
root.resizable(width=False, height=False)

def generator():
    small_alphabets=string.ascii_lowercase 
    capital_alphabets=string.ascii_uppercase 
    numbers=string.digits 
    special_charecters=string.punctuation

    all=small_alphabets+capital_alphabets+numbers+special_charecters
    password_length=int(lengthbox.get())

    passfield.insert(0,random.sample(all,password_length))

    



choice=IntVar()
Font=('arial',15,'bold')
password=Label(root,text='Password Generator',font=('times new roman',20,'bold'))
password.grid(pady=10)

lengthlabel=Label(root,text='Password length',font=Font)
lengthlabel.grid(pady=5)

lengthbox=Spinbox(root,from_=6,to_=18,width=10,font=Font)
lengthbox.grid(pady=5)

generatebutton=Button(root,text='Generate',font=Font,bg='black',fg='white',command=generator)
generatebutton.grid(pady=15)

passfield=Entry(root,width=25,bd=2,font=Font)
passfield.grid()

root.mainloop()