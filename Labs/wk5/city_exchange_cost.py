def city_exchange_cost(i, j, tour, cities, od_matrix):
    ''' Calculate the cost of a city exchange
    '''
    n_cities = len(tour)
    
    if i == j:
        return 0
    
    # Ensure i < j
    if j < i:
        temp = i
        i = j
        j = temp
    
    # Check if the edges are consecutive    
    consecutive = j == i + 1
    if j == n_cities - 1 and i == 0:
        consecutive = True
        temp = i
        i = j
        j = temp

    city_i = tour[i]
    city_j = tour[j]
    prev_i = tour[i - 1]
    next_i = tour[(i + 1) % n_cities]
    prev_j = tour[j - 1]
    next_j = tour[(j + 1) % n_cities]     
    
    solution_change = 0
    if consecutive:
        solution_change += od_matrix[prev_i, city_j]
        solution_change += od_matrix[city_i, next_j]
        solution_change += od_matrix[city_j, city_i]
        
        solution_change -= od_matrix[prev_i, city_i]
        solution_change -= od_matrix[city_i, city_j]
        solution_change -= od_matrix[city_j, next_j]
    else:
        solution_change += od_matrix[prev_j, city_i] + od_matrix[city_j, next_i]
        solution_change += od_matrix[prev_i, city_j] + od_matrix[city_i, next_j]
        solution_change -= od_matrix[prev_i, city_i] + od_matrix[city_i, next_i]
        solution_change -= od_matrix[prev_j, city_j] + od_matrix[city_j, next_j]
        
    return solution_change