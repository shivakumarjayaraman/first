#!/usr/bin/env python

from twisted.internet import reactor, protocol

class EchoClient(protocol.Protocol) :
    def connectionMade(self) :
        self.transport.write(b'Hello World')

    def dataReceived(self, data) :
        print (f"Server said {data}")
        self.transport.loseConnection()

class EchoFactory(protocol.ClientFactory) :
    def buildProtocol(self, addr) :
        return EchoClient()

    def clientConnectionFailed(self, connector, reason) :
        print (f"Connection failed {reason}")
        reactor.stop()

    def clientConnectionLost(self, connector, reason) :
        print (f"Connection lost {reason}")
        reactor.stop()

reactor.connectTCP('localhost', 8000, EchoFactory())
reactor.run()

