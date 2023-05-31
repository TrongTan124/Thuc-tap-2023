import random
import timeit

def bubbleSort(arr):
    start_time = timeit.default_timer()
    for i in range(0, len(arr) - 1):
        for j in range(0, len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                temp = arr[j + 1]
                arr[j + 1] = arr[j]
                arr[j] = temp
    excecution_time = timeit.default_timer() - start_time
    return excecution_time
def insertionSort(arr):
    start_time = timeit.default_timer()

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    excecution_time = timeit.default_timer() - start_time
    return excecution_time


def selectionSort(arr):
    start_time = timeit.default_timer()

    for i in range(0, len(arr)):
        minIndex = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j
        if minIndex != i:
            temp = arr[minIndex]
            arr[minIndex] = arr[i]
            arr[i] = temp
    excecution_time = timeit.default_timer() - start_time
    return excecution_time


def validateNumber(mess):
    print(mess)
    while True:
        try:
            number = int(input())
            if number < 0:
                print("You have entered a number larger than zero!")
            else:
                return number
        except ValueError:
            print("You must enter a number")

def validateChoice(mess, min, max):
    print(mess)
    while True:
        number = validateNumber("Enter a number")
        if number < min or number > max:
            print("You have entered a number out of range")
        else:
            return number

def genRanArray(sizeOfArray):
    arr = []
    for i in range(0, sizeOfArray):
        arr.append(random.randint(0, sizeOfArray))
    return arr

def menu():
    number = validateNumber("Enter the size of the array")
    new_arr = genRanArray(number)
    print("Unsorted array:", new_arr)
    
    while True:
        print("Enter choice in 1-4 to select function")
        print("Enter 1 to sort array by bubble sort")
        print("Enter 2 to sort array by insertion sort")
        print("Enter 3 to sort array by selection sort")
        print("Enter 4 to exit")
        choice = validateChoice("Enter a number in the range 1-4", 1, 4)
        if choice == 1:
            time_excecute = bubbleSort(new_arr)
            print("Sorted array by bubble sort:", new_arr, " Time excecute is ", time_excecute)
        elif choice == 2:
            time_excecute = insertionSort(new_arr)
            print("Sorted array by insertion sort:", new_arr," Time excecute is ", time_excecute)
        elif choice == 3:
            time_excecute= selectionSort(new_arr)
            print("Sorted array by selection sort:", new_arr," Time excecute is ", time_excecute)
        elif choice == 4:
            return

if __name__ == '__main__':
    menu()
