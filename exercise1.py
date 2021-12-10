from sympy import Symbol

from elementary_matrix import compute_elementary_matrix
from print_matrix import print_matrix


if __name__ == "__main__":
    hx = hy = Symbol("h")
    a1 = (0, 0)
    a2 = (hx, 0)
    a3 = (0, -hy)
    matrix = compute_elementary_matrix(a1, a2, a3, hx, hy)
    print("Elementary assembly matrix of exercise 1 :")
    print_matrix(matrix)
