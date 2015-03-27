"""
Class Matrix is used to store and manipulate matrices. Matrices are stored as an array of arrays with traditional row and column
definitions respected. For example a 1 dimensional array will always be a matrix with a single row.
"""
import copy
from numbers import Number

class Matrix:
	
	
	######################################################################################
	# Object initialization
	def __init__(self):
		self.typeErrorMessage = "Value must be a an array or an array of arrays of numbers and rows must be of equal length"
		self.matrix = []
		self.mutli = False
		self.rows = 0
		self.cols = 0
		
	######################################################################################
	# @returns - string reprsentation of its matrix
	def __str__(self):
		if not self.multi:
			return str(self.matrix)
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
	# if val is array test to make sure elements are numbers
	# supported arrays are like:
	# [1]
	# [1,2,3,...]
	# [[1,2,3,...],[1,2,3,...],...]
	def set(self,val):
		
		# if val is matrix
		if isinstance(val,Matrix):
			self.multi = val.getIsMulti()
			self.matrix = val.get()
			self.rows = val.getRows()
			self.cols = val.getCols()
			return
		
		if not isinstance(val,list):
			raise TypeError(self.typeErrorMessage)
		
		if len(val) == 0:
			self.matrix = []
			self.multi = False
			self.rows = 0
			self.cols = 0
			return
		
		if self._isListOfNumbers(val):
			self.matrix = copy.deepcopy(val)
			self.multi = False
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
		self.multi = True
	
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
		if self.multi:
			return self.matrix[row][col]
		if row == 0:
			return self.matrix[col]
		
		return None
		
	######################################################################################
	# Returns true if matrix is multi dimensional
	def getIsMulti(self):
		return self.multi
		
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
		if self.cols != other.rows:
			raise TypeError("The number of rows for the given matrix must be equal to the number of columns of the current matrix")
		
		for r in range(0,rows):
			sum = 0
			for c in range(0,cols):
				sum += self.getItem(row,col) * other.getItem(col,row)
			
		
		result = Matrix()
		return result