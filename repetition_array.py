def list_duplicate_numbers(arr : list) -> list:
    # to-do
    result_array = []
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] == arr[j]:
                result_array.append(arr[i])
    return result_array

array=[1,2,3,3,4,2,54,99]
print(list_duplicate_numbers(array))