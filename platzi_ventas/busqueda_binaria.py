"""Algorimo busqueda binaria."""
import random


def binary_search(data, target, low, high):
    """Funcion para hallar el numero en la lista."""
    if low > high:
        return False
    middle = ((low + high) // 2)

    if target == data[middle]:
        return True
    elif target < data[middle]:
        return binary_search(data, target, low, middle - 1)  # Low se mantiene, cambia high
    else:  # Target es mayor que el dato a la mitad
        return binary_search(data, target, middle + 1, high)   # High se mantiene, cambia low

if __name__ == '__main__':
    data = [random.randint(0, 100) for i in range(10)]
    data.sort()
    print(data)
    target = int(input('Which numer would you like to find? \t'))
    found = binary_search(data, target, 0, len(data) - 1)
    print(found)
