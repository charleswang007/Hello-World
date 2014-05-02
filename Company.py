#!/usr/bin/python
import Employee

class Company:
   'Common base class for all company'

   def __init__(self, name):
      self.name = name
      self.employee_count = 0
      self.employees = []
   
   def addEmployee(self, employee):
      self.employees.append(employee)
      self.employee_count += 1

   def removeEmployee(self, employee):
      self.employees.remove(employee)
      self.employee_count -= 1

   def getName(self):
      return self.name

   def getTotalNumOfEmployee(self):
      return self.employee_count

   def getTotalSalaryofEmployee(self):
      salary_total = 0
      for employee in self.employees:
         salary_total += employee.getSalary()
      return salary_total
