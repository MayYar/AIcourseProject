import numpy as np
import sys

def main():
	# print (sys.argv[1])
	A = list()
	with open(sys.argv[1], 'r') as f:
		next(f)	#跳過第一行:size
		# data = f.read()
		# print(data)
		for line in f:
			data = list()
			for alphabet in line.split(" "):
				data.append(alphabet[0])
			A.append(data)

	firstorNot = input("User go first or not(Y/N):")
	if firstorNot == 'Y':
		color = input("Enter your color(B/R): ")
		row = input("Enter a row: ")
		col = input("Enter a col: ")
		A[int(row)-1][int(col)-1] = 'X'
	else:
		pass


	#see the result
	for i in A:
		for j in i:
			print(j, end=" ")
		print()


if __name__ == "__main__":
	main()