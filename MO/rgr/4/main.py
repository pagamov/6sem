#!python
# -*- coding: utf-8 -*-
#
# считаем точки методом градиентного наискорейшего спуска

import numpy as np
import math
from collections import namedtuple

CF = namedtuple("CF", "a11 a12 a22 b1 b2")
# XXX:
#   something might not work if a12 != 1
cf = CF(a11 = 3, a12 = 1, a22 = 2, b1 = -50, b2 = 25)

def grad_func(np_arr):
    """calculate labmda function from column `np_arr`"""
    assert np_arr.shape == (2,1), "you must pass column with shape (2,1)"
    x1, x2 = np_arr[0,0], np_arr[1,0]
    new_x1 = 6*x1+x2-50
    new_x2 = x1+4*x2+25
    return np.array([new_x1, new_x2]).reshape((2,1))

def first_way(x, grad):
    """
    return h calculated by first way
    """
    above = 2*cf.a11*x[0,0]*grad[0,0] \
        + cf.a12*x[0,0]*grad[1,0] + cf.a12*x[1,0]*grad[0,0] \
        + 2*cf.a22*x[1,0]*grad[1,0] \
        + cf.b1*grad[0,0] + cf.b2*grad[1,0]
    under = 2*cf.a11 * grad[0,0]**2 \
        + 2 * cf.a12 * grad[0,0] * grad[1,0] \
        + 2*cf.a22*grad[1,0]**2
    return above / under

def second_way(x, grad):
    above = 2*cf.a11*x[0,0]*grad[0,0] \
        + x[1,0]*grad[0,0] \
        + cf.b1*grad[0,0] \
        + x[0,0]*grad[1,0] \
        + 2*cf.a22*x[1,0]*grad[1,0] \
        + cf.b2*grad[1,0]
    under = 2*cf.a11 * grad[0,0]**2 \
        + 2*grad[0,0]*grad[1,0] \
        + 2*cf.a22 * grad[1,0]**2
    return above / under

# accuracy
accuracy = 0.9
# (9, 2) - start point
start_point = np.array([9,2]).reshape((2,1))
# iteration num
MAX_ITERATIONS = 3
# there are two ways:
#   1. through partial derivative by h_k
#   2. through dot product of (grad(f(x1)), grad(f(x2))) = 0
ways = [0,1,1]
x = start_point
print("Starting point:", x, sep="\n")
for _ in range(MAX_ITERATIONS):
    print("=" * 40)
    print("Iteration:\t{}".format(_))
    grad = grad_func(x)
    print("Gradient:", grad, sep="\n")
    grad_mod = math.sqrt(grad[0,0]**2 + grad[1,0]**2)
    print("|grad|:\t{}".format(grad_mod))
    if grad_mod < accuracy:
        print("Reached given accuracy: {}".format(accuracy))
        break
    print(f"Using {ways[_] + 1} method")
    if ways[_] == 0:
        h = first_way(x, grad)
    elif ways[_] == 1:
        h = second_way(x, grad)
    print("calculated h:", h, sep="\n")
    new_x = x - h * grad
    print("calculated new_x:", new_x, sep="\n")
    diff_btw_x = abs(new_x - x)
    diff_btw_x_scalar = math.sqrt(diff_btw_x[0,0]**2 + diff_btw_x[1,0]**2)
    print("Difference between new and old x is:\t{}".format(diff_btw_x_scalar))
    if diff_btw_x_scalar < accuracy:
        print("Reached given accuracy: {}".format(accuracy))
        break
    x = new_x
