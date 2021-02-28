class DemoException(Exception):
    pass

def demo_exc_handling() :
    print ("coro started")
    while (True) :
        try :
            x = yield
        except DemoException :
            print ("** DemoException handled **.. Continuing")
        else :
            print (f"-> coro received {x}")
    raise RuntimeError("We should never get here")

