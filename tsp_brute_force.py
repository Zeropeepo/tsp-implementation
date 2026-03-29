import sys
from itertools import permutations


def tsp_brute_force(distances):
    n = len(distances)
    start_city = 0
    other_cities = [i for i in range(1, n)]
    min_distance = sys.maxsize
    best_path = []
    
    all_permutations = permutations(other_cities)
    
    for perm in all_permutations:
        current_distance = 0
        current_city = start_city
        
        for next_city in perm:
            current_distance += distances[current_city][next_city]
            current_city = next_city
            
        current_distance += distances[current_city][start_city]
        
        if current_distance < min_distance:
            min_distance = current_distance
            best_path = [start_city] + list(perm) + [start_city]
            
    return best_path, min_distance

distances = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

optimal_path, min_cost = tsp_brute_force(distances)
print(f"Rute optimal: {optimal_path}")
print(f"Jarak minimum: {min_cost}")
