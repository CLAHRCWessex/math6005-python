#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MATH6005: Loops Revision.

Nested Loops

"""

# =============================================================================
# 4. Nested Loops
# =============================================================================

def main():
    #try change the values of these variables to see how it affects
    #the console output
    n_outer_loops = 3
    n_inner_loops = 5
    
    #Tbe outer loop iterates 'n_outer_loops' times
    for outer_index in range(n_outer_loops):
        print('Outer loop iteration: {0}'.format(outer_index))
        
        #For each outer loop iteration we run 'n_inner_loops' inner loops
        for inner_index in range(n_inner_loops):
            print('\tInner loop iteration: {0}'.format(inner_index))
            
            
if __name__ == '__main__':
    main()
