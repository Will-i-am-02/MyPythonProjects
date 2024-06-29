"""
File: class_reviews.py
Name:William
-------------------------------
At the beginning of this program, the user is asked to input
the class name (either SC001 or SC101).
Attention: your input should be case-insensitive.
If the user input "-1" for class name, your program would show
the maximum, minimum, and average among all the inputs.
"""
EXIT = '-1'


def main():
    """
    At the beginning of this program, the user is asked to input
    the class name (either SC001 or SC101).
    Attention: your input should be case-insensitive.
    If the user input "-1" for class name, your program would show
    the maximum, minimum, and average among all the inputs.
    """
    max_001 = -float('inf')       # ------------------->Use to store SC001's max score.
    min_001 = float('inf')       # ------------------->Use to store SC001's min score.
    sum_001 = 0       # ------------------->Use to store SC001's all scores.
    times_001 = 0     # ------------------->Use to store SC001's score enter times.
    max_101 = -float('inf')         # ------------------->Use to store SC101's max score.
    min_101 = float('inf')       # ------------------->Use to store SC101's min score.
    sum_101 = 0       # ------------------->Use to store SC101's all scores.
    times_101 = 0     # ------------------->Use to store SC101's score enter times.
    class_name = input('Which class? ')
    if class_name == EXIT:
        print('No class scores were entered ')
    else:
        score = int(input('Score: '))
        while True:
            if class_name[2] == '0':
                sum_001 += score
                times_001 += 1
                if score > max_001:
                    max_001 = score
                if score < min_001:
                    min_001 = score
            elif class_name[2] == '1':
                sum_101 += score
                times_101 += 1
                if score > max_101:
                    max_101 = score
                if score < min_101:
                    min_101 = score
            class_name = input('Which class? ')
            if class_name == '-1':
                break
            score = int(input('Score: '))
        if sum_001 == 0:
            print('=============SC001=============')
            print('No score for SC001')
        else:
            print('=============SC001=============')
            print('Max (001): ' + str(max_001))
            print('Min (001): ' + str(min_001))
            print('Avg (001): ' + str(sum_001/times_001))
        if sum_101 == 0:
            print('=============SC101=============')
            print('No score for SC101')
        else:
            print('=============SC101=============')
            print('Max (101): ' + str(max_101))
            print('Min (101): ' + str(min_101))
            print('Avg (101): ' + str(sum_101/times_101))


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
