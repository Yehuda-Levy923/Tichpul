def getNumber(prompt):
 while True:
  try:
   x = float(input(prompt))
   return x
  except ValueError:
   print("Input must be a number!")

def is_valid_triangle(x, y, z):
  return (x + y > z) and (x + z > y) and (y + z > x)

a = getNumber("Enter the first side length: ")
b = getNumber("Enter the second side length: ")
c = getNumber("Enter the third side length: ")

if is_valid_triangle(a, b, c):
 print("correct triangle sides lengths")
else:
 print("not correct triangle sides lengths")



###end of question 1 ###




import math
from myboolfuncs import *
#
# Area calculation program
def rectangleArea(w, h):
     return w*h
#
def circleArea(r):
     return math.pi * r**2
#
def triangleArea(a: float, b: float, c: float) -> float:
    s: int = (a + b + c)/2
    return math.sqrt(s * (s - a) *(s - b) * (s - c))
#
def squareArea(x: float) -> float:
    return x**2
#
def sphereVolume(r: float) -> float:
    return 4/3 * (r**3) * math.pi
#
def squarePyramidArea(a: float, b: float, h: float) -> float:
    return (a * b * h)/3
#

#
# printing the menu options
def prtMenu(shapes):
   for i in range(len(shapes)):
      print (i+1, shapes[i])
   return
#
# main program
#
print ("Welcome to the Area calculation program")
print ("---------------------------------------\n")
# Print out the menu
shapes = ("Triangle", "Rectangle", "square", "Square pyramid", "Circle", "sphere")
while True:
    print ("\nPlease select a shape (press 0 to quit):")
    prtMenu(shapes)
    # Get the user's choice:
    shape: int = input("> ")
    # Calculate the area:
    if shape == "0":
        print("Bye!")
        break
    elif shape == "1":
        a: float = getNumber("Please enter the first side: ")
        b: float = getNumber("Please enter the second side: ")
        c: float = getNumber("Please enter the third side: ")
        area: float = triangleArea(a, b, c)
        print("The area is", area)
        continue
    elif shape == "2":
        height = getNumber("Please enter the height: ")
        width = getNumber("Please enter the width: ")
        area = rectangleArea(width, height)
        print("The area is", area)
    elif shape == "3":
        width = getNumber("Please enter the width: ")
        area: float = squareArea(width)
        print("The area is", area)
        continue
    elif shape == "4":
        height = getNumber("Please enter the height: ")
        width = getNumber("Please enter the width: ")
        length = getNumber("Please enter the length: ")
        Volume = squarePyramidArea(width, length, height)
        print("The Volume is", Volume)
        continue
    elif shape == "5":
        radius = getNumber("Please enter the radius: ")
        area = circleArea(radius)
        print("The area is", area)
        continue
    elif shape == "6":
        radius = getNumber("Please enter the radius: ")
        Volume = sphereVolume(radius)
        print("The Volume is", Volume)
        continue
    else:
         print ("Invalid shape")



###end of question 2 ###



from typing import List, Any, Tuple, Optional
MiddlePair = Optional[List[float]]

# -------------------- Part A --------------------
# Version 1: using sort or sorted
def middle_numbers_sorted(nums: List[float]) -> MiddlePair:
    """receives a list of 4 numbers and returns the 2 middle numbers by size using sorting"""
    if len(nums) != 4:
        print("input list must contain exactly 4 numbers")
        return None

    sorted_nums = sorted(nums)
    return sorted_nums[1:3]

# Version 2: without using sort or sorted
def middle_numbers_no_sort(nums: List[float]) -> MiddlePair:
    """receives a list of 4 numbers and returns the 2 middle numbers by size without full sorting"""
    if len(nums) != 4:
        print("input list must contain exactly 4 numbers")
        return None
    # find minimum and maximum
    try:
        min_num = min(nums)
        max_num = max(nums)
    except ValueError:
        return None

    # find middle elements
    middle_elements = [x for x in nums if x != min_num and x != max_num]

    # handles duplicate cases
    if len(middle_elements) == 2:
        return sorted(middle_elements)
    elif len(middle_elements) < 2 and len(set(nums)) < 4:
        temp_list = list(nums)  # Work on a copy
        try:
            temp_list.remove(min_num)

            if min_num in temp_list:
                temp_list.remove(min_num)
            else:
                temp_list.remove(max_num)

            return sorted(temp_list)
        except ValueError:
            print("problem removing min/max possibly due to unexpected duplicates")
            return None
    else:
        print("could not isolate exactly two middle numbers.")
        return None

# -------------------- Part B --------------------
# generalization for a list of any even length

# Version 1: using sort or sorted
def middle_numbers_sorted_general(nums: List[float]) -> MiddlePair:
    """receives a list of any even length and returns the 2 middle numbers by size using sorting"""
    n = len(nums)
    if n == 0 or n % 2 != 0:
        print("input list must have a non-zero even length")
        return None

    sorted_nums = sorted(nums)
    mid_index_upper = n // 2
    mid_index_lower = mid_index_upper - 1
    return [sorted_nums[mid_index_lower], sorted_nums[mid_index_upper]]

# Version 2: without using sort or sorted
def middle_numbers_no_sort_general(nums: List[float]) -> MiddlePair:
    """receives a list of any even length and returns the 2 middle numbers by size without full sorting"""
    n = len(nums)
    if n == 0 or n % 2 != 0:
        print("input list must have a non-zero even length.")
        return None

    temp_list = list(nums)
    elements_to_remove = n // 2 - 1

    try:
        # find and remove the smaller elements
        for _ in range(elements_to_remove):
            minimum = min(temp_list)
            temp_list.remove(minimum)  # Remove the minimum

        # find the first middle element
        lower_middle = min(temp_list)
        temp_list.remove(lower_middle)

        # find the second middle element
        # reset the list to find upper elements
        temp_list = list(nums)

        # remove smaller elements including the lower middle
        for _ in range(elements_to_remove + 1):
            minimum = min(temp_list)
            temp_list.remove(minimum)

        upper_middle = min(temp_list)

        return [lower_middle, upper_middle]
    except ValueError:
        print("Error during min/remove process, check input or logic.")
        return None
    except IndexError:
        print("Error: Index out of bounds, likely issue with list modification.")
        return None


# -------------------- Part C --------------------
#additional generalization for lists with mixed data types

def extract_numerical_values(mixed_list: List[Any]) -> List[float]:
    """receives a list of values of different types and returns a new list containing only the numerical values"""
    result = []

    for item in mixed_list:
        if isinstance(item, (int, float)):
            result.append(float(item))
        elif isinstance(item, list):
            # Handle nested lists
            for subitem in item:
                if isinstance(subitem, (int, float)):
                    result.append(float(subitem))

    return result

def middle_numbers_mixed_list(mixed_list: List[Any]) -> MiddlePair:
    """receives a list of values of different types and returns the 2 middle numbers by size"""
    numerical_values = extract_numerical_values(mixed_list)
    return middle_numbers_sorted_general(numerical_values)


if __name__ == "__main__":

    #Part A known values
    print("/n --- Part A ---")
    example_a = [100.0, 20.0, 35.0, 40.0]
    print(f"Input: {example_a}")
    print(f"Output: {middle_numbers_sorted(example_a)}")

    # Part B generalization for an even-length list
    print("\n--- Part B  ---")
    b_input = [32.0, 67.0, 40.0, 35.0, 20.0, 100.0]
    print(f"Input: {b_input}")

    res_b_sorted = middle_numbers_sorted_general(b_input)
    res_b_no_sort = middle_numbers_no_sort_general(list(b_input))

    print(f"Middle numbers (using sort): {res_b_sorted}")
    print(f"Middle numbers (without sort): {res_b_no_sort}")

    # Part C generalization for a list with mixed data types
    print("\n--- Part C ---")
    c_input = [100, [20, 35, 'abc'], 40, "my test", 67, 32, 15, 34]
    print(f"Input: {c_input}")

    numerical_values = extract_numerical_values(c_input)
    print(f"Extracted numerical values: {numerical_values}")
    res_c_mixed = middle_numbers_mixed_list(c_input)
    print(f"Middle numbers: {res_c_mixed}\n\n\n")



### end of question 3###


import random

def nihushTest(lotteryNumbers: tuple, gess: tuple) -> tuple:
    score: tuple =()
    for i in range(len(lotteryNumbers)):
        if lotteryNumbers[i] == gess[i]:
            score = score + (lotteryNumbers[i], )
        else:
            score = score + ("X",)
    return score

def main():
    lotteryNumbers: tuple = ()
    gess: tuple = ()
    maxpct: float = 0
    length = random.randint(3, 9)
    for i in range(length):
        lotteryNumbers = lotteryNumbers + (random.randint(1,9),)

    while True:
        gess = input("Enter " + str(length) + " numbers as a guess: ")
        if gess == "-1":
            break
        gess = tuple(map(int, gess.split()))

        result = nihushTest(lotteryNumbers, gess)
        score = (1-result.count("X")/length) * 100

        print(result, score)
        if score > maxpct:
            maxpct = score
        if score == 100:
            print("You wan!")
            break

    print("the numbers were ", lotteryNumbers)
    print("Maximum percent of gesses: ", maxpct)

if __name__ =="__main__":
 print(main())


### end of question 4 ###


def count_data_types(input_list):
    counts = {
        list: 0,
        int: 0,
        float: 0,
        str: 0,
        tuple: 0
    }
    for item in input_list:
        if isinstance(item, list):
            counts[list] += 1
        elif isinstance(item, int):
            counts[int] += 1
        elif isinstance(item, float):
            counts[float] += 1
        elif isinstance(item, str):
            counts[str] += 1
        elif isinstance(item, tuple):
            counts[tuple] += 1
    return counts

def print_counts(counts):
    print(f"Total tuples: {counts[tuple]}")
    print(f"Total lists: {counts[list]}")
    print(f"Total integers: {counts[int]}")
    print(f"Total floats: {counts[float]}")
    print(f"Total strings: {counts[str]}")

if __name__ == "__main__":
    L = [1, 2, 'a', (11, 2, 'b'), [22, 'c'], (33,), ['d'], 'e']
    counts = count_data_types(L)
    print_counts(counts)


### end of question 5 ###
