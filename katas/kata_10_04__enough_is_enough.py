# paste code in kata function

def delete_nth(order, max_e):
    count = {}
    order = order[:]
    result = []
    for num in range(len(order)):
        el = order[num]

        try:
            count[el] += 1
        except KeyError:
            count[el] = 1

        if count[el] <= max_e:
            result.append(order[num])
    return result


if __name__ == '__main__':
    print(delete_nth([20,37,20,21], 1) == [20,37,21])
    print(delete_nth([1,1,3,3,7,2,2,2,2], 3) == [1, 1, 3, 3, 7, 2, 2, 2])
