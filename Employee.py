#!/usr/bin/python

class Employee:
   'Common base class for all employees'
   empCount = 0
   title_extension = {'Software Engineer':'001', 'Program Manager':'002', 'CEO':'003', 'CFO':'004', 'CTO':'005', 'Secretary':'006'}

   def __init__(self, name, title, salary, rank):
      self.name = name
      self.title = title
      self.salary = salary
      self.rank = rank
      Employee.empCount += 1
   
   def displayCount(self):
      print "Total Employee %d" % Employee.empCount

   def displayEmployee(self):
      print "Name : ", self.name,  ", Salary: ", self.salary

   def getRank(self):
      return self.rank

   def getTitle(self):
      return self.title

   def getExtension(self):
      return Employee.title_extension[self.title]
