# Урок 5.  Виртуальная среда, встроенные модули Python, определение собственных модулей, внешние модули и их установка, Основы GIT.

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
            elif self.unit == "kilometers" and obj.unit == "meters":
                return Distance(value=self.value + obj.value / 1000, unit="kilometers")
            elif self.unit == "meters" and obj.unit == "kilometers":
                return Distance(value=self.value + obj.value * 1000, unit="meters")
            else:
                return "только meters и kilometers являются допустимыми единицами измерения"
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
            elif self.unit == "kilometers" and obj.unit == "meters":
                new_value = self.value - obj.value / 1000
                if new_value < 0:
                    raise ValueError("Растояние не может быть отрицательным (попробуйте поменять атрибуты местами)")
                return Distance(value=new_value, unit="kilometers")
            elif self.unit == "meters" and obj.unit == "kilometers":
                new_value = self.value - obj.value * 1000
                if new_value < 0:
                    raise ValueError("Растояние не может быть отрицательным (попробуйте поменять атрибуты местами)")
                return Distance(value=new_value, unit="meters")
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
            elif self.unit == "kilometers" and obj.unit == "meters":
                return self.value * 1000 == obj.value
            elif self.unit == "meters" and obj.unit == "kilometers":
                return self.value == obj.value * 1000
            else:
                return "только meters и kilometers являются допустимыми единицами измерения"
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


print(obj3)

print(obj4 + obj5)
print(obj3 - obj2)
