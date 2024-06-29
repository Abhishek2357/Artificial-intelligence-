from itertools import permutations

def is_solution(letters, perm, formula):
    trans_table = str.maketrans(letters, ''.join(map(str, perm)))
    try:
        return eval(formula.translate(trans_table))
    except ArithmeticError:
        return False

def solve_cryptarithmetic(formula):
    letters = ''.join(set(filter(str.isalpha, formula)))
    for perm in permutations(range(10), len(letters)):
        if is_solution(letters, perm, formula):
            trans_table = str.maketrans(letters, ''.join(map(str, perm)))
            solution = formula.translate(trans_table)
            return solution
    return "No solution found"

# Example usage
formula = "SEND + MORE == MONEY"
solution = solve_cryptarithmetic(formula)
print(solution)
