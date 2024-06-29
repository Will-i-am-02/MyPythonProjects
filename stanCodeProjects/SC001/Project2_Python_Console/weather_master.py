"""
File: weather_master.py
Name:William
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""
QUIT = -100


def main():
	"""
	This program will show highest and lowest temperature,
	then count average temperature and how many cold days(<16)
	by temperatures user entered.
	"""
	print("stanCode \"Weather 4.0\"!")
	temperature = int(input('Next Temperature: (or '+str(QUIT)+' to quit)? '))
	if temperature == QUIT:
		print('No temperatures were entered.')
	else:
		highest = temperature  # To store highest temperature.
		lowest = temperature   # To store lowest temperature.
		cold = 0               # To count how many cold days.
		enter_times = 0        # To count how many times user enter a temperature.
		data = 0               # To store all temperatures user entered.
		while not temperature == QUIT:
			if temperature > highest:
				enter_times += 1
				data = data+temperature
				if temperature < 16:
					cold += 1
				highest = temperature
				temperature = int(input('Next Temperature: (or '+str(QUIT)+' to quit)? '))
			elif temperature < lowest:
				enter_times += 1
				data = data + temperature
				if temperature < 16:
					cold += 1
				lowest = temperature
				temperature = int(input('Next Temperature: (or '+str(QUIT)+' to quit)? '))
			else:
				enter_times += 1
				data = data + temperature
				if temperature < 16:
					cold += 1
				temperature = int(input('Next Temperature: (or '+str(QUIT)+' to quit)? '))
		average = data/enter_times
		"""
		This formula will count average temperature
		after user enter a number to break loop.
		"""
		print('Highest temperature = '+str(highest))
		print('Lowest temperature = '+str(lowest))
		print('Average = '+str(average))
		print(str(cold)+' cold day(s)')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
