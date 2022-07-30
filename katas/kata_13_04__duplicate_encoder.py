class test:
    @classmethod
    def assert_equals(cls, val1, val2, *args, **kwargs):
        print(val1 == val2)

# paste code in kata function

def duplicate_encode(string):
    l = string.lower()
    return ''.join([')' if l.count(i) > 1 else '(' for i in l])


if __name__ == '__main__':
    test.assert_equals(duplicate_encode("din"), "(((")
    test.assert_equals(duplicate_encode("recede"), "()()()")
    test.assert_equals(duplicate_encode("Success"), ")())())", "should ignore case")
    test.assert_equals(duplicate_encode("(( @"), "))((")
