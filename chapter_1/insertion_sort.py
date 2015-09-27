####    Author: Adam Catto                           ####
####    Date: Sept.26 2015                           ####
####    git: acatto/sadme/chapter_1/insertionsort    ####
####    written in python                            ####




    
def InsertionSort(lyst):
    
    n = len(lyst)        
    for i in range(0, n-1):
        j = i
        while j>=0 and lyst[j+1] < lyst[j]:
            lyst[j+1], lyst[j] = lyst[j], lyst[j+1]
            j -= 1
    
    return lyst


