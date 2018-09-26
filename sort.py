unsorted = [4,1,6,8,3,5,2,7]

def bubblesort(array):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(array)-1):
            if array[i] > array[i+1]:
                array[i],array[i+1] = array[i+1],array[i]
                swapped = True
    return array

def insertionsort(array):
    for i in range(1,len(array)): # assume array[0] sorted
        extracted = array[i]
        while i > 0 and extracted < array[i-1]:
            array[i] = array[i-1]
            array[i-1] = extracted
            i -= 1
    return array

def quicksort(array):
    if array == []:
        return []
    else:
        pivot = array[0]
        less = []
        more = []
        for i in range(1,len(array)):
            if array[i] < pivot:
                less.append(array[i])
            else:
                more.append(array[i])
        return quicksort(less) + [pivot] + quicksort(more)


#main
print(bubblesort(unsorted))
print(insertionsort(unsorted))
print(quicksort(unsorted))
