# Yehuda Levy 332300433

def evenprt(n1, n2, n3):
    # generator for even numbers in range - more efficient
    def even_nums_gen(start, end):
        current = start if start % 2 == 0 else start + 1
        while current <= end:
            yield current
            current += 2

    # groups numbers into chunks
    def group_nums(nums, size):
        group = []
        for n in nums:
            group.append(n)
            if len(group) == size:
                yield group
                group = []
        if group:
            yield group

    # check inputs are valid
    if not all(isinstance(x, int) and x > 0 for x in [n1, n2, n3]) or n1 >= n2 or n3 >= (n2 - n1):
        print("ERROR: at least one of the input values is incorrect")
        return

    # print the groups
    for group in group_nums(even_nums_gen(n1, n2), n3):
        print(" ".join(map(str, group)))


def napa(n):
    # sieve of eratosthenes using list comprehension like prof wanted
    if n < 1:
        return []

    if n == 1:
        return [1]

    candidates = list(range(2, n + 1))
    primes = [p for p in candidates if not any(p % i == 0 for i in range(2, int(p ** 0.5) + 1))]

    return [1] + primes  # gotta include 1 based on examples


def primefactors(n):
    # find prime divisors using napa
    if n <= 0:
        print("ERROR: the number must be a positive integer")
        return []

    primes = napa(n)
    return [x for x in primes if n % x == 0]


def make_list_processor():
    # zip function
    def zip_lists(lists):
        if not lists or not lists[0]:
            return []
        return [list(x) for x in zip(*lists)]

    # sort mixed types - numbers first then strings
    def custom_sort(lst):
        nums = sorted([x for x in lst if isinstance(x, (int, float))])
        strs = sorted([x for x in lst if isinstance(x, str)])
        return nums + strs

    def sortedzip(lists):
        sorted_lists = [custom_sort(lst) for lst in lists]
        return zip_lists(sorted_lists)

    def reversedzip(lists):
        reversed_lists = [lst[::-1] for lst in lists]
        return zip_lists(reversed_lists)

    def funczip(func, lists):
        return func(lists)

    def unzippy(zipped):
        if not zipped:
            return []
        return [[item[i] for item in zipped] for i in range(len(zipped[0]))]

    # the closure part prof wants
    def process_lists(choice, lists):
        operations = {
            1: sortedzip,
            2: reversedzip
        }
        if choice not in operations:
            return None
        result = funczip(operations[choice], lists)
        return result, unzippy(result)

    return process_lists


def parse_lists(input_str, size):
    # parse the input string into lists
    input_str = input_str.strip()
    if not (input_str.startswith('[[') and input_str.endswith(']]')):
        return None

    # remove outer brackets
    inner = input_str[2:-2]
    sublists_str = inner.split('],[')

    result = []
    for sublist_str in sublists_str:
        items_str = [item.strip() for item in sublist_str.split(',')]

        if len(items_str) != size:
            return None

        parsed_items = []
        for item in items_str:
            # check if its a number
            if item.lstrip('-').isdigit():
                parsed_items.append(int(item))
            # check if quoted string
            elif (item.startswith("'") and item.endswith("'")) or (item.startswith('"') and item.endswith('"')):
                parsed_items.append(item[1:-1])
            else:
                parsed_items.append(item)

        result.append(parsed_items)

    return result


def main():
    # get user input
    n = int(input("Enter the size of the sublists of the list to process: "))
    input_str = input("Enter the list to process: ")

    # parse the lists
    lists = parse_lists(input_str, n)
    if lists is None:
        print(f"ERROR - all sublists must be of size {n}")
        return

    # show menu
    print("1: sortedzip")
    print("2: reversedzip")
    choice = int(input("Which function do you want to choose? "))

    # process with closure
    processor = make_list_processor()
    result = processor(choice, lists)

    if result is None:
        print("ERROR - chosen function does not exist.")
        return

    zipped, unzipped = result
    print(zipped)
    print(unzipped)


if __name__ == "__main__":
    main()