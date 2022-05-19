class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

if __name__ == '__main__':
    print(f"{emp_1.fullname()} {(emp_1.email)} {(str(emp_1.pay))}")
    print(emp_2.fullname(), (emp_2.email), (str(emp_2.pay)))