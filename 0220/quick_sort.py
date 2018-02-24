# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 12:17:36 2018

@author: 서경
"""


r = 0

def quick_sort(lst):
    
    global r

    if len(lst) <= 1:
        return lst
    
    elif len(lst) > 1:
        pivot = lst[0]
        left_fin = 1
        right_fin = len(lst) - 1
        
        while left_fin < right_fin:
            print('left = %d right = %d, 현 상황 = ' % (left_fin, right_fin), lst)
            if lst[left_fin] < pivot:
                left_fin += 1
                
            else:
                if lst[right_fin] >= pivot:
                    right_fin -= 1
                    
                else:
                    new_left = lst[right_fin]
                    new_right = lst[left_fin]
                    lst[left_fin] = new_left
                    lst[right_fin] = new_right
                    print('swap 후', lst)
                    
        # 자리 바꾸고 나누기
        print('out because', left_fin, right_fin, 'is equal')
        r += 1
        new_zero = lst[right_fin]
        lst[right_fin] = pivot
        lst[0] = new_zero
        print('round %d finish' % r, lst)
        
        lst_left = lst[0:right_fin]
        lst_right = lst[right_fin + 1:len(lst)]
        
        # 재귀
        lst[0:right_fin] = quick_sort(lst_left)
        lst[right_fin + 1:] = quick_sort(lst_right)
        
        return lst


# lst = [3, 1, 5, 6, 8, 0, 1, 3, 4, 23, 25, 2, 1]
lst = [9, 0, 2, 1, 3, 7]
sorted_lst = quick_sort(lst)
print(sorted_lst)




