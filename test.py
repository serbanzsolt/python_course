import math
import random

def PrintTheList(the_list):
    for item in the_list:
        print(item)
        
def RandomizerInt(number_of_ints = 1, lower_value = 0, upper_value = 0):
    random_array = []
    odds = 0
    evens = 0
    
    for counter in range(0,number_of_ints):
        random_array.append( random.randint(lower_value,upper_value) )
        if random_array[counter] % 2 == 0:
            evens += 1
        else:
            odds += 1
    return [random_array, odds, evens]

print('Result_1:')
result_1 = RandomizerInt(10,100,200)
PrintTheList(result_1[0])

print('Result_2:')
result_2 = RandomizerInt(1,1000,100000)
PrintTheList(result_2[0])

print('Lottery (5):')
result_3 = RandomizerInt(5,0,91)
PrintTheList(result_3[0])

print('Lottery (6)')
result_4 = RandomizerInt(6,0,46)
PrintTheList(result_4[0])