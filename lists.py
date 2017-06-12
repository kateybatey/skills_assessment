def all_vowel_words(lst):
    """Return a list containing every word that starts with a vowel.

    This function takes in a list of words. It should return a list
    containing only the words from the input list that start with vowels.

    Assume that 'y' always counts as a vowel.

        >>> all_vowel_words(['apple', 'berry', 'cherry'])
        ['apple']

        >>> all_vowel_words(['bear', 'duck'])
        []

        >>> all_vowel_words(['yellow', 'green', 'eggplant'])
        ['yellow', 'eggplant']
    """ 
    #make a list of words
    vowels = ["a", "e", "i", "o", "u", "y"]

    # create a new word list
    vowel_words = []

    # loop through all words in the list given through the parameters/parentheses
    # to check whether the first character is a vowel
    for i in range(len(lst)):
        word = lst[i]
        # get letter at position zero in the word
        firstLetter = word[0]
        # check if first letter in word one of the
        if firstLetter in vowels:
            # if so, append to new list
            vowel_words.append(word)
    # once it goes through all words return vowel_words so that other
    # functions outside vowel_words can 'see' the new list
    return vowel_words

all_vowel_words(["a", "e", "i", "o", "u", "y"])

    # this could have also been done using a bunch of if
    # and elif statements

def is_item_in_list(lst, item):
    """Return True if item is in the list, False if not.
    
        >>> is_item_in_list(['apple', 'berry', 'cherry'], 'durian')
        False

        >>> is_item_in_list(['apple', 'berry', 'cherry'], 'berry')
        True
    """
    # checks if item in this list
    if item in lst:
        return True
    else:
        return False


is_item_in_list(['apple', 'berry', 'cherry'], 'durian')


def print_index_of_item(lst, item):
    """Print the index of an item in a list, followed by the item.

    If the item appears multiple times in the list, return the index and
    the item for each time it appears in the list.

    If the item does not appear, print '_item_ not found' (substitute the
    name of the item.)

        >>> print_index_of_item(['a', 'b', 'c', 'b', 'c'], 'b')
        1 b
        3 b

        >>> print_index_of_item([1, 2, 3], 4)
        4 not found

        >>> print_index_of_item(['apple', 'berry', 'cherry', 'durian'], 'apple')
        0 apple
    """
    # if item in this list
    if item in lst:
        # loop through list
        for i in range(len(lst)):
            # if one of the elements is equal to 'item'
            if lst[i] == item:
                # print it
                print(str(i) + " " + str(item))
    else:
        # if not in list print not found
        print(str(item) + " not found")

print_index_of_item(['apple', 'berry', 'cherry', 'durian'], 'apple')


# You can ignore everything below here
if __name__ == "__main__":
    import doctest

    result = doctest.testmod()
    if not result.failed:
        print("\nALL TESTS PASSED. GOOD WORK!\n")