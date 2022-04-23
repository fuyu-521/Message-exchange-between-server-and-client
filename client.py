from socket import *
import time

udp_socket=socket(AF_INET, SOCK_DGRAM)
udp_socket.settimeout(1)
LostDataCnt=0
serverPort= ('127.0.0.1', 1200)


for i in range(10):
    sendTime=time.time()
    message=('ping %d %s' % (i + 1, sendTime)).encode()

    try:
        udp_socket.sendto(message, serverPort)
        modifiedMessage, serverAddress =udp_socket.recvfrom(1024)
        rtt=time.time() - sendTime

        print('客户机发送的数据包编号: %d\n返回数据的服务器名称: %s\n往返时间: %.3fs\n' % (i + 1, '127.0.0.1', rtt))

    except:
       print('客户机发送的数据包编号:\n请求超时\n')
       LostDataCnt+=1
print('十次请求中丢包的次数为: %d\n' % (LostDataCnt))

udp_socket.close()


