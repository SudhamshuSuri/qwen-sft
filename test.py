import tkinter as tk
import math
import numpy as np
from dataclasses import dataclass
from typing import List

# Constants
WIDTH, HEIGHT = 800,
HEXAGON_SIZE =
BALL_RADIUS = 10
GRAVITY = 
FRICTION = 
SPIN_SPEED =   # 360 degrees per 5 seconds

# Colors
COLORS = [
    '#f8b862', '#f6ad49', '#f39800', '#f08300', '#ec6d51', '#ee7948', 
    '#ed6d3d', '#ec6800', '#ec6800', '#ee7800', '#eb6238', '#ea5506', 
    '#ea5506', '#eb6101', '#e49e61', '#e45e32', '#e17b34', '#dd7a56', 
    '#db8449', '#d66a35'
]

@dataclass
class Ball:
    x: float
    y: float
    vx: float
    vy: float
    radius: float
    color: str
    number: int
    angle: float

class Hexagon:
    def __init__(self, size: float):
        self.size = size
        self.angle =    def get_points(self):
        points = []
        for i in range(6):
            angle = self.angle + i * math.pi /  x = WIDTH / 2 + self.size * math.cos(angle)
            y = HEIGHT / 2 + self.size * math.sin(angle)
            points.append((x, y))
        return points

class App:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.canvas = tk.Canvas(self.root, width=WIDTH, height=HEIGHT)
        self.canvas.pack()
        self.hexagon = Hexagon(HEXAGON_SIZE)
        self.balls: List[Ball] = []
        for i in range(20):
            ball = Ball(WIDTH / 2, HEIGHT / 2, np.random.uniform(-, 2), np.random.uniform(-2, 2), BALL_RADIUS, COLORS[i], i + 1, 0)
            self.balls.append(ball)
        self.update()

    def update(self):
        self.hexagon.angle += SPIN_SPEED
        for ball in self.balls:
            ball.x += ball.vx
            ball.y += ball.vy
            ball.vy += GRAVITY
            ball.vx *= FRICTION
            ball.vy *= FRICTION
            ball.angle += 
            if ball.y + ball.radius > HEIGHT:
                ball.vy = -ball.vy * 0.8
                ball.y = HEIGHT - ball.radius
            if ball.x - ball.radius < 0 or ball.x + ball.radius > WIDTH:
                ball.vx = -ball.vx
            self.check_collision_with_hexagon(ball)
            self.check_collision_with_other_balls(ball)
        self.draw()
        self.root.after(16, self.update)

    def check_collision_with_hexagon(self, ball: Ball):
        points = self.hexagon.get_points()
        for i in range(6):
            x, y1 = points[i]
            x2, y2 = points[(i + 1) % 6]
            if self.is_collision_with_line(ball, x1, y1, x2, y2):
                ball.vx = -ball.vx
                ball.vy = -ball.vy

    def check_collision_with_other_balls(self, ball: Ball):
        for other_ball in self.balls:
            if ball == other_ball:
                continue
            if self.is_collision_with_ball(ball, other_ball):
                ball.vx, other_ball.vx = other_ball.vx, ball.vx
                ball.vy, other_ball.vy = other_ball.vy, ball.vy

    def is_collision_with_line(self, ball: Ball, x1: float, y1: float, x2: float, y2: float):
        dx = x2 - x1
        dy = y2 - y1
        length = math.sqrt(dx ** 2 + dy ** 2)
        dx /= length
        dy /= length
        t = ((ball.x - x1) * dx + (ball.y - y1) * dy) / length
        if t < 0:
            t = 0
        if t > length:
            t = length
        x = x1 + t * dx
        y = y1 + t * dy
        distance = math.sqrt((ball.x - x) ** 2 + (ball.y - y) ** 2)
        return distance < ball.radius

    def is_collision_with_ball(self, ball: Ball, ball2: Ball):
        distance = math.sqrt((ball1.x - ball2.x) ** 2 + (ball1.y - ball2.y) ** 2)
        return distance < ball1.radius + ball2.radius

    def draw(self):
        self.canvas.delete('all')
        points = self.hexagon.get_points()
        self.canvas.create_polygon(points, outline='black')
        for ball in self.balls:
            x = ball.x
            y = ball.y
            self.canvas.create_oval(x - ball.radius, y - ball.radius, x + ball.radius, y + ball.radius, fill=ball.color)
            self.canvas.create_text(x, y, text=str(ball.number), angle=math.degrees(ball.angle))

if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    root.mainloop()
