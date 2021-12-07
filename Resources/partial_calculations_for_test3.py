# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 23:20:29 2021

@author: Zsolt
"""
# =============================================================================
# 1
# =============================================================================
def lesser_of_two_evens(a,b):
    if a % 2 == 0 and b % 2 == 0:
        if a > b:
            return b
        elif b > a:
            return a
        else:
            pass
    else:
        if a > b:
            return a
        elif b > a:
            return b
        else:
            pass

result = lesser_of_two_evens(2, 4)
result2 = lesser_of_two_evens(2, 5)

print(result)
print(result2)
# =============================================================================
# 2
# =============================================================================
def animal_crackers(text='default'):
    textlist = []
    for letter in text:
        if letter == ' ':
            textlist = text.split(' ')
            
    if len(textlist) == 2:
        print(textlist)
        if textlist[0][0].lower() == textlist[1][0].lower():
            print('TRUE')
            return True
        else:
            print('They not start the same letter')
    else:
        print('not two words you given')
        
animal_crackers('Levelheaded Llama')
        
# =============================================================================
# 3
# =============================================================================
        
def makes_twenty(n1,n2):
    if n1+n2 == 20 or n1 == 20 or n2 == 20:
        return True
    else:
        return False
    
print(makes_twenty(20,10))
print(makes_twenty(2,3))
print(makes_twenty(12,8))

# =============================================================================
# 4
# =============================================================================

def old_macdonald(name='default'):        
    string_return = ''
    for index,letter in enumerate(name):
        if index == 0 or index == 3:
            string_return += letter.upper()
        else:
            string_return += letter.lower()
        
    return string_return

print(old_macdonald('macdonald'))

# =============================================================================
# 5
# =============================================================================
        
def master_yoda(text):
    text_return = ''
    text_list = text.split()
    print(text_list)
    text_list.reverse()
    print(text_list)
    list_len = 1
    for word in text_list:
        if list_len < (len(text_list)):
            text_return += word
            text_return += ' '
            list_len += 1
        else:
            text_return += word
    return text_return

print(master_yoda('I am home'))
print(len(master_yoda('I am home')))
print(master_yoda('We are ready'))
        
# =============================================================================
# 6
# =============================================================================
def almost_there(n):
    if (n >= 110 and n <=190) or (n <= 90) or (n >= 210):
        return False
    else:
        return True

print(almost_there(104))
print(almost_there(150))
print(almost_there(209))

# =============================================================================
# 7
# =============================================================================

def has_33(nums):
    list_pos = 0
    list_len = len(nums)
    print(f'len: {list_len}')
    for number in nums:
       
        if number == 3:
            if list_pos > 0 and list_pos < list_len:
                if nums[list_pos] == nums[(list_pos-1)] or nums[list_pos] == nums[(list_pos+1)]:
                    return True
                else:
                    pass
                    # list_pos += 1 //ERROR took 1h to find...
            elif list_pos == 0:
                if nums[list_pos] == nums[(list_pos+1)]:
                    return True
            elif list_pos == list_len:
                if nums[list_pos] == nums[(list_pos-1)]:
                    return True
                else:
                    list_pos += 1
            else:
                pass
        else:
            list_pos += 1
    return False
        
print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))
# mylist = [12,32,123,3,1]
# pos = 1
# print(mylist[(pos-1)])

# =============================================================================
# 8
# =============================================================================












