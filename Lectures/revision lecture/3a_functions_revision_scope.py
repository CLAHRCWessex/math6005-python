#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MATH6005 Lecture 6. Functions Revision.

# =============================================================================
# Example: Scope of a variable
#
# The code below attempts to double the value of the 'my_salary' variable
# but FAILS.  This is because within double_value() the argument 'to_double'
# is called a 'local variable' with 'local scope'.  Changes to 'to_double'
# only happen within the function.  You can think of to_double as a copy
# of my_salary when it is passed in.
# =============================================================================

"""

def double_value(to_double):
    print('double_value() has been called')
    to_double = to_double * 2 
    print('Inside double_value() to_double now = {}'.format(to_double))    
    
def main():
    my_salary = 25000
    print('value of my_salary BEFORE calling function {}'.format(my_salary))
    #call the function and pass in keyword argument
    double_value(to_double=my_salary)
    print('value of my_salary AFTER calling function {}'.format(my_salary))
    
if __name__ == '__main__':
    main()
    
