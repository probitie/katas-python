class test:
    @classmethod
    def assert_equals(cls, val1, val2, *args, **kwargs):
        print(val1 == val2)

# paste code in kata function

def unique_in_order(iterable):
    l = [*iterable]
    res = []
    cur = None
    for el in l:
        if cur == el:
            pass
        else:
            res.append(el)
            cur = el

    return res


if __name__ == '__main__':
    test.assert_equals(unique_in_order('AAAABBBCCDAABBB'), ['A', 'B', 'C', 'D', 'A', 'B'])
