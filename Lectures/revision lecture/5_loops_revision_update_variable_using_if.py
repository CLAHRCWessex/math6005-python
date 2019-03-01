#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MATH6005: Loops Revision

Example: Looping over a list to search for a largest or smallest value

We need to make use of if-statements to keep track of 'if' 
an update to a variable is required.

"""

# =============================================================================
# The function below finds the smallest value in an array
# =============================================================================

def find_smallest_value(data):
    smallest = data[0]
    
    for i in range(1, len(data)):
        #we only update 'smallest' if we have found
        #a new minimum value in the list
        if data[i] < smallest:
            smallest = data[i]
    
    return smallest
    

def main():
    data = [10.6, 32.1, 4.2, 45.0, 8.6]
    smallest = find_smallest_value(data)
    print(smallest)
    
    
if __name__ == '__main__':
    main()