from datetime import date

class Person:

    def __init__(self, name, sex, year_of_birth, city):
        self.name = name
        self.sex = sex
        self.year_of_birth = year_of_birth
        self._age = date.today().year - self.year_of_birth
        self.city = city


    def eat(self):
        return 'I can eat.'

    def walk(self):
        return 'I can walk.'

    def info(self):
        print(f'name: {self.name}, '
              f'sex: {self.sex}, '
              f'age: {self._age}, '
              f'city: {self.city}')


class Employee(Person):

    def __init__(self, name, sex, year_of_birth, city, company, departament, position ):
        super().__init__(name, sex, year_of_birth, city)
        self.company = company
        self.departament = departament
        self.position = position

    def work(self):
        return 'I can work.'

    def info(self):
        print(f'name: {self.name}, '
              f'sex: {self.sex}, '
              f'age: {self._age}, '
              f'city: {self.city}, '
              f'company: {self.company}, '
              f'departament: {self.departament} '
              f'position: {self.position}')

class Developer(Employee):
    defolt_departament = 'development departament'
    def __init__(self, name, sex, year_of_birth, city, company, position, language):
        super().__init__(name, sex, year_of_birth, city, company, Developer.defolt_departament, position)
        self.language = language

    def work(self):
        return 'I can write cod.'

    def info(self):
        print(f'name: {self.name}, '
              f'sex: {self.sex}, '
              f'age: {self._age}, '
              f'city: {self.city}, '
              f'company: {self.company}, '
              f'departament: {self.departament} '
              f'position: {self.position}, '
              f'language: {self.language}')



personBob = Person('Bob', 'M', 1976, 'London')
personBob.info()
# print(personBob.name, personBob.sex, personBob._age, personBob.city, personBob.eat())

personLi = Person('Li', 'F', 1979, 'Paris')
personLi.info()
# print(personLi.name, personLi.sex, personLi._age, personLi.city, personLi.walk())

employee1 = Employee('Tina', 'F', 1980, 'Vena', 'ABC', 'administrative department', 'Manager')
employee1.info()
# print(employee1.name, employee1.sex, employee1._age, employee1.city, employee1.company, employee1.position, employee1.eat(), employee1.work())

developer1 = Developer('Den', 'M', 1975, 'San Diego', 'ITCod', 'developer', 'C++')
developer1.info()
# print(developer1.name, developer1.sex, developer1._age, developer1.city, developer1.company, developer1.position, developer1.eat(), developer1.work())

developer2 = Developer('Anna', 'F', 1986, 'Riga', 'Script', 'junior', 'Java')
developer2.info()
# print(developer2.name, developer2.sex, developer2._age, developer2.city, developer2.company, developer2.position, developer2.walk(), developer2.work())

developer3 = Developer('Sem', 'M', 1988, 'Mumbai', 'MIX', 'intern', 'Python')
developer3.info()
# print(developer3.name, developer3.sex, developer3._age, developer3.city, developer3.company, developer3.position, developer3.walk(), developer3.work())