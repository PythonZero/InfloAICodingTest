"""
Thought Process:
1) Quickly find the upper/lower limits by incrementing in
   log space (factors of 10)
2) Use binary search to hone into the final value

- Increment in factors of 10 as we want to search the
  biggest space as quick as possible.
- Decrement between the min and max using binary search
  as want to reduce the search space as quick as possible.
"""


# import time
#
#
# def timeit(f):
#
#     def timed(*args, **kw):
#
#         ts = time.time()
#         result = f(*args, **kw)
#         te = time.time()
#
#         print(f'Took: {te-ts:2.4f} sec')
#
#         return result
#
#     return timed


class LenFinder(int):
    """Usage: LenFinder(container)
    >>> LenFinder([1, 4, 5, 91, 6, 'bob', 'mike'])
    7
    """

    # @timeit
    def __new__(cls, container):
        len = cls.len_(container)
        return super(LenFinder, cls).__new__(cls, len)

    @classmethod
    def len_(cls, container: list or tuple):
        """Counts the number of elements in a list without using
        len. List can only be asked for their element at certain positions
        :param container: list to count
        :return: length of container
        """
        min, max = cls._find_max_size_factor_10(container)
        len = cls._binary_search_len(container, min, max)
        return len

    @staticmethod
    def _find_max_size_factor_10(container: list) -> tuple:
        """Returns the lower and uppper bound of the length
        of the object, as a factor of 10
        (lower >= len(container) >= upper)
        :returns: lower, upper - as multiples of 10"""
        idx = 1
        while True:
            try:
                container[idx]
                idx *= 10
            except IndexError:
                min = idx // 10
                max = idx
                return (min, max)

    @staticmethod
    def _binary_search_len(container, min, max):
        """ Does a binary search on the container.
        :param container: list
        :param min: minimum length of the list
        :param max: maximum length of list
        :return: length of list
        """
        while True:
            idx = (max + min) // 2
            try:
                container[idx]
                min = idx
            except IndexError:
                max = idx

            if max - min == 1:
                idx = (max + min) // 2
                # print(f'max:{max} min:{min} idx:{idx}')
                try:
                    container[idx]
                    return idx + 1
                except IndexError:
                    return idx


if __name__ == '__main__':
    for number in [9845831, 3123433]:
        assert number == LenFinder([i for i in range(1, number + 1)])
