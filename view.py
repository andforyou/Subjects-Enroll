import tkinter as tk 
from tkinter import ttk, messagebox
from db import db
from student import Student, students

class ShowErnoll(tk.Frame):
    def __init__(self,root):
        super().__init__(root)
        self.table_view = tk.Frame()
        self.table_view.pack()
        self.create_page()
        
    def create_page(self):
        columns = ("Subject ID", "Mark", "Grade")
        columns_values = ("Subject ID", "Mark", "Grade")
        self.tree_view = ttk.Treeview(self,show = 'headings', columns = columns)
        self.tree_view.column('Subject ID',width = 200,anchor = 'center')
        self.tree_view.column('Mark',width = 200,anchor = 'center')
        self.tree_view.column('Grade',width = 200,anchor = 'center')
        self.tree_view.heading('Subject ID',text = 'Subject ID')
        self.tree_view.heading('Mark',text = 'Mark')
        self.tree_view.heading('Grade',text = 'Grade')
        self.tree_view.pack(fill = tk.BOTH, expand= True)
        self.show_data_frame()
        tk.Button(self, text ='Refresh', command = self.show_data_frame).pack(anchor = tk.E, pady = 5)
        
    def show_data_frame(self):
        for _ in map(self.tree_view.delete,self.tree_view.get_children('')):
            pass
        students = db.all()
        index = 0
        
        for subject in students['Subjects']:
            subject_ID = subject['Code']
            subject_grade = subject['Grade']
            subject_mark = subject['Mark']    
            self.tree_view.insert('',index +1, values=(
                subject_ID, subject_mark,subject_grade
                ))    
    
    
    
class Enrollin(tk.Frame):
    def __init__(self,root):
        super().__init__(root)
        #tk.Label(self, text='Enroll subjects').pack()    
        
        self.name = tk.StringVar()
        self.create_page()
    
    def create_page(self):
        tk.Label(self).grid(row= 0,pady=20)   
        tk.Label(self,text = 'Subject Name:').grid(row=1,column=1,pady=20)
        tk.Entry(self,textvariable=self.name).grid(row=1,column=2,pady=20)
        tk.Button(self, text ='Submit', command = self.submit_enroll).grid(row=2,column=2, pady = 5)
        
    def submit_enroll(self):
        subject = self.name.get()
        # while True:
        #     subject = self.name.get()
        #     try:
        #         note = Student.enroll(subject)
        #         print("\t\t"+note.replace('\n','\n\t\t'))
                
        #         break
        #     except ValueError as e:
        #         print(str(e))
        #     if ValueError:
        #         messagebox.showwarning(title='Warning',message=ValueError)
        #     else:
        #         messagebox.showwarning(title='Feedback',message='Enrolled')
        #     break
        student = db.all()
        email = student['Email']
        db.enroll(subject)
    
        self.name.set('')
        
        