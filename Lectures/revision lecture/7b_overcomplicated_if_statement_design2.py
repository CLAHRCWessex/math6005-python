#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Exercise: Booking Cinema Tickets and Refreshments

You are going to the cinema and want to know the cost.

Create 3 functions.

tickets.  returns the costs of tickets (i.e one or more) purchased.
          Normal tickets cost 10.99.  Wednesdays reduce the cost by 2.00.
          Premium seating adds an extra 1.50 regardless of the day

refreshments. returns the cost of refreshments.  A user could buy 'popcorn' for 2.00 or 'fizzy pop' for 3.50
             
cinema_trip. Adds the cost of tickets and refreshments together.


*** REVISION NOTES:
    Look at how the If-statement has been designed in tickets()
    This is an improvement on the overcomplicated design we had
    previously, but it is still complicated and has 
    a lot of opportunity for introducing
    bugs into out code (typos in calculations).
    
    Can you think of a simpler way to code it?

"""


def tickets(number, day, premium_seating):
    """
    The cost of the cinema ticket.
    Normal ticket cost is £10.99
    Wednesdays reduce the cost by £2.00
    Premium seating adds an extra £1.50 regardless of the day
    
    Keyword arguments:
    number -- integer value representing the number of seats to book
    day -- day of the week to book (1 = Monday ... 7 = Sunday)
    premium_seating -- boolean True/False.  Are premium seats required.
    """            
    
    if day == 3 and premium_seating:
        return (10.99 - 2.00 + 1.50) * number 
    
    #We have dropped the 'and not premium' boolean comparison 
    elif day == 3:
        return (10.99 - 2.00) * number
    
    #we have dropped the day != 3 boolean comparison
    elif premium_seating:
        return (10.99 + 1.50) * number 
    
    else:
        return 10.99 * number
            

def refreshment(choice ='popcorn'):
    """ 
    The cost of refreshments.  
    Choices are popcorn or fizzy pop 
    
    Keyword arguments:
    choice The users choice of refreshment (default = 'popcorn')
    """
    if choice.lower() == "popcorn":
        return 2.00
    elif choice.lower() == "fizzy pop":
        return 3.50


def cinema_trip(persons, day, premium_seating, treat):
    """ 
    The total cost of going to the cinema 
    
    Keyword arguments:
    persons -- number of people who need a ticket
    day -- day of the week to book (1 = Monday, 7 = Sunday)
    preimum_seating -- boolean True/False if premium seats are required
    treat -- string value representing a choice of refreshment 
    """
    #fill in your code here
    return tickets(persons, day, premium_seating) + refreshment(treat)


def main(): 
    persons = 2
    day = 1
    premium_seating = True
    treat = "popcorn"
    
    msg = "today a trip to the cinema will cost you £{:.2f}"
    print(msg.format(cinema_trip(persons, day, premium_seating, treat)))
    #expected answer = £26.98
    
    persons = 3
    day = 3
    premium_seating = True
    treat = "fizzy pop"
    
    print(msg.format(cinema_trip(persons, day, premium_seating, treat)))
    #expected answer = £34.97

if __name__ == '__main__':
    main()