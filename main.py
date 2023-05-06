import time
import random

def generate_list(elements: int) -> list:
    '''Function that generates a randomised list of integers'''
    
    # Generate sorted list of n elements
    sorted_list = [n for n in range(1, elements + 1)]

    # Create a new randomised list of n elements
    random_list = random.sample(sorted_list, elements)

    return random_list

def sorting_algorithm(randomised_list: list) -> list:
    ''''''

    list_to_sort = randomised_list[:]
    length = len(randomised_list)

    # Stores the value of the first element in the list
    start_element = int
    swapped_order = False

    for i in range(length):
        # Check if elements had their order swapped or at last element in list
        if not swapped_order:     
        # Check if list is sorted           
            sorted = True
            for j, element in enumerate(list_to_sort[1:]):
                if list_to_sort[j] > element:
                    sorted = False
                    break
        
            if sorted:
                print('sorted')
                return list_to_sort
        
        # Check ordering
        swapped_order = False
        start_element = list_to_sort[i]
        for j, element in enumerate(list_to_sort[i + 1:]):
            if element <= start_element:
                # Insert element to start position
                list_to_sort.pop(j + (i + 1))
                list_to_sort.insert(i, element)
                start_element = element
                swapped_order = True

    return list_to_sort

def timsort(randomised_list: list) -> list:
    randomised_list.sort()
    return randomised_list

def main():
    random_list = generate_list(100)

    start = time.time()
    sorting_algorithm(random_list)
    print(time.time() - start)

    start = time.time()
    timsort(random_list)
    print(time.time() - start)

if __name__ == '__main__':
    main()