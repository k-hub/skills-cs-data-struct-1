def string_compare(s1, s2):
    """Given two strings, figure out if they are exactly the same (without using ==).

    Put runtime here:
    -----------------
    [ O(n) ]


    """

    if len(s1) != len(s2):  # O(1)
        return False

    for i in range(len(s1)):  # O(n)
        if s1[i] != s2[i]:  # O(1) because indexing is constant.
            return False

    return True


def has_exotic_animals(animals):
    """Determine whether a list of animals contains exotic animals.

    Put runtime here:
    -----------------
    [ O(n) ]

    """

    # Iterating through list to find "hippo" is O(n) linear time. 
    # If "hippo" not found, iterating through list again to find "platpypus" is O(n).
    if "hippo" in animals or "platpypus" in animals:
        return True
    else:
        return False


def sum_zero_1(numbers):
    """Find pairs of integers that sum to zero.

    Put runtime here:
    -----------------
    [     O(n^2)     ]

    """

    result = []

    # Hint: the following line, "s = set(numbers)", is O(n) ---
    # we'll learn exactly why later
    s = set(numbers)

    for x in s:  # O(n) because iterating through a set.
        if -x in s:  # O(n). Hidden for-loop. 
            result.append([-x, x])  # O(1) because appending is in constant time.

    return result


def sum_zero_2(numbers):
    """Find pairs of integers that sum to zero.

    Put runtime here:
    -----------------
    [ O(n^2) ]

    """

    result = []

    for x in numbers:  # O(n) because iterating through a list of numbers.
        for y in numbers:  # O(n) because iterating through a list of numbers.
            if x == -y:
                result.append((x, y))  # O(1) because appending is in constant time.
    return result


def sum_zero_3(numbers):
    """Find pairs of integers that sum to zero.

    This version gets rid of duplicates (it won't add (1, -1) if (-1, 1) already there.

    Put runtime here:
    -----------------
    [  O(n^n)          ]

    """

    result = []

    for x in numbers:  # O(n) because iterating through numbers.
        for y in numbers:  # O(n) because iterating through numbers. 
            if x == -y and (y, x) not in result:  # O(n) iterating through result to check if x == -y and O(n) iterating again to check if (y, x) not in result.
                result.append((x, y))
    return result
