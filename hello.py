from Employee import Employee
import unittest
print "testing the Employee class!"

class BasicTest(unittest.TestCase):
    def test_total_employee_count(self):
        emp1 = Employee("Alice", 2000)
        emp2 = Employee("Bob", 5000)
        self.assertEqual(Employee.empCount, 2)

if __name__ == '__main__':
    unittest.main() 
