#!/usr/bin/env python
# coding: utf-8

# In[ ]:
import numpy as np


class Vec:
    def __init__(self, inp=[]):
        self.nums = inp

    def norm(self, p):
        lp_sum = 0
        for i in range(len(self.nums)):
            # Lp norm formula with parameter p
            lp_sum += pow(abs(self.nums[i]), p)
        return pow(lp_sum, 1 / p)

    def __sub__(self, other):
        result = []
        for i in range(len(self.nums)):
            result.append(self.nums[i] - other.nums[i])
        return Vec(result)

    def __str__(self):
        """prints the rows and columns in matrix form """
        return str(self.nums)
        row_str = ''
        for num in self.nums:
            row_str += str(num) + ' '
        return row_str


class Matrix:
    def __init__(self, inp_rows=[]):
        self._row_space = inp_rows
        self._col_space = []
        self.R = len(inp_rows)
        self.C = len(inp_rows[0])
        num_rows = len(self._row_space)
        if num_rows > 0:
            row_size = len(self._row_space[0])
            for row in self._row_space:
                if len(row) != row_size:
                    raise ValueError("Input is not a valid row-space")
            self._col_space = [[0] * num_rows for _ in range(row_size)]
            for row_index, row in enumerate(self._row_space):
                for item_index, num in enumerate(row):
                    self._col_space[item_index][row_index] = num

    def rank(self):
        A = copy.deepcopy(self._row_space)
        n = len(A)
        m = len(A[0])
        EPS = 1E-9  # epsilon for 0 rounding errors

        rank = 0
        row_selected = [False for i in range(n)]
        for i in range(m):
            flag = True
            for j in range(n):
                # break when you find non zero value in matrix
                if (row_selected[j] == False and abs(A[j][i]) > EPS):
                    flag = False
                    break
            if (flag):
                j += 1
            if (j != n):
                # rank increment if the column is not the last one
                rank += 1
                row_selected[j] = True
                # updating the matrix values for next iteration
                for p in range(i + 1, m):
                    A[j][p] /= A[j][i]
                for k in range(n):
                    if (k != j and abs(A[k][i]) > EPS):
                        for p in range(i + 1, m):
                            A[k][p] -= A[j][p] * A[k][i]
        return rank

    def get_col(self, j):
        return self._col_space[j - 1]

    def get_row(self, i):
        return self._row_space[i - 1]

    def get_entry(self, i, j):
        return self._row_space[i][j]

    def col_space(self):
        return self._col_space

    def row_space(self):
        return self._row_space

    def get_diag(self, k):
        diag = []
        index = 0
        if k < 0:
            k = -k
            while (index < len(self._col_space) and (index + k) < len(self._row_space)):
                diag.append(self._row_space[index + k][index])
                index += 1
        else:
            while (index < len(self._row_space) and (index + k) < len(self._col_space)):
                diag.append(self._row_space[index][index + k])
                index += 1
        return diag

    def set_row(self, i, v):
        i = i - 1
        if len(v) != len(self._col_space):
            raise ValueError("Incompatible row length")
        self._row_space[i] = v
        self._update_colspace_from_rowspace()

    def set_col(self, j, u):
        j = j - 1
        if len(u) != len(self._row_space):
            raise ValueError("Incompatible column length")
        self._col_space[j] = u
        self._update_rowspace_from_colspace()

    def set_entry(self, i, j, x):
        i = i - 1
        j = j - 1
        self._row_space[i][j] = x
        self._col_space[j][i] = x

    def __add__(self, other):
        other_rows = other.row_space()
        other_cols = other.col_space()

        if len(other_rows) != len(self._row_space) or len(other_cols) != len(self._col_space):
            raise ValueError("Operands incompatible for Matrix addition")

        new_rowspace = [[0] * len(self._col_space) for _ in range(len(self._row_space))]
        for i, row in enumerate(self._row_space):
            for j, item in enumerate(row):
                new_rowspace[i][j] = self._row_space[i][j] + other_rows[i][j]
        return Matrix(new_rowspace)

    def __sub__(self, other):
        other_rows = other.row_space()
        other_cols = other.col_space()

        if len(other_rows) != len(self._row_space) or len(other_cols) != len(self._col_space):
            raise ValueError("Operands incompatible for Matrix sutraction")

        new_rowspace = [[0] * len(self._col_space) for _ in range(len(self._row_space))]
        for i, row in enumerate(self._row_space):
            for j, item in enumerate(row):
                new_rowspace[i][j] = self._row_space[i][j] - other_rows[i][j]
        return Matrix(new_rowspace)

    def __mul__(self, other):
        if type(other) == float:
            return self.__rmul__(other)
        elif type(other) == Matrix:
            other_rows = other.row_space()
            other_cols = other.col_space()

            # (m1, n1) x (m2, n2) multiplication
            m1 = len(self._row_space)
            n1 = len(self._col_space)
            m2 = len(other_rows)
            n2 = len(other_cols)

            if n1 != m2:
                raise ValueError("Incompatible matrices for matrix multiplication")

            # result dim: (m1, n2)
            new_rowspace = [[0] * n2 for _ in range(m1)]
            for i in range(m1):
                for j in range(n2):
                    for k in range(n1):
                        new_rowspace[i][j] += self._row_space[i][k] * other_rows[k][j]

            return Matrix(new_rowspace)
        elif type(other) == Vec:
            nums = other.nums

            if len(self._col_space) != len(nums):
                raise ValueError("Incompatible dimensions for matrix-vector multiplication")

            new_nums = [0] * len(self._row_space)
            two_D = np.reshape(new_nums, (-1, 2))
            for i in range(len(self._row_space)):
                for k in range(len(nums)):
                    a = two_D[i] + self._row_space[i][k] * nums[k]
                    two_D[i] = a

            return Vec(two_D)
        else:
            print("ERROR: Unsupported Type.")
        return

    def __rmul__(self, other):
        if type(other) == float:
            new_rowspace = [[0] * len(self._col_space) for _ in range(len(self._row_space))]
            for i, row in enumerate(self._row_space):
                for j, item in enumerate(row):
                    new_rowspace[i][j] = self._row_space[i][j] * other
            return Matrix(new_rowspace)
        else:
            print("ERROR: Unsupported Type.")
        return

    def __str__(self):
        """prints the rows and columns in matrix form """
        mat_str = ''
        for row in self._row_space:
            row_str = ''
            for num in row:
                row_str += str(num) + ' '
            mat_str += row_str + '\n'
        return mat_str

    def __eq__(self, other):
        """overloads the == operator to return True if
        two Matrix objects have the same row space and column space"""
        this_rows = self._row_space()
        other_rows = other.row_space()
        this_cols = self._col_space()
        other_cols = other.col_space()
        return this_rows == other_rows and this_cols == other_cols

    def __req__(self, other):
        """overloads the == operator to return True if
        two Matrix objects have the same row space and column space"""
        this_rows = self._row_space()
        other_rows = other.row_space()
        this_cols = self._col_space()
        other_cols = other.col_space()
        return this_rows == other_rows and this_cols == other_cols

    def _update_colspace_from_rowspace(self):
        for row_index, row in enumerate(self._row_space):
            for item_index, num in enumerate(row):
                self._col_space[item_index][row_index] = num

    def _update_rowspace_from_colspace(self):
        for col_index, col in enumerate(self._col_space):
            for item_index, num in enumerate(col):
                self._row_space[item_index][col_index] = num


A = [[1, 1, 0], [0, 1, 1], [1, 0, 1]]
Q, R = np.linalg.qr(A)

print("Q =\n", Q)
print("\nR =\n", R)

print("\n\nOriginal A =\n", Matrix(A))
print("\nQ * R =\n", Matrix(Q) * Matrix(R))


def solve_qr(A, b):
    """
    Function that uses QR-factorization of A to compute and return the solution to the
    the system 𝐴𝑥=𝑏"""
    Q, R = np.linalg.qr(A, mode="r")  # compute the qr factorization of matrix A

    # multiply both sides of the equation by the transpose of 𝑄
    q_transpose_b = np.dot(Q.T, b)  # product of q_transpose and vector b
    q_transpose_q = np.dot(Q.T, Q)  # product of q_transpose and Q

    solution = np.linalg.solve((q_transpose_q) * R, q_transpose_b)  # multiplying both sides
    return solution


# tests
A = Matrix([[2, -2, 18], [2, 1, 0], [1, 2, 0]])
x_true = Vec([3, 4, 5])
b = A * x_true
print("Expected:", x_true)
x = solve_qr(A, b)
print("Returned:", x)

