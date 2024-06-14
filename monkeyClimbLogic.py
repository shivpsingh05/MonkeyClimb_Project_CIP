"""
This is a worked example. This code is starter code; you should edit and run it to 
solve the problem. You can click the blue show solution button on the left to see 
the answer if you get too stuck or want to check your work!

Note: The starter code for this example is the solution.
"""

from graphics import Canvas
import time

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 450
BALL_DIAMETER = 30
INITIAL_VELOCITY = 5
START_X = 0
START_Y = 0
DELAY = 0.1

POLE_WIDTH = 20
POLE_HEIGHT = CANVAS_HEIGHT - 50

# Monkey Anthropometric Data
BODY_HEIGHT = 40
BODY_WIDTH = 15
BODY_GAP = 1

DISTANCE_CLIMB_1ST_MINUTE = 2
DISTANCE_SLIP_2ND_MINUTE = 13

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    #make pole
    pole_x_left = CANVAS_WIDTH // 3
    pole_y_top = CANVAS_HEIGHT - POLE_HEIGHT
    pole_x_right = pole_x_left + POLE_WIDTH
    pole_y_bottom = CANVAS_HEIGHT
    canvas.create_rectangle(pole_x_left, pole_y_top, pole_x_right, pole_y_bottom, 'black') 

    #make Ball
    x_velocity = INITIAL_VELOCITY
    y_velocity = INITIAL_VELOCITY
    ball_x = pole_x_left + POLE_WIDTH + 2
    ball_y = CANVAS_HEIGHT - BODY_HEIGHT
    ball = canvas.create_oval(ball_x, ball_y,
                              ball_x + BALL_DIAMETER,
                              ball_y + BALL_DIAMETER,
                              'blue')
                              
    while True:
        if ball_y > CANVAS_HEIGHT - POLE_HEIGHT:
            ball_y -= 20
            canvas.moveto(ball, ball_x, ball_y)
            time.sleep(DELAY)
            ball_y += 10
            canvas.moveto(ball, ball_x, ball_y)
            time.sleep(DELAY)

if __name__ == '__main__':
    main()