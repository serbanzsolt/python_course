# -*- coding: utf-8 -*-
"""
Created on Sun Nov 28 01:22:05 2021

@author: Zsolt
"""

# =============================================================================
# .format method
# =============================================================================

print("this is a string {}".format("INSERTED"))
print("the {} {} {}".format("fox","brown", "quick"))
print("the {2} {1} {0}".format("fox","brown", "quick"))
print("the {0} {0} {0}".format("fox","brown", "quick"))
print("the {q} {b} {f}".format(f="fox",b="brown", q="quick"))

# =============================================================================
# Float formatting
# =============================================================================

result = 100/777
print( result )
print("The result was {r}".format(r=result))
print("The result was {r:1.3f}".format(r=result))
print("The result was {r:10.3f}".format(r=result))
print("The result was {r:10.5f}".format(r=result))
result=102.432
print("The result was {r:1.2f}".format(r=result))

# =============================================================================
# F-Strings
# =============================================================================

name = "jose"

print("hello, his name is {name}")
print(f"hello, his name is {name}")

name = "sam"
age = 3
print(f"{name} is {age} years old")