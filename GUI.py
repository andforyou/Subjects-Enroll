import tkinter as tk 
from tkinter import messagebox
from db import db
from mainpage import MainPage
import re





class LoginPage:

    def __init__(self,master):
        self.root = master
        self.root.geometry('400x300')
        self.root.title("University System")

        self.student_email = tk.StringVar()
        self.password = tk.StringVar()
        self.page = tk.Frame(root)
        self.page.pack()
        tk.Label(self.page).grid(row = 0, column= 0)

        tk.Label(self.page, text = 'Email:').grid(row=1,column=1,padx=40,pady=30)
        tk.Entry(self.page,textvariable=self.student_email).grid(row=1,column=2)
        tk.Label(self.page, text = 'Password:').grid(row=2,column=1,pady= 20)
        tk.Entry(self.page, textvariable=self.password).grid(row=2,column=2)
        tk.Button(self.page, text = 'Submit', command=self.login).grid(row=3,column=1,pady=5)
        tk.Button(self.page, text = 'Cancel', command=self.page.quit).grid(row=3,column=2,padx = 140,pady=20)

    def login(self):
        email = self.student_email.get()
        zpass = self.password.get()
        email_formatting =  r'(?i)[a-zA-Z0-9]+\.[a-zA-Z0-9]+@university\.com$'
        password_formatting = r'^[A-Z](?=(?:[^0-9]*[0-9]){3})(?=(?:[^a-zA-Z]*[a-zA-Z]){5}).*$'
        flag, message = db.check_login(email,zpass)
        if re.match(email_formatting,email) and re.match(password_formatting,zpass):
            if flag:
                messagebox.showwarning(title='Feedback',message=message)
                #db.all(email,zpass)
                self.page.destroy()
                MainPage(self.root)
            else:
                messagebox.showwarning(title='Warning',message=message)
            
        else:
            messagebox.showwarning(title='Warning',message='Incorrect email or password format')
            
        




if __name__ == '__main__':
    root = tk.Tk()
    LoginPage(master=root)

    root.mainloop()