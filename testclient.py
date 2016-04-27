from twisted.internet import reactor, protocol

HOST = '10.2.1.62'
PORT = 9000

def sendSampleData(self):
	for i in range(0, 10):
		self.transport.write("a;10.00;0.43")

class MyClient(protocol.Protocol):
    def connectionMade(self):
        print "connected!"
       	self.transport.write("hello")
	sendSampleData(self)
    def dataReceived(self, data):
        print data

class MyClientFactory(protocol.ClientFactory):
    protocol = MyClient

factory = MyClientFactory()
connection = reactor.connectTCP(HOST, PORT, factory)
reactor.run()
