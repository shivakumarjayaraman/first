def averager() :
    total = 0
    count = 0
    avg = None
    while (True) :
        val = yield avg
        total += val
        count += 1
        avg = total/count




