import datetime

class Choice:
    #def __init__(self):
        #self.name = "Admin"

    def register(self,university):
        university.register()

    def login(self,university):
        university.login()

    def remove_subject(self,university):
        university.remove_subject()

    def group(self,university):
        university.group()
    
    def change(self,university):
        university.change()

    def enroll(self,university):
        university.enroll()
        
    def show_subject(self,university):
        university.show_subject()
        
    
    def read_choice(self):
        print("\033[36mStudent System (l/r/x): \033[0m", end="")
        return input().strip().lower()
    
    def use(self,university):
        print(f"Student System menu: {datetime.datetime.now()}")
        c = ''
        while True:
            c = self.read_choice()
            if c == 'x':
                break
            elif c == 'l':
                self.login(university)
            elif c == 'r':
                self.register(university)
            # elif c == 'p':
            #     self.partition(university)
            # elif c == 'r':
            #     self.remove(university)
            # elif c == 's':
            #     self.show(university)
            # else:
            #     self.help()
        print("Back to University menu")
        
    def read_sub_choice(self):
        print("Student Course Menu (c/e/r/s/x):", end="")
        return input().strip().lower()
    
    def use_second(self,university):
        c = ''
        while True:
            c = self.read_sub_choice()
            if c =='x':
                break
            elif c == 'c':
                self.change(university)
            elif c == 'e':
                self.enroll(university)
            elif c == 'r':
                self.remove_subject(university)
            elif c =='s':
                self.show_subject(university)
        print("Back to student system menu")