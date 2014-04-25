#!/usr/bin/python

class Employee:
   'Common base class for all employees'
   empCount = 0

   def __init__(self, name, salary, rank):
      self.name = name
      self.salary = salary
      self.rank = rank
      Employee.empCount += 1
   
   def displayCount(self):
      print "Total Employee %d" % Employee.empCount

   def displayEmployee(self):
      print "Name : ", self.name,  ", Salary: ", self.salary

   def getRank(self):
      return self.rank
