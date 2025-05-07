import random

def random_sampling(objective_function, domain, iterations):
    best_solution = None
    best_value = float('-inf')
    for _ in range(iterations):
        candidate = [random.uniform(d[0], d[1]) for d in domain]
        value = objective_function(candidate)
        if value > best_value:
            best_solution, best_value = candidate, value
    return best_solution, best_value

if __name__ == "__main__":
    def objective_function(x):
        return -(x[0] ** 2 + x[1] ** 2)  # Massimizza -x^2 - y^2

    domain = [(-10, 10), (-10, 10)]
    best_solution, best_value = random_sampling(objective_function, domain, 1000)
    print("Best solution:", best_solution)
    print("Best value:", best_value)