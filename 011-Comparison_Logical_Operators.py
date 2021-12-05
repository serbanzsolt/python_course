# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# =============================================================================
# Comparison operators
# =============================================================================

print (2==2)
print (2==1)
print ('hello'=='bye')
print ('hello'=='Hello')
print (2 == 2.0)

print (2 != 2)
print (2 != 3)

print (2 < 2)
print (2 <= 2)
print (2 < 3)

# =============================================================================
# Logical operators (and, or, not)
# =============================================================================

print( 1<2<3 )
print( 1<2 == 2<3 )

print( 1>2 and 2>3 )
print ( 'a' == 'a' and 11 == 11 )
print ( ('a' == 'a') and (11 == 11) )

print ( 'a' == 'a' or 11 == 11 )
print ( 'a' == 'a' or 11 == 110 )

print(100>1000)
print(not 100>1000)
