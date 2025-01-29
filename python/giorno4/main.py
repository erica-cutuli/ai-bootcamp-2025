# Implement qui il codice
class Person:
    def __init__(self, name, surname, phone=None):
        self.name = name
        self.surname = surname
        self.phone = phone


class Business:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone


class Directory:
    def __init__(self):
        self.saved = []
    def add(self, contact):
        if isinstance(contact, (Person, Business)):
            self.saved.append(contact)
        else:
            raise TypeError("Puoi aggiungere solo oggetti di tipo Person o Business.")
    def __len__(self):
        return len(self.saved)
    def query(self, name):
        return [contact for contact in self.saved if contact.name == name]
    def find(self, term):
        return [
            contact for contact in self.saved
            if str(term) in str(contact.name)
            or (isinstance(contact, Person) and str(term) in str(contact.surname))
            or str(term) in str(contact.phone)
        ]