

class Person:
    def __init__(self, name: str, birth_date: int, occupation: str ="unemployed", higher_education: bool =False):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education


bob = Person("Bob", 1990, "builder", True)
carl = Person("Carl", 2015)
dave = Person("Dave", 2006, higher_education=True)

print(f"{bob.name} was born in {bob.birth_date}, works as a {bob.occupation} and has higher education: {bob.higher_education}")
print(f"{carl.name} was born in {carl.birth_date}, works as a {carl.occupation} and has higher education: {carl.higher_education}")
print(f"{dave.name} was born in {dave.birth_date}, works as a {dave.occupation} and has higher education: {dave.higher_education}")