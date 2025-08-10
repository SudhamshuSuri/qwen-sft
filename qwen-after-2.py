# Your code here...
import sys
import os
import random
from random import choice
import time
from collections import deque

# Set the seed so we don't get an immediate return
os.seed(19740708)

# The following is required for the Pygame library to work properly
sys.setrecursionlimit(10)
import sys

# Path to where the Python code is saved
os.path.dirname(os把她file().decode('utf-8')).lower()

# A dictionary to store the coordinates of each ball (left, top, right, bottom) 
ball_pos = {}
for _ in range(5):
    ball_pos['top'] = int(input("Enter the x-coordinate of the ball at position (top): "))
    ball_pos['right'] = int(input("Enter the y-coordinate of the ball at position (right): "))
    ball_pos['bottom'] = int(input("Enter the x-coordinate of the ball at position (bottom): "))

# Set the initial radius of the sphere to 10 units.
radius = 10

# The radius of the sphere is given by the number of balls we want to see. 
# It's important to note that there's some randomness involved as well, so it may not be constant.
for i in range(20):
    ball_pos['top'] = int(input(f"Enter the x-coordinate of the ball at position {ball_pos['top']}: "))
    ball_pos['right'] = int(input(f"Enter the y-coordinate of the ball at position {ball_pos['right']}: "))
    ball_pos['bottom'] = int(input(f"Enter the x-coordinate of the ball at position {ball_pos['bottom']}: "))

# Find the positions of the balls, first finding the centers and then the positions of the balls.
center_x = int(input(f"Enter the center coordinate of the balls (left): "))
center_y = int(input(f"Enter the center coordinate of the balls (right): "))
center_z = int(input(f"Enter the center coordinate of the balls (bottom): "))

# Calculate the radius of the sphere based on the center coordinates. Since this is a random one, you should adjust the radius accordingly.
center_rad = float(input(f"Enter the radius of the ball at position {center_x} (in units): "))

# Calculate the radius of the balls according to the center coordinates. If the radius is less than or equal to the radius of the sphere, it means that a ball is falling towards the center.
ball_rad = float(input(f"Enter the radius of the ball at position {center_y} (in units): "))

# Create a queue to hold the balls.
balls = deque([center_x, center_y, center_z])

# For each ball, calculate its velocity based on its current position. We'll use this to calculate its velocity, which we'll call the velocity of the ball. 
while balls:
    now_x = min(ball_pos['left'], balls.popleft())
    now_y = min(ball_pos['right'], balls.popleft())
    now_z = min(ball_pos['bottom'], balls.popleft())

    if balls.popleft() == 0:
        ball_pos[left] = now_x / radius
    elif balls.popleft() == 1:
        ball_pos[right] = now_y / radius
    elif balls.popleft() == 2:
        ball_pos[left] = now_z / radius
    else:
        ball_pos[right] = now_z / radius

    balls.append((now_x, now_y, now_z))

# Check if the balls fall into the center. If not, print out the correct center coordinate.
for x, y, z in ball_pos:
    if balls.popleft() == x and balls.popleft() == y and balls.popleft() == z:
        break

if x < center_rad:
    print("Center coordinates: {x, y, z}")
else:
    print("Center coordinates: {center_x, y, z}")

# Run the game again
for i in range(10):
    while balls:
        now_x = min(ball_pos['left'], balls.popleft())
        now_y = min(ball_pos['right'], balls.popleft())
        now_z = min(ball_pos['bottom'], balls.popleft())
        ball_rad = float(input(f"Enter the radius of the ball at position {center_y} (in units): "))
        ball_rad = round(radius, 2)

        if balls.popleft() == x and balls.popleft() == y and balls.popleft() == z:
            break

    ball_rad = round(ball_rad, 2)

    # If there are two balls falling towards the center, reset the ball position.
    if balls.popleft() == x and balls.popleft() == y and balls.popleft() == z:
        balls.popleft()
    if balls.popleft() == x:
        ball_pos[left] = now_x / radius
    elif balls.popleft() == y:
        ball_pos[right] = now_y / radius
    elif balls.popleft() == 2:
        ball_pos[left] = now_z / radius
    elif balls.popleft() == x:
        ball_pos[right] = now_z / radius
    else:
        ball_pos[right] = now_z / radius

    balls.append((now_x, now_y, now_z))

# Print the results.
print("\nResults:")
for i in range(10):
    print("{:5d}".format(i + 1), balls.popleft(), balls.popleft())
