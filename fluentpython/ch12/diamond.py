class A :
    def ping(self) :
        print ("A::ping", self)

class B(A) :
    def pong(self) :
        print ("B::pong", self)

class C(A) :
    def pong(self) :
        print ("C::pong", self)

class D(B, C):
    def ping(self) :
        super().ping()
        print ("D::postping", self)

    def pingpong(self) :
        self.ping()
        super().ping()
        self.pong()
        super().pong()
        C.pong(self)
