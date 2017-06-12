# having trouble with part two, specifically how I would save output into a new list. 
#could not find info on this in my notes

def all_odd_or_even(lst, type):
    # If a number is even, it means that when you divide it by two its remainder is zero.
    # the operator for remainder is modulo '%'. 5 % 2 = 1. 

	# nums = [0, 2, 3, 6, 4, 11, -1]
    #created an empty list
    new_list = []


    if type == "even":
        # go through every item in list
        for num in lst:
            # if the remainder when divided by two is zero, then it's even
            if num % 2 == 0:
                # add to list
                new_list.append(num)

    # if 'type' is not even then it must be odd
    else:
        for num in lst:
            # same as above but here it's the "not equals" operator.
            # "If num not even"
            if num % 2 != 0:
                new_list.append(num)
    # return the new list after it's done
    print new_list

all_odd_or_even([0, 2, 3, 6, 4, 11, -1], 'even')


