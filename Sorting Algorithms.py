#!/usr/bin/env python
# coding: utf-8

# In[1]:


def bubble_sort(arr):
    """
    Bubble Sort: 
    - Compares adjacent elements and swaps them if they are in the wrong order.
    - Repeats this process until the array is sorted.
    """
    n = len(arr)

    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def selection_sort(arr):
    """
    Selection Sort: 
    - Finds the minimum element from the unsorted part of the array and moves it to the beginning.
    - Repeats this process for the remaining unsorted elements.
    """
    n = len(arr)

    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

def merge_sort(arr):
    """
    Merge Sort: 
    - Divides the array into two halves, recursively sorts them, and then merges the sorted halves.
    """
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def insertion_sort(arr):
    """
    Insertion Sort:
    - Builds the final sorted array one item at a time by repeatedly moving elements.
    - Each new element is inserted into the correct position among the sorted elements.
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def partition(arr, low, high):
    """
    Partition function for Quick Sort:
    - Selects a pivot element and partitions the array into two sub-arrays
    - All elements less than the pivot are placed before it, and all elements greater are placed after it.
    """
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort(arr, low, high):
    """
    Quick Sort:
    - Divides the array into sub-arrays by selecting a pivot element and partitioning the array around the pivot.
    - Recursively sorts the sub-arrays.
    """
    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)

# Get user input for array
input_str = input("Enter space-separated integers for the array: ")
arr = list(map(int, input_str.split()))

# Get user input for sorting method
sorting_method = input("Enter sorting method (bubble/selection/merge/insertion/quick): ").lower()

# Perform the selected sorting method
if sorting_method == 'bubble':
    bubble_sorted_arr = list(arr)
    bubble_sort(bubble_sorted_arr)
    print("\nBubble Sort:")
    print("Description: Bubble Sort compares adjacent elements and swaps them if they are in the wrong order, repeating this process until the array is sorted.")
    print("Sorted Array:", bubble_sorted_arr)
elif sorting_method == 'selection':
    selection_sorted_arr = list(arr)
    selection_sort(selection_sorted_arr)
    print("\nSelection Sort:")
    print("Description: Selection Sort finds the minimum element from the unsorted part of the array and moves it to the beginning, repeating this process for the remaining unsorted elements.")
    print("Sorted Array:", selection_sorted_arr)
elif sorting_method == 'merge':
    merge_sorted_arr = list(arr)
    merge_sort(merge_sorted_arr)
    print("\nMerge Sort:")
    print("Description: Merge Sort divides the array into two halves, recursively sorts them, and then merges the sorted halves.")
    print("Sorted Array:", merge_sorted_arr)
elif sorting_method == 'insertion':
    insertion_sorted_arr = list(arr)
    insertion_sort(insertion_sorted_arr)
    print("\nInsertion Sort:")
    print("Description: Insertion Sort builds the final sorted array one item at a time by repeatedly moving elements, inserting each new element into the correct position among the sorted elements.")
    print("Sorted Array:", insertion_sorted_arr)
elif sorting_method == 'quick':
    quick_sorted_arr = list(arr)
    quick_sort(quick_sorted_arr, 0, len(quick_sorted_arr) - 1)
    print("\nQuick Sort:")
    print("Description: Quick Sort selects a pivot element, partitions the array around the pivot, and recursively sorts the sub-arrays.")
    print("Sorted Array:", quick_sorted_arr)
else:
    print("Invalid sorting method. Please enter 'bubble', 'selection', 'merge', 'insertion', or 'quick'.")


# In[ ]:




