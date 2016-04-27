import socket, time
import random
s = socket.socket()
address = "10.2.1.62"
port = 9000
for x in range(0,100):
    try:
        for i in range(0,100):
            s.connect((address,port))
            s.send(("a;" + str(round(random.random(), 5)) + "," + str(round(random.random(), 5))).encode('ascii'))
            s.close()
    except Exception as e: 
        print("something's wrong with %s:%d. Exception is %s" % (address, port, e))
    finally:
        s.close()
    time.sleep(5)
