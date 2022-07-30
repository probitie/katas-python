class test:
    @classmethod
    def assert_equals(cls, val1, val2, *args, **kwargs):
        print(val1 == val2)

# paste code in kata function

def kata():
    pass


if __name__ == '__main__':
    test.assert_equals(kata(), False)
