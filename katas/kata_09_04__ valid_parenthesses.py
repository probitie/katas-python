# paste code in kata function


def kata(string):
    opened = 0
    closed = 0

    for char in string:
        if char == "(" and opened >= closed:
            opened += 1
        elif char == ")":
            closed += 1
    return opened == closed

if __name__ == '__main__':
    print(kata("def(new(123, 423, 1))"))
    print(kata("(((widsdsds))))"))
    print(kata("((((((widsdsds))))"))
