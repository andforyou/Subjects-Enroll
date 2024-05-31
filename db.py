import json
import re
from tkinter import messagebox 
from student import Student
import random



class MysqlDatabase:
    def __init__(self):
        with open('students.data', mode ='r') as f:
            text = f.read()
        self.users = json.loads(text)
        
        with open('students.data', mode ='r') as f:
            data = f.read()
        self.students = json.loads(data)
        self.current_student =None
        
    def check_login(self,email,password):
        for user in self.users:
            if email == user['Email']:
                self.current_student = user
                if password == user['Password']:
                    return True,'Sign in successful'
                else:
                    return False, 'Invalid Password'
        return False, 'Student does not exist'
    
    
    def all(self):
        # student = next((stu for stu in self.students if stu["Email"] == email and stu["Password"] == password), None)
        # if student:
        #     return student
        # else:
        #     return None
        return self.current_student
    
    def enroll(self,subject):
        stu = self.current_student
        
        if len(stu['Subjects']) >=4:
            messagebox.showwarning(title='Warning',message='Students are allowed to enroll in 4 subjects only')
            return False,'Students are allowed to enroll in 4 subjects only'
        
        else:
            code = str(random.randint(1,999)).zfill(3)
            
            
            mark = random.randint(25,100)
            if mark < 50:
                grade = "Z"
            elif mark < 65:
                grade = "P"
            elif mark < 75:
                grade = "C"
            elif mark < 85:
                grade = "D"
            else:
                grade = "HD"

            subject_data = {
                "Subject": subject,
                "Code": code,
                "Mark": mark,
                "Grade": grade
            }
                
            stu['Subjects'].append(subject_data)
            messagebox.showinfo(title='Success',message='Enrolled')
   
        #             with open('students.data',mode ='w') as f:
        #                 json.dump(self.users,f,indent=4)
        #             return True 
        # except StopIteration:
        #     return False, "User not found!"
        
        # except IOError:
        #     return False, "Failed to save data. Please try again."
                
                
                
                
                
                
                
                
                
                
                
                
db = MysqlDatabase()
if __name__ == '__main__':
    print(db.check_login('z.x@university.com','Worldhello123'))
    