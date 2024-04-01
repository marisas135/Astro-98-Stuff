#problem 1
import numpy as np

def findEqual(arr):
    equal_rows = arr[(arr == arr[:, 0][:, None]).all(axis=1)]
    return equal_rows

arr = np.array([[1, 1, 1], [1, 2, 3], [2, 2, 2]])
result = findEqual(arr)
print(result)
#i have problems with importing numpy in vs code even after installing it in terminal, so this is what I think may work
    #this function compares each row with its first element and adds the rows with equal elements into a new array


#problem 2

def checkerboard():
    arr = np.zeros((8, 8), dtype=int)
    arr[::2, ::2] = 1
    arr[1::2, 1::2] = 1
    return arr

result = checkerboard()
print(result)
    #first, you can create an  8x8 array with only 0s in it
    #then select alternating elements of odd rows, and set those to 1
    #then select alternating elements of even rows and set them to 1


#problem 3

def spaceBetween(arr):
    result = []
    for word in arr:
        word_with_spaces = ' '.join(list(word))
        result.append(word_with_spaces)
    result_array = np.array(result)
    return result_array

myarr = np.array(['python', 'is', 'cool!'])
result = spaceBetween(myarr)
print(result)

    #created an empty list, iterate over each word in the array, turn the word into a list of characters with spaces between, 
    #and add each spaced word to another list, then convert that to an array

#problem 4

def sorting(matrix):
    sorted_matrix = np.sort(matrix, axis=0)
    return sorted_matrix

a = np.array([[35, 38, 30,  2, 37],
              [42, 38, 35, 30,  2],
              [15, 42, 28, 17, 10],
              [12, 14, 11, 18, 19]])
result = sorting (a)
print (result)

    #the function sorting takes a matrix as input and sorts it along the columns using np.sort
