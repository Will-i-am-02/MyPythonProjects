"""
File: prime_checker.py
Name:William
-----------------------
This program asks our user for input and checks if the input is a
prime number or not. First, ” Welcome to the prime checker” will be printed on Console.
And the program will continually ask the user to enter an integer 
that is greater than 1 and checks if it is a prime number.
The program ends when the user enter the EXIT number.
"""
EXIT = -100


def main():
	"""
	This program will continually identify if the number(>1) user enter is a prime number.
	The prime number has only two divisors, "1" and "itself".
	"""
	print('Welcome to the prime checker!')
	num = int(input('n: '))
	if num == EXIT:
		print('Have a good one!')
	else:
		while not num == EXIT:
			if num > 2:
				data = 0  # ---------> To count how many divisors the number has.
				for i in range(num):
					if i == 0:  # ---------> I set this condition because the dividend can't be 0.
						i = i+1
					if num % i == 0:  # ---------> Divisible, means i is one of the number's divisors.
						data += 1
				if data == 2:  # ---------> Only have two divisors, "1" and "the number user entered".
					print(str(num)+' is a prime number.')
					num = int(input('n: '))
				else:
					print(str(num)+' is not a prime number.')
					num = int(input('n: '))
			elif num == 2:  # ---------> "2" have only two divisors, "1" and "2".
				print(str(num)+' is a prime number.')
				num = int(input('n: '))
		print('Have a good one!')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
