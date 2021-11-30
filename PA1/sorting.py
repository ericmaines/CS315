# Project Assignment 1 - CS315
# Erin Maines - 912273694
# 27 September, 2021
import csv
import sys
import pdb
import time
import math

quicksort_count = 0
mergesort_count = 0

def open_csv(file_name):
    master_list = []
    with open(file_name, newline='') as csv_file:
            unsorted_list = csv.reader(csv_file, delimiter=',', quotechar='|')
            for row in unsorted_list:
                master_list += [row]
    return master_list

def sort_list(unsorted_list):
    cleaned_list = cleanup_list(unsorted_list)
    sorted_list = insertion_sort(cleaned_list)
    call_quick_sort(cleaned_list)
    call_merge_sort(cleaned_list)
    return sorted_list

def cleanup_list(uns_list):
    cleaned_list = []
    for entry in uns_list:
        cleaned_list.append(entry[1])
    cleaned_list.pop(0) #Remove the first element -- aka header to csv
    return cleaned_list

def call_merge_sort(cleaned_list):
    global mergesort_count
    start_time = time.time()
    merge_sort(cleaned_list,0)
    expected = len(cleaned_list) * math.log(len(cleaned_list),2) //1
    print("Merge Sort Comparisons: %s" % mergesort_count)
    print("Expected %s comparisons - O(nlogn)" % expected)
    print("Done in %s seconds" % (time.time()-start_time))


def merge_sort(A,c):
    global mergesort_count

    if len(A) <= 1:
        return A

    mid   = len(A)//2
    left  = A[:mid]
    right = A[mid:]

    merge_sort(left, c)
    merge_sort(right, c)

    left_index  = 0
    right_index = 0
    main_index  = 0

    while left_index < len(left) and right_index < len(right):
        mergesort_count += 1
        if right[right_index] < left[left_index]:
            mergesort_count += 1
            A[main_index] = right[right_index]
            right_index += 1
            main_index  += 1
        else:
            A[main_index] = left[left_index]
            left_index += 1
            main_index += 1

    while left_index < len(left):
        mergesort_count += 1
        A[main_index] = left[left_index]
        left_index += 1
        main_index += 1

    while right_index < len(right):
        mergesort_count += 1
        A[main_index] = right[right_index]
        right_index += 1
        main_index  += 1

def insertion_sort(uns_list):
    count = 0
    start_time = time.time()
    for i in range(1, (len(uns_list)-1)):
        key = uns_list[i]
        #Insert A[j] into the sorted sequence
        j = i - 1
        count += 1
        while j >= 0 and uns_list[j] > key:
            count += 1
            uns_list[j+1] = uns_list[j]
            j -= 1
        uns_list[j+1] = key

    expected = len(uns_list) * len(uns_list)
    print("Insertion Sort Comparisons: ",count)
    print("Expected %s comparisons - O(n^2)" % expected )
    print("Done in %s seconds" % (time.time()-start_time))
    return uns_list

def call_quick_sort(unsorted_list):
    global quicksort_count
    start_time = time.time()
    r = len(unsorted_list) #Pivot
    p = 0                  #Start
    count = quick_sort(unsorted_list, p, r-1) 
    expected = (r * math.log(r, 2))//1
    print("Quicksort Comparisons:", quicksort_count)
    print("Expected %s comparisons - O(nlogn) " % expected)
    print("Done in %s seconds" % (time.time()-start_time))

def quick_sort(A,p,r):
    if len(A) == 1:
        return A
    if p < r:
            q = partition(A,p,r)
            quick_sort(A,p,q-1)
            quick_sort(A,q+1,r)

def partition(A,p,r):
    global quicksort_count
    i = p - 1
    pivot = A[r]

    for j in range(p,r):
        if A[j] <= pivot:
            quicksort_count += 1
            i += 1
            A[i], A[j] = A[j], A[i]

    A[i+1], A[r] = A[r], A[i+1]
    return(i+1)

def binary_search(A,v):
    if len(A) == 1:
        return A[0] == v
    mid = len(A) //2
    if A[mid] > v:
        return binary_search(A[:mid], v)
    elif A[mid] < v:
        return binary_search(A[mid+1:], v)
    else:
        return True


def run_binary_search(A):
    bin_s = input("Do a binary search? (Y/N) ")
    if bin_s.capitalize() == "Y":
        pwr_lvl = input("For what power level would you like to search? ")
        if binary_search(A, pwr_lvl):
            print("Power Level: %s was found!" % pwr_lvl)
        else:
            print("Power Level: %s was not found :( " % pwr_lvl)
    else:
        print("Goodbye!")

def main():
    if sys.argv[1]:
        file_name = sys.argv[1]
        unsorted_list = open_csv(file_name)
        sorted_list = sort_list(unsorted_list)
        run_binary_search(sorted_list)

if __name__ == "__main__":
    main()
