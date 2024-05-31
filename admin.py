# import datetime

class Admin:
    def __init__(self):
        self.name = "Admin"

    def clear(self, university):
        university.clear()

    def show(self, university):
        university.show()

    def remove(self, university):
        university.remove()

    def group(self, university):
        university.group()

    def partition(self, university):
        university.partition()

    def read_choice(self):
        print(f'{"":8}\033[36mAdmin menu (c/g/p/r/s/x): \033[0m', end="")
        return input().strip().lower()

    def use(self, university):
        # print(f"{self.name} menu: {datetime.datetime.now()}")
        c = ''
        while True:
            c = self.read_choice()
            if c == 'x':
                break
            elif c == 'c':
                self.clear(university)
            elif c == 'g':
                self.group(university)
            elif c == 'p':
                self.partition(university)
            elif c == 'r':
                self.remove(university)
            elif c == 's':
                self.show(university)
            else:
                self.help()
        # print("Back to University menu")

    def help(self):
        print(f'{"":8}Menu options')
        print(f'{"":8}c = clear database')
        print(f'{"":8}r = remove a student')
        print(f'{"":8}s = show students')
        print(f'{"":8}g = group students')
        print(f'{"":8}p = partition students')
        print(f'{"":8}x = exit')
