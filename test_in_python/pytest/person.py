class Person:
    def __init__(self, name, lastname, age, location):
        self.name = name
        self.lastname = lastname
        self.age = age
        self.location = location

    def full_name(self):
        return f"{self.name} {self.lastname}".capitalize()

    def locat(self):
        return f"{self.full_name} in {self.location}"

    def email_person(self):
        return f"{self.name}{self.lastname}@gmail.com"