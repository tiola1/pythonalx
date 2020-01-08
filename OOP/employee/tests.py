from Employee import Employee and PremiumEmployee, AmountBonus,

class Bonus:
    def __init__(self,value):
        self.value = value

class AmountBonus()

# def test_employee():
#     emp = Employee ('Jan', 'Nowak', '100.00')
#     assert emp.name      # robione samodzielnie


class TestEmployee:


    def test_init_(self):
        e = Employee("Jan", "Kowalski", 100)
        assert e.first_name == "Jan"
        assert e.last_name == "Kowalski"
        assert e.rate_per_hour == 100


    def test_register_time(self):
        e = Employee("Jan", "Kowalski", 100)
        e.register_time(5)
        assert e.registered_hours == 5

    def  test_pay_salary_normal_hours(self):
        e = Employee("Jan", "Kowalski", 100)
        e.register_time(5)
        assert e.pay_salary() == 500

    def  test_pay_salary_without_registered_time(self):
        e = Employee("Jan", "Kowalski", 100)
        e.register_time(0)
        assert e.rate_per_hour== 100
        assert e.pay_salary() == 0

    def test_pay_salary_twice_normal_hours(self):
        e = Employee("Jan", "Kowalski", 100)
        e.register_time(5)
        assert e.pay_salary() == 500
        assert e.pay_salary() == 0

    def test_pay_salary_over_hours(self):
        e = Employee("Jan", "Kowalski", 100)
        e.register_time(10)
        assert e.pay_salary() == 1200

class TestPremiumEmployee:
    def test_init_(self):
        e = PremiumEmployee("Jan", "Kowalski", 100)
        assert e.first_name == "Jan"
        assert e.last_name == "Kowalski"
        assert e.rate_per_hour == 100

    def test_register_time(self):
        e = PremiumEmployee("Jan", "Kowalski", 100)
        e.register_time(5)
        assert e.registered_hours == 5

    def test_pay_salary_normal_hours(self):
        e = PremiumEmployee("Jan", "Kowalski", 100)
        e.register_time(5)
        assert e.pay_salary() == 500

    def test_pay_salary_without_registered_time(self):
        e = PremiumEmployee("Jan", "Kowalski", 100)
        e.register_time(0)
        assert e.rate_per_hour == 100
        assert e.pay_salary() == 0

    def test_pay_salary_twice_normal_hours(self):
        e = PremiumEmployee("Jan", "Kowalski", 100)
        e.register_time(5)
        assert e.pay_salary() == 500
        assert e.pay_salary() == 0

    def test_pay_salary_over_hours(self):
        e = PremiumEmployee("Jan", "Kowalski", 100)
        e.register_time(10)
        assert e.pay_salary() == 1200

    def test_give_bonus(self):
        e = PremiumEmployee("Jan", "Kowalski", "100")
        bonus = AmountBonus(1000)
        e.give_bonus(1000)
        assert e.bonuses == [1000]

    def test_pay_salary_with_over_hours(self):
        e = PremiumEmployee("Jan", "Kowalski", 100)
        e.register_time(10)
        e.give.bonus(AmountBonus(1000))
        assert e.pay_salary() == 2200
        assert e.pay_salary() ==0





