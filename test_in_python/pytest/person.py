import datetime




class Person:


    def __init__(self,name,lastname,gender,birthdate):
        self.name = name 
        self.lastname =lastname
        self.gender = gender
        self.birthdate = birthdate

    def full_name(self):
        return f"{self.name} {self.lastname}".capitalize()


    def generate_email(self):
        return f"{self.name}{self.lastname}@gmail.com"


    def age(self):
        return datetime.datetime.today().year - self.birthdate
