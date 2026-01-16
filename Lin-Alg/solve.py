
import sympy
from sympy import Matrix, symbols, solve, eye

def solve_prob_17():
    print("--- Problem 17 ---")
    m = symbols('m')
    # Vectors as rows. Check if last vector is dependent.
    # We transpose to putting vectors as columns to check if u is in col space, 
    # OR we just check the rank of the matrix of all vectors.
    # Vector u is in span{u1, u2, u3} iff rank(u1, u2, u3) == rank(u1, u2, u3, u).
    # u1 = (1; 3; -2; 1)
    # u2 = (-2; 3; 1; 1)
    # u3 = (2; 1; 0; 1)
    # u = (1; -1; -3; m)
    A = Matrix([
        [1, 3, -2, 1],
        [-2, 3, 1, 1],
        [2, 1, 0, 1]
    ])
    Au = Matrix([
        [1, 3, -2, 1],
        [-2, 3, 1, 1],
        [2, 1, 0, 1],
        [1, -1, -3, m]
    ])
    print(f"Rank A without u: {A.rank()}")
    # To find m, we can Gaussian elimination
    M = Au.copy()
    print("Matrix M:")
    print(M)
    # Just reduce
    echelon = M.echelon_form()
    print("Echelon form last row:", echelon[-1, :])

def solve_prob_12():
    print("\n--- Problem 12 ---")
    m = symbols('m')
    A = Matrix([
        [1, -1, 1, 2],
        [-1, 2, 2, 1],
        [1, 0, 4, m]
    ])
    # Find m for rank(A) = 2
    # Reduce
    print("Reducing A...")
    curr = A.copy()
    # R2 = R2 + R1
    # R3 = R3 - R1
    # ...
    print(A.echelon_form())

def solve_prob_21():
    print("\n--- Problem 21 ---")
    m = symbols('m')
    # Coeff matrix
    A = Matrix([
        [m, 2, -1],
        [1, m, 2],
        [2, 3, 1]
    ])
    detA = A.det()
    print(f"Determinant of A: {detA}")
    print(f"Roots of detA = 0: {solve(detA, m)}")

def solve_prob_18():
    print("\n--- Problem 18 ---")
    # (a)
    # 3x1 - 5x2 + 2x3 + 4x4 = 2
    # 7x1 - 4x2 + x3 + 3x4 = 5
    # 5x1 + 7x2 - 4x3 - 6x4 = 3
    A = Matrix([
        [3, -5, 2, 4, 2],
        [7, -4, 1, 3, 5],
        [5, 7, -4, -6, 3]
    ])
    print("(a) RREF:")
    print(A.rref())
    
    # (b)
    # 3x1 - x2 + 3x3 = 1
    # -4x1 + 2x2 + x3 = 3
    # -2x1 + x2 + 4x3 = 4
    # 10x1 - 5x2 - 6x3 = -10
    B = Matrix([
        [3, -1, 3, 1],
        [-4, 2, 1, 3],
        [-2, 1, 4, 4],
        [10, -5, -6, -10]
    ])
    print("(b) Rank coeff:", B[:, :-1].rank())
    print("(b) Rank aug:", B.rank())
    print("(b) RREF:", B.rref())

    # (c)
    # 2x1 + 3x2 + 4x3 = 1
    # 3x1 - x2 + x3 = 2
    # 5x1 + 2x2 + 5x3 = 3
    # x1 - 4x2 - 3x3 = 1
    C = Matrix([
        [2, 3, 4, 1],
        [3, -1, 1, 2],
        [5, 2, 5, 3],
        [1, -4, -3, 1]
    ])
    print("(c) Rank coeff:", C[:, :-1].rank())
    print("(c) Rank aug:", C.rank())
    print("(c) RREF:", C.rref())

if __name__ == "__main__":
    solve_prob_17()
    solve_prob_12()
    solve_prob_21()
    solve_prob_18()
