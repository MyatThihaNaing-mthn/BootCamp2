class SchoolMember:
	'''Represents any school member.'''

	def __init__(self, name, age):
		self.name = name
		self.age = age
		print('(Initialized ShcoolMember: {})'.format(self.name))


	def tell(self):
		'''Tell my details.'''
		print('Name:"{}" Age:"{}" Marks:"{}"'.format(self.name, self.age, self.marks),end="")


class Teacher(SchoolMember):
	'''Represents a teacher.'''

	def __init__(self, name, age, marks):
		SchoolMember.__init__(self, name, age)
		self.marks = marks
		print('(Initialized Teacher:{})'.format(self.name))

	def tell(self):
		SchoolMember.tell(self)
		#print('Marks: "{:d}"'.format(self.marks))
		#print('Age: "{:d}"'.format(self.age))

	def say_hi(self):
		print('Age: {} and marks: {}'.format(self.age, self.marks))


# class Student(SchoolMember):
# 	'''Represents a Student'''

# 	def __init__(self, name, age, marks):
# 		SchoolMember.__init__(self, name, age)
# 		self.marks = marks
# 		print('Initialized Student:{}'.format(self.name))

# 	def tell(self):
# 		SchoolMember.tell(self)
# 		print('Marks: "{:d}"'.format(self.marks))	



t = Teacher('Mrs. Shrividya', 40, 30000)
t.tell()
t.say_hi()
# s = Student('Swaroop', 25, 75)


# print()


# members =[t,s]
# for member in members:
# 	member.tell()		