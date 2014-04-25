from Employee import Employee
import unittest
print "testing the Employee class!"

class BasicTest(unittest.TestCase):
    
    def test_total_employee_count(self):
        emp1 = Employee("Alice", 2000, 3)
        emp2 = Employee("Bob", 5000, 5)
        self.assertEqual(Employee.empCount, 4)

    def test_employee_rank(self):
        emp1 = Employee("Charlie", 3000, 3)
        emp2 = Employee("Deborah", 4000, 5)
        self.assertTrue(emp1.getRank() < emp2.getRank())

if __name__ == '__main__':
    unittest.main() 
