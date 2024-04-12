# merge sorting

def merge(elements,array1,array2):
    i,j,k=0,0,0
    while i <len(array1) and j <len(array2):
        if array1[i]<array2[j]:
            elements[k] = array1[i]
            i+=1
            k+=1 
        else:
            elements[k] = array2[j]
            j +=1
            k +=1
    
    while i<len(array1):
        elements[k] = array1[i]
        i+=1
        k+=1

    while j<len(array2):
        elements[k] = array2[j]
        j+=1
        k+=1
        
    return elements    
    
def mergesort(elements):
    if len(elements) > 1:
        left =0
        right = len(elements)
        mid = (right)//2
        left_list = elements[:mid]
        right_list = elements[mid:]
        mergesort(left_list)
        mergesort(right_list)
    
        return merge(elements,left_list,right_list)
    
    
a = [1,4,6,7,2,5,28]

print(mergesort(a))
    
        