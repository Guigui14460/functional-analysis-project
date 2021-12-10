def print_matrix(matrix, string_format="{:.2f}"):
    for row in matrix:
        print("\t".join([string_format.format(float(e)) for e in row]))
