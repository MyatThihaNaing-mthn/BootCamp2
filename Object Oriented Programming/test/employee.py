class CompanyMember:
	"""Represents any company member"""
	def __init__(self, name, age, position):
		self.name = name
		self.age = age
		self.position = position
		print("A CompanyMember {} is created".format(self.name))

	def tell_detail(self):
		"""telling details"""
		print('My name is "{}" I am "{}" years old my position is "{}"'.format(self.name, self.age, self.position), end ="")



class Chairman(CompanyMember):
	"""represent a CEO"""
	def _init__(self, name, age, position):
		CompanyMember.__init__(self, name, age, position)
		print('A Chairman "{}"has been created'.format(self.name))

	def tell_detail(self):
		"""telling chairman's detail"""
		CompanyMember.tell_detail(self)



class Manager(CompanyMember):
	"""represent manager"""
	def __init__(self, name, age, position, salary, workdays):
		CompanyMember.__init__(self, name, age, position)
		self.salary = salary
		self.workdays = workdays
		print('A manager "{}" has been created'.format(self.name))

	def tell_detail(self):
		CompanyMember.tell_detail(self)
		print('I got "{}" and I have to work for"{}"'.format(self.salary, self.workdays), end="")



class staff(CompanyMember):
	"""represent staff"""
	def __init__(self, name, age, position, salary, workdays):
		CompanyMember.__init__(self, name, age, position)
		self.salary = salary
		self.workdays = workdays
		print('A staff "{}" has been created'.format(self.name))

	def tell_detail(self):
		CompanyMember.tell_detail(self)
		print('I got "{}" and I have to work for"{}"'.format(self.name, self.age, self.position, self.salary, self.workdays), end="")
		
owner = Chairman("Steven", 40, "chairman")
manager1 = Manager("Dave", 30, "sale manager", 800000, 25 )
staff1 = staff("Ryan", 23, "developer", 300000, 20)

owner.tell_detail()
manager1.tell_detail()
staff1.tell_detail()