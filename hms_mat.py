"""
Class Matrix is used to store and manipulate matrices. Matrices are stored as an array of arrays with traditional row and column
definitions respected. For example a 1 dimensional array will always be a matrix with a single row.

supported arrays are like:
[1]
[1,2,3,...]
[[1,2,3,...],[1,2,3,...],...]

These values can be used in the constructor and the set command

To get matrix values the class supports:
get
getItem
print(Matrix)

Current operations supported are:
*
"""

import copy
from numbers import Number

class Matrix:
	
	
	######################################################################################
	# Object initialization
	# @param val {Matrix or [[]]} - the initial value of the matrix
	def __init__(self,val=None):
		self.typeErrorMessage = "Value must be a an array or an array of arrays of numbers and rows must be of equal length"
		self.matrix = []
		self.rows = 0
		self.cols = 0
		if not val is None:
			self.set(val)
		
	######################################################################################
	# @returns - string reprsentation of its matrix
	def __str__(self):
		strMatrix = ""
		for item in self.matrix:
			if strMatrix != "" :
				strMatrix += "\n"
			strMatrix += str(item)
		return strMatrix
			
	######################################################################################
	# Tests if an object is a list of numbers
	#
	# @param items - object to test
	def _isListOfNumbers(self,items):
		if not isinstance(items,list):
			return False
		for item in items:
			if not isinstance(item,Number):
				return False
		return True
				
	
	######################################################################################
	# Sets the value of the matrix
	# @param val - An array or an array of arrays of numbers
	#
	# supported arrays are like:
	# [1]
	# [1,2,3,...]
	# [[1,2,3,...],[1,2,3,...],...]
	def set(self,val):
		
		# if val is matrix
		if isinstance(val,Matrix):
			self.matrix = val.get()
			self.rows = val.getRows()
			self.cols = val.getCols()
			return
		
		if not isinstance(val,list):
			raise TypeError(self.typeErrorMessage)
		
		if len(val) == 0:
			self.matrix = [[]]
			self.rows = 0
			self.cols = 0
			return
		
		if self._isListOfNumbers(val):
			self.matrix = [copy.deepcopy(val)]
			self.rows = 1
			self.cols = len(val)
			return
			
		rows = 0
		cols = len(val[0])
		for item in val:
			rows += 1
			if not self._isListOfNumbers(item) or len(item) != cols:
				raise TypeError(self.typeErrorMessage)
				
		self.matrix = copy.deepcopy(val)
		self.rows = rows
		self.cols = cols
	
	######################################################################################
	# Returns a copy of the underlying array
	def get(self):
		return copy.deepcopy(self.matrix)
		
	######################################################################################
	# Gets an item in the matris
	#
	# @param row - integer representing the row to be accessed
	# @para col - integer representing the col to be accessed
	def getItem(self,row,col):
		return self.matrix[row][col]
		
	######################################################################################
	# Returns the number of rows in the matrix
	def getRows(self):
		return self.rows

	######################################################################################
	# Returns the number of columns in the matrix
	def getCols(self):
		return self.cols

	######################################################################################
	# multiplies two matrices and returns the result matrix
	# @param other {Matrix} - the matrix to muliply with self
	def __mul__(self,other):
		if not isinstance(other,Matrix):
			raise TypeError("You can only multiple this Matrix with another Matrix")
		if self.getCols() != other.getRows():
			raise TypeError("The number of rows for the given matrix must be equal to the number of columns of the current matrix")
		
		result = []
		for r1 in range(0,self.rows):
			result.append([])
			for c2 in range(0,other.getCols()):
				sum = 0
				for c1 in range(0,self.cols):
					sum += self.getItem(r1,c1) * other.getItem(c1,c2)
				result[r1].append(sum)
				
		return Matrix(result)
		