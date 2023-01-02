def binarysearch(arr, l, h, key):
    if h >= l:
        mid = (l+h)//2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            return binarysearch(arr, mid+1, h, key)
        elif arr[mid] > key:
            return binarysearch(arr, l, mid-1, key)
    return -1


a = [12, 34, 56, 78, 90, 110, 123, 134]
l = 0
h = len(a)-1
key = 120
print(binarysearch(a, l, h, key))
