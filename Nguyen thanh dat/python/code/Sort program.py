import random
import timeit


def bubble_sort(arr):
    for i in range(0, len(arr) - 1):
        for j in range(0, len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                temp = arr[j + 1]
                arr[j + 1] = arr[j]
                arr[j] = temp

def calculate_runtime(func):
    start_time = timeit.default_timer()
    func
    excecution_time = timeit.default_timer() - start_time
    return excecution_time

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def selection_sort(arr):
    for i in range(0, len(arr)):
        minIndex = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j
        if minIndex != i:
            temp = arr[minIndex]
            arr[minIndex] = arr[i]
            arr[i] = temp

def validate_number(mess):
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

def validate_choice(mess, min, max):
    print(mess)
    while True:
        number = validate_number("Enter a number")
        if number < min or number > max:
            print("You have entered a number out of range")
        else:
            return number

def gen_array(sizeOfArray):
    arr = []
    for i in range(0, sizeOfArray):
        arr.append(random.randint(0, sizeOfArray))
    return arr

def menu():
    number = validate_number("Enter the size of the array")
    new_arr = gen_array(number)
    print("Unsorted array:", new_arr)
    
    while True:
        print("Enter choice in 1-4 to select function")
        print("Enter 1 to sort array by bubble sort")
        print("Enter 2 to sort array by insertion sort")
        print("Enter 3 to sort array by selection sort")
        print("Enter 4 to exit")
        choice = validate_choice("Enter a number in the range 1-4", 1, 4)
        if choice == 1:
            time_excecute = calculate_runtime(bubble_sort(new_arr))
            print(f"Sorted array by bubble sort:{new_arr}Time excecute is {time_excecute}")
        elif choice == 2:
            time_excecute = calculate_runtime(insertion_sort(new_arr))
            print(f"Sorted array by bubble sort:{new_arr}Time excecute is {time_excecute}")
        elif choice == 3:
            time_excecute= calculate_runtime(selection_sort(new_arr))
            print(f"Sorted array by bubble sort:{new_arr}Time excecute is {time_excecute}")
        elif choice == 4:
            return

if __name__ == '__main__':
    menu()
