import numpy as np
from itertools import product, combinations

# Generates the t-tuple table
def generate_t_tuple_table(dimension, values_per_parameter):
    columns = [''.join(pair) for pair in combinations('ABCD', 2)]
    table = {col: list(product(range(values_per_parameter), repeat=2)) for col in columns}
    return table

# Calculates fitness based on covered entries
def fitness(test_case, t_tuple_table):
    covered = set()
    for col, pairs in t_tuple_table.items():
        indices = [ord(c) - ord('A') for c in col]
        for idx, pair in enumerate(pairs):
            if pair is not None and all(test_case[i] == pair[j] for i, j in zip(indices, range(2))):
                covered.add((col, idx))
    return len(covered), covered

# Initializes the hyenas
def init_hyenas(N, dimension, values_per_parameter):
    return [np.random.randint(values_per_parameter, size=dimension) for _ in range(N)]

# Updates the position of hyenas based on the best found solution
def update_hyenas(hyenas, best_hyena, dimension, values_per_parameter, iteration, max_iterations):
    a = 2 - iteration * (2 / max_iterations)
    for i, hyena in enumerate(hyenas):
        for j in range(dimension):
            r1 = a * (np.random.rand() - 0.5) * 2  # Random value in [-a, a]
            r2 = np.random.rand()  # Random value in [0, 1]
            d = abs(r2 * best_hyena[j] - hyena[j])  # Distance d in the equations
            hyena[j] = int(np.clip(best_hyena[j] - r1 * d, 0, values_per_parameter - 1))
    return hyenas

# Prints the current state of the t-tuple table
def print_t_tuple_table(t_tuple_table, best_test_case):
    print("T-tuple Table:", best_test_case)
    for col in sorted(t_tuple_table.keys()):
        print(f"{col} Column: ", end="")
        for entry in t_tuple_table[col]:
            print('XXXX' if entry is None else ''.join(str(e) for e in entry), end=" ")
        print()

# Marks the covered entries in the t-tuple table as None
def mark_covered_entries(t_tuple_table, covered):
    for col, idx in covered:
        t_tuple_table[col][idx] = None

def sho(N, Max_iterations, dimension, values_per_parameter):
    t_tuple_table = generate_t_tuple_table(dimension, values_per_parameter)
    hyenas = init_hyenas(N, dimension, values_per_parameter)
    test_suite = []

    for iteration in range(Max_iterations):
        best_fitness = 0
        best_test_case = None
        best_covered = set()

        for hyena in hyenas:
            f, covered = fitness(hyena, t_tuple_table)
            if f > best_fitness:
                best_fitness = f
                best_test_case = hyena
                best_covered = covered

        if best_test_case is not None:
            mark_covered_entries(t_tuple_table, best_covered)
            test_suite.append((best_test_case.tolist(), best_fitness))
            print_t_tuple_table(t_tuple_table, best_test_case)
            hyenas = init_hyenas(N, dimension, values_per_parameter)  # Reinitialize hyenas to get fresh candidates

        if not any(pairs for pairs in t_tuple_table.values()):
            print("\nAll t-tuples are covered.")
            break

    return test_suite

# Parameters for the SHO algorithm
N = 30  # Number of hyenas (solutions)
Max_iterations = 100
dimension = 4  # Number of parameters
values_per_parameter = 2  # Binary parameters

# Execute the SHO algorithm
final_test_suite = sho(N, Max_iterations, dimension, values_per_parameter)

# Output the final test suite
print("\nFinal Test Suite:")
for test_case, weight in final_test_suite:
    print(f"Test case: {test_case}, Weight: {weight}")
# print_t_tuple_table(t_tuple_table)
