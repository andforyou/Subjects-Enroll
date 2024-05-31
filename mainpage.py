import tkinter as tk
#from tkinter import Menu
from view import Enrollin, ShowErnoll


class MainPage:
    def __init__(self,master):
        self.root = master
        self.root.geometry('800x600') 
        self.root.title('Student System')
        self.create_page()
    def create_page(self):
        self.show_enroll_frame = ShowErnoll(self.root)
        #tk.Label(self.show_enroll_frame, text='View enrolled subjects').pack()
        self.enrollin_frame = Enrollin(self.root)
        #tk.Label(self.enrollin_frame,text='Enroll the subjects').pack()
        menubar = tk.Menu(self.root)
        menubar.add_command(label='Enroll Subjects',command=self.enrollin)
        menubar.add_command(label='Show enrolled Subjects',command=self.show_enroll)
        self.root['menu'] = menubar
        
    def show_enroll(self):
        self.show_enroll_frame.pack()
        self.enrollin_frame.pack_forget()
        
    def enrollin(self):
        self.enrollin_frame.pack()
        self.show_enroll_frame.pack_forget()
            
        
if __name__ =='__main__':
    root = tk.Tk()
    MainPage(master=root)
    root.mainloop()