"""Given two lists, find the smallest difference between any two nums.

For example, given the lists:

  {10, 20, 14, 16, 18}
  {30, 23, 54, 33, 96}

The result would be 3, since 23 - 20 = 3 is the smallest difference of
any pair of numbers in those lists.

IMPORTANT: you must solve this with an algorithm that is faster than
O(ab)---that is, you cannot compare each item of list a against
each item of list b (that would be O(ab) time).

Joel Burton <joel@joelburton.com>.

Adapted from a problem in `Cracking the Coding Interview, 6th Edition`.
Gayle Laakmann McDowell, Career Cup (Palo Alto, CA). 2015.
"""


def smallest_diff(a, b):
    """Return smallest diff between all items in a and b.

        >>> smallest_diff([10, 20, 30, 40], [15, 25, 33, 45])
        3
        >>> smallest_diff([10, 20, 14, 16, 18], [30, 23, 54, 33, 96])
        3
    """
    #sort each list
    a.sort()
    b.sort()
    final_diff = []
    i = 0
    while i < len(a):
        j = 0
        diff = 0
        while j < len(b) and diff <= 0:
            diff = b[j] - a[i]
            j += 1
        final_diff.append(diff)
        i += 1
    return min(final_diff)





if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. NICE WORK!\n")
