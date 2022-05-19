class Employee:
    def __init__(self, surname="Default", month_remuneration="Nie podałeś", hours_a_week="Nie podałeś"):
        self._surname = surname
        self.month_remuneration = month_remuneration
        self.hours_a_week = hours_a_week

    def get_surname(self):
        return self._surname

if __name__ == "__main__":
    e1 = Employee("Kowalski", hours_a_week=160)
    e2 = Employee("Wiśniewski", 50)
    print(e1._surname, e1.month_remuneration, e1.hours_a_week)
    print(e2._surname, e2.month_remuneration, e2.hours_a_week)