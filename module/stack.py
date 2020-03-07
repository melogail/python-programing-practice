# stack module


def getStack():
    """ Creates and returns an empty stack """

    return []


def isEmpty(s):

    """ Retruns True if stack is empty, otherwise returns false """

    if s == []:
        return True
    else:
        return False


def top(s):

    """ Returns value of the top item of stack, if stack not empty.
        Otherwise, returns False
    """

    if isEmpty(s):
        return False
    else:
        return s[len(s) - 1]


def push(s, item):

    """ Pushes item on the top of stack """

    s.append(item)


def pop(s):

    """ Returns top of stack if stack not empty. Otherwise, returns None. """

    if isEmpty(s):
        return None
    else:
        item = s[len(s) - 1]
        del s[len(s) - 1]
        return item

