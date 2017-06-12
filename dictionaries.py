def create_state_capital_dictionary():
    """Create a dictionary that maps a state name to its capital. 

    This dictionary should contain at least the following three states and capitals:
        The capital of California is Sacramento.
        The capital of Washington is Olympia.
        The capital of Oregon is Salem.

        >>> capitals = create_state_capital_dictionary()

        >>> capitals['California']
        'Sacramento'

        >>> capitals['Washington']
        'Olympia'

        >>> capitals['Oregon']
        'Salem'
    """
    #created the dictionary of State and Capital pairs
    state_capitals = {
    'New York': 'Albany',
    'California': 'Sacramento',
    'Texas': 'Austin',
    'Washington': 'Olympia',
    'Oregon': 'Salem'
    }
    #returning "state_capitals" will return the values (the capitals)
    return state_capitals

    create_state_capital_dictionary()    


    

def get_inventory(inventory, item):
    """Takes in an inventory of items (dictionary) and an item. Prints the
    number of that item in the inventory.

    If the item is not in the inventory, function should print
    "Cannot find __item__"

        >>> inv = {'apples': 5, 'berries': 0, 'cherries': 3}
        
        >>> get_inventory(inv, 'apples')
        5 apples
        
        >>> get_inventory(inv, 'berries')
        0 berries

        >>> get_inventory(inv, 'durian')
        Cannot find durian

    """
    # already have the dictionary "inventory" and a variable "item"
    # since it was passed inside the parameters/parentheses
    inventory = {'apples': 5, 'berries': 0, 'cherries': 3}

    # if item is as key in dictionary "inventory" ...
    if item in inventory:
        print(str(inventory[item]) + " " + item)

    else:
        # if it's not an item then print "cannot find [item]"
        print("Cannot find " + item)



def count_items(items):
    """Take in a list of items and return a dictionary with each item and
    the number of times it appears in the list.

        >>> items = ['a', 'b', 'a', 'c', 'd', 'e', 'a', 'e']

        >>> item_counts = count_items(items)
        
        >>> sorted(item_counts.items())
        [('a', 3), ('b', 1), ('c', 1), ('d', 1), ('e', 2)]
    """
    # create an empty dictionary called "items_dict"
    items_dict = {}

    # loop through every item in list "items"
    for i in range(len(items)):
        # if item 'i' is not equal to None then replace current value with
        # same value plus 1
        if items[i] in items_dict:
            items_dict[items[i]] += 1
        # if item is not yet in dictionary then add the item as a key and give
        # it a value of 1
        else:
            items_dict[items[i]] = 1
    # return the dictionary to exit the function
    return items_dict


    #passing the list to create the dict and enable the function
    count_items(['a', 'b', 'a', 'c', 'd', 'e', 'a', 'e'])

# Optional
def find_word_lengths(words):
    """Take in a list of words and return a dictionary where the key is the
    length of a word and the value is a list of words of that length.

        >>> words = ['blue', 'green', 'pink', 'yellow', 'lavender']

        >>> word_lengths = find_word_lengths(words)
        
        >>> sorted(word_lengths.items())
        [(4, ['blue', 'pink']), (5, ['green']), (6, ['yellow']), (8, ['lavender'])]
    """
    # create empty dictionary
    word_dict = {}

    # loop through entire list of words list
    for i in range(len(words)):
        # if the length of word 'i' is already inside the dictionary...
        if len(words[i]) in word_dict:
            # append to list corresponding to that length
            word_dict[len(words[i])].append(words[i])
        else:
            # else means there is not yet a list with words of this length.
            # So we create a list of a single word..
            word_dict[len(words[i])] = [words[i]]

    return word_dict

find_word_lengths(['blue', 'green', 'pink', 'yellow', 'lavender'])


# You can ignore everything below here
if __name__ == "__main__":
    import doctest

    result = doctest.testmod()
    if not result.failed:
        print("\nALL TESTS PASSED. GOOD WORK!\n")