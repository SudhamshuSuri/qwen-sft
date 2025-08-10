# import required libraries
import math
from tkinter import *
from tkinter import messagebox as messagebox
from random import randn
from collections import deque

def get_direction(x):
    return x * 10 + 360 / (2*60*60)
def is_bounce(radius):
    return radius >= 10 and radius <= 20 and radius < 360 and radius % 10 == 1 and radius % 20 == 2 and radius % 360 == 0 and radius % 360 == 0 and radius % 10 == 1 and radius % 20 == 2 and radius % 20 == 2 and radius % 360 == 0 and radius % 360 == 0 and radius % 10 == 1 and radius % 20 == 2 and radius % 20 == 2 and radius % 360 == 0 and radius % 360 == 0 and radius % 10 == 1 and radius % 20 == 2 and radius % 20 == 2 and radius % 360 == 0 and radius % 360 == 0 and radius % 10 == 1 and radius % 20 == 2 and radius % 20 == 2 and radius % 360 == 0 and radius % 360 == 0 and radius % 10 == 1 and radius % 20 == 2 and radius % 20 == 2 and radius % 360 == 0 and radius % 360 == 0 and radius % 10 == 1 and radius % 20 == 2 and radius % 20 == 2 and radius % 360 == 0 and radius % 360 == 0 and radius % 10 == 1 and radius % 20 == 2 and radius % 20 == 2 and radius % 360 == 0 and radius % 360 == 0 and radius % 10 == 1 and radius % 20 == 2 and radius % 20 == 2 and radius % 360 == 0 and radius % 360 == 0 and radius % 10 == 1 and radius % 20 == 2 and radius % 20 == 2 and radius % 360 == 0 and radius % 360 == 0 and radius % 10 == 1 and radius % 20 == 2 and radius % 20 == 2 and radius % 360 == 0 and radius % 360 == 0 and radius % 10 == 1 and radius % 20 == 2 and radius % 20 == 2 and radius % 360 == 0 and radius % 360 == 0 and radius % 10 == 1 and radius % 20 == 2 and radius % 20 == 2 and radius % 360 == 0 and radius % 360 == 0 and radius % 10 == 1 and radius % 20 == 2 and radius % 20 == 2 and radius % 360 == 0 and radius % 360 == 0 and radius % 10 == 1 and radius % 20 == 2 and radius % 20 == 2 and radius % 360 == 0 and radius % 360 == 0 and radius % 10 == 1 and radius % 20 == 2 and radius % 20 == 2 and radius % 360 == 0 and radius % 360 == 0 and radius % 10 == 1 and radius % 20 == 2 and radius % 20 == 2 and radius % 360 == 0 and radius % 360 == 0 and radius % 10 == 1 and radius % 20 == 2 and radius % 20 == 2 and radius % 360 == 0 and radius % 360 == 0 and radius % 10 == 1 and radius % 20 == 2 and radius % 20 == 2 and radius % 360 == 0 and radius % 360 == 0 and radius % 10 == 1 and radius % 20 == 2 and radius % 20 == 2 and radius % 36

