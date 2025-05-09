import random

def genetic_algorithm(objective_function, domain, population_size, generations, mutation_rate):
    def create_individual():
        return [random.uniform(d[0], d[1]) for d in domain]

    def mutate(individual):
        index = random.randint(0, len(domain) - 1)
        individual[index] += random.uniform(-1, 1)
        individual[index] = max(min(individual[index], domain[index][1]), domain[index][0])

    def crossover(parent1, parent2):
        point = random.randint(1, len(domain) - 1)
        return parent1[:point] + parent2[point:]

    population = [create_individual() for _ in range(population_size)]
    for _ in range(generations):
        population = sorted(population, key=objective_function, reverse=True)
        next_generation = population[:2]
        while len(next_generation) < population_size:
            if random.random() < mutation_rate:
                individual = random.choice(population[:10])
                mutate(individual)
                next_generation.append(individual)
            else:
                parent1, parent2 = random.sample(population[:10], 2)
                child = crossover(parent1, parent2)
                next_generation.append(child)
        population = next_generation
    best_individual = max(population, key=objective_function)
    return best_individual, objective_function(best_individual)

if __name__ == "__main__":
    def objective_function(x):
        return -(x[0] ** 2 + x[1] ** 2)

    domain = [(-10, 10), (-10, 10)]
    best_solution, best_value = genetic_algorithm(objective_function, domain, 20, 100, 0.1)
    print("Best solution:", best_solution)
    print("Best value:", best_value)