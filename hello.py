from Employee import Employee
from Company import Company
import unittest
print "testing the Employee class!"

class BasicTest(unittest.TestCase):
    
    def test_employee_salary(self):
        emp1 = Employee("Alice", title = "Software Engineer", salary = 2000, rank = 5)
        emp2 = Employee("Bob", title = "Program Manager", salary = 5000, rank = 4)
        self.assertTrue(emp1.getSalary() < emp2.getSalary())

    def test_employee_rank(self):
        emp3 = Employee("Charlie", title = "CTO", salary = 3000, rank = 2)
        emp4 = Employee("Deborah", title = "CFO", salary = 4000, rank = 3)
        self.assertTrue(emp3.getRank() < emp4.getRank())

    def test_employee_title(self):
        emp5 = Employee("Ethan", title = "CEO", salary = 100000, rank = 1)
        emp6 = Employee("Frank", title = "Program Manager", salary = 5000, rank = 4)
        self.assertEqual(emp5.getTitle(), "CEO")

    def test_employee_extension(self):
        emp7 = Employee("Gilbery", title = "Secretary", salary = 1500, rank = 5)
        emp8 = Employee("Henry", title = "Program Manager", salary = 5000, rank = 4)
        self.assertTrue(not emp7.getTitle() is emp8.getTitle())

    def test_employee_extension(self):
        emp7 = Employee("Gilbery", title = "Secretary", salary = 1500, rank = 5)
        emp8 = Employee("Henry", title = "Program Manager", salary = 5000, rank = 4)
        self.assertTrue(not emp7.getTitle() is emp8.getTitle())

    def test_company_employee_count(self):
        company1 = Company("Apple")
        emp9 = Employee("Ian", title = "Program Manager", salary = 7000, rank = 4)
        company1.addEmployee(emp9)
        self.assertTrue(company1.getTotalNumOfEmployee() is 1)

    def test_company_employee_count2(self):
        company2 = Company("Apple2")
        emp10 = Employee("Jack", title = "Secretary", salary = 3000, rank = 3)
        emp11 = Employee("Kevin", title = "CTO", salary = 53000, rank = 2)
        company2.addEmployee(emp10)
        company2.addEmployee(emp11)
        self.assertTrue(company2.getTotalNumOfEmployee() is 2)


if __name__ == '__main__':
    unittest.main() 
