
class Contact:
    id = 0

    def __init__(self, phone_number: str, name: str):
        self.phone_number = phone_number
        self.name = name
        Contact.id += 1

    def __str__(self):
        return f"name={self.name}; number={self.phone_number}"
    
    @staticmethod
    def validate_phone_number(phone_number: str):
        if len(phone_number) == 10 and phone_number[0] == "0":
            int(phone_number)
            return True
        elif "+" in phone_number:
            raise  ValueError("Программа работает без кода страны")
            # return "Программа работает без кода страны"
        else:
            raise ValueError("Неверный формат номера телефона")
            # return "Неверный формат номера телефона"

class ContactList:
    all_contacts = {}

    def __init__(self):
        pass

    @staticmethod
    def add_contact(cls, phone_number: str, name: str):
        try:
            Contact.validate_phone_number(phone_number)
            ContactList.all_contacts[Contact.id] = str(Contact(phone_number, name))
        except ValueError:
            return "Неверный формат номера телефона"
    
    @staticmethod
    def remove_contact(cls, contact_id: int):
        try:
            del ContactList.all_contacts[contact_id]
        except:
            print("такого контакта нету")


# user1 = Contact("+996578645376", "Ivan")
# print(Contact.validate_phone_number("+996578645376"))

contact_list = ContactList()
# print(ContactList.add_contact("0548649654", "Petr"))
# print(ContactList.add_contact("0578644376", "Ivan"))
# print(ContactList.add_contact("0578644654", "Petr"))
# print(ContactList.add_contact("0757864465", "Petr"))
print(ContactList.add_contact(ContactList, "0775786446", "Petr"))
print(ContactList.add_contact(ContactList, "0757578644", "Petr"))
print(ContactList.all_contacts)
print(Contact.id)
# contact_list.remove_contact(contact_id=4)
# print(contact_list.add_contact("0757575644", "nazik"))
# print(contact_list.add_contact("0757574644", "gulnazik"))
print(ContactList.all_contacts)
print(Contact.id)