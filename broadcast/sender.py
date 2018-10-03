from socket import *
s = socket(AF_INET, SOCK_DGRAM)
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
s.sendto('this is testing',('192.168.0.255',12345))
