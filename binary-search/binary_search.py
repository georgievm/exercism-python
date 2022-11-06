def find(arr, x):
    low = 0
    high = len(arr)-1
    mid = 0

    while low <= high:
        mid = (low + high) // 2
        if x < arr[mid]:
            high = mid - 1
        elif x > arr[mid]:
            low = mid + 1
        else:
            return mid
    raise ValueError("value not in array")