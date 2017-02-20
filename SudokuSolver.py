##Bingxu Ren
#Sudoku Solver
from subprocess import call
import os

class Sudoku:
	def __init__(self):
		self.grid = ''
		self.variables = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
		self.cnf = []  #list that used to contain cnf values

	def readFile(self, fileName):
		print 'Opening \'' + fileName + '\'...\n'
		f = open(fileName, 'r')
		self.grid = f.read()  ##save data from file to grid
		f.close()
		return self.grid

	def show(self, l, p):
		#pretty print
		grid = l
		#print grid
		output = ''
		accu = 1
		print p + '\n'
		for i in range(272):
			if accu == 17:
				accu = 0
			if accu % 4 == 0 and accu != 0:
				output = output + grid[i] + '    '
			elif grid[i] == '\n':
				output = output + grid[i]
			else:
				output = output + grid[i] + ' '
			if (i+1) % 68 == 0 and i != 271:
				output = output + '\n'
			accu = accu + 1
		print output

	def reduce(self):
		print 'reducing puzzle...\n'
		#r represents row, c represents column, v means the value of the variable
		#define individual cells
		#this loop writes boolean variables to make sure each cell contains exactly one value in 0 to f
		for r in range(1, 17):
			for c in range(1, 17):
				for v in range(0, 16):
					self.cnf.append(17*17*r+17*c+v)
					if v == 15:
						self.cnf.append(0)
		#make sure each cell contains a value (cannot be empty)
		for r in range(1, 17):
			for c in range(1, 17):
				for v1 in range(0, 16):
					for v2 in range(0, 16):
						if v1 != v2:
							self.cnf.append(-(17*17*r+17*c+v1))
							self.cnf.append(-(17*17*r+17*c+v2))
							self.cnf.append(0)
		#define rows
		#make sure each value exists in each row
		for v in range(0, 16):
			for r in range(1, 17):
				for c in range(1, 17):
					self.cnf.append(17*17*r+17*c+v)
					if c ==16:
						self.cnf.append(0)
		#make sure each row contains a unique value
		for v in range(0, 16):
			for r in range(1, 17):
				for c1 in range(1, 17):
					for c2 in range(1, 17):
						if c1 != c2:
							self.cnf.append(-(17*17*r+17*c1+v))
							self.cnf.append(-(17*17*r+17*c2+v))
							self.cnf.append(0)
		#define columns
		#make sure each value exists in each column
		for v in range(0, 16):
			for c in range(1, 17):
				for r in range(1, 17):
					self.cnf.append(17*17*r+17*c+v)
					if r == 16:
						self.cnf.append(0)
		#make sure each column contains a unique value
		for v in range(0, 16):
			for c in range(1, 17):
				for r1 in range(1, 17):
					for r2 in range(1, 17):
						if r1 != r2:
							self.cnf.append(-(17*17*r1+17*c+v))
							self.cnf.append(-(17*17*r2+17*c+v))
							self.cnf.append(0)
		#define blocks
		#br is the row of the block, bc is the column of the block
		#there are 4 rows and 4 columns of blocks
		#make sure each value exists in each block
		for v in range(0, 16):
			for r in range(1, 5):
				for c in range(1, 5):
					self.cnf.append(17*17*r+17*c+v)
			self.cnf.append(0)
		#print self.cnf
		for v in range(0, 16):
			for r in range(1, 5):
				for c in range(5, 9):
					self.cnf.append(17*17*r+17*c+v)
			self.cnf.append(0)
		for v in range(0, 16):
			for r in range(1, 5):
				for c in range(9, 13):
					self.cnf.append(17*17*r+17*c+v)
			self.cnf.append(0)
		for v in range(0, 16):
			for r in range(1, 5):
				for c in range(13, 17):
					self.cnf.append(17*17*r+17*c+v)
			self.cnf.append(0)
		for v in range(0, 16):
			for r in range(5, 9):
				for c in range(1, 5):
					self.cnf.append(17*17*r+17*c+v)
			self.cnf.append(0)
		for v in range(0, 16):
			for r in range(5, 9):
				for c in range(5, 9):
					self.cnf.append(17*17*r+17*c+v)
			self.cnf.append(0)
		for v in range(0, 16):
			for r in range(5, 9):
				for c in range(9, 13):
					self.cnf.append(17*17*r+17*c+v)
			self.cnf.append(0)
		for v in range(0, 16):
			for r in range(5, 9):
				for c in range(13, 17):
					self.cnf.append(17*17*r+17*c+v)
			self.cnf.append(0)
		for v in range(0, 16):
			for r in range(9, 13):
				for c in range(1, 5):
					self.cnf.append(17*17*r+17*c+v)
			self.cnf.append(0)
		for v in range(0, 16):
			for r in range(9, 13):
				for c in range(5, 9):
					self.cnf.append(17*17*r+17*c+v)
			self.cnf.append(0)
		for v in range(0, 16):
			for r in range(9, 13):
				for c in range(9, 13):
					self.cnf.append(17*17*r+17*c+v)
			self.cnf.append(0)
		for v in range(0, 16):
			for r in range(9, 13):
				for c in range(13, 17):
					self.cnf.append(17*17*r+17*c+v)
			self.cnf.append(0)
		for v in range(0, 16):
			for r in range(13, 17):
				for c in range(1, 5):
					self.cnf.append(17*17*r+17*c+v)
			self.cnf.append(0)
		for v in range(0, 16):
			for r in range(13, 17):
				for c in range(5, 9):
					self.cnf.append(17*17*r+17*c+v)
			self.cnf.append(0)
		for v in range(0, 16):
			for r in range(13, 17):
				for c in range(9, 13):
					self.cnf.append(17*17*r+17*c+v)
			self.cnf.append(0)
		for v in range(0, 16):
			for r in range(13, 17):
				for c in range(13, 17):
					self.cnf.append(17*17*r+17*c+v)
			self.cnf.append(0)
		
		#add puzzle to cnf
		#convert grid to a list
		gridList = list(self.grid)

		for i in range(272):
			if gridList[i] in self.variables:
				'''test
				print 'row ' + str((i+1)/17 + 1)
				print 'column ' + str((i+1)%17)
				print gridList[i]
				print 'index ' + str(self.variables.index(gridList[i]))
				print 'value ' + str(((i+1)/17+1)*17*17 + ((i+1)%17)*17 + self.variables.index(gridList[i]))
				'''
				self.cnf.append(((i+1)/17+1)*17*17 + ((i+1)%17)*17 + self.variables.index(gridList[i]))
				self.cnf.append(0)
				#print self.cnf
		return self.cnf

	def sat(self, cnfl):
			cnf = cnfl

			#convert cnf list to sat format
			sat = ' '.join(str(e) for e in cnf)
			sat = 'p cnf 4911 ' + str(sat.count(' 0')) + '\n' + sat

			#write cnf to a file
			out = open('sudoku.txt', 'w')
			out.write(sat)
			out.close()

			#use minisat, and writes result to a file
			#it uses os module to redirect minisat output to /dev/null, so it doesnt show on my screen
			####I googled this subprocess method!!!###
			####source see here: http://stackoverflow.com/questions/11269575/how-to-hide-output-of-subprocess-in-python-2-7
			call(['minisat', 'sudoku.txt', 'result.txt'], stdout = open(os.devnull, 'w'))

	def showResult(self):
		#display result
		result = open('result.txt', 'r')
		result_list = result.read().split()
		result.close()
		if result_list[0] == 'UNSAT':
			print 'Sorry, no solution!'
		else:
			#print current solution
			print 'solution found!\n'
			solution_list = list(self.grid)
			temp_r = 0  #temporary row and column value to map result back into the grid
			temp_c = 0
			temp_v = 0
			int_result = 0
			for n in range(306, 4913):
				int_result = int(result_list[n])
				if int_result > 0:
					temp_r = int_result / 289
					temp_c = (int_result - temp_r * 289) / 17
					temp_v = int_result - temp_r * 289 - temp_c * 17
					solution_list[(temp_r-1)*17+(temp_c-1)] = self.variables[temp_v]
			self.show(solution_list, 'solution:')

			#check uniqueness by adding the negation of the solution to clauses
			#if new file is SAT, then there is another solution
			#else solution is unique
			result_list.remove('SAT')
			for element in result_list:
				self.cnf.append(-int(element))
			self.sat(self.cnf)

			result = open('result.txt', 'r')
			result_list1 = result.read().split()
			solution_list1 = list(self.grid)
			temp_r = 0  #temporary row and column value to map result back into the grid
			temp_c = 0
			temp_v = 0
			int_result = 0
			for n in range(306, 4912):
				int_result = int(result_list1[n])
				if int_result > 0:
					temp_r = int_result / 289
					temp_c = (int_result - temp_r * 289) / 17
					temp_v = int_result - temp_r * 289 - temp_c * 17
					solution_list1[(temp_r-1)*17+(temp_c-1)] = self.variables[temp_v]
			if result_list1[0] == 'UNSAT' or solution_list == solution_list1:
				print 'solution is unique!'
			else:
				self.show(solution_list, 'there is another solution:')

		result.close()

def main():
	#perform reduction
	s = Sudoku()
	l = s.readFile('./SudokuPuzzles/prob_3.inp')
	s.show(list(l), 'puzzle: ')
	s.sat(s.reduce())
	s.showResult()
	
main()





