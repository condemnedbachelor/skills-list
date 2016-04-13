"""Skills Assessment: Lists

Edit the function bodies until all of the doctests pass when you run this file.
"""


def all_odd(number_list):
    """Return a list of only the odd numbers in the input list.

        >>> all_odd([1, 2, 7, -5])
        [1, 7, -5]

        >>> all_odd([2, -6, 8])
        []

    """
    odd_numbers = []
    for item in number_list:
        if item % 2 != 0:
        #modulo: if you can divide it by two but there is a remainder
            odd_numbers.append(item)

    return odd_numbers
# Solution: return [d for d in number_list if d % 2 != 0]

def all_even(number_list):
    """Return a list of only the even numbers in the input list.

        >>> all_even([2, 6, -1, -2])
        [2, 6, -2]

        >>> all_even([-1, 3, 5])
        []

    """
    even_numbers = []
    for item in number_list:
        if item % 2 == 0:
        #modulo: if you can divide it by two and there is no remainder
            even_numbers.append(item)

    return even_numbers
# Solution: return [d for d in number_list if d % 2 == 0]

def print_indexes(my_list):
    """Print the index of each item in the input_list, followed by the item itself.

    Do this without using a counting variable---that is, don't do something
    like this:

        count = 0
        for item in list:
            print count
            count = count + 1

    Output should look like this:

        >>> print_indexes(["Toyota", "Jeep", "Volvo"])
        0 Toyota
        1 Jeep
        2 Volvo

    """
    #For each item in my list, I want to return its index position followed by its content.
    for item in (my_list):
        is_indexed = my_list.index[:]

    #struggle notes: I tried to look up the best way to do this and saw "enumerate()", 
    #but I think we're supposed to do this manually using what we've already learned.

    #At this point I've tried so many things. I foolishly left my notes in
    #our space and I can't seem to find more info in our lecture notes
    #on this particular scenario.

    return is_indexed

    # Solution: 
    # for i in range(len(my_list)):
    #     print i, my_list[i]
    # Or: 
    # for i, vehicle in enumerate(my_list):
    #     print i, vehicle

def long_words(word_list):
    """Return all words in input list that are longer than 4 characters.

        >>> long_words(["hello", "hey", "spam", "spam", "bacon", "bacon"])
        ['hello', 'bacon', 'bacon']

        >>> long_words(["all", "are", "tiny"])
        []

    """
    is_more_than_four = []
    for item in word_list:
        if len(item) > 4:
            is_more_than_four.append(item)

    return is_more_than_four
    # Solution: 
    # return [w for w in word_list if len(w) > 4]


def smallest_int(number_list):
    """Find the smallest integer in a list of integers and return it.

    DO NOT USE the built-in function `min`!

        >>> smallest_int([-5, 2, -5, 7])
        -5


        >>> smallest_int([3, 7, 2, 8, 4])
        2

    If the input list is empty, return None:


        >>> smallest_int([]) is None
        True

    """
    is_smallest = []
    for item in number_list:
        is_smallest = sorted(number_list)

    try:
        return is_smallest[0]
    except IndexError:
        return None
    #returns index 0 of a numerically-sorted list

    # Solution: 
    # smallest = None
    # for item in number_list:
    #     if smallest is None or item < smallest:
    #          smallest = item
    # return smallest


def largest_int(number_list):
    """Find the largest integer in a list of integers and return it.

    DO NOT USE the built-in function `max`!

        >>> largest_int([-5, 2, -5, 7])
        7

        >>> largest_int([3, 7, 2, 8, 4])
        8

    If the input list is empty, return None:

        >>> largest_int([]) is None
        True

    """
    is_largest = []
    for item in number_list:
        is_largest = sorted(number_list, reverse=True)
        #apologies if this is too off-book, had a hard time
        #remembering how to do a reverse sort and looked it up.
    try:
        return is_largest[0]
    except IndexError:
        return None
    #returns index 0 of a reverse-numerically-sorted list

def halvesies(number_list):
    """Return list of numbers from input list, each divided by two.

        >>> halvesies([2, 6, -2])
        [1.0, 3.0, -1.0]

    If any of the numbers are odd, make sure you don't round off the half:

        >>> halvesies([1, 5])
        [0.5, 2.5]

    """
    is_halved = []
    number_list[:] = [float(item) / 2 for item in number_list]
    # for each item in number_list, convert item to float, divide by 2, iterate.
    is_halved = number_list
    # this may be unnecessary but I like having a special var for this function
    return is_halved


def word_lengths(word_list):
    """Return the length of words in the input list.

        >>> word_lengths(["hello", "hey", "hello", "spam"])
        [5, 3, 5, 4]

    """

    length = []
    word_list[:] = [len(item) for item in word_list]
    length = word_list
    return length

def sum_numbers(number_list):
    """Return the sum of all of the numbers in the list.

    Python has a built-in function, `sum()`, which already does this -- but for
    this exercise, you should not use it.

        >>> sum_numbers([1, 2, 3, 10])
        16

    Any empty list should return the sum of zero:

        >>> sum_numbers([])
        0

    """
    #I couldn't get this one but I'll try to explain my thinking:
    sum = []
    #defined a global variable to use later
    for item in number_list:
        # num = item in number_list
        # This var is not necessary but this leads me to the next problem:
        number_list[:] == item + item
        #for each index in list, item plus item?
        sum = number_list[:]
        # Nothing is fixed by using item is the variable. 
        # I'm not sure how to do this without the sum function.
        # Trying to mult each item by each item but not sure how to iterate that 
        # or how to refer to "the indices that are not the one we're on now"
        return sum
# Solution: 
# total = 0
# for i in number_list:
#     total = total + i

# return total


def mult_numbers(number_list):
    """Return product (result of multiplication) of the numbers in the list.

        >>> mult_numbers([1, 2, 3])
        6

    Obviously, if there is a zero in the input, the product will be zero:

        >>> mult_numbers([10, 20, 0, 50])
        0

    As explained at http://en.wikipedia.org/wiki/Empty_product, if the list is
    empty, the product should be 1:

        >>> mult_numbers([])
        1

    """
    # Failed this one for the same reason, same line of thinking. Commenting out my 
    # attempt so you can see it without breaking terminal.
    # product = []
    # for item in number_list:
    #     number_list == item * item
    #     product = number_list
    # return product

# Solution:
# product = 1 < because mult by 1 is the same as adding zero
# for i in number_list:
#     product = product * i

# return product


def join_strings(word_list):
    """Return a string of all input strings joined together.

    Python has a built-in method on lists, `join`---but for this exercise, you
    should not use it.

        >>> join_strings(["spam", "spam", "bacon", "balloonicorn"])
        'spamspambaconballoonicorn'

    For an empty list, you should return an empty string:

        >>> join_strings([])
        ''

    """
    #Defined a thus far empty list.
    all_strings = []
    for item in word_list:
        # Tried to split the items by comma to append them together
        x = item.split(',')
        # This is where I tried to append them, which failed.
        all_strings = word_list.append(x)
        # Tried to attach it to my original empty list for returning.
        return all_strings
        # Sometimes I could get it to return "spam" once or twice, but never all objects
        # as one word. :( I can not figure out how to make this one work.
    return all_strings
# Solution:
# result = "" < because you're dealing with strings, but this works same as sum

# for s in word_list:
#     result = result + s

# return result

def average(number_list):
    """Return the average (mean) of the list of numbers given.

        >>> average([2, 12, 3])
        5.666666666666667

    There is no defined answer if the list given is empty. It's fine if
    this raises an error when given an empty list.
    """
    average = []
    total = []
    # defining average and total as empty lists globally to use inside for loop
    for item in number_list:
        # Changed items to floats in case of decimals
        # Tried to add all items together to divide by the amount of them.
        total = float(item) + float(item) in number_list[:] 
        # I want total to equal the float of the sum of two items for each index in
        # number_list. I know this is wrong because the join one was also wrong.
        size = len(total)
        # Size equals the length of the new total list above
        average = total / size
        # average equals total sum divided by size of list
    return average

# Solution:
# total = sum_numbers(number_list)
# return total / float(len(number_list))

def join_strings_with_comma(list_of_words):
    """Return ['list', 'of', 'words'] like "list, of, words".

        >>> join_strings_with_comma(["Labrador", "Poodle", "French Bulldog"])
        'Labrador, Poodle, French Bulldog'

    If there's only one thing in the list, it should return just that
    thing, of course:

        >>> join_strings_with_comma(["Pretzel"])
        'Pretzel'

#     """
# I had the same problem as the first join exercise.
    is_joined = []
    for item in list_of_words:
        split = list_of_words.split(",")
        is_joined = list_of_words.append(split)
    return is_joined

# Solution:
# return ", ".join(list_of_words)



##############################################################################
# END OF ASSIGNMENT: You can ignore everything below.


if __name__ == "__main__":
    import doctest
    print
    result = doctest.testmod()
    if not result.failed:
        print "*** %s TESTS PASSED. GOOD WORK!" % result.attempted
    print
