# -*- coding: utf-8 -*-

import Tkinter as tk

import re
import socket
import sys
import threading

class App(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)

        self.multicast_addr = '239.255.4.3'
        self.multicast_port = 1234

        self.var_send = tk.StringVar()
        self.var_recv = tk.StringVar()

        self.txt_send = tk.Entry(self, textvariable=self.var_send)
        self.txt_send.pack()

        self.txt_recv = tk.Entry(self, textvariable=self.var_recv)
        self.txt_recv.pack()

        self._bind_events()

        self.listening_thread = threading.Thread(target=listen_loop, args=(self.multicast_addr, self.multicast_port, self.var_recv))
        self.listening_thread.setDaemon(True)
        self.listening_thread.start()

    def quit_application(self, event=None):
        self.destroy()
        self.quit()

    def send_message(self, event=None):
        send_msg(self.multicast_addr, self.multicast_port, self.var_send)

    def _bind_events(self):
        self.bind('<Escape>', self.quit_application)
        self.txt_send.bind('<Return>', self.send_message)

def ip_is_local(str_ip):
    combined_regex = '(^10\.)|(^172\.1[6-9]\.)|(^172\.2[0-9]\.)|(^172\.3[0-1]\.)|(^192\.168\.)'
    return re.match(combined_regex, str_ip) is not None

def get_local_ip():
    local_ips = [ x[4][0] for x in socket.getaddrinfo(socket.gethostname(), 80) if ip_is_local(x[4][0])]

    local_ip = local_ips[0] if len(local_ips) > 0 else None

    if not local_ip:
        temp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            temp_socket.connect(('8.8.8.8', 9))
            local_ip = temp_socket.getsockname()[0]
        except socket.error:
            local_ip = '127.0.0.1'
        finally:
            temp_socket.close()
    return local_ip

def create_socket(addr, port):
    local_ip = get_local_ip()

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    s.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_IF, socket.inet_aton(local_ip))

    s.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 2)

    membership_request = socket.inet_aton(addr) + socket.inet_aton(local_ip)

    s.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, membership_request)

    print('local_ip %s' % local_ip)

    if sys.platform.startswith('darwin'):
        s.bind(('0.0.0.0', port))
    else:
        s.bind((local_ip, port))

    return s


def listen_loop(addr, port, var):
    s = create_socket(addr, port)
    while True:
        data, address = s.recvfrom(4096)
        print('received %s' % data)
        var.set(data)

def send_msg(addr, port, var):
    s = create_socket(addr, port + 1)

    s.sendto(var.get(), (addr, port))

    s.close()

if __name__ == '__main__':
    app = App()
    app.mainloop()