import pandas as pd
import plotly.express as px
from math import ceil, floor, log


# The Rule is xn = xn−1 + xn−2
# def solution(total_lambs):

#     total_lambs = int(total_lambs)

#     if total_lambs != abs(total_lambs) or total_lambs == 0:
#         return 0

#     # Caculate the most generous way of distribution
#     generousDistro = floor(log(total_lambs, 2)), ceil(log(2, 2))

#     def stD(z): return abs(total_lambs-2**z)

#     generousDistroAmount = min(generousDistro, key=stD)

#     # Calculate the most stringy way of distribution
#     # Initla value
#     x1 = 1
#     # 2nd term
#     x2 = 1
#     #  Var to hold the current value
#     x1PlusX2 = 0
#     # total sum of the sequence
#     xn = 2
#     # Index of the current term
#     i = 2
#     while xn <= total_lambs:
#         x1PlusX2 = x1+x2
#         x1 = x2
#         x2 = x1PlusX2
#         xn = xn+x1PlusX2
#         i += 1

#     stringyDistroAmount = i-1
#     ans = stringyDistroAmount-generousDistroAmount
#     return float(ans)


# print(solution(10))
# print(solution(143))

# # The Rule is xn = xn−1 + xn−2
# def solution(total_lambs):
#     # Caculate the most generous way of distribution
#     generousDistro = floor(log(total_lambs, 2)), ceil(log(total_lambs, 2))
#     generousDistroAmount = min(
#         generousDistro,
#         key=lambda z: abs(total_lambs-2**z))
#     # Calculate the most stringy way of distribution
#     # Initla value
#     x1 = 1
#     # 2nd term
#     x2 = 1
#     #  Var to hold the current value
#     x1PlusX2 = 0
#     # total sum of the sequence
#     xn = 2
#     # Index of the current term
#     i = 2
#     while xn <= total_lambs:
#         x1PlusX2 = x1+x2
#         x1 = x2
#         x2 = x1PlusX2
#         xn = xn+x1PlusX2
#         i += 1

#     stringyDistroAmount = i-1
#     return int(stringyDistroAmount-generousDistroAmount)

from math import ceil, floor, log


def solution(total_lambs):
    # Caculate the most generous way of distribution
    # +1 (binary-specific)
    generousDistroAmount = floor(log(total_lambs+1, 2))

    # Calculate the most stringy way of distribution
    # Initla value
    x1 = 1
    # 2nd term
    x2 = 1
    #  Var to hold the current value
    x1PlusX2 = 0
    # total sum of the sequence
    xn = 2
    # Index of the current term
    i = 2
    # Fibonacci seq
    while xn <= total_lambs:
        x1PlusX2 = x1+x2
        x1 = x2
        x2 = x1PlusX2
        xn = xn+x1PlusX2
        i += 1
    # Nth term (over) -1 term
    stringyDistroAmount = i-1
    ans = stringyDistroAmount-generousDistroAmount
    return int(ans)
