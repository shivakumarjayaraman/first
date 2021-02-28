class Demo :
    @staticmethod
    def statmet(*args):
        print (*args)


    @classmethod
    def clsmet(*args) :
        print (type(args[0]))
        print (*args)


