def input_Array():
    n = int(input("Nhập số lượng phần tử trong mảng: "))
    arr = []
    for i in range(n):
        value = int(input("Nhập phần tử thứ {}: ".format(i + 1)))
        arr.append(value)
    return arr

def output_Array(arr):
    print(str(arr))  

arr_test = [1, 7, 4, 1, 10, 9, -2]

#bumblesort
def bumblesort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            #compare two element continuous
            if arr[j] > arr[j + 1]:
                #swap value two element
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

#quicksort
def quicksort(arr):
	if len(arr) <= 1:
		return arr
	else:
        # pivot of array
		pivot = arr[0] 
        #all element small than pivot
		left = [x for x in arr[1:] if x < pivot]
        #all element big than pivot
		right = [x for x in arr[1:] if x >= pivot]
        # call recursive arr left, add pivot to array, call recursive array right
		return quicksort(left) + [pivot] + quicksort(right)

#insertionsort
def insertionsort(arr):
    #check length array less than or equal 1 then return array
    if (n := len(arr)) <= 1:
      return
    n = len(arr)
    for i in range(1,n):
        #key in the loop
        key = arr[i] 
        j = i - 1
        #if index less than 0 stop while do and check key less than elements before or not
        while (j >= 0 and key < arr[j]):
            arr[j+1]=arr[j]
            #back index 1 point
            j = j - 1
        #return value to element index i in the loop
        arr[j+1] = key
    return arr

#mergesort
def mergesort(arr):
    #check length array less than or equal 1 then return array
    if (len(arr) <= 1):
        return arr
    #get middle element of array
    mid = len(arr) // 2
    #get array from element 0 to middle-1
    left = arr[0:mid]
    #get array from element middle to len(arr)-1
    right = arr[mid:len(arr)]
    #call recursive with left array
    mergesort(left)
    #call recursive with right array 
    mergesort(right)
    #get method megre two array
    arr = merge(left, right)
    return arr

def merge(left, right):
    result = []
    i = 0
    j = 0
    
    #check index left and right array
    while (i < len(left) and j < len(right)):
        if (left[i] <= right[j]):
            result.append(left[i])
            i+=1
        else: 
            result.append(right[j])
            j+=1
    #extend element remaining left array
    result.extend(left[i:])
    #extend element remaining right array
    result.extend(right[j:])
    return result


#selection sort
def selectionsort(arr):
    for index in range(len(arr)):
        #get index min in each loop
        min = index
        for j in range(index+1, len(arr)):
            if (arr[index] > arr[j]):
                #swap value 2 element
                arr[index],arr[j] = arr[j],arr[index]
    return arr

arr = input_Array()
arr = selectionsort(arr)
output_Array(arr)
    