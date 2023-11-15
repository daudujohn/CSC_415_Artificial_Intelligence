import random
from datetime import datetime

mutation_probability = 0.6

def print_board(chess_board: str):
    for i in range(7, -1, -1):
        for j in range(8):
            val = chess_board[j]
            if str(i) == val:
                print('Q', end=" ")
            else:
                print('_', end=" ")
        print()
    print()

def generate_chess_board():
    board = ''
    for i in range(0, 8):
        position = random.randint(0, 7)  # generate a real number in the range [0, 7]
        board += str(position)
    return board

def weighted_by(population, fitness):
    weights = [fitness(chromosome) for chromosome in population]
    return weights

def weighted_random_choices(population, weights, k):
    selected_parents = random.choices(population=population, weights=weights, k=k)

    return tuple(selected_parents)

def reproduce(mum, dad):
    n = len(mum)
    c = random.randint(1, n)

    return mum[0: c] + dad[c: n]

def mutate(child: str, mutation_probability, mutation_choices: list):
    if (random.random() < mutation_probability):
        child_copy = '' + child
        index_to_mutate = random.randint(0, len(child_copy) - 1)
        child_copy = child_copy[:index_to_mutate] + random.choice(mutation_choices) + child_copy[index_to_mutate + 1:]
        return child_copy
    else:
        return child

def same_diagonal(chess_board, i, j):
    abs_diff_a = i - int(chess_board[i])
    abs_diff_b = j - int(chess_board[j])
    sum_a = i + int(chess_board[i])
    sum_b = j + int(chess_board[j])
    if abs_diff_a == abs_diff_b or sum_a == sum_b:
        return True
    else:
        return False

def compute_fitness_value(chess_board):  # compute the heuristic function value of the current solution, # attacking pairs
    fitness_value = 0  # if h_value = 0 is eventually returned, then the configuration is a solution to the 8-queens problem
    for i in range(0, 7):
        for j in range(i + 1, 8):
            if chess_board[i] == chess_board[j]:  # same row attack
                fitness_value += 1
            elif same_diagonal(chess_board, i, j):  # same diagonal attack
                fitness_value += 1
    return fitness_value

def genetic_algorithm(population: list, fitness):
    itr = 0
    correct_chromosome_index = None
    fitness_accepted = False
    
    while not fitness_accepted:
        fitness_values = []
        weights = weighted_by(population, fitness)

        for chromosome in population:
            fitness_values.append(fitness(chromosome))

        if (0 in fitness_values or 0 in weights):
            correct_chromosome_index = fitness_values.index(0)
            fitness_accepted = True
            break

        itr += 1
        next_population = []

        for _ in range(0, len(population)):
            try:
                parents = weighted_random_choices(population=population, weights=weights, k=2)
            except ValueError:
                break

            child = reproduce(parents[0], parents[1])

            mutated_child = mutate(child, mutation_probability, ['1', '2', '3', '4', '5', '6', '7', '8'])

            next_population.append(mutated_child)

        population = next_population
    print('population', population)
    print('fitness_values', fitness_values)

    return {"itr": itr, "population": population, "correct_chromosome_index": correct_chromosome_index}

def main(number_of_chromosome):
    population = [generate_chess_board() for _ in range(number_of_chromosome)]

    print('Initial chromosomes printed below')
    for i in range(len(population)):
        print(population[i])
    
    while True:
        result = genetic_algorithm(population, compute_fitness_value)

        if result:
            print(result)
            print('The Genetic algorithm has found a solution to the 8-queens problem')
            print("correct chromosome:", population[result['correct_chromosome_index']])
            print(f'Done after {result["itr"]} iterations. Solution printed below')
            print_board(population[result['correct_chromosome_index']])  # FIXME: print_board output does not match correct chromosome
            break

if __name__ == '__main__':
    global start_time
    start_time = datetime.now()
    main(number_of_chromosome=4)
    print('Start Time:', start_time, '\nEnd Time:', datetime.now())

