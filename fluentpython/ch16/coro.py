
def mycoro(x) :
    print ("started coro", x)
    val = yield
    print ("Received val ", val)
    c = yield x + val
    print ("Received c ", c)

