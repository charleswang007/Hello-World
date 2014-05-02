#!/usr/bin/python
import Employee

class Company:
   'Common base class for all company'
   employee_count = 0
   employees = []

   def __init__(self, name):
      self.name = name
   
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
