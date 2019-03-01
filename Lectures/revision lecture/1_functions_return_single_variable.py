#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MATH6005 Python Lecture 6. (Revision)

Functions Revision.

Passing keyword arguments to a function and returning a single variable.

"""

# =============================================================================
# Example 1: Passing keyword argument to a function and 
#            returning a single variable
#
# When a house is purchase in the UK the buyer must pay the 
# government tax - this is called stamp_duty
# =============================================================================
def stamp_duty(house_price, first_time_buyer=False):
    '''
    First time buyers recieve more tax relief than 
    those buying their next home.
    Returns a float representing the amount of house
    tax (called stamp duty in the UK) owed when purchasing
    a house
    
    Keyword arguments:
    house_price -- a float representing the purchase cost of the house
    first_time_buyer -- bool True or False (Default = false)
    '''
    if first_time_buyer:
        #this if statement is nested within the first
        if house_price <= 300000:
            return 0.0
        else: 
            return house_price * 0.05     
    else:
        if house_price < 125000:
            return 0.0
        else:
            return house_price * 0.05
        

def main():
    price = 150000
    
    # the function stamp duty is returning a float which we are
    # storing in the variable called duty_owed
    duty_owed = stamp_duty(price)
    print(duty_owed)
    
    #if you wanted to be more explicit you 
    #could call the function as follows:
    duty_owed = stamp_duty(house_price=price)
    print(duty_owed)
                
    #call the function
    price = 150000
    duty_owed = stamp_duty(house_price=price, first_time_buyer=True)
    print(duty_owed)
            

if __name__ == '__main__':
    main()