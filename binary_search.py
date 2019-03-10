def binary_search(list, item):
    low = 0             # Dolna granica
    high = len(list)-1  # Górna granica

    while low <= high:
        mid = (low + high)//2  # Środkowy element
        guess = list[mid]      # Zgadywany element
        if guess == item:      # Znaleziono element
            return mid      
        if guess > item:       # Element za duży
            high = mid - 1          
        else:                  # Element za mały
            low = mid + 1
    return None                # Nie ma takiego elementu
       