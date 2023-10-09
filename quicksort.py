import random as rnd

def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivotIndex = rnd.randint(0, len(arr) - 1)
        lower = list(filter(lambda el: el <= arr[pivotIndex], arr[:pivotIndex] + arr[pivotIndex + 1:]))
        higher = list(filter(lambda el: el > arr[pivotIndex], arr[:pivotIndex] + arr[pivotIndex + 1:]))
        return quicksort(lower) + [arr[pivotIndex]] + quicksort(higher)


arr = input().split(" ")
arr = list(map(lambda el: int(el), arr))
print(quicksort(arr))


