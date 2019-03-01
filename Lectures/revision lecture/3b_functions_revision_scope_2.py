#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MATH6005 Lecture 6. Functions Revision.

# =============================================================================
# Example: Scope of a variable
# A more suitable approach to double the value would be to for a function
# to return a value e.g.
# =============================================================================

"""

def double_value_with_return(to_double):
    #this time we return the doubled value
    #this means that we do not have scope problems
    #because the calling function is returned a new variable
    return to_double * 2 
    
def main():
    my_salary = 25000
    print('value of my_salary BEFORE calling function {}'.format(my_salary))
    #call the function and pass in keyword argument
    my_salary = double_value_with_return(to_double=my_salary)
    print('value of my_salary AFTER calling function {}'.format(my_salary))
    
if __name__ == '__main__':
    main()
    