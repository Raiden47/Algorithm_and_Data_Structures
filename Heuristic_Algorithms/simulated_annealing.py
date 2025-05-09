import random
import math

def simulated_annealing(objective_function, domain, steps, initial_temp, cooling_rate):
    current = [random.uniform(d[0], d[1]) for d in domain]
    current_value = objective_function(current)
    temperature = initial_temp
    for _ in range(steps):
        neighbor = [current[i] + random.uniform(-1, 1) for i in range(len(domain))]
        neighbor = [max(min(neighbor[i], domain[i][1]), domain[i][0]) for i in range(len(domain))]
        neighbor_value = objective_function(neighbor)
        delta = neighbor_value - current_value
        if delta > 0 or random.random() < math.exp(delta / temperature):
            current, current_value = neighbor, neighbor_value
        temperature *= cooling_rate
    return current, current_value

if __name__ == "__main__":
    def objective_function(x):
        return -(x[0] ** 2 + x[1] ** 2)

    domain = [(-10, 10), (-10, 10)]
    best_solution, best_value = simulated_annealing(objective_function, domain, 1000, 100, 0.95)
    print("Best solution:", best_solution)
    print("Best value:", best_value)