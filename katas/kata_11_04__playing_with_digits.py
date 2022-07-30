class P:

    def __init__(self, n):
        self.n = n

    def __call__(self, *args, **kwargs):
        n = self.n
        self.n += 1
        return n

def kata(n, p):
    p = P(p)
    n_list = [int(i) for i in str(n)]
    m = map(lambda el: el**p(), n_list)

    res = sum(m)
    k = res // n

    return k if k >= res / n else -1

if __name__ == '__main__':

    print(kata(89, 1) == 1)
    print(kata(92, 1) == -1)
    print(kata(46288, 3) == 51)
