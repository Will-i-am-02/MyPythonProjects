"""
File: quadratic_solver.py
Name:William
-----------------------
This program should implement a console program
that asks 3 inputs (a, b, and c)
from users to compute the roots of equation:
ax^2 + bx + c = 0
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

import math


def main():
	"""
	In this program we can enter any 3 number to present (a,b,c)
	to find if "ax^2+bx+c=0" have root and root's value.
	"""
	print('stanCode Quadratic Solver!')
	a = int(input('Enter a: '))
	if a == 0:
		print("a can't be zero")
	else:
		b = int(input('Enter b: '))
		c = int(input('Enter c: '))
		judge = b*b-4*a*c
		if judge > 0:
			root1 = (-b+math.sqrt(judge))/(2*a)
			root2 = (-b-math.sqrt(judge))/(2*a)
			print('Two roots: '+str(root1)+", "+str(root2))
		elif judge == 0:
			root_only = (-b+math.sqrt(judge))/(2*a)
			print('One root: '+str(root_only))
		else:
			print('No real roots')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
