#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MATH6005 Lecture 6. Functions Revision.

# =============================================================================
# Example: Returning a Tuple and unpacking it
# A Tuple allows a function to return more than one value
# The code below first gives an example of a Tuple
# =============================================================================

"""

def descriptive_stats(data):
    '''Calculate mean, max and min
       of the data (list)
    '''
    mean_value = sum(data) / len(data)
    max_value = max(data)
    min_value = min(data)
    
    #when the return statement is a set of variables
    #seperate by a comma (',') then a function returns a
    # Tuple
    return mean_value, max_value, min_value
    

def main():
    #yearly income represented as a python list
    yearly_income = [50, 250, 300, 500, 1000]
    
    #tuple unpacking example
    mean_income, max_income, min_income = descriptive_stats(yearly_income)
    
    #you can then work with each variable seperately e.g.
    double_the_mean = mean_income * 2
    print(double_the_mean)
    
    #return the tuple and do not unpack
    stats_tuple = descriptive_stats(yearly_income)
    
    #you then work with the tuple and its items
    double_the_mean = stats_tuple[0] * 2
    print(double_the_mean)


if __name__ == '__main__':
    main()
