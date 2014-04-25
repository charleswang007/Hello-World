from Employee import Employee
import unittest
print "testing the Employee class!"

class BasicTest(unittest.TestCase):
    
    def test_total_employee_count(self):
        emp1 = Employee("Alice", title = "Software Engineer", salary = 2000, rank = 5)
        emp2 = Employee("Bob", title = "Program Manager", salary = 5000, rank = 4)
        self.assertEqual(Employee.empCount, 6)

    def test_employee_rank(self):
        emp3 = Employee("Charlie", title = "CTO", salary = 3000, rank = 2)
        emp4 = Employee("Deborah", title = "CFO", salary = 4000, rank = 3)
        self.assertTrue(emp3.getRank() < emp4.getRank())

    def test_employee_title(self):
        emp5 = Employee("Ethan", title = "CEO", salary = 3000, rank = 1)
        emp6 = Employee("Frank", title = "Program Manager", salary = 4000, rank = 4)
        self.assertEqual(emp5.getTitle(), "CEO")


if __name__ == '__main__':
    unittest.main() 
