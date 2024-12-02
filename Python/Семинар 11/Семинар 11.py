import numpy as np

#task1

def double_this(arr):
    return arr * 2

arr = np.array([1, 2, 3, 4])
print(f'#1 {double_this(arr)}')



#task2

def select_even(arr):
    return arr[ arr % 2 == 0 ]

arr = np.array([1, 2, 3, 4])
print(f'#2 {select_even(arr)}')



#task3

#def wipe_even(arr, target_value, in_place):





#task4

def weighted_sum(weights, grades, normalize):

    #1
    grades = np.array([7, 9, 8])
    weights = np.array([0.3, 0.3, 0.4])
    normalize = True
    
    r = np.dot(grades, weights)

    if (normalize == True) and (np.sum(r) != 1):

    
    return np.sum(weights * grades)



print(f'#4.1 {weighted_sum(weights, grades, normalize)}')

#2
grades = np.array([7, 9, 8])
weights = np.array([0.3, 0.3, 0.4])
normalize = False

print(f'#4.2 {weighted_sum(weights, grades, normalize)}')



#task5

def mean_by_gender(grades, genders):
    



grades = np.array([5, 4, 3, 5, 2])
genders = np.array(["female", "male", "male", "female", "male"])

print(f'#5 {mean_by_gender(grades, genders)}')



#task6

def calculate_tax(income):


    income = np.array([])
