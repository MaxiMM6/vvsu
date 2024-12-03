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
    total_weight = np.sum(weights)
    
    if (normalize == True) and (total_weight != 1):
        weights = weights / total_weight

    return np.dot(weights, grades)

#1
weights = np.array([1, 2, 3, 4])
grades = np.array([1, 5, 3, 2])
normalize = True

print(f'#1 {weighted_sum(weights, grades, normalize)}')

#2
weights = np.array([1, 2, 3, 4])
grades = np.array([1, 5, 3, 2])
normalize = False

print(f'#2 {weighted_sum(weights, grades, normalize)}')



#task5

def mean_by_gender(grades, genders):

    male_grades = grades[ genders == 'male' ]
    female_grades = grades[ genders == 'female' ]

    male_mean = np.mean(male_grades)
    female_mean = np.mean(female_grades)

    result = {'male' : float(male_mean), 'female' : float(female_mean)}
    return result

grades = np.array([5, 4, 3, 5, 2])
genders = np.array(["female", "male", "male", "female", "male"])

print(f'#5 {mean_by_gender(grades, genders)}')



#task6

def calculate_tax(income):
    pass






income = np.array([150] * 12)
print(f'#6 {calculate_tax(income)}')