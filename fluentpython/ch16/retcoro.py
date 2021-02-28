from collections import namedtuple

Result = namedtuple('Result', 'count average')

def averager() :
    total = 0
    count = 0
    average = None
    while (True) :
        term = yield
        if (term == None) : 
            break

        total += term
        count += 1
        average = total/count

    return Result(average, count)
