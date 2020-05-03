import math


def get_bonus(salary, percentage=35):
    return math.floor(salary * (percentage / 100))
