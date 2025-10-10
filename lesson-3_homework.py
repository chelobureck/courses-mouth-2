import datetime as dt


class Person:
    def __init__(self, name: str, birth_date: int | str, occupation: str ="unemployed", higher_education: bool =False):
        self.name = name
        self.__birth_date = birth_date
        self.__occupation = occupation
        self.__higher_education = higher_education
    def introduce(self):
        return f"{self.name} was born in {self.__birth_date}, works as a {self.__occupation} and has higher education: {self.__higher_education}"
    @property
    def age(self):
        current_year = dt.datetime.now().year
        return current_year - int(self.__birth_date)


# класс наследник по домашке
class Classmate(Person):
    def __init__(self, name: str, birth_date: int, occupation: str ="unemployed", higher_education: bool =False, group_name: str ="unknown"):
        super().__init__(name, birth_date, occupation, higher_education) # init по родителю
        self.group_name = group_name
    def introduce(self):
        return f"{super().introduce()}, and is in group: {self.group_name}"


# класс наследник по домашке
class Friend(Person):
    def __init__(self, name: str, birth_date: int, occupation: str ="unemployed", higher_education: bool =False, hobby: str ="unknown"):
        super().__init__(name, birth_date, occupation, higher_education) # init по родителю
        self.hobby = hobby
    def introduce(self):
        return f"{super().introduce()}, and has hobby: {self.hobby}"


fr1 = Friend("Айбек", 2000, "студент", True, "футбол")
cl1 = Classmate("Иван", 2000, "студент", True, "11D")

print(fr1.introduce())
print(cl1.introduce())
print(f"{fr1.name} is {fr1.age} years old")
print(f"{cl1.name} is {cl1.age} years old")