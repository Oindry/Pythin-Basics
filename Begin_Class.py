class Employee:
	empcount=0
	def __init__(self,name,salary):
		self.name= name
		self.salary=salary
		Employee.empcount+=1
	def displayCount(self):
		print("Total Employee %d" % Employee.empcount)
	def displayEmployee(self):
		print("Name: ",self.name,",salery:",self.salary)
emp1 = Employee ("Grag",5000)
emp2 = Employee ("Chris",7000)
emp3 = Employee()
emp3.name= "Oindry"
emp3.salary= 90000
emp3.displayEmployee()
emp1.displayEmployee()
emp2.displayEmployee()
	