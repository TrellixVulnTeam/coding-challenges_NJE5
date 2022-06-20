def insertion_sort(array):
    """
    Simple Insertion Sort 
    Usage:
        insertion_sort(unordered_list)
    """

    print("Unsorted: ", array)
    for i in range(1, len(array)):
        current_value = array[i]
        j = i - 1

        while j >= 0 and current_value < array[j]:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = current_value

    print("Sorted: ", array)


def selection_sort(array):
    print("Unsorted: ", array)
    sorted_array = []
    print(min(array))
    lenght = len(array)
    for i in range(lenght):
        minimum = i

        for j in range(i+1, lenght):
            if array[j] < array[minimum]:
                minimum = j
        (array[i], array[minimum]) = (array[minimum], array[i])

    print("Sorted: ", array)

def pop_sort(array):
    lenght = len(array)

    for i in range(lenght-1):
        minimum=min(array)
        array.remove(minimum)
        print(array)




list = [23, 42, 722, 12, 1, -3, 45, 42]
# insertion_sort(list)

# selection_sort(list)

pop_sort(list)
#list.sort()
#print(list)