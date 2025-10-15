# Урок .  Виртуальная среда, встроенные модули Python, определение собственных модулей, внешние модули и их установка, Основы GIT.

class Money:
    def __init__(self, user: str, amount: float = 0, val: str = "not vallue", name: str = "", admin: bool = False):
        self.amount = amount
        self.val = val
        self.name = name
        self.user = user
        self.admin = admin 
    
    def __repr__(self):
        if self.__chek():
            return f"user: {self.user} \namount: {self.amount} \nval type: {self.val} \nadmin status: {self.admin}"
        else:
            return "у вас нет доступа к данной операции"


    def __chek(self) -> bool:
        if self.user == self.name or self.admin:
            return True
        else:
            return False


    def get_info(self) -> dict:
        if self.__chek():
            return {
                "amount": self.amount,
                "val": self.val
            }
        else:
            return {
                "error": "у вас нет доступа к данной операции"
            }


    def replen(self, sudj):
        if self.__chek():
            try:
                sum = float(input("какую сумму вы хотите перевести: "))
                if self.amount >= sum:
                    res1 = self.amount - sum
                    res2 = sudj.amount + sum
                    return res1, res2
                else:
                    print("у вас нет подобной суммы")
            except ValueError:
                print("введите число или число с точкой")
            except AttributeError:
                print("проверьте обьект который передаете в метод, он должен быть класса Money")
    
user_1 = Money(user="Bob", amount=12750.5, val="$", name="Bob", admin=False)
user_2 = Money(user="Carl", amount=720.0, admin=False)
user_3 = Money(user="Dag", amount=3024.7, val="$", admin=True)
user_4 = Money(user="Greg", amount=3054.6, val="$", name="Greg", admin=False)


"""
проверка работоспособности кода (класса)
"""

print(user_1.get_info())
print(user_3.get_info())
print("")
print(user_1)
print(user_3)
print("")
try:
    print(user_3.__chek)
except:
    print("приватный метод рабочий и вне класса недоступен")
print("")
user_1.replen(user_3)
print(user_1)
print(user_3)
print("")
user_3.replen(user_2)
print(user_3)
print(user_2)
print("")

class Distance:
    def __init__(self, value: float, unit: str):
        self.value = value
        self.unit = unit

    def __str__(self):
        return f"value={self.value}; \nunit={self.unit}"

    def __add__(self, obj):
        try:
            if self.unit == obj.unit:
                new_obj = Distance(value=self.value + obj.value, unit=self.unit)
                return new_obj
            else:
                return "у атрибутов должна быть одна единица измерения"
        except AttributeError:
            return "Проверьте что оба атрибута являются обьектами на основе класса Money"
        except:
            return "Произошла ошибка, проверьте вводимые данные"
        
    def __sub__(self, obj):
        try:
            if self.unit == obj.unit:
                new_obj = Distance(value=self.value - obj.value, unit=self.unit)
                if new_obj.value < 0:
                    raise ValueError("Растояние не может быть отрицательным (попробуйте поменять атрибуты местами)")
                return new_obj
            else:
                return "у атрибутов должна быть одна единица измерения"
        except AttributeError:
            return "Проверьте что оба атрибута являются обьектами на освнове класса Distance"
        except ValueError:
            return "Растояние не может быть отрицательным (попробуйте поменять атрибуты местами)"
        except:
            return "Произошла ошибка, проверьте вводимые данные"
        
    def __eq__(self, obj):
        try:
            if self.unit == obj.unit:
                if self.value == obj.value:
                    return True
                return False
            else:
                return "у атрибутов должна быть одна единица измерения"
        except AttributeError:
            return "Проверьте что оба атрибута являются обьектами на основе класса Distance"
        except:
            return "Произошла ошибка, проверьте вводимые данные"

    def unit_meters(self):
        if self.unit == "kilometers":
            self.value = self.value * 1000
            self.unit = "meters"
        elif self.unit == "meters":
            print("ваша единица измерения уже равна метрам")
        else:
            print("ввидите meters или kilometers")

    def unit_kilemeters(self):
        if self.unit == "meters":
            self.value /= 1000
            self.unit = "kilometers"
        elif self.unit == "kilometers":
            print("ваша единица измерения уже равно километрам")
        else:
            print("введите meters или kilometers")

obj1 = Distance(value=12000, unit="meters")
obj2 = Distance(value=12, unit="kilometers")
obj3 = Distance(value=24, unit="kilometers")
obj4 = Distance(value=5600, unit="meters")
obj5 = Distance(value=400, unit="meters")

print(obj1 == obj2)
print(obj1.unit_kilemeters == obj2)

print(obj3)

print(obj4 + obj5)
print(obj3 - obj2)
