import re
import random
import json


class Student:
    def __init__(self, name, email, password, subject=[], from_file=False):
        self.name = name
        self.email = email
        self.password = password
        self.subject = subject
        if not from_file:
            self.generate_id()
            self.save_students_file()

    def load():
        global students
        students.clear()
        try:
            with open("students.data", "r") as file:
                data = json.load(file)
                for student_data in data:
                    id = student_data['Student_ID']
                    del student_data['Student_ID']
                    student_data = {
                        'name': student_data['Name'],
                        'email': student_data['Email'],
                        'password': student_data['Password'],
                        'subject': student_data['Subjects'],
                    }
                    student = Student(**student_data, from_file=True)
                    student.id = id
                    students.append(student)

        except FileNotFoundError:
            with open("students.data", "w") as file:
                json.dump([], file)

    def generate_id(self):
        global students

        random_id = str(random.randint(0, 999999)).zfill(6)
        ids = [student.id for student in students]
        while random_id in ids:
            random_id = str(random.randint(0, 999999)).zfill(6)
        self.id = random_id
        students.append(self)

    def verify_email(email):
        formatting = r'(?i)[a-zA-Z0-9]+\.[a-zA-Z0-9]+@university\.com$'
        return re.match(formatting, email)

    def verify_password(password):
        formatting = r'^[A-Z](?=(?:[^0-9]*[0-9]){3})(?=(?:[^a-zA-Z]*[a-zA-Z]){5}).*$'
        return re.match(formatting, password)

    def searchbyid(id):
        for student in students:
            if student.id == id:
                return student
        return None

    @staticmethod
    def existemail(email):
        for student in students:
            if student.email == email:
                return student
        return None

    # def existemail(email):
    #     return any(student.email.upper() == email.upper() for student in students)

    def enroll(self, subject=None):
        if len(self.subject) >= 4:
            raise ValueError(
                f'{"":16}\033[31mStudents are allowed to enroll in 4 subjects only\033[0m')
        if subject is None:
            subject = f"Subject {len(self.subject) + 1}"

        code = str(random.randint(1, 999)).zfill(3)
        while any(s['Code'] == code for s in self.subject):
            code = str(random.randint(1, 999)).zfill(3)

        for sbj in self.subject:
            if sbj['Subject'] == subject.lower():
                raise ValueError(
                    f'{"":16}You have already enrolled in this subject')

        # subject_code = f"subject - {code}"

        mark = random.randint(25, 100)

        if mark >= 85:
            grade = "HD"
        elif mark >= 75:
            grade = "D"
        elif mark >= 65:
            grade = "C"
        elif mark >= 50:
            grade = "P"
        else:
            grade = "Z"

        subject_dict = {
            "Subject": subject,
            "Code": code,
            "Mark": mark,
            "Grade": grade
        }
        self.subject.append(subject_dict)
        self.save_students_file()

        return f'{"":16}\033[33mEnrolled in Subject - {code}\033[0m'\
            f'\n\033[33mYou have enrolled in {len(self.subject)} out of 4 subjects \033[0m'

    def remove_subject(self, subject_code):
        for subject in self.subject:
            if str(subject['Code']) == str(subject_code):
                self.subject.remove(subject)
                self.save_students_file()
                return f'{"":16}\033[33mDroping Subject -- {subject["Code"]}\033[0m' \
                    f'\n\033[33mYou have enrolled in {len(self.subject)} out of 4 subjects\033[0m'
        raise ValueError(
            f'{"":16}\033[31mYou did not enrolled in the Subject -- [{subject_code}]\033[0m')

    def show_enroll(self):
        print(f'{"":16}\033[33mShowing {len(self.subject)} subjects\033[0m')
        for subject in self.subject:
            print(
                f'{"":16}Subject :: {subject["Code"]}-- mark = {subject["Mark"]} -- grade = {subject["Grade"]}')

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

    def change(self, new_pass):
        if Student.verify_password(new_pass):
            self.password = new_pass
            # print("Updating Password")
            self.save_students_file()
        else:
            print(f'{"":16}Incorrect password format')

    def __str__(self):
        return f"Name: {self.name}\nStudent ID {self.id}\nEmail: {self.email}\nPassword: {self.password}\n"

    def __repr__(self):
        return f"Name: {self.name}\nStudent ID {self.id}\nEmail: {self.email}\nPassword: {self.password}\n"


students = []
