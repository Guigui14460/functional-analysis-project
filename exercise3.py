from dirichlet_problem import dirichlet_problem
from print_matrix import print_matrix


if __name__ == "__main__":
    hx = hy = .25
    x_min = y_min = 0
    x_max = y_max = 1
    matrix = dirichlet_problem(
        hx, hy, x_min, x_max, y_min, y_max, border_excluded=True)
    print("Global matrix A of exercise 3 :")
    print_matrix(matrix)
