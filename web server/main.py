from socket import *


serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind(('127.0.0.1',1234))

serverSocket.listen(1)


while True:
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(1024)
        filename = message.split()[1]
        # 将字符串以所有的空字符，包括空格、换行(\n)、制表符(\t)等开割形成一个字符串数组，然后再通过索引[1]取出所得数组中的第二个元素的值
        f = open(filename[1:],encoding='utf-8')
        outputdata =f.read(1024)


        header = ' HTTP/1.1 200 OK\nConnection: close\nConnent-Type: text/html\nConnent-Length: %d\n\n' % (len(outputdata))
        connectionSocket.send(header.encode())

        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())


        connectionSocket.close()



    except IOError:
        header = ' HTTP/1.1 404 Not Found'
        connectionSocket.send(header.encode())

        connectionSocket.close()
    serverSocket.close()
