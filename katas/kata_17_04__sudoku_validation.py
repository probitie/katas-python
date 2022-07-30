class test:
    @classmethod
    def assert_equals(cls, val1, val2, *args, **kwargs):
        print(val1 == val2)

# paste code in kata function
def get_row(matrix, n):
    return matrix[n]

def get_col(matrix, n):
    return [i[n] for i in matrix ]

def is_unique(li) -> bool:
    return len(set(li)) == len(li)

def is_squares_unique(matrix):
    for n in range(0, 9, 3):
        line1 = matrix[n]
        line2 = matrix[n+1]
        line3 = matrix[n+2]
        for m in range(0, 9, 3):
            side1 = line1[n: n + 3]
            side2 = line2[n: n + 3]
            side3 = line3[n: n + 3]

            if not is_unique(side1 + side2 + side3):
                return False
    return True


def valid_solution(matrix) -> bool:  # 2d array 9x9
    size = 9
    valid = False
    for diagonal_elem_id in range(size):
        col = get_col(matrix, diagonal_elem_id)
        row = get_row(matrix, diagonal_elem_id)
        if not is_unique(row) or not is_unique(col) or not is_squares_unique(matrix):
            break  # if this line is not unique, then valid returns as False
    else:
        valid = True  # if all lines are unique, valid become True

    return valid


if __name__ == '__main__':
    test.assert_equals(valid_solution([[5, 3, 4, 6, 7, 8, 9, 1, 2],
                                       [6, 7, 2, 1, 9, 5, 3, 4, 8],
                                       [1, 9, 8, 3, 4, 2, 5, 6, 7],
                                       [8, 5, 9, 7, 6, 1, 4, 2, 3],
                                       [4, 2, 6, 8, 5, 3, 7, 9, 1],
                                       [7, 1, 3, 9, 2, 4, 8, 5, 6],
                                       [9, 6, 1, 5, 3, 7, 2, 8, 4],
                                       [2, 8, 7, 4, 1, 9, 6, 3, 5],
                                       [3, 4, 5, 2, 8, 6, 1, 7, 9]]), True);

    test.assert_equals(valid_solution([[5, 3, 4, 6, 7, 8, 9, 1, 2],
                                       [6, 7, 2, 1, 9, 0, 3, 4, 9],
                                       [1, 0, 0, 3, 4, 2, 5, 6, 0],
                                       [8, 5, 9, 7, 6, 1, 0, 2, 0],
                                       [4, 2, 6, 8, 5, 3, 7, 9, 1],
                                       [7, 1, 3, 9, 2, 4, 8, 5, 6],
                                       [9, 0, 1, 5, 3, 7, 2, 1, 4],
                                       [2, 8, 7, 4, 1, 9, 6, 3, 5],
                                       [3, 0, 0, 4, 8, 1, 1, 7, 9]]), False);

'''[1, 3, 2, 5, 7, 9, 4, 6, 8],
[4, 9, 8, 2, 6, 1, 3, 7, 5],
[7, 5, 6, 3, 8, 4, 2, 1, 9],
[6, 4, 3, 1, 5, 8, 7, 9, 2],
[5, 2, 1, 7, 9, 3, 8, 4, 6],
[9, 8, 7, 4, 2, 6, 5, 3, 1],
[2, 1, 4, 9, 3, 5, 6, 8, 7],
[3, 6, 5, 8, 1, 7, 9, 2, 4],
[8, 7, 9, 6, 4, 2, 1, 3, 5]'''



