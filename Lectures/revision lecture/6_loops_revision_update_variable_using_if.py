#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MATH6005: Loops Revision.

# =============================================================================
# Example: Calling another function from within a loop.
#
# In this example you are given a Python list of vehicle types
# (1 = bicycle, 2 = motorcyle, 3 = car, 4 = Lorry)
# These vehicles are to be loaded onto a ferry.
# Before loading begins you need to estimate a total weight of the load
# To do this the function estimated_ferry_load_weight() loops over the list
# of vehicles and calls a function that returns their individual weight.
# The individual weights are summed in the loop to calculate the total weight
# of the load.
# =============================================================================

"""

# =============================================================================
# 3. Calling another function from within a loop.
#
# In this example you are given a Python list of vehicle types
# (1 = bicycle, 2 = motorcyle, 3 = car, 4 = Lorry)
# These vehicles are to be loaded onto a ferry.
# Before loading begins you need to estimate a total weight of the load
# To do this the function estimated_ferry_load_weight() loops over the list
# of vehicles and calls a function that returns their individual weight.
# The individual weights are summed in the loop to calculate the total weight
# of the load.
# =============================================================================

def vehicle_weight_kg(vehicle_type):
    '''returns weight of vehicle type in kilograms
    '''
    if vehicle_type == 1:
        #bicycle
        return 14
    elif vehicle_type == 2:
        #motocycle
        return 200
    elif vehicle_type == 3:
        #car
        return 1000
    else:
        #7 tonne lorry
        return 7000
    
def estimated_ferry_load_weight(to_load):
    '''Loops over vehicle types to load
    and calls the vehicle_weight_kg function to calculate
    an estimated total weight of the load.
    '''
    total_weight = 0.0
    
    #loop over the vehicles to load
    for vehicle_type in to_load:
        #on each loop iteration we called the vehicle_weight_kg function
        #we add the weight of the current vehicle to the total_weight variable
        total_weight = total_weight + vehicle_weight_kg(vehicle_type)
    
    return total_weight
    
def main():
    #list of vehicle types of load onto ferry
    vehicles_to_load = [3, 3, 3, 3, 3, 3, 4, 2, 1, 1, 1] 
    total_load_weight =  estimated_ferry_load_weight(vehicles_to_load)
    print("Estimated total kg's to load: {}".format(total_load_weight))
    
if __name__ == '__main__':
    main()