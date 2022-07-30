class test:
    @classmethod
    def assert_equals(cls, val1, val2, *args, **kwargs):
        print(val1 == val2)

# paste code in kata function

def rgb(r, g, b) -> str:
    args = [r, g, b]
    # replace values that are out of range
    def limit(x):
        if x < 0:
            x = 0
        elif x > 255:
            x = 255
        return x

    args = list(map(limit, args))

    return "".join(f"{i:02X}" for i in args)


if __name__ == '__main__':
    test.assert_equals(rgb(-20, 5000, 0), "000000")
    test.assert_equals(rgb(0, 0, 0), "000000", "testing zero values")
    test.assert_equals(rgb(1, 2, 3), "010203", "testing near zero values")
    test.assert_equals(rgb(255, 255, 255), "FFFFFF", "testing max values")
    test.assert_equals(rgb(254, 253, 252), "FEFDFC", "testing near max values")
    test.assert_equals(rgb(-20, 275, 125), "00FF7D", "testing out of range values")
