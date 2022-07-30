def spin(word):
    lst = [*word]
    lst.reverse()
    return ''.join(lst)

def spin_words(sentence):
    # Your code goes here
    result = []
    for word in sentence.split(' '):
        rev_word = spin(word) if len(word) > 4 else word
        result.append(rev_word)
    return ' '.join(result)


if __name__ == '__main__':
    print(spin_words('eeee3333 ere ere try mikasa'))
