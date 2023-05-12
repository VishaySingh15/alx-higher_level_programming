def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for col in row:
            if col == row[len(row) - 1]:
                print("{}".format(col), end="")
                continue
            print("{}".format(col), end=" ")
        print()
