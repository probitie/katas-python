"""нет смысла тратить время, у меня не получится сейчас"""


class test:
    @classmethod
    def assert_equals(cls, val1, val2, *args, **kwargs):
        print(val1 == val2)

# paste code in kata function


class NextPair:
    def __init__(self, start_x, start_y):
        self.x = [start_x]
        self.y = [start_y]
        self.state_n = 0

        self.current, self.step = self._states()

    def current_pair(self):
        return self.x[0], self.y[0]

    def _states(self):

        states = (  #
            (self.y, 1),  # movement to the right
            (self.x, 1),  # movement to the downward
            (self.y, -1),  # movement to the left
            (self.x, -1),  # movement to the upward
        )

        if self.state_n == len(states):
            self.state_n = 0
        n = self.state_n
        self.state_n += 1
        return states[n]

    def next(self):
        self.current[0] += self.step  # this must change self.y too
        print(f"{self.x=}, {self.y=}, {self.step=}")
        # here we must check IndexOutOfRange and return item on [x][y] and make _states able to move back

    def previous(self):
        self.current[0] -= self.step
        print(f"back {self.x=}, {self.y=}, {self.step=}")

    def turn(self):
        self.current, self.step = self._states()


class Snail:
    def __init__(self, matrix):
        self.matrix = matrix

        # index pairs - where move method already was ( after being at point (x, y) it adds to self.pairs )
        self._pairs = []  # [(x, y), (m, n)]
        self.pair = NextPair(0, 0)

    def make_steps(self) -> list:
        res = []
        if not self._exists(self.pair.current_pair()):
            return []
        res.append(self.matrix[self.pair.current_pair()[0]][self.pair.current_pair()[1]])
        for _ in range(1, len(self.matrix) * len(self.matrix[0])):
            res.append(self._make_step())
        return res

    def _make_step(self):
        cur_pair = self.pair.current_pair()
        if self._can_move(cur_pair) and self._exists(cur_pair):
            obj = self.pair.next()

    def _exists(self, pair: tuple):
        try:
            self.matrix[pair[0]][pair[1]]
            return True
        except IndexError:
            return False

    def _can_move(self, pair):
        return pair not in self._pairs

def snail(matrix) -> list:
    res = []
    s = Snail(matrix)
    for _ in range(len(matrix) * len(matrix[0])):
        res.append(s.make_step())
    return res


if __name__ == '__main__':

    array = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]
    expected = [1, 2, 3, 6, 9, 8, 7, 4, 5]
    test.assert_equals(snail(array), expected)

    array = [[1, 2, 3],
             [8, 9, 4],
             [7, 6, 5]]
    expected = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    test.assert_equals(snail(array), expected)

