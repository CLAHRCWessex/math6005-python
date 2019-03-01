#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MATH6005: Loops Revision

Example: Using a FOR loop to repeatedly update a variable
"""

def calc_average_income(data):
    
    #We must define the variable we want to update 
    #BEFORE we begin looping.
    running_sum = 0.0
    
    for i in range(len(data)):
        #each tiUsing a FOR loop to repeatedly update a variableme we loop the value of running sum is
        #updated.  We add the value of data[i] to it.
        running_sum = running_sum + data[i]
        #alternatively you could have used 'running_sum += data[i]'
        
    average_income = running_sum / len(data)
    
    return average_income


def main():
    #code to test the function
    yearly_income = [50, 250, 300, 500, 1000]
    
    expected_answer = 420.0
    print('expected return value: {}'.format(expected_answer))
    
    average_income = calc_average_income(yearly_income)
    print('actual return value: {}'.format(average_income))



if __name__ == '__main__':
    main()

