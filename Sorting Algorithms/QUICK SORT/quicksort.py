"""

@DESC : Quick sort algorithm using Python
@Performance : Worst-case time complexity - O(n ^ 2), Space complexity - O(log(n))

"""
import random
import time

class QuickSort:

    def __init__(self):
        pass

    def partition_list(self, arr, low, high):

        # Selecting the pivot as the final element (arr[high])
        pivot = arr[high]
        i = low - 1

        # Partitioning technique - All elements smaller than the pivot are placed on the left side and all greater elements are placed on the right side
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
        
        arr[i+1], arr[high] = pivot, arr[i+1]
        return(i+1)

    def quick_sort(self, arr,low, high):
        
        #Base case for recursion
        if low >= high:
            return ;

        # i is where the pivot is currently
        pivot_idx = self.partition_list(arr, low, high)

        # For sorting the left sub-part
        self.quick_sort(arr, low, pivot_idx -1)

        # For sorting the right sub-part
        self.quick_sort(arr, pivot_idx+1, high)
        

if __name__ == "__main__":

    q = QuickSort()
    arr = [random.randint(1, 10000) for _ in range(5000)]
    start = time.time()
    q.quick_sort(arr, 0, len(arr) -1)
    print(arr)
    end = time.time()
    print(f"Time Elapsed - {end - start} s")