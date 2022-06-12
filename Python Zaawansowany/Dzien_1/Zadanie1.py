"""
    Przykład z danymi osobowymi na dwa sposoby
"""

name = "Zygmunt"
surname = "Stary"
age = 50
phone = "123-456-789"
job = "listonosz"

person_data = [name, surname, age, job, phone]
person_data2 = [name, surname, age, job, phone]

NAME_INDEX = 0
SURNAME_INDEX = 1
AGE_INDEX = 2
JOB_INDEX = 3
PHONE_INDEX = 4

print(f"Imię: {person_data[NAME_INDEX]}")

person_data_dict = {
    "name": name,
    "surname": surname,
    "age": age,
    "job": job,
    "phone": phone
}

print(f"Nazwisko: {person_data_dict['surname']}")

def generate_person_data(name, surname, age, job, phone):
    """Funkcja do generacji danych osobowych.

    :param name: Imie do wstawienia do słownika typ: str
    :param surname: Nazwisko do wstawienia do słownika typ: str
    :param age: Wiek do wstawienia do słownika typ: int
    :param job: Praca do wstawienia do słownika typ: str
    :param phone: Numer do wstawienia do słownika typ: str
    :return: Wygenerowany słownik z danymi.
    """
    person_data_dict = {
        "name": name,
        "surname": surname,
        "age": age,
        "job": job,
        "phone": phone
    }
    return person_data_dict

print(generate_person_data("Anna", "Inna", 30, "3333333","Programistka"))