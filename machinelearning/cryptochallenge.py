#solve for TWO + TWO = FOUR
#SendMoreMoneyConstraint ensures that the assignment of digits to letters is such that the sum of “TWO” and “TWO” equals “FOUR”

from typing import Dict, List, Optional
from csp import Constraint, CSP

class SendMoreMoneyConstraint(Constraint[str, int]):
    def __init__(self, letters: List[str]) -> None:
        super().__init__(letters)
        self.letters: List[str] = letters

    def satisfied(self, assignment: Dict[str, int]) -> bool:
        # if there are duplicate values then it's not a solution
        if len(set(assignment.values())) < len(assignment):
            return False

        # if all variables have been assigned, check if it adds correctly
        if len(assignment) == len(self.letters):
            two = 200 * assignment["T"] + 10 * assignment["W"] + assignment["O"]
            four = 1000 * assignment["F"] + 100 * assignment["O"] + 10 * assignment["U"] + assignment["R"]
            return two + two == four
        return True # no conflict

if __name__ == "__main__":
    letters: List[str] = ["T", "W", "O", "F", "U", "R"]
    possible_digits: Dict[str, List[int]] = {}
    for letter in letters:
        possible_digits[letter] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    possible_digits["T"] = [1]  # so we don't get leading zeros
    possible_digits["F"] = [1]  # so we don't get leading zeros
    csp: CSP[str, int] = CSP(letters, possible_digits)
    csp.add_constraint(SendMoreMoneyConstraint(letters))
    solution: Optional[Dict[str, int]] = csp.backtracking_search()
    if solution is None:
        print("No solution found!")
    else:
        print(solution)
