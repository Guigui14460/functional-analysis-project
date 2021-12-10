from typing import Sequence

from elementary_matrix import compute_elementary_matrix


class MeshTriangle:
    __slots__ = ("vertices", "hx", "hy", "elementary_matrix")

    def __init__(self, v1: Sequence, v2: Sequence, v3: Sequence, hx, hy) -> None:
        self.vertices = {v1: 0, v2: 1, v3: 2}  # local numbering
        # elementary assembly matrix associated with the triangle
        self.elementary_matrix = compute_elementary_matrix(v1, v2, v3, hx, hy)

    def __repr__(self) -> str:
        string = f"MeshTriangle["
        for ii, vi in enumerate(self.vertices.keys()):
            string += f"v{ii}={vi}"
        string += "]"
        return string

    def is_in(self, v: Sequence) -> bool:
        # check if the point v is a point defining the triangle
        return v in self.vertices

    def get_local_num(self, v: Sequence) -> int:
        # retrieves the local number
        return self.vertices[v]

    def get_matrix_entry(self, v1: Sequence, v2: Sequence):
        # retrieves the input associated with points v1 (row) and v2 (column)
        return self.elementary_matrix[self.get_local_num(v1)][self.get_local_num(v2)]
