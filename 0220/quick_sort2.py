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
    
    else:
        pivot = lst[0]
        fin_l = 1
        fin_r = len(lst) - 1
        
        #왼쪽은 기준보다 작은리스트, 오른쪽은 기준보다 같거나 큰 리스트
        
            #왼쪽 포인트
            if lst[fin_l] < pivot:
                print('왼쪽 이동')
                fin_l += 1
                
                #오른쪽 포인트
                elif lst[fin_r] >= pivot:
                    print('오른쪽 이동')
                    fin_r -= 1
                    
                #둘다 멈춤 ==> 바꾸기
                else
        
        #둘이 만남 > 기준점 변경 및 나누기
        if fin-r = fin_l:
            
        
        
        
     
    
    
    

#lst = [3,1,5,6,8,0,1,3,4,23,25,2,1]
#lst = [5,4,3,2]
#sorted_lst = quick_sort(lst)
#print(sorted_lst)




