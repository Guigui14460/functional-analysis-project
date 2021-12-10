from typing import Sequence, Set, Union

from mesh_triangle import MeshTriangle


def compute_global_matrix(points, triangles: Union[Sequence[MeshTriangle], Set[MeshTriangle]]):
    n = len(points)

    # init to 0
    matrix = [[0 for _ in range(n)] for _ in range(n)]

    # we look at all the triangles joining the points ii and jj
    for ii in range(n):
        point1 = points[ii]
        for jj in range(n):
            point2 = points[jj]
            for triangle in triangles:
                # we check that the points belong to the triangle
                if triangle.is_in(point1) and triangle.is_in(point2):
                    # we add the entry of the elementary assembly matrix to the entry
                    # associated to ii and jj in the global assembly matrix
                    matrix[ii][jj] += triangle.get_matrix_entry(point1, point2)

    return matrix


def dirichlet_problem(hx, hy, min_x, max_x, min_y, max_y, border_excluded=True):
    assert min_x <= max_x
    assert min_y <= max_y

    # we get the number of points to create in x and y
    pts_x = int((max_x - min_x) / hx) + 1
    pts_y = int((max_y - min_y) / hy) + 1

    # definition of the mesh
    points = []
    for j in range(pts_y):
        sublist = []
        for i in range(pts_x):
            sublist.append((i * hx + min_x, j * hy + min_y))
        points.append(sublist)

    mesh_triangles = set()

    # creation of the triangles of the mesh
    for jj in range(pts_y - 1):
        for ii in range(pts_x - 1):
            v1 = points[jj][ii]
            v2 = points[jj][ii + 1]
            v3 = points[jj + 1][ii]
            v4 = points[jj + 1][ii + 1]
            mesh_triangles.add(MeshTriangle(v1, v2, v3, hx, hy))
            mesh_triangles.add(MeshTriangle(v2, v3, v4, hx, hy))

    # we keep only the points for which we calculate the assembly matrix
    if border_excluded:
        points = [points[ii][jj] for ii in range(
            1, pts_y - 1) for jj in range(1, pts_x - 1)]

    # calculation of the global matrix
    return compute_global_matrix(points, mesh_triangles)
