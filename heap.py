""" Consolidating concepts by implementing heap creation 
Originally by: Wyzzard123
Feel free to make changes."""

# Heap Array Representation Rules:
# for i starting at 1:
# for a node at i, parent node is at = i // 2
# for a node at i, left child node is at i * 2
# for a node at i, right child node is at (i * 2) + 1

def heap_insert(heap, value, type="max"):
    """Insert value at the top of a max or min heap"""
    heap.append(value)
    n = len(heap)
    current_index = n
    current_i = n - 1
    parent_index = current_index // 2
    
    
    # print("not none")
    # print(f"parent_index - 1 is {parent_index-1}")
    # print(f"current index is {current_i}")

    # print(f"heap[parent_index -1] = {heap[parent_index - 1]}; heap[current_i] = {heap[current_i]}")
    
    if type == "max":
        while heap[parent_index - 1] < heap[current_i]:
            print(f"current_index is {current_index}")
            print(f"current i is {current_i}")
            temp_value = heap[parent_index - 1]
            heap[parent_index - 1] = heap[current_i]
            heap[current_i] = temp_value

            current_index //= 2 
            parent_index = current_index // 2
            current_i = current_index - 1
            left_child = current_index * 2
            right_child = (current_index * 2 + 1)
            if current_i == 0:
                break
            else:
                pass
                # print("none")
    elif type == "min":
        while heap[parent_index - 1] > heap[current_i]:
            print(f"current_index is {current_index}")
            print(f"current i is {current_i}")
            temp_value = heap[parent_index - 1]
            heap[parent_index - 1] = heap[current_i]
            heap[current_i] = temp_value

            current_index //= 2 
            parent_index = current_index // 2
            current_i = current_index - 1
            left_child = current_index * 2
            right_child = (current_index * 2 + 1)
            if current_i == 0:
                break
            else:
                pass
                # print("none")

    return heap




def heap_create(array, type="max"):
    """Create max or min heap from a given array in nlogn time"""
    # Start from the left and add
    n = len(array)
    heap = [None] * n
    # print(heap)
    height = 0

    # Max Heap
    if type == "max":
        # starting from 1 to handle this mathematically
        for index in range (1, n + 1):
            parent_index = index // 2 
            left_child = index * 2
            right_child = (index * 2) + 1
            
            # insert index into heap
            heap[index - 1] = array[index - 1]

            
            # -1 to compensate for 0-counting
            if heap[parent_index - 1] is not None:
                current_index = index
                i = index - 1
                current_i = i
                # print("not none")
                # print(f"parent_index - 1 is {parent_index-1}")
                # print(f"current index is {current_i}")

                # print(f"heap[parent_index -1] = {heap[parent_index - 1]}; heap[current_i] = {heap[current_i]}")
                
                
                while heap[parent_index - 1] < heap[current_i]:
                    # print(f"current_index is {current_index}")
                    # print(f"current i is {current_i}")
                    temp_value = heap[parent_index - 1]
                    heap[parent_index - 1] = heap[current_i]
                    heap[current_i] = temp_value

                    current_index //= 2 
                    parent_index = current_index // 2
                    current_i = current_index - 1
                    left_child = current_index * 2
                    right_child = (current_index * 2 + 1)
                    if current_i == 0:
                        break
            else:
                # print("none")
                pass
        # Min Heap
    if type == "min":
        # starting from 1 to handle this mathematically
        for index in range (1, n + 1):
            parent_index = index // 2 
            left_child = index * 2
            right_child = (index * 2) + 1
            
            # insert index into heap
            heap[index - 1] = array[index - 1]

            
            # -1 to compensate for 0-counting
            if heap[parent_index - 1] is not None:
                current_index = index
                i = index - 1
                current_i = i
                # print("not none")
                # print(f"parent_index - 1 is {parent_index-1}")
                # print(f"current index is {current_i}")

                # print(f"heap[parent_index -1] = {heap[parent_index - 1]}; heap[current_i] = {heap[current_i]}")
                
                
                while heap[parent_index - 1] > heap[current_i]:
                    # print(f"current_index is {current_index}")
                    # print(f"current i is {current_i}")
                    temp_value = heap[parent_index - 1]
                    heap[parent_index - 1] = heap[current_i]
                    heap[current_i] = temp_value

                    current_index //= 2 
                    parent_index = current_index // 2
                    current_i = current_index - 1
                    left_child = current_index * 2
                    right_child = (current_index * 2 + 1)
                    if current_i == 0:
                        break
            else:
                pass
                # print("none")

    return heap
                
# array = [30, 123, 12, 321, 10, 442, 13, 320, 111, 310, 11, 1]
# # array = [1, 2, 3, 4, 5]
# heap = heap_create(array, "max")
# print("array is", array)
# print(heap)

# heap_insert(heap,554)
# print(heap)

    

    

def heapify(array, type=max):
    """Create a max or min heap from a given array in logn time."""
    #TODO
    pass
    

def heap_delete(heap, type="max"):
    """Delete from top of a max or min heap in logn time. Returns the deleted value (which can be used in heap sort)."""

    deleted_element = heap[0] # Stores deleted element to be returned

    n = len(heap)
    current_index = 1
    current_i = current_index - 1

    left_child = current_index * 2
    right_child = (current_index * 2) + 1

    left_child_i = left_child - 1
    right_child_i = right_child - 1
    has_left_child = True
    has_right_child = True
    

    last_element_index = n - 1

    if right_child_i > last_element_index:
        has_right_child = False
    if left_child_i > last_element_index:
        has_left_child = False

    # Replace deleted element with last element
    heap[current_i] = heap[last_element_index]
    
    # Remove last element of heap.
    heap.pop()
    n = len(heap)
    last_element_index = n - 1

    if right_child_i > last_element_index:
        has_right_child = False
    if left_child_i > last_element_index:
        has_left_child = False
    if type == "max":
        # Check and swap elements below
        # Condition is if it has a left child because this is a complete binary tree
        while has_left_child is True:
            if has_right_child is True:
                # Check which child node is greater
                if heap[right_child_i] > heap[left_child_i]:
                    # Check if greater child node is greater than current node
                    if heap[right_child_i] > heap[current_i]:
                        
                        temp_value = heap[right_child_i]
                        heap[right_child_i] = heap[current_i]
                        heap[current_i] = temp_value

                        # + 1 because the current_index is now the right node
                        current_index = (current_index * 2) + 1
                        current_i = current_index - 1
                        left_child = current_index * 2
                        left_child_i = left_child - 1
                        right_child = (current_index * 2) + 1
                        right_child_i = right_child - 1
                    # Break if the sorting is done
                    else:
                        break
                # This currently will also swap the left child by default if the two child nodes are equal
                elif  heap[left_child_i] >= heap[right_child_i]:

                    if heap[left_child_i] > heap[current_i]:
                        
                        temp_value = heap[left_child_i]
                        heap[left_child_i] = heap[current_i]
                        heap[current_i] = temp_value

                        current_index *= 2 
                        current_i = current_index - 1
                        left_child = current_index * 2
                        left_child_i = left_child - 1
                        right_child = (current_index * 2 + 1)
                        right_child_i = right_child - 1
                    # Break if the sorting is done
                    else:
                        break
            # In this condition, has_left_child is true, but has_right_child is false
            else:
                if heap[left_child_i] > heap[current_i]:
                        
                    temp_value = heap[left_child_i]
                    heap[left_child_i] = heap[current_i]
                    heap[current_i] = temp_value

                current_index *= 2 
                current_i = current_index - 1
                left_child = current_index * 2
                left_child_i = left_child - 1
                right_child = (current_index * 2 + 1)
                right_child_i = right_child - 1
            
            # Reset has_right_child and has_left_child for loop
            if right_child > last_element_index:
                has_right_child = False
            if left_child > last_element_index:
                has_left_child = False
                break
    elif type == "min":
        # Check and swap elements below
        # Condition is if it has a left child because this is a complete binary tree
        while has_left_child is True:
            if has_right_child is True:
                # Check which child node is smaller
                if heap[right_child_i] < heap[left_child_i]:
                    # Check if smaller child node is greater than current node
                    if heap[right_child_i] < heap[current_i]:
                        
                        temp_value = heap[right_child_i]
                        heap[right_child_i] = heap[current_i]
                        heap[current_i] = temp_value

                        # + 1 because the current_index is now the right node
                        current_index = (current_index * 2) + 1
                        current_i = current_index - 1
                        left_child = current_index * 2
                        left_child_i = left_child - 1
                        right_child = (current_index * 2) + 1
                        right_child_i = right_child - 1
                    # Break if the sorting is done
                    else:
                        break
                # This currently will also swap the left child by default if the two child nodes are equal
                elif  heap[left_child_i] <= heap[right_child_i]:

                    if heap[left_child_i] < heap[current_i]:
                        
                        temp_value = heap[left_child_i]
                        heap[left_child_i] = heap[current_i]
                        heap[current_i] = temp_value

                        current_index *= 2 
                        current_i = current_index - 1
                        left_child = current_index * 2
                        left_child_i = left_child - 1
                        right_child = (current_index * 2 + 1)
                        right_child_i = right_child - 1
                    # Break if the sorting is done
                    else:
                        break
            # In this condition, has_left_child is true, but has_right_child is false
            else:
                if heap[left_child_i] < heap[current_i]:
                        
                    temp_value = heap[left_child_i]
                    heap[left_child_i] = heap[current_i]
                    heap[current_i] = temp_value

                current_index *= 2 
                current_i = current_index - 1
                left_child = current_index * 2
                left_child_i = left_child - 1
                right_child = (current_index * 2 + 1)
                right_child_i = right_child - 1
            
            # Reset has_right_child and has_left_child for loop
            if right_child > last_element_index:
                has_right_child = False
            if left_child > last_element_index:
                has_left_child = False
                break
        
        

    return deleted_element


# heap_delete(heap)    
# print(heap)

    

def heap_sort_from_heap(heap, type="max"):
    """Return a sorted array in nlogn time by deleting from top of heap."""
    temp_heap = []
    temp_heap += heap
    # print("Temp =",temp_heap)
    n = len(heap) 
    sorted_heap = [None] * n

    for i in range(n):
        
        sorted_heap[n - 1 - i] = heap_delete(heap)
    

    # Copies the old values back into heap to ensure that the heap itself is not changed
    # print("Temp =", temp_heap)
    heap += temp_heap
    return(sorted_heap)

# # You must reassign the heap to another variable
# sorted_heap = heap_sort_from_heap(heap)

# # Heap is sorted
# print(sorted_heap)

# # Heap is replicated into place
# print(heap)

def heap_sort_from_unsorted(array, reverse="false"):
    """Return a sorted array in nlogn time by deleting from top of heap. This does not modify the original array, and must be assigned. Takes second parameter of reverse which can be 'true' or 'false'"""

    if reverse == "false" or reverse == "False":
        heap = heap_create(array, "max")
        print("new max heap: \n", heap)
        # print("Temp =",temp_heap)
        n = len(heap) 
        sorted_array = [None] * n

        for i in range(n):
            
            sorted_array[n - 1 - i] = heap_delete(heap, "max")
            # print(f"heap now for i = {i}: {heap}")
            # print(f"sorted array now for i = {i}: {sorted_array}")
    if reverse == "true" or reverse == "reversed" or reverse == "True" or reverse == "Reversed":
        heap = heap_create(array, "min")
        print("new min heap: \n", heap)
        # print("Temp =",temp_heap)
        n = len(heap) 
        sorted_array = [None] * n

        for i in range(n):
            
            sorted_array[n - 1 - i] = heap_delete(heap, "min")
            # print(f"heap now for i = {i}: {heap}")
            # print(f"sorted array now for i = {i}: {sorted_array}")

    # Copies the old values back into heap to ensure that the heap itself is not changed
    # print("Temp =", temp_heap)
    return(sorted_array)

array2 = [1, 3, 4, 51,3,53,45 ,234,5 ,32,534, 213, 21, 214124213, 1231, 1231, 123213, 5136, 1324, 634, 634, 632, 246, 4253, 632, 3, 4, 51, 231, 1251, 23, 12, 3115, 122, 1231, 232, 111, 321, 421, 231, 24, 123, 41241, 23, 12312, 123, 12,3 ,123 ,2132,1,32 ,123,213,12, 421,55, 31,5,325 ,23, 53,215,23,523,15,532,6,783,73,45 ,3,53,45 ,234,5 ,32,534, 213, 21, 214124213, 1231, 1231, 123213, 5136, 1324, 634, 634, 632, 246, 4253, 632, 3, 4, 51, 231, 1251, 23, 12, 3115, 122, 1231, 232, 111, 321, 421, 231, 24, 123, 41241, 23, 12312, 123, 12,3 ,123 ,2132,1,32 ,123,213,12, 421,55, 31,5,325 ,23, 53,215,23,523,15,532,6,783,73,45 ,3,53,45 ,234,5 ,32,534, 213, 21, 214124213, 1231, 1231, 123213, 5136, 1324, 634, 634, 632, 246, 4253, 632]

# array2 = [52, 23, 1, 52, 1, 23, 12, 21, 1]

import time

print("Sorting by max")
print("original: \n", array2)

t0 = time.time()
sorted_array = heap_sort_from_unsorted(array2, "false")
t1 = time.time()
print(f"b Time for heapsort max is: %f" % (t1-t0))
print("sorted: \n", sorted_array)

print("Sorting by min")
print("original: \n", array2)
t0 = time.time()
sorted_array = heap_sort_from_unsorted(array2, "true")
t1 = time.time()
print(f"b Time for heapsort min is: %f" % (t1-t0))
print("sorted: \n", sorted_array)

t0 = time.time()
python_sorted_array = sorted(array2)
t1 = time.time()
print(f"b Time for python sort is: %f" % (t1-t0))
print("sorted: \n", python_sorted_array)

t0 = time.time()
python_sorted_array_reversed = sorted(array2, reverse=False)
t1 = time.time()
print(f"b Time for python sort reversed is: %f" % (t1-t0))
print("sorted: \n", python_sorted_array_reversed)

# array3 = [3115, 1251, 2132, 421, 1, 534, 321, 55, 325, 1231, 783, 234, 421, 123, 232, 51, 31, 231, 215, 523, 532, 123, 73, 53, 123, 111, 231, 23, 32, 213, 12, 1, 32, 24, 5, 12, 23, 53, 123, 4, 23, 15, 23, 6, 122, 12, 45, 3, 3, 3, 45, 5]

# array3 = [10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 20, 20, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 20, 20, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 20, 20]
# array3 = [140, 130, 120, 110, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 23, 180, 170, 160, 200, 190,  150 ]
# heap3 = heap_sort_from_unsorted(array3)


# print(heap3)