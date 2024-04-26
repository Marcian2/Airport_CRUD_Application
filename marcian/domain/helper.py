def bubbleSort(l, criteria,help = None):
    '''
    Sorts a list in ascending order
    :param l:
    :param criteria:
    :param help:
    :return:
    '''
    isSort = False
    while not isSort:
        isSort = True
        for i in range(len(l) - 1):
            if criteria(l[i], l[i+1], help):
                aux = l[i]
                l[i] = l[i+1]
                l[i+1] = aux
                isSort = False
    return l

def search(l, criteria, help = None):
    '''
    Searches through a llist
    :param l:
    :param criteria:
    :param help:
    :return:
    '''
    result = []
    for i in range(len(l)):
        if criteria(l[i], help):
            result.append(l[i])
    return result

def isInt(value):
    '''
    Checks if a value is an integer
    :param value:
    :return:
    '''
    if int(value) == value:
        return True
    else:
        return False

def makeIntList(n):
    '''
    Makes a list of int numbers
    :param n:
    :return:
    '''
    n = str(n)
    n = list(n)
    for i in range(len(n)):
        n[i] = int(n[i])
    return n




