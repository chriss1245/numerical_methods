import numpy as np
class aux(type): # Axiliar class for making str(type(Polynomial)) = 'Polynomial'
	def __repr__(self):
		return self.__name__
	

class Polynomial(metaclass = aux):
	def __init__(self, *coefficients):
		self.__degree = len(coefficients)-1
		self.__coefficients = np.array(coefficients).astype(float)
		self.__letter = 'x'

	def __getitem__(self, i):
		return self.__coefficients[i]

	def __setitem__(self, value, i):
		self.__coefficients[i] = value

	def __iter__(self):
		return iter(self.__coefficients)

	def __gt__(self,q):
		return self.__degree > q.__degree
	
	def __lt__(self,q):
		return not self > q
	
	def __eq__(self,q):
		return self.__degree == q.__degree

	def __repr__(self):
		return 'Polynomial: ' + str(self.__coefficients)

	def __str__(self):	
		def getCoefficient(self,i):
			sign = ''
			coefficient = ''
			letter = ''
			degree = ''
			string = ''

			# Nothing is printed if a given coefficient is 0
			if self.__coefficients[i] != 0.0:
				coefficient = str(np.round(self.__coefficients[i],3))
				if self.__coefficients[i] > 0.0:
					sign = '+'
				if self.__coefficients[i] < 0.0:
					sign = '-'
					coefficient = coefficient[1:]
				# Fill in string according to previous values			
				if i != self.__degree:
					string += sign + ' '
				elif sign == '-':
					string += sign
				string += coefficient
				if i != 0:
					string += self.__letter
				if i > 1:
					string += '^' + str(i)
				if i > 0:
					string += ' '
			return string
			
		s  = ''
		for i in range(self.degree,-1,-1):
			s += getCoefficient(self, i)
		return s + ' (Rounded)'

	def __add__(self, q):
		if str(type(q)) == 'Polynomial':
			if self.__degree >= q.__degree:
				coefficients = np.zeros_like(self.__coefficients)
				for i in range(len(self)):
					if i > q.__degree:
						coefficients[i] = self[i]
					else:
						coefficients[i] = self[i] + q[i]
			else:
				coefficients = np.zeros_like(q.__coefficients)
				for i in range(len(q)):
					if i > self.__degree:
						coefficients[i] = q[i]
					else:
						coefficients[i] = self[i] + q[i]
			return Polynomial(*coefficients)

		print('Warning: non-polynomial addition is yet not defined')
		return None

	def __sub__(self,q):
		return self+q.changeSign()
	
	def __mul__(self,q):
		if type(self) == type(q):
			coefficients = [0 for _ in range(len(self)+q.degree)]

			for i in range(len(self)):
				for j in range(q.degree+1):
					coefficients[i+j] += self[i]*q[j]
			return Polynomial(*coefficients)
		
		elif type(q) in (type(0), type(1.1)):
			for i in range(self.degree+1):
				self.__coefficients[i] = self.__coefficients[i]*q
			
			return self
		
		else:
			print('Not supported {} type'.format(type(q)))

	def __pow__(self,power):
		p = self
		while power > 0:
			p = p*self
			power -= 1
		return p

	def __call__(self,x_0):
		y = 0
		for i in range(len(self)):
			y += self[i]*x_0**i
		return y

	def __len__(self):
		return len(self.__coefficients)

	def changeSign(self):
		for i in range(self.degree):
			self.__coefficients[i] = -self.__coefficients[i]
	
	@property
	def degree(self): return self.__degree
