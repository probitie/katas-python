def descending_order(num):
    # Bust a move right here
    digits = [*str(num)]
    sorted_digits = sorted(digits, reverse=True)
    return int(''.join(sorted_digits))


if __name__ == '__main__':
    print(descending_order(3234536))
