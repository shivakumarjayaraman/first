#!/usr/bin/env python

def fib(n) :
    if (n <= 2) :
        return n

    return fib(n-1) + fib(n-2)


from unittest import TestCase, main
class FibTest(TestCase) :
    def setUp(self) :
        self.count = 10

    def test_fib(self) :
        for i in range(self.count) :
            k = fib(i)
            print (i, k)
            if (i == 8) :
                self.assertEqual(k, 34)

    def test_another(self) :
        print ("oopsie")


    def tearDown(self) :
        print ("Tests done")

if (__name__ == "__main__") :
    main()
