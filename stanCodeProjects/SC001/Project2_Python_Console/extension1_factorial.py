"""
File: extension1_factorial.py
Name: William
-------------------
This program will continually ask our user to give a number
and will calculate the factorial result of the number and print it on the console.

The program ends when the user enter the EXIT number.
"""
EXIT = -100


def main():
	"""
	This program will continually ask our user to give a number
	and will calculate the factorial result of the number and print it on the console.

	The program ends when the user enter the EXIT number.
	"""
	print('Welcome to stanCode factorial master!')
	num = int(input('Give me a number, and I will list the answer of factorial: '))
	if num == EXIT:
		print('- - - - - - See ya! - - - - - -')
	else:
		while not num == EXIT:
			data = 1  # --------->To do the factorial, the multiplier must start with 1.
			for i in range(num+1):  # ----------> I use "num+1" is because that when "i = num" will leave the loop.
				if i == 0:
					continue
				data = data * i
			print('Answer: '+str(data))
			num = int(input('Give me a number, and I will list the answer of factorial: '))
		print('- - - - - - See ya! - - - - - -')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
	main()