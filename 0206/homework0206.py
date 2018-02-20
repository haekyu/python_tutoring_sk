# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def merge_sort(lst):
    # Initial condition

    if len(lst) <= 1:
        return lst
        
    # Split
    left_lst = lst[0: int(len(lst) / 2)]
    right_lst = lst[int(len(lst) / 2): len(lst)]
    
    print("재귀", left_lst, right_lst)
    # Inner sort
    left_lst = merge_sort(left_lst)
    right_lst = merge_sort(right_lst)
    
    # Merge
    sorted_lst = [0] * (len(left_lst + right_lst))
    left_finger, right_finger, sorted_finger = 0, 0, 0
    print("Sorted", left_lst, right_lst)
    while sorted_finger < len(lst):
        # If left copy is done alreadly
        if left_finger >= len(left_lst):
            # Do right copy
            sorted_lst = sorted_lst[:sorted_finger] + right_lst[right_finger:]
            right_finger += len(left_lst) - right_finger + 1
            print("else: all right")
            
        # If right copy is done alreadly
        elif right_finger >= len(right_lst):
            # Do left copy
            sorted_lst = sorted_lst[:sorted_finger] + left_lst[left_finger:]
            left_finger += len(left_lst) - left_finger + 1
            print("else: all left")
        
        elif sorted_finger == len(sorted_lst):
            break
        
        # If both copies are not finished
        else:
            left_val = left_lst[left_finger]
            right_val = right_lst[right_finger]
            
            # if left_value is smaller
            if left_val < right_val:
                # Do left copy
                sorted_lst[sorted_finger] = left_val
                left_finger += 1
                
            # if not
            else:
                # Do right copy
                sorted_lst[sorted_finger] = right_val
                right_finger += 1

        sorted_finger = left_finger + right_finger
        print("merge", sorted_finger, sorted_lst)
    
    print("-" * 10)
    
    return sorted_lst


lst = [5,2,6,45,7,8,3,2,-1, 0]

slst = merge_sort(lst)
print(slst)

