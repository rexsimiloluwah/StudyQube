"""

@DESC : Insertion sort algorithm using Python
@Performance : Worst-case time complexity - O(n ^ 2), Worst-case space complexity - O(1)

"""
import time
import random

class InsertionSort:

    sorted_arr = []

    @staticmethod
    def sort(arr, reverse = False):
        """
            @desc - Function for sorting the list
            Args - arr (list), reverse (boolean - True for descending and False for ascending)
            Returns - Sorted list in the specific order
        """

        for index in range(len(arr)):

            currentElement = arr[index]
            
            # When a new element is added

            if(reverse):
                while (index > 0) and (arr[index - 1] < currentElement ):
                    arr[index] = arr[index - 1]
                    index -= 1

            while (index > 0) and (arr[index - 1] > currentElement ):
                arr[index] = arr[index - 1]
                index -= 1

            arr[index] = currentElement

        return arr

if __name__ == "__main__":
    algo = InsertionSort()
    start = time.time()
    arr = [random.randint(0,1000) for i in range(100)] #Random unordered array with 100 elements
    print("Ascending Order :-", end = "\n")
    print(algo.sort(arr))
    print("Descending Order :-", end = "\n")
    print(algo.sort(arr, reverse = True))
    end = time.time()
    print("-"*30)
    print(f"Time Elapsed - {end - start}s")

