number_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # since binary search can be performed only on sorted list
number_to_find = 8


def binary_search_recursive(data, target, low, high):
    """Binary Search function using the Recursive approach"""

    """exit condition is a must. low will be higher than high as we are doing mid+1 or mid-1
    and we will compare till low and high are same"""
    if low > high:
        return False

    mid = (low + high) // 2

    if target == data[mid]:
        return True
    elif target < data[mid]:
        return binary_search_recursive(data, target, low, mid - 1)
    else:
        return binary_search_recursive(data, target, mid + 1, high)

def binary_search_iterative(data, target):
    low = 0
    high = len(number_array)-1
    while low <= high:
        mid = (low + high) // 2
        if number_to_find == data[mid]:
            return True
        elif target < data[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return False


print(binary_search_recursive(number_array, number_to_find, 0, len(number_array) - 1))
print(binary_search_iterative(number_array, number_to_find))