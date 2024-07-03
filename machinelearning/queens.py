#goal is to print the solution for each size of the chess board (n=10, 15, 20) and the time it took to find the solution.
#note: time complexity of the backtracking algorithm is exponential, so it may take a while

import time
from typing import Dict, List, Optional
from csp import Constraint, CSP

class QueensConstraint(Constraint[int, int]):
    def __init__(self, columns: List[int]) -> None:
        super().__init__(columns)
        self.columns: List[int] = columns

    def satisfied(self, assignment: Dict[int, int]) -> bool:
        for q1c, q1r in assignment.items():
            for q2c in range(q1c + 1, len(self.columns) + 1):
                if q2c in assignment:
                    q2r: int = assignment[q2c]
                    if q1r == q2r:  # same row?
                        return False
                    if abs(q1r - q2r) == abs(q1c - q2c):  # same diagonal?
                        return False
        return True  # no conflict

if __name__ == "__main__":
    ns = [10, 15, 20]  # The sizes of the chess boards
    for n in ns:
        columns: List[int] = [i+1 for i in range(n)]
        rows: Dict[int, List[int]] = {}
        for column in columns:
            rows[column] = [i+1 for i in range(n)]
        csp: CSP[int, int] = CSP(columns, rows)
        csp.add_constraint(QueensConstraint(columns))
        start = time.time()
        solution: Optional[Dict[int, int]] = csp.backtracking_search()
        end = time.time()
        elapsed_time = end - start
        print(f"Time elapsed for n={n}: {elapsed_time} seconds")
        if solution is None:
            print("No solution found!")
        else:
            print(solution)
