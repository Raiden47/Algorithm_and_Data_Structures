import random

def hill_climbing(objective_function, domain, steps, step_size):
    current = [random.uniform(d[0], d[1]) for d in domain]
    current_value = objective_function(current)
    for _ in range(steps):
        neighbor = [current[i] + random.uniform(-step_size, step_size) for i in range(len(domain))]
        neighbor = [max(min(neighbor[i], domain[i][1]), domain[i][0]) for i in range(len(domain))]
        neighbor_value = objective_function(neighbor)
        if neighbor_value > current_value:
            current, current_value = neighbor, neighbor_value
    return current, current_value

if __name__ == "__main__":
    def objective_function(x):
        return -(x[0] ** 2 + x[1] ** 2)

    domain = [(-10, 10), (-10, 10)]
    best_solution, best_value = hill_climbing(objective_function, domain, 1000, 0.1)
    print("Best solution:", best_solution)
    print("Best value:", best_value)