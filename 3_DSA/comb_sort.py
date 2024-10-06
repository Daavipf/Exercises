import random

def get_new_step(step):
    step = (step * 10) // 13
    if step < 1:
        return 1
    return step

def sort(array):
    size = len(array)
    step = size
    swapped = True
    while step != 1 or swapped:
        step = get_new_step(step)
        swapped = False
        for i in range(0, size - step):
            if array[i] > array[i+step]:
                array[i], array[i+step] = array[i+step], array[i]
                swapped = True

array = [num for num in range(1000000)]
random.shuffle(array)
sort(array)
