"""

@DESC : Bubble sort algorithm using Python
@Performance : Worst-case time complexity - O(n ^ 2), Space complexity - O(1)

"""
import time
import random 

class BubbleSort:

    @staticmethod
    def sort(arr, reverse = False):

        for i in range(len(arr)):

            if reverse:
                for j in range(0, len(arr)- i-1):
                    if arr[j] > arr[j+1]:
                        temp = arr[j+1]
                        arr[j+1] = arr[j]
                        arr[j] = temp
            else:
                for j in range(0, len(arr)- i-1):
                    if arr[j] < arr[j+1]:
                        temp = arr[j+1]
                        arr[j+1] = arr[j]
                        arr[j] = temp

        return arr


if __name__ == "__main__":
    algo = BubbleSort()
    arr = [random.randint(1, 100) for _ in range(10000)]
    start = time.time()
    print(algo.sort(arr, reverse = True))
    print("-"*30)
    print(algo.sort(arr, reverse = False))
    end = time.time()
    print("-"*30)
    print(f"Time Elapsed : {end - start}s")

    
