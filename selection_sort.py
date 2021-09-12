'''
Time Complexity best, average, worst = O(n^2)
Space Complexity O(1)
Algorithm used to sort a sequence of numbers, using a linear search. The smallest value is swapped with the leftmost value.
'''


def selection_sort(sequence):
    size = len(sequence)
    
    #Traverse through the unsorted array (sequence)
    for i in range(size):
        #Find the minimum element in the unsorted array (sequence)
        minimum_element = i
        for j in range(i + 1, size):
            if sequence[minimum_element] > sequence[j]:
                minimum_element = j
        #swap the first element with the minimum element
        sequence[i], sequence[minimum_element] = sequence[minimum_element], sequence[i]
    return sequence



unsorted_array = [64,25,12,22,11]
sorted_array = selection_sort(unsorted_array)


for i in range(len(sorted_array)):
    print(sorted_array[i], end=' ') 
print()
