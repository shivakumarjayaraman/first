from functools import wraps

def primecoro(func) :
    @wraps(func)
    def primed(*args, **kwargs) :
        gen = func(*args, **kwargs)

        ## prime the coroutine
        next(gen)
        return gen
    return primed

@primecoro
def averager() :
    total = 0
    count = 0
    avg = None

    while (True) :
        val = yield avg
        total += val
        count += 1
        avg = total/count


