#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Exercise: Booking Cinema Tickets and Refreshments

You are going to the cinema and want to know the cost.

Create 3 functions.

tickets.  returns the costs of tickets (i.e one or more) purchased.
          Normal tickets cost 10.99.  Wednesdays reduce the cost by 2.00.
          Premium seating adds an extra 1.50 regardless of the day

refreshments. returns the cost of refreshments.  
A user could buy 'popcorn' for 2.00 or 'fizzy pop' for 3.50
             
cinema_trip. Adds the cost of tickets and refreshments together.

*** REVISION NOTES:
    Look at how the If-statement has been designed in tickets()
   
    The complexity of the code has been greatly reduced by 
    designing the if statements and function carefully.
    
    In this example you can think of the tickets function as a 
    process.
    
    Stage 1. A ticket is created with a base price of 10.99
    Stage 2. If a customer is visiting on Wednesday then subtract 2.00 
    Stage 3. If the customer has ordered premium seating then add 1.50
    Stage 4. Multiply the cost of a single ticket by the number of seats needed
             to get the final cost.
             
    Tips:
       
    Once you have written a function you should think about
    how complex the code is.  Ask yourself can my code be simplified
    and still give the same answer?  
    
    (Make sure you test your code if you change it!)
    
    There are usually multiple ways to write your code.  You should
    always aim for simple code.
    
    Simple code is easier to maintain (fix or alter at a later date)
    and is much easier to read and understand.  It might also be
    more efficient.
    
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
    cost = 10.99
    
    if day == 3: 
        cost -= 2.0

    if premium_seating:
        cost += 1.50

    cost *= number

    return cost
    

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