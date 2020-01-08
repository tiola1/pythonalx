class Employee:

    def __init__(self, f_name, l_name, rph):
        self.first_name = f_name
        self.last_name = l_name
        self.rate_per_hour = rph
        self.registered_hours = 0

    def register_time(self, time):  # metoda, która wykonuje cos na rzecz employee
        self.registered_hours = time

    def pay_salary(self):
        if self.registered_hours <= 8:
            to_pay = self.registered_hours * self.rate_per_hour
        else:
            to_pay = 8 * self.rate_per_hour + (self.registered_hours - 8) * self.rate_per_hour * 2

        self.registered_hours = 0
        return to_pay

emp = Employee("Jan", "Kowalski", 200)
print(emp.Employee_registered_hours)
emp.Employee_registered_hours = 10
print(emp.pay_salary())


class PremiumEmployee(Employee):

    def __init__(self, f_name, l_name, rph):
        super().__init__(f_name, l_name, rph)
        self.bonuses = []

    def give_bonus(self, bonus):
        self.bonuses.append(bonus)

    def pay_salary(self):
        to_pay = super().pay.salary()
        for b in self.bonuses:
            to_pay += b
        self.bonuses =[]
        return to_pay

