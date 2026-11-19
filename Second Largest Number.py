
def second_largest(arr):
    largest = float('-inf')
    second = float('-inf')

    for num in arr:
        if num > largest:
            second = largest
            largest = num

        elif num > second and num != largest:
            second = num

    if second == float('-inf'):
        return -1

    return second


numbers = [10, 20, 5, 8, 30, 20]

print("Second largest:", second_largest(numbers))
