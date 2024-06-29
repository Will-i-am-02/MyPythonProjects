"""
File: sierpinski.py
Name: William
---------------------------
This file recursively prints the Sierpinski triangle on GWindow.
The Sierpinski triangle is a fractal described in 1915 by Waclaw Sierpinski.
It is a self similar structure that occurs at different levels of iterations.
"""

from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GLine
from campy.gui.events.timer import pause

# Constants
ORDER = 6                  # Controls the order of Sierpinski Triangle
LENGTH = 600               # The length of order 1 Sierpinski Triangle
UPPER_LEFT_X = 150		   # The upper left x coordinate of order 1 Sierpinski Triangle
UPPER_LEFT_Y = 100         # The upper left y coordinate of order 1 Sierpinski Triangle
WINDOW_WIDTH = 950         # The width of the GWindow
WINDOW_HEIGHT = 700        # The height of the GWindow

# Global Variable
window = GWindow(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)  # The canvas to draw Sierpinski Triangle


def main():
	"""
	In this program I will use recursion to make sierpinski triangles(use GLine instead of GPolygons)
	with order given at Constants.
	"""
	sierpinski_triangle(ORDER, LENGTH, UPPER_LEFT_X, UPPER_LEFT_Y)


def sierpinski_triangle(order, length, upper_left_x, upper_left_y):
	"""
	:param order: int, controls the order of Sierpinski Triangle
	:param length: int, the length of order 1 Sierpinski Triangle
	:param upper_left_x: int, the upper left x coordinate of order 1 Sierpinski Triangle
	:param upper_left_y: int, the upper left y coordinate of order 1 Sierpinski Triangle
	:return: None, only draw Sierpinski Triangle, doesn't have to return anything.
	"""
	if order == 0:
		pass
	else:
		# This part's code is use to draw order 1 Sierpinski Triangle
		# Upper Line
		line1 = GLine(upper_left_x, upper_left_y, upper_left_x+length, upper_left_y)
		window.add(line1)
		# Left line
		line2 = GLine(upper_left_x, upper_left_y, upper_left_x+length*0.5, upper_left_y+length*0.866)
		window.add(line2)
		# Right line
		line3 = GLine(upper_left_x+length, upper_left_y, upper_left_x+length*0.5, upper_left_y+length*0.866)
		window.add(line3)
		# ----------------------------------------------------------------------------------------------------
		# This part's code start to use recursion to draw next order's Sierpinski Triangle.
		# Upper left triangle
		sierpinski_triangle(order-1, length/2, upper_left_x, upper_left_y)
		# Upper right triangle
		sierpinski_triangle(order-1, length/2, upper_left_x+length*0.5, upper_left_y)
		# Lower triangle
		sierpinski_triangle(order-1, length/2, upper_left_x+(length*0.5)/2, upper_left_y+(length*0.866)/2)


if __name__ == '__main__':
	main()
