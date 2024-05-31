
# from utils import DTF,NOW,CUSTOMER_FILE,initialize,read_from_file,write_to_file
from admin import Admin
from database import Database as db
import ast
# import datetime
from student import Student, students
import json
from choice import Choice


class University:
    def __init__(self):
        self.admin = Admin()
        db.initialize()
        self.choice = Choice()
        # self.customers = read_from_file()

    def main(self):

        try:
            with open("students.data", "r") as file:
                data = json.load(file)
                for student_data in data:
                    id = student_data['Student_ID']
                    del student_data['Student_ID']
                    student_data = {'name': student_data['Name'], 'email': student_data['Email'],
                                    'password': student_data['Password'], 'subject': student_data['Subjects']}
                    student = Student(**student_data, from_file=True)
                    student.id = id
                    students.append(student)
        except FileNotFoundError:
            with open("students.data", "w") as file:
                json.dump([], file)
        self.menu()

    def read_choice(self):
        print(
            "\033[36mUniversity System: (A)dmin, (S)tudent, or X :\033[0m", end="")
        return input().strip().upper()

    def admin_login(self, university):
        self.admin.use(university)

    def student_sub_login(self, university):
        self.choice.use_second(university)

    def student_login(self, university):
        # self.choice.use(university)
        while True:
            choice = input(f'{"":8}\033[36mStudent System (l/r/x) :\033[0m')
            if choice.lower() == "x":
                break
            elif choice.lower() == "r":
                print(f'{"":8}\033[32mStudent sigh up\033[0m')
                while True:
                    try:
                        email = input(f'{"":8}Email: ')
                        password = input(f'{"":8}Password: ')
                        if not Student.verify_password(password) or not Student.verify_email(email):
                            raise ValueError(
                                f'{"":8}\033[31mIncorrect email or password format\033[0m')
                        print(
                            f'{"":8}\033[33mEmail and password formats acceptable\033[0m')

                        # check_email = Student.existemail(email)
                        existing_student = Student.existemail(email)
                        # if check_email:
                        if existing_student:
                            print(
                                f'{"":8}\033[31mStudent {existing_student.name} already exists\033[0m')
                            break
                        name = input(f'{"":8}Name: ')
                        student = Student(name, email, password)
                        print(f'{"":8}\033[33mEnrolling Student {name}\033[0m')
                        student_new = '\t\t' + \
                            '\t\t'.join(str(student).splitlines(True))
                        student.save_students_file()
                        break
                    except ValueError as e:
                        print(str(e))
            elif choice.lower() == "l":
                print(f'{"":8}\033[32mStudent sign in \033[0m')
                Student.load()
                while True:
                    matched_student = None
                    main_manu = False
                    try:
                        email = input(f'{"":8}Email: ')
                        password = input(f'{"":8}Password: ')
                        if not Student.verify_password(password) or not Student.verify_email(email):
                            raise ValueError(
                                f'{"":8}\033[31mIncorrect email or password format\033[0m')

                        print(
                            f'{"":8}\033[33mEmail and password formats acceptable\033[0m')

                        for student in students:
                            if student.email == email and student.password == password:
                                matched_student = student
                                # print("Sign in successful")
                                break
                        if not matched_student:
                            if Student.existemail(email):
                                raise ValueError(
                                    f'{"":8}\033[31mInvalid password\033[0m')
                            else:
                                print(
                                    f'{"":8}\033[31mStudent does not exist\033[0m')
                                break

                    except ValueError as e:
                        print(str(e))
                        # if str(e) in ["Student DNE", "Invalid password",]:
                        continue

                    if matched_student:
                        while True:
                            sub_choice = input(
                                f'{"":16}\033[36mStudent Course Menu (c/e/r/s/x): \033[0m')
                            if sub_choice.lower() == "x":
                                main_manu = True
                                break

                            elif sub_choice.lower() == "c":
                                print(
                                    f'{"":16}\033[33mUpdating password\033[0m')
                                while True:
                                    new_pass = input(f'{"":16}New password: ')
                                    second_pass = input(
                                        f'{"":16}Confirm Password: ')
                                    if new_pass == second_pass:  # Check if passwords match
                                        # Verify password format
                                        if Student.verify_password(new_pass):
                                            student.change(new_pass)
                                            print(
                                                f'{"":16}\033[33mPassword updated successfully\033[0m')
                                            break
                                        else:
                                            print(
                                                f'{"":16}\033[31mIncorrect password format\033[0m')
                                    else:
                                        print(
                                            f'{"":16}\033[31mPassword does not match - try again\033[0m')
                                main_manu = True
                                break

                            elif sub_choice.lower() == "e":
                                while True:
                                    try:
                                        note = matched_student.enroll()
                                        print(
                                            "\t\t"+note.replace('\n', '\n\t\t'))
                                        main_manu = True
                                        break
                                    except ValueError as e:
                                        print(str(e))
                                    break

                            elif sub_choice.lower() == "r":
                                while True:
                                    subject_code = input(
                                        f'{"":16}Remove subject by ID: ')
                                    try:
                                        note = student.remove_subject(
                                            subject_code)
                                        print(
                                            "\t\t"+note.replace('\n', '\n\t\t'))
                                        main_manu = True
                                        break
                                    except ValueError as e:
                                        print(str(e))
                                    break
                            elif sub_choice.lower() == "s":
                                student.show_enroll()
                                main_manu = True
                            else:
                                # print(f'{"":16}033\31mInvalid Choice\033[0m')
                                # break
                                print(f'{"":16}Menu options')
                                print(f'{"":16}c = change password')
                                print(f'{"":16}e = enroll a subject')
                                print(f'{"":16}r = remove a subject')
                                print(f'{"":16}s = show subject list')
                                print(f'{"":16}x = exit')
                    if main_manu:
                        break

    def menu(self):
        # print("University menu: " + str(datetime.datetime.now()))
        while True:
            choice = self.read_choice()
            if choice == 'X':
                break
            elif choice == 'S':
                self.student_login(self)
            elif choice == 'A':
                self.admin_login(university)
            else:
                self.help()
        print("\033[33mThank You\033[0m")

    def help(self):
        print("Menu options")
        print("L = Login into student menu")
        print("A = Login to admin menu")
        print("X = exit")

    def save_students_file(self):
        def extract_subject_info(subj_str):
            if isinstance(subj_str, str):

                subj_name, rest = subj_str.split("::", 1)
                subj_id, rest = rest.split(" -- Mark = ", 1)
                mark, grade = rest.split(" -- Grade = ", 1)
                return {
                    "Subject": subj_name.strip(),
                    "ID": int(subj_id.strip()),
                    "Mark": float(mark.strip()),
                    "Grade": grade.strip()
                }
            elif isinstance(subj_str, dict):
                return subj_str
        data = [{
            "Name": student.name,
            "Email": student.email,
            "Password": student.password,
            "Subjects": [extract_subject_info(subject) for subject in student.subject],
            "Student_ID": student.id,
        }
            for student in students
        ]

        with open("students.data", "w") as file:
            json.dump(data, file, indent=4)

    def clear(self):
        print(f'{"":8}\033[33mClearing students database\033[0m')
        answer = input(
            f'{"":8}\033[31mAre you sure you want to clear the database (Y)es/(N)o: \033[0m')
        global students
        if answer.upper() == 'Y':
            students.clear()
            with open("students.data", "w") as file:
                json.dump([], file)
            print(f'{"":8}\033[33mStudents data cleared\033[0m')
        # elif answer == 'y':
        #     students.clear()
        #     with open("students.data", "w") as file:
        #         json.dump([], file)
        #     print(f'{"":8}\033[33mStudents data cleared\033[0m')
        elif answer.upper() == 'N':
            print(f'{"":8}Operation stopped')
        # elif answer == 'n':
        #     print(f'{"":8}Operation stopped')
        else:
            raise ValueError(f'{"":8}\033[31mInvalid command\033[0m')

    def show(self):
        print(f'{"":8}\033[33mStudent list\033[0m')
        # data = db.read()
        if students:
            for stu in students:
                print(f'{"":8}{stu.name} :: {stu.id} --> Email: {stu.email}')
        else:
            print(f'{"":8}Nothing to display')

    @staticmethod
    def average_mark(student):
        if not student.subject:
            return 0
        total = 0
        for subj in student.subject:
            total += subj['Mark']
        return round(total/len(student.subject), 2)

    def grade_student(self, average_mark):
        if average_mark is None:
            grade = "No result"
        elif average_mark >= 85:
            grade = "HD"
        elif average_mark >= 75:
            grade = "D"
        elif average_mark >= 65:
            grade = "C"
        elif average_mark >= 50:
            grade = "P"
        else:
            grade = "Z"

    def group(self):
        print(f'{"":8}\033[33mGrade Grouping\033[0m')
        # grade_list ={'HD':[],'D':[],'C':[],'P':[],'Z':[]}
        grade_list_HD = []
        grade_list_D = []
        grade_list_C = []
        grade_list_P = []
        grade_list_Z = []
        if students:
            for student in students:
                if student.subject == []:
                    continue
                else:
                    average_mark = University.average_mark(student)
                    if average_mark is None:
                        grade = "No result"
                    elif average_mark >= 85:
                        grade = "HD"
                        grade_list_HD.append(
                            (student.name, student.id, grade, average_mark))
                    elif average_mark >= 75:
                        grade = "D"
                        grade_list_D.append(
                            (student.name, student.id, grade, average_mark))
                    elif average_mark >= 65:
                        grade = "C"
                        grade_list_C.append(
                            (student.name, student.id, grade, average_mark))
                    elif average_mark >= 50:
                        grade = "P"
                        grade_list_P.append(
                            (student.name, student.id, grade, average_mark))
                    else:
                        grade = "Z"
                        grade_list_Z.append(
                            (student.name, student.id, grade, average_mark))

        else:
            print(f'{"":8}Nothing to display')
            return
        if grade_list_HD:

            for entry in grade_list_HD:
                frmt_entries_HD = []
                for entry in grade_list_HD:
                    frmt_entry = f'{entry[0]}::{entry[1]} --> GRADE: {entry[2]} - MARK: {entry[3]}'
                    frmt_entries_HD.append(frmt_entry)
            print(f'{"":8}HD--> {frmt_entries_HD}')
                # print(
                #     f'{"":8}HD --> [{entry[0]}::{entry[1]} --> GRADE: {entry[2]} - MARK: {entry[3]}]')
        if grade_list_D:

            for entry in grade_list_D:
                
                frmt_entries_D = []
                for entry in grade_list_D:
                    frmt_entry = f'{entry[0]}::{entry[1]} --> GRADE: {entry[2]} - MARK: {entry[3]}'
                    frmt_entries_D.append(frmt_entry)
            print(f'{"":8}D --> {frmt_entries_D}')
                # print(
                #     f'{"":8}D --> [{entry[0]}::{entry[1]} --> GRADE: {entry[2]} - MARK: {entry[3]}]')
        if grade_list_C:

            for entry in grade_list_C:
                frmt_entries_C = []
                for entry in grade_list_C:
                    frmt_entry = f'{entry[0]}::{entry[1]} --> GRADE: {entry[2]} - MARK: {entry[3]}'
                    frmt_entries_C.append(frmt_entry)
            print(f'{"":8}C --> {frmt_entries_C}')
                # print(
                #     f'{"":8}C --> [{entry[0]}::{entry[1]} --> GRADE: {entry[2]} - MARK: {entry[3]}]')
        if grade_list_P:

            for entry in grade_list_P:
                frmt_entries_P = []
                for entry in grade_list_P:
                    frmt_entry = f'{entry[0]}::{entry[1]} --> GRADE: {entry[2]} - MARK: {entry[3]}'
                    frmt_entries_P.append(frmt_entry)
            print(f'{"":8}P --> {frmt_entries_P}')
                # print(
                #     f'{"":8}P --> [{entry[0]}::{entry[1]} --> GRADE: {entry[2]} - MARK: {entry[3]}]')
        if grade_list_Z:

            for entry in grade_list_Z:
                frmt_entries_Z = []
                for entry in grade_list_Z:
                    frmt_entry = f'{entry[0]}::{entry[1]} --> GRADE: {entry[2]} - MARK: {entry[3]}'
                    frmt_entries_Z.append(frmt_entry)
            print(f'{"":8}Z --> {frmt_entries_Z}')
                # print(
                #     f'{"":8}Z --> [{entry[0]}::{entry[1]} --> GRADE: {entry[2]} - MARK: {entry[3]}]')

    def partition(self):
        # data = db.read()
        # if data:
        #     student_list = ast.literal_eval(db.read())
        #     if not student_list:
        #         print("Nothing to display")
        #         return

        #     pass_list = []
        #     fail_list = []
        #     for student in student_list:
        #         email, password, name, id, average_mark = student
        #         student_info = f'{name}::{id} --> {average_mark}'
        #         if average_mark >=50:
        #             pass_list.append(student_info)
        #         else:
        #             fail_list.append(student_info)
        pass_list = []
        fail_list = []
        for student in students:
            average_mark = University.average_mark(student)
            if average_mark is None:
                grade = "No result"
            elif average_mark >= 85:
                grade = "HD"
            elif average_mark >= 75:
                grade = "D"
            elif average_mark >= 65:
                grade = "C"
            elif average_mark >= 50:
                grade = "P"
            else:
                grade = "Z"

            if average_mark:
                if average_mark >= 50:
                    pass_list.append(
                        (student.name, student.id, grade, average_mark))
                else:
                    fail_list.append(
                        (student.name, student.id, grade, average_mark))
        print(f'{"":8}\033[33mPASS/FALL partition\033[0m')
        # print('PASS --> %s' %pass_list)
        # print('FALL -->%s' %fail_list)
        # if not pass_list:
        #     print(f'{"":8}PASS --> []')
        # else:
        #     for entry in pass_list:
        #         print(
        #             f'{"":8}Pass --> [{entry[0]}::{entry[1]} --> GRADE: {entry[2]} - MARK: {entry[3]}]')
        # if not fail_list:
        #     print(f'{"":8}FAIL --> []')
        # else:
        #     for entry in fail_list:
        #         print(
        #             f'{"":8}Fail --> [{entry[0]}::{entry[1]} --> GRADE: {entry[2]} - MARK: {entry[3]}]')
        # print(f'Pass: {pass_list[1]} ')
        # print(f'Pass: {fail_list[]} ')
        if not pass_list:
            print(f'{"":8}PASS --> []')
        else:
            formatted_entries =[]
            for entry in pass_list:
                formatted_entry = f'{entry[0]}::{entry[1]} --> GRADE: {entry[2]} - MARK: {entry[3]}'
                formatted_entries.append(formatted_entry)
            print(f'{"":8}PASS --> {formatted_entries}')
        if not fail_list:
            print(f'{"":8}FAIL --> []')
        else:
            frmt_entries = []
            for entry in fail_list:
                frmt_entry = f'{entry[0]}::{entry[1]} --> GRADE: {entry[2]} - MARK: {entry[3]}'
                frmt_entries.append(frmt_entry)
            print(f'{"":8}FAIL --> {frmt_entries}')
        
        
        
        

    def remove(delete_id):
        try:
            delete_id = input(f'{"":8}Remove by ID: ')
            global student
            target = next(
                (student for student in students if student.id == delete_id), None)
            if target is None:
                raise ValueError(
                    f'{"":8}\033[31mStudent {delete_id} does not exist\033[0m')

            students.remove(target)
            target.save_students_file()
            print(
                f'{"":8}\033[33mRemoving student %s account\033[0m' % delete_id)
        except ValueError as e:
            print(str(e))
        # if data:
        #     student_list = ast.literal_eval(db.read())
        #     if not student_list:
        #         print("Nothing to display")
        #     else:
        #         id_list = [student[len(student_list)-2] for student in student_list]
        #         if delete_id not in id_list:
        #             print('Student %s does not exist'%delete_id)
        #             return False
        #         for student in student_list:
        #             if student[len(student_list)-2] == delete_id:
        #                 student_list.remove(student)
        #                 print('Removing student %s account'%delete_id)
        # else:
        #     student_list =[]
        # db.save()
        # return True


# Running the main function
university = University()
university.main()
