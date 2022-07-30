class test:
    @classmethod
    def assert_equals(cls, val1, val2):
        print(val1 == val2)


# paste code in kata function


from functools import reduce
from math import prod

class mul:
    _count = 0

    @classmethod
    def get_count(cls):
        res = cls._count
        cls._count = 0
        return res

    @classmethod
    def mul(cls, args):
        cls._count += 1
        return prod(args)


def persistence(n) -> int:
    n_list = [*map(lambda x: int(x), [*str(n)])]

    if len(n_list) == 1:
        return mul.get_count()
    else:
        return persistence(mul.mul(n_list))


if __name__ == '__main__':
    test.assert_equals(persistence(39), 3)
    test.assert_equals(persistence(4), 0)
    test.assert_equals(persistence(25), 2)
    test.assert_equals(persistence(999), 4)
