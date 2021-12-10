from typing import Sequence

from sympy import ImmutableMatrix, Triangle, Symbol, solve_linear_system


def abs(x, hx, hy):
    # evaluation of x by substituting the symbols hx and hy by 1
    evaluation = x.evalf(subs={hx: 1, hy: 1})
    if evaluation < 0:
        return -x
    return x


def compute_barycenters(a1: Sequence, a2: Sequence, a3: Sequence, x: Sequence, lambdas: Sequence):
    # creation of the system of equations
    system = ImmutableMatrix((
        (a1[0], a2[0], a3[0], x[0]),
        (a1[1], a2[1], a3[1], x[1]),
        (1, 1, 1, 1),
    ))
    # we return the solution of the system
    return solve_linear_system(system, *lambdas)


def get_triangle_area(a1: Sequence, a2: Sequence, a3: Sequence):
    return Triangle(a1, a2, a3).area


def compute_gradient(function, x: Sequence) -> list:
    return [function.diff(x_i) for x_i in x]


def scalar_product(a, b):
    assert len(a) == len(b)  # we check that a and b are of the same length
    acc = 0
    for ii in range(len(a)):
        acc += a[ii] * b[ii]
    return acc


def compute_elementary_matrix(a1: Sequence, a2: Sequence, a3: Sequence, hx, hy):
    # initialization of vectors
    x = [Symbol("x_" + str(ii)) for ii in range(1, len(a1)+1)]
    lambdas = [Symbol("lambda_" + str(ii)) for ii in range(1, 4)]

    # calculation of barycentric coordinates
    barycenters = compute_barycenters(a1, a2, a3, x, lambdas)
    if barycenters is None:
        raise RuntimeError(
            "We have no solution to compute barycenters coordinates")

    # calculation of gradients for each barycentric coordinate
    gradients = {lambda_: compute_gradient(
        barycenters[lambda_], x) for lambda_ in lambdas}

    triangle_area = abs(get_triangle_area(a1, a2, a3), hx, hy)

    # calculation of the entries of the alpha matrix
    return [
        [triangle_area * scalar_product(gradients[lambda_i], gradients[lambda_j])
            for lambda_j in lambdas]
        for lambda_i in lambdas
    ]
