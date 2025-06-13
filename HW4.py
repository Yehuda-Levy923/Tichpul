## Yehuda Levy 332300433

# question 1

def proj_times(file_name):
    """
    function that gets project data and finds time diff between planned and actual for each stage
    """
    # get project info using provided function
    project_data = info_proj_get(file_name)

    def calculate_time_diff(stage_data):
        """helper that finds time diff recursively"""
        if not stage_data:
            return []

        stage_info, substages = stage_data[0], stage_data[1]
        stage_name, planned_time, actual_time = stage_info
        time_diff = actual_time - planned_time

        # go over substages recursively
        processed_substages = [calculate_time_diff(substage) for substage in substages]

        return [[stage_name, time_diff], processed_substages]

    return [calculate_time_diff(stage) for stage in project_data]


def proj_time_cost(file_name, cost_per_time_unit):
    """
    function that calculates project total times and costs
    returns planned actual and diff in time and cost
    """
    project_data = info_proj_get(file_name)

    def extract_times(stage_data):
        """helper to get planned and actual from top level"""
        stage_info = stage_data[0]
        return stage_info[1], stage_info[2]

    # get all time pairs
    time_pairs = [extract_times(stage) for stage in project_data]

    # calc totals
    total_planned = sum(planned for planned, actual in time_pairs)
    total_actual = sum(actual for planned, actual in time_pairs)
    time_diff = total_actual - total_planned

    # calc costs
    planned_cost = total_planned * cost_per_time_unit
    actual_cost = total_actual * cost_per_time_unit
    cost_diff = actual_cost - planned_cost

    return ((total_planned, planned_cost), (total_actual, actual_cost), (time_diff, cost_diff))


# question 2

def reverseList(lst):
    """
    function that reverses list recursively also works on nested stuff
    """
    if not isinstance(lst, (list, tuple)):
        return lst

    # reverse and apply recursively
    reversed_elements = [reverseList(item) for item in lst[::-1]]

    return type(lst)(reversed_elements)


def reverse_list_interface():
    """
    function to get list from user and reverse it
    """
    user_input = input("Enter a list: ")
    original_list = eval(user_input)
    reversed_result = reverseList(original_list)
    print(reversed_result)


# question 3

def isPalindrome(lst):
    """
    checks if list is same forward and backward
    """
    return lst == reverseList(lst)


def palindrome_interface():
    """
    gets list from user and tells if palindrome
    """
    user_input = input("Enter a list: ")
    input_list = eval(user_input)

    if isPalindrome(input_list):
        print("It is a palindrome")
    else:
        print("It is not a palindrome")


# question 4

def sieve_of_eratosthenes(n):
    """
    sieve method to get primes up to n using list comp
    """
    if n < 2:
        return []

    candidates = list(range(2, n + 1))

    def filter_multiples(primes, remaining):
        """helper that filters out multiples"""
        if not remaining:
            return primes

        prime = remaining[0]
        if prime * prime > n:
            return primes + remaining

        new_remaining = [x for x in remaining[1:] if x % prime != 0]
        return filter_multiples(primes + [prime], new_remaining)

    return filter_multiples([], candidates)


def twinp(n):
    """
    finds all twin primes from 1 to n returns as dict
    """
    if n <= 1:
        return {}

    primes = sieve_of_eratosthenes(n)

    twin_pairs = [(p, p + 2) for p in primes if p + 2 in primes and p + 2 <= n]

    return dict(twin_pairs)


def twin_primes_interface():
    """
    gets number from user and shows twin primes
    """
    n = int(input("Enter a Natural number n: "))

    if n <= 0:
        print("ERROR: Input number is incorrect!")
        return

    twin_primes = twinp(n)

    for first, second in twin_primes.items():
        print(first, second)


# question 5 - dictionary combination functions

def get_shared_keys(d1, d2, d3):
    """gets keys shared in 2 or more dicts"""
    all_keys = lambda d: set(d.keys())
    shared_12 = lambda: all_keys(d1) & all_keys(d2)
    shared_13 = lambda: all_keys(d1) & all_keys(d3)
    shared_23 = lambda: all_keys(d2) & all_keys(d3)
    shared_all = lambda: all_keys(d1) & all_keys(d2) & all_keys(d3)

    return shared_12() | shared_13() | shared_23()


def get_unique_keys(d1, d2, d3):
    """gets keys that only show in one dict"""
    all_keys = lambda d: set(d.keys())
    all_combined = all_keys(d1) | all_keys(d2) | all_keys(d3)
    shared = get_shared_keys(d1, d2, d3)

    return all_combined - shared


def dicts3add(d1, d2, d3):
    """
    combines three dicts shared keys get tuple of values unique keys stay same
    """
    result = {}

    shared_keys = get_shared_keys(d1, d2, d3)
    unique_keys = get_unique_keys(d1, d2, d3)

    for key in shared_keys:
        values = []
        if key in d1:
            values.append(d1[key])
        if key in d2:
            values.append(d2[key])
        if key in d3:
            values.append(d3[key])
        result[key] = tuple(values)

    for key in unique_keys:
        if key in d1:
            result[key] = d1[key]
        elif key in d2:
            result[key] = d2[key]
        elif key in d3:
            result[key] = d3[key]

    return result


def dict_combination_interface():
    """
    gets three dicts from user and combines them
    """

    def safe_eval_dict(input_str):
        """eval input safely must be dict"""
        result = eval(input_str)
        if not isinstance(result, dict):
            return None
        return result

    dict1_input = input("Enter a dictionary: ")
    dict1 = safe_eval_dict(dict1_input)

    dict2_input = input("Enter a dictionary: ")
    dict2 = safe_eval_dict(dict2_input)

    dict3_input = input("Enter a dictionary: ")
    dict3 = safe_eval_dict(dict3_input)

    if dict1 is None or dict2 is None or dict3 is None:
        print("ERROR: Input is incorrect!")
        return

    combined_dict = dicts3add(dict1, dict2, dict3)
    print(sorted(combined_dict.items()))


# helper for question 1 (assumes this function is given)

def info_proj_get(file_name):
    """
    mock function to simulate project file input
    """
    return [[['a1', 10, 12], []], [['a2', 13, 18], [[['a21', 6, 8], []], [['a22', 7, 10], []]]], [['a3', 3, 7], []]]


# testing section
if __name__ == "__main__":
    print("Testing Project Functions:")
    print("proj_times result:", proj_times("test.txt"))
    print("proj_time_cost result:", proj_time_cost("test.txt", 1000.0))

    print("\nTesting List Reversal:")
    test_list = [("abc", 1), 5.9, [[1, 2, 3, [6], "a"], 9.1]]
    print("Original:", test_list)
    print("Reversed:", reverseList(test_list))

    print("\nTesting Palindrome Check:")
    palindrome_test = [1, 2, 3, 2, 1]
    print("Is palindrome:", isPalindrome(palindrome_test))

    print("\nTesting Twin Primes:")
    print("Twin primes up to 20:", twinp(20))

    print("\nTesting Dictionary Combination:")
    d1 = {2: 'bc', 3: (34, 2)}
    d2 = {4: 'gg', 2: (7, 'f'), 5: 'd'}
    d3 = {5: (2, 6, 'def'), 7: 'abc', 8: (2,), 2: (5, 7, 8)}
    print("Combined dictionary:", sorted(dicts3add(d1, d2, d3).items()))
