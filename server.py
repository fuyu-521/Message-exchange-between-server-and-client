import random
from socket import *

serverSocket = socket(AF_INET, SOCK_DGRAM)


serverSocket.bind(('127.0.0.1', 1200))


while True:
    rand = random.randint(0, 10)

    message, address = serverSocket.recvfrom(1024)

    print("收到来自 %s 的报文: (%s)" % (address, message))
    print("随机数是: %d" % rand)

    message = message.upper()

    if rand < 4:
       continue
    serverSocket.sendto(message, address)

