animals = {'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')


def how_many(aDict):
    """
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    """
    num_values = 0

    for i in aDict:
        num_values += len(aDict[i])

    return num_values


print(how_many(animals))


def biggest(aDict):
    """
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    """

    if len(aDict) == 0:
        return None

    big_key = None
    big_num = 0

    for k, v in aDict.items():
        if len(v) > big_num:
            big_key = k
            big_num = len(v)

    return big_key


print(biggest(animals))
