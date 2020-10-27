"""

@DESC : Merge sort algorithm using Python
@Performance : Worst-case time complexity - O(n * log(n)), Space complexity - O(n)

"""
import random
import time

class MergeSort:

    def __init__(self, reverse = False):
        self.reverse = reverse
    
    def merge_sort(self, arr):
        """
            @desc - This function recursively sorts the sub-arrays and calls the mergeHalves function also to merge sub-arrays
            Args - left_index (int), right_index (int)
        """
        # Base condition for recursion
        if (len(arr) <= 1):
            return arr;

        mid = (len(arr))//2  # Incase of odd numbers to produce integers
        left_arr = self.merge_sort(arr[:mid])
        right_arr = self.merge_sort(arr[mid:])

        
        return self.mergeHalves(left_arr, right_arr)

    def mergeHalves(self,left_arr, right_arr):
        """
            @desc - This function is used to merge halves (sub-arrays) gotten from the main array
        """

        left_arr_index = 0
        right_arr_index = 0

        temp = [] #stores the result

        while left_arr_index < len(left_arr) and right_arr_index < len(right_arr):

            if not self.reverse:

                if left_arr[left_arr_index] < right_arr[right_arr_index]: #Since we are dealing with ascending order
                    temp.append(left_arr[left_arr_index])
                    left_arr_index += 1

                else:
                    temp.append(right_arr[right_arr_index])
                    right_arr_index += 1

            else:
                if left_arr[left_arr_index] > right_arr[right_arr_index]: #Since we are dealing with ascending order
                    temp.append(left_arr[left_arr_index])
                    left_arr_index += 1

                else:
                    temp.append(right_arr[right_arr_index])
                    right_arr_index += 1


            
        temp.extend(left_arr[left_arr_index:])
        temp.extend(right_arr[right_arr_index:])

        return temp


if __name__ == "__main__":
    arr = [random.randint(0, 10000) for _ in range(1000)]
    start = time.time()
    mergesort = MergeSort(reverse = False)
    print(mergesort.merge_sort(arr))
    end = time.time()

    print("-"*50)
    print(f"Time Elapsed - {end -start} s")

