"""
File: largest_digit.py
Name:William
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n: int, a number given by user to find this number's largest digit.
	:return: int, the largest digit(not initial largest digit I definite).
	"""
	largest_digit = -float('inf')							# initial largest digit
	return find_largest_digit_helper(n, largest_digit)


def find_largest_digit_helper(n, largest_digit):
	"""
	This function add additional param to help me use recursion to find largest digit in 'n'.
	:param n: int, a number given by function called find_largest_digit(n).
	:param largest_digit: int, use to continually store new largest digit.
	:return largest_digit: int, when this help function goes to base case will return final largest digit.
	"""
	if n == 0:
		return largest_digit
	elif n <= 0:
		n = -n
		return find_largest_digit_helper(n, largest_digit)
	else:
		if n % 10 > largest_digit:
			largest_digit = n % 10
		return find_largest_digit_helper(n//10, largest_digit)


if __name__ == '__main__':
	main()
