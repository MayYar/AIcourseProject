import numpy as np
import sys
import random

A = list()

def printResult():
	#see the result
	for i in range(len(A)):
		for j in range(len(A)):
			if A[i][j] != 0:
				print(A[i][j], end=" ")
		print()

def main():
	# print (sys.argv[1])
	with open(sys.argv[1], 'r') as f:
		size = int(f.readline())
		# A = [[0] * (size + 2)] * (size + 2)
		
		for i in range(size+2):
			c = []
			for j in range(size+2):
				c.append(0)
			A.append(c)
		# print(d)

		temp = list()
		for line in f:
			data = list()
			for alphabet in line.split(" "):
				data.append(alphabet[0])
			temp.append(data)
		# print(temp)

		for i in range(len(temp)):
			for j in range(len(temp)):
				# print(temp[i][j])
				A[i+1][j+1] = temp[i][j]

		print(A)
		printResult()
	firstorNot = input("User go first or not(Y/N):")
	if firstorNot == 'Y':
		color = input("Enter your color(B/R): ")

		if color == 'B':
			AIcolor = 'R'
		else:
			AIcolor = 'B'

		while 1:
			if color not in (j for i in A for j in i):
				print("User Win")
				break
			elif AIcolor not in (j for i in A for j in i):
				print("AI Win")
				break
			row = input("Enter a row: ")
			col = input("Enter a col: ")

			while A[int(row)][int(col)] != color:
				print("Wrong position... try again")
				row = input("Enter a row: ")
				col = input("Enter a col: ")
				
			A[int(row)][int(col)] = 'X'
			printResult()

			# if A == [['X'] * size] * size:
			# 	winner = "User"
			# 	break
			#上：檢查左右上 A[int(row)-1][int(col)]
			ncount = 0
			if A[int(row)-1][int(col)] == 0 or A[int(row)-1][int(col)] == 'X':
				pass
			else:
				ncount = 0
				if A[int(row)-1][int(col)-1] != 'X':
					ncount += 1
				if A[int(row)-1][int(col)+1] != 'X':
					ncount += 1
				if A[int(row)-2][int(col)] != 'X':
					ncount += 1	
				if ncount < 3:
					print("Side Effect on: [", int(row)-1, "][", int(col),"]")
					A[int(row)-1][int(col)] = 'X'

			# #下：檢查左右下 A[int(row)+1][int(col)]
			if A[int(row)+1][int(col)] == 0 or A[int(row)+1][int(col)] == 'X':
				pass
			else:
				ncount = 0
				if A[int(row)+1][int(col)-1] != 'X':
					ncount += 1
				if A[int(row)+1][int(col)+1] != 'X':
					ncount += 1
				if A[int(row)+2][int(col)] != 'X':
					ncount += 1	
				if ncount < 3:
					print("Side Effect on: [", int(row)+1, "][", int(col),"]")
					A[int(row)+1][int(col)] = 'X'

			# #左：檢查左上下 A[int(row)][int(col)-1]
			if A[int(row)][int(col)-1] == 0 or A[int(row)][int(col)-1] == 'X':
				pass
			else:
				ncount = 0
				if A[int(row)][int(col)-2] != 'X':
					ncount += 1
				if A[int(row)-1][int(col)-1] != 'X':
					ncount += 1
				if A[int(row)+1][int(col)-1] != 'X':
					ncount += 1	
				if ncount < 3:
					print("Side Effect on: [", int(row), "][", int(col)-1,"]")
					A[int(row)][int(col)-1] = 'X'

			# #右：檢查右上下 A[int(row)][int(col)+1]
			if A[int(row)][int(col)+1] == 0 or A[int(row)][int(col)+1] == 'X':
				pass
			else:
				ncount = 0
				if A[int(row)][int(col)+2] != 'X':
					ncount += 1
				if A[int(row)-1][int(col)+1] != 'X':
					ncount += 1
				if A[int(row)+1][int(col)+1] != 'X':
					ncount += 1	
				if ncount < 3:
					print("Side Effect on: [", int(row), "][", int(col)+1,"]")
					A[int(row)][int(col)+1] = 'X'
			
			printResult()

			if color not in (j for i in A for j in i):
				print("User Win")
				break
			elif AIcolor not in (j for i in A for j in i):
				print("AI Win")
				break

			AIrow = random.randint(1,size)
			AIcol = random.randint(1,size)
			
			while(A[int(AIrow)][int(AIcol)] == 'X' or A[int(AIrow)][int(AIcol)] == color):
				AIrow = random.randint(1,size)
				AIcol = random.randint(1,size)

			print("AI Enter a row: " , AIrow)
			print("AI Enter a col: " , AIcol)

			A[int(AIrow)][int(AIcol)] = 'X'

			if A[int(AIrow)-1][int(AIcol)] == 0 or A[int(AIrow)-1][int(AIcol)] == 'X':
				pass
			else:
				ncount = 0
				if A[int(AIrow)-1][int(AIcol)-1] != 'X':
					ncount += 1
				if A[int(AIrow)-1][int(AIcol)+1] != 'X':
					ncount += 1
				if A[int(AIrow)-2][int(AIcol)] != 'X':
					ncount += 1	
				if ncount < 3:
					print("Side Effect on: [", int(AIrow)-1, "][", int(AIcol),"]")
					A[int(AIrow)-1][int(AIcol)] = 'X'

			# #下：檢查左右下 A[int(AIrow)+1][int(AIcol)]
			if A[int(AIrow)+1][int(AIcol)] == 0 or A[int(AIrow)+1][int(AIcol)] == 'X':
				pass
			else:
				ncount = 0
				if A[int(AIrow)+1][int(AIcol)-1] != 'X':
					ncount += 1
				if A[int(AIrow)+1][int(AIcol)+1] != 'X':
					ncount += 1
				if A[int(AIrow)+2][int(AIcol)] != 'X':
					ncount += 1	
				if ncount < 3:
					print("Side Effect on: [", int(AIrow)+1, "][", int(AIcol),"]")
					A[int(AIrow)+1][int(AIcol)] = 'X'

			# #左：檢查左上下 A[int(AIrow)][int(AIcol)-1]
			if A[int(AIrow)][int(AIcol)-1] == 0 or A[int(AIrow)][int(AIcol)-1] == 'X':
				pass
			else:
				ncount = 0
				if A[int(AIrow)][int(AIcol)-2] != 'X':
					ncount += 1
				if A[int(AIrow)-1][int(AIcol)-1] != 'X':
					ncount += 1
				if A[int(AIrow)+1][int(AIcol)-1] != 'X':
					ncount += 1	
				if ncount < 3:
					print("Side Effect on: [", int(AIrow), "][", int(AIcol)-1,"]")
					A[int(AIrow)][int(AIcol)-1] = 'X'

			# #右：檢查右上下 A[int(AIrow)][int(AIcol)+1]
			if A[int(AIrow)][int(AIcol)+1] == 0 or A[int(AIrow)][int(AIcol)+1] == 'X':
				pass
			else:
				ncount = 0
				if A[int(AIrow)][int(AIcol)+2] != 'X':
					ncount += 1
				if A[int(AIrow)-1][int(AIcol)+1] != 'X':
					ncount += 1
				if A[int(AIrow)+1][int(AIcol)+1] != 'X':
					ncount += 1	
				if ncount < 3:
					print("Side Effect on: [", int(AIrow), "][", int(AIcol)+1,"]")
					A[int(AIrow)][int(AIcol)+1] = 'X'

			printResult()

			if color not in (j for i in A for j in i):
				print("User Win")
				break
			elif AIcolor not in (j for i in A for j in i):
				print("AI Win")
				break

			# if A == [['X'] * size] * size:
			# 	winner = "AI"
			# 	break





	elif firstorNot == 'N':

		color = input("Enter your color(B/R): ")

		if color == 'B':
			AIcolor = 'R'
		else:
			AIcolor = 'B'

		while 1:
			if color not in (j for i in A for j in i):
				print("User Win")
				break
			elif AIcolor not in (j for i in A for j in i):
				print("AI Win")
				break
			AIrow = random.randint(1,size)
			AIcol = random.randint(1,size)
			
			while(A[int(AIrow)][int(AIcol)] == 'X' or A[int(AIrow)][int(AIcol)] == color):
				AIrow = random.randint(1,size)
				AIcol = random.randint(1,size)

			print("AI Enter a row: " , AIrow)
			print("AI Enter a col: " , AIcol)

			A[int(AIrow)][int(AIcol)] = 'X'

			if A[int(AIrow)-1][int(AIcol)] == 0 or A[int(AIrow)-1][int(AIcol)] == 'X':
				pass
			else:
				ncount = 0
				if A[int(AIrow)-1][int(AIcol)-1] != 'X':
					ncount += 1
				if A[int(AIrow)-1][int(AIcol)+1] != 'X':
					ncount += 1
				if A[int(AIrow)-2][int(AIcol)] != 'X':
					ncount += 1	
				if ncount < 3:
					print("Side Effect on: [", int(AIrow)-1, "][", int(AIcol),"]")
					A[int(AIrow)-1][int(AIcol)] = 'X'

			# #下：檢查左右下 A[int(AIrow)+1][int(AIcol)]
			if A[int(AIrow)+1][int(AIcol)] == 0 or A[int(AIrow)+1][int(AIcol)] == 'X':
				pass
			else:
				ncount = 0
				if A[int(AIrow)+1][int(AIcol)-1] != 'X':
					ncount += 1
				if A[int(AIrow)+1][int(AIcol)+1] != 'X':
					ncount += 1
				if A[int(AIrow)+2][int(AIcol)] != 'X':
					ncount += 1	
				if ncount < 3:
					print("Side Effect on: [", int(AIrow)+1, "][", int(AIcol),"]")
					A[int(AIrow)+1][int(AIcol)] = 'X'

			# #左：檢查左上下 A[int(AIrow)][int(AIcol)-1]
			if A[int(AIrow)][int(AIcol)-1] == 0 or A[int(AIrow)][int(AIcol)-1] == 'X':
				pass
			else:
				ncount = 0
				if A[int(AIrow)][int(AIcol)-2] != 'X':
					ncount += 1
				if A[int(AIrow)-1][int(AIcol)-1] != 'X':
					ncount += 1
				if A[int(AIrow)+1][int(AIcol)-1] != 'X':
					ncount += 1	
				if ncount < 3:
					print("Side Effect on: [", int(AIrow), "][", int(AIcol)-1,"]")
					A[int(AIrow)][int(AIcol)-1] = 'X'

			# #右：檢查右上下 A[int(AIrow)][int(AIcol)+1]
			if A[int(AIrow)][int(AIcol)+1] == 0 or A[int(AIrow)][int(AIcol)+1] == 'X':
				pass
			else:
				ncount = 0
				if A[int(AIrow)][int(AIcol)+2] != 'X':
					ncount += 1
				if A[int(AIrow)-1][int(AIcol)+1] != 'X':
					ncount += 1
				if A[int(AIrow)+1][int(AIcol)+1] != 'X':
					ncount += 1	
				if ncount < 3:
					print("Side Effect on: [", int(AIrow), "][", int(AIcol)+1,"]")
					A[int(AIrow)][int(AIcol)+1] = 'X'

			printResult()

			if color not in (j for i in A for j in i):
				print("User Win")
				break
			elif AIcolor not in (j for i in A for j in i):
				print("AI Win")
				break

			row = input("Enter a row: ")
			col = input("Enter a col: ")

			while A[int(row)][int(col)] != color:
				print("Wrong position... try again")
				row = input("Enter a row: ")
				col = input("Enter a col: ")
				
			A[int(row)][int(col)] = 'X'
			printResult()

			# if A == [['X'] * size] * size:
			# 	winner = "User"
			# 	break
			#上：檢查左右上 A[int(row)-1][int(col)]
			ncount = 0
			if A[int(row)-1][int(col)] == 0 or A[int(row)-1][int(col)] == 'X':
				pass
			else:
				ncount = 0
				if A[int(row)-1][int(col)-1] != 'X':
					ncount += 1
				if A[int(row)-1][int(col)+1] != 'X':
					ncount += 1
				if A[int(row)-2][int(col)] != 'X':
					ncount += 1	
				if ncount < 3:
					print("Side Effect on: [", int(row)-1, "][", int(col),"]")
					A[int(row)-1][int(col)] = 'X'

			# #下：檢查左右下 A[int(row)+1][int(col)]
			if A[int(row)+1][int(col)] == 0 or A[int(row)+1][int(col)] == 'X':
				pass
			else:
				ncount = 0
				if A[int(row)+1][int(col)-1] != 'X':
					ncount += 1
				if A[int(row)+1][int(col)+1] != 'X':
					ncount += 1
				if A[int(row)+2][int(col)] != 'X':
					ncount += 1	
				if ncount < 3:
					print("Side Effect on: [", int(row)+1, "][", int(col),"]")
					A[int(row)+1][int(col)] = 'X'

			# #左：檢查左上下 A[int(row)][int(col)-1]
			if A[int(row)][int(col)-1] == 0 or A[int(row)][int(col)-1] == 'X':
				pass
			else:
				ncount = 0
				if A[int(row)][int(col)-2] != 'X':
					ncount += 1
				if A[int(row)-1][int(col)-1] != 'X':
					ncount += 1
				if A[int(row)+1][int(col)-1] != 'X':
					ncount += 1	
				if ncount < 3:
					print("Side Effect on: [", int(row), "][", int(col)-1,"]")
					A[int(row)][int(col)-1] = 'X'

			# #右：檢查右上下 A[int(row)][int(col)+1]
			if A[int(row)][int(col)+1] == 0 or A[int(row)][int(col)+1] == 'X':
				pass
			else:
				ncount = 0
				if A[int(row)][int(col)+2] != 'X':
					ncount += 1
				if A[int(row)-1][int(col)+1] != 'X':
					ncount += 1
				if A[int(row)+1][int(col)+1] != 'X':
					ncount += 1	
				if ncount < 3:
					print("Side Effect on: [", int(row), "][", int(col)+1,"]")
					A[int(row)][int(col)+1] = 'X'
			
			printResult()

			if color not in (j for i in A for j in i):
				print("User Win")
				break
			elif AIcolor not in (j for i in A for j in i):
				print("AI Win")
				break
	else:
		pass


if __name__ == "__main__":
	main()