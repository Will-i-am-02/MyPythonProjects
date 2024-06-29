"""
File: my_drawing.py
Name: William
----------------------
Title: Squeeze Toy Aliens

I like Squeeze Toy Aliens so much, so I decided to draw a picture with it.
"""

from campy.graphics.gobjects import GOval, GRect, GArc, GPolygon, GLine
from campy.graphics.gwindow import GWindow


def main():
    """
    Use campy to draw a picture with Squeeze Toy Aliens in python.
    """
    window = GWindow(800, 800)

    planet = GOval(100, 100)
    planet.color = 'yellow'
    planet.filled = True
    planet.fill_color = planet.color
    window.add(planet, 150, 100)
    planet_black_dot = GOval(15, 15)
    planet_black_dot.filled = True
    window.add(planet_black_dot, 170, 120)
    planet_black_dot = GOval(20, 20)
    planet_black_dot.filled = True
    window.add(planet_black_dot, 190, 110)
    planet_black_dot = GOval(10, 10)
    planet_black_dot.filled = True
    window.add(planet_black_dot, 160, 140)

    ufo_top = GArc(500, 1000, 0, 180)
    ufo_top.color = 'violet'
    window.add(ufo_top, x=150, y=300)

    ufo_mid_line_up = GLine(x0=150, y0=550, x1=650, y1=550)
    ufo_mid_line_up.color = 'violet'
    window.add(ufo_mid_line_up)
    ufo_mid_line_left = GLine(x0=150, y0=550, x1=80, y1=650)
    ufo_mid_line_left.color = 'violet'
    window.add(ufo_mid_line_left)
    ufo_mid_line_right = GLine(x0=650, y0=550, x1=720, y1=650)
    ufo_mid_line_right.color = 'violet'
    window.add(ufo_mid_line_right)
    ufo_mid_line_down = GLine(x0=80, y0=650, x1=720, y1=650)
    ufo_mid_line_down.color = 'violet'
    window.add(ufo_mid_line_down)

    ufo_mid = GOval(60, 60)
    ufo_mid.filled = True
    window.add(ufo_mid, 145, 570)
    ufo_mid = GOval(60, 60)
    ufo_mid.filled = True
    window.add(ufo_mid, 235, 570)
    ufo_mid = GOval(60, 60)
    ufo_mid.filled = True
    window.add(ufo_mid, 325, 570)
    ufo_mid = GOval(60, 60)
    ufo_mid.filled = True
    window.add(ufo_mid, 415, 570)
    ufo_mid = GOval(60, 60)
    ufo_mid.filled = True
    window.add(ufo_mid, 505, 570)
    ufo_mid = GOval(60, 60)
    ufo_mid.filled = True
    window.add(ufo_mid, 595, 570)

    ufo_bottom = GArc(150, 300, 180, 180)
    ufo_bottom.color = 'violet'
    window.add(ufo_bottom, x=120, y=575)
    ufo_bottom = GArc(150, 300, 180, 180)
    ufo_bottom.color = 'violet'
    window.add(ufo_bottom, x=320, y=575)
    ufo_bottom = GArc(150, 300, 180, 180)
    ufo_bottom.color = 'violet'
    window.add(ufo_bottom, x=520, y=575)

    three_eye_head = GOval(200, 100)
    three_eye_head.filled = True
    three_eye_head.color = 'lime'
    three_eye_head.fill_color = three_eye_head.color
    window.add(three_eye_head, 300, 380)

    three_eye_left = GOval(30, 30)
    three_eye_left.color = 'white'
    three_eye_left.filled = True
    three_eye_left.fill_color = three_eye_left.color
    window.add(three_eye_left, 326, 405)

    three_eye_right = GOval(30, 30)
    three_eye_right.color = 'white'
    three_eye_right.filled = True
    three_eye_right.fill_color = three_eye_right.color
    window.add(three_eye_right, 440, 405)

    three_eye_mid = GOval(40, 40)
    three_eye_mid.color = 'white'
    three_eye_mid.filled = True
    three_eye_mid.fill_color = three_eye_mid.color
    window.add(three_eye_mid, (three_eye_left.x+three_eye_right.x)//2-5, 390)

    black_eye_left = GOval(15, 15)
    black_eye_left.filled = True
    window.add(black_eye_left, 330, 410)

    black_eye_right = GOval(15, 15)
    black_eye_right.filled = True
    window.add(black_eye_right, 448, 412)

    black_eye_mid = GOval(20, 20)
    black_eye_mid.filled = True
    window.add(black_eye_mid, (three_eye_left.x+three_eye_right.x)//2+5, 400)

    three_eye_mouth = GArc(15, 25, 80, 160)
    window.add(three_eye_mouth, 330, 440)
    three_eye_mouth = GArc(120, 40, 180, 180)
    window.add(three_eye_mouth, 330, 440)
    three_eye_mouth = GArc(15, 25, 180, 90)
    window.add(three_eye_mouth, 450, 440)
    three_eye_mouth = GOval(20, 30)
    three_eye_mouth.filled = True
    window.add(three_eye_mouth, 390, 445)

    three_eye_corn = GPolygon()
    three_eye_corn.add_vertex((389, 380))
    three_eye_corn.add_vertex((409, 380))
    three_eye_corn.add_vertex((399, 340))
    three_eye_corn.color = 'lime'
    three_eye_corn.filled = True
    three_eye_corn.fill_color = three_eye_corn.color
    window.add(three_eye_corn)

    three_eye_corn = GOval(20, 20)
    three_eye_corn.filled = True
    three_eye_corn.color = 'lime'
    three_eye_corn.fill_color = three_eye_corn.color
    window.add(three_eye_corn, 389, 335)

    left_ear = GPolygon()
    left_ear.add_vertex((260, 400))
    left_ear.add_vertex((300, 440))
    left_ear.add_vertex((320, 450))
    left_ear.color = 'lime'
    left_ear.filled = True
    left_ear.fill_color = left_ear.color
    window.add(left_ear)

    right_ear = GPolygon()
    right_ear.add_vertex((540, 400))
    right_ear.add_vertex((520, 440))
    right_ear.add_vertex((480, 450))
    right_ear.color = 'lime'
    right_ear.filled = True
    right_ear.fill_color = right_ear.color
    window.add(right_ear)



if __name__ == '__main__':
    main()
