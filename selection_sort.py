def find_smallest(arr):
    smallest = arr[0]           # Najmniejsza wartość
    smallest_index = 0          # Index najmniejszej wartości
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selection_sort(arr):            # Sortuje tablicę
    newArr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)     # Znajduje najmniejszy element 
        newArr.append(arr.pop(smallest))  # w tablicy i dodaje go do nowej
    return newArr