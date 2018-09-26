sorted1 = [1,2,3,4,5]
unsorted1 = [3,2,5,1,6]
list2 = [1,2,4,8,16,32,64]

def linearsearch(data,target):
    for i in range(len(data)):
        if target == data[i]:
            return 'Found'
    return 'Not found'

def binarysearch_i(data,target):
    low = 0
    high = len(data) - 1
    while low <= high:
        mid = (low+high) // 2
        if data[mid] == target:
            return 'Found'
        else:
            if target < data[mid]:
                high = mid - 1
            else:
                low = mid + 1
    return 'Not found'

def binarysearch_r(data,target,low,high):
    mid = (low + high) // 2
    if data[mid] == target:
        return 'Found'
    elif low > high:
        return 'Not found'
    elif target < data[mid]:
        return binarysearch_r(data,target,low,mid-1)
    elif target > data[mid]:
        return binarysearch_r(data,target,mid+1,high)

