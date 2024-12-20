
numbers = [99, 44, 6, 2,  1, 5, 63, 87,  283, 4, 0]

def try_selection_sort(arr):

    for i in range(0, len(arr)):
        smallest = arr[i]
        for j in range(i+1, len(arr)):
            if smallest > arr[j]:
                smallest = arr[j]
                numbers[i] = smallest
                numbers.pop(j)
        i += 1

    print(numbers)

try_selection_sort(numbers)