import numpy as np
import matplotlib.pyplot as plt

def main():
    ''' Read list of cities, solve with nearest neighbour,
        write solution on a file and make plot'''

    csvfile = 'cities.csv'

    cities = read_input_file(csvfile)

    city_order = nearest_neighbour(cities)
    
    print(city_order)
    plot_tour(city_order, cities)

def read_input_file(csvfile):
    ''' Read an input file with cities
    '''
    return np.genfromtxt(csvfile, skip_header=1, delimiter=',')


def euclidean_distance(x1, y1, x2, y2):
    ''' Computes Euclidean distance between (x1, y1) and (x2, y2)
    '''
    return np.sqrt((x1 - x2)**2 + (y1 - y2) ** 2)


def city_distance(i, j, cities):
    ''' Computes Euclidean distance between city i and j
    using the coordinates given in the 2D array cities
    '''
    return euclidean_distance(cities[i, 0],
                              cities[i, 1],
                              cities[j, 0],
                              cities[j, 1])


def plot_cites(cities, style='ro'):
    ''' Plots a list of cities with the style given in 'style'
    '''    
    plt.plot(cities[:,0], cities[:,1], style)

def plot_tour(tour, cities):
    ''' Plots the tour given in 'tour' based on the city coordinates
    given in 'cities'
    '''
    n_cities = cities.shape[0]
    new_cities = np.empty((n_cities + 1, 2))
    new_cities[:n_cities,:] = cities[tour,:]
    new_cities[n_cities:,:] = cities[tour[0],:]
    plot_cites(new_cities, style='ro-')

def nearest_neighbour(cities):
    ''' Returns a tour of N cities constructed by adding the nearest neighbouring city
    iteratively.
    Arguments:
        cities - 2D array of coordinates for the cities (N rows, 2 Columns)
    '''

    # Initialise variables
    n_cities = cities.shape[0]
    city_order = np.full(n_cities, -1, dtype=np.int32)
    city_visited = np.full(n_cities, False, dtype=np.bool)

    # Add first city (the first on the list)
    city_order[0] = 0
    city_visited[0] = True

    for next_city in range(1, n_cities):
        
        last_visit = city_order[next_city - 1]
        nearest_city = -1
        nearest_dist = np.inf

    
        # Loop 2, fill distances
        for p_des in range(n_cities):
            if city_visited[p_des]:
                continue
            
            distance = city_distance(last_visit,
                                     p_des,
                                     cities)
            if distance < nearest_dist:
                nearest_city = p_des
                nearest_dist = distance
        
        # Add next city
        city_order[next_city] = nearest_city
        city_visited[nearest_city] = True



    return city_order


if __name__ == '__main__':
    main()