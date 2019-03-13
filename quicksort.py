def quicksort(array):
    if len(array) < 2:                      # Simple case
        return array
    else:
        pivot = array[0]                     # Recursive case
        less = [i for i in array[1:] if i<= pivot]  # Subb array with elements less than pivot
        grater = [i for i in array[1:] if i > pivot]  # Subb array with larger elements than pivot
        return quicksort(less) + [pivot] + quicksort(grater)