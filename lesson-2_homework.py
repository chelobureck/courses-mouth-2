class Person:
    def __init__(self, name: str, birth_date: int, occupation: str ="unemployed", higher_education: bool =False):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education
    def introduce(self):
        return f"{self.name} was born in {self.birth_date}, works as a {self.occupation} and has higher education: {self.higher_education}"


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


# класс для доп задания номер 2
class BestFriend(Friend):
    def __init__(self, name: str, birth_date: int, occupation: str ="unemployed", higher_education: bool =False, hobby: str ="unknown", shared_memory: str = "none"):
        super().__init__(name, birth_date, occupation, higher_education, hobby) # init по родителю
        self.shared_memory = shared_memory
    def introduce(self):
        return f"{super().introduce()}, and our shared memory is: {self.shared_memory}"

carl = Classmate("Carl", 2015, group_name="Python Basics")
bob = Classmate("Bob", 1990, higher_education=True, group_name="Python Advanced")
leclerc = Friend("Leclerc", 2014, hobby="racing")
dave = Friend("Dave", 2006, higher_education=True, hobby="chess")

# обьект для доп задание номер 2
akmal = BestFriend("Akmal", 1995, "developer", True, "gaming", "We met in 2010 at a gaming event.")

# доп задание номер 1
gorge = Person("Gorge", 1980, "driver", True)
people = [carl, bob, leclerc, dave, gorge, akmal]

for person in people:
    print(person.introduce())


# print(str(person.introduce() for person in people))  # выводит ошибку <generator object <genexpr> at 0x7feba0de69b0>

