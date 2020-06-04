#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import socket
import time

from ..platform import ManageProcessor, Color

'''
get Weblogic version info by T3 handshake
'''


@ManageProcessor.poc_register('T3handshake')
class T3handshake(object):
    def process(self, ip, port, scheme):
        return self.run(ip, port)

    def t3handshake(self, sock, server_addr):
        try:
            sock.connect(server_addr)
            # sock.send(bytes.fromhex('74332031322e322e310a41533a3235350a484c3a31390a4d533a31303030303030300a0a'))
            sock.send(bytes.fromhex('743320372E302E302E300A41533A31300A484C3A31390A0A'))
            time.sleep(1)
            res = sock.recv(1024)
            # print(res)
            res = res.decode('utf-8')
            versionInfo = res.splitlines()[0].replace("HELO:", "").replace(".false", "")
            if versionInfo in ["10.3.6.0", "12.1.3.0", "12.2.1.3", "12.2.1.4"]:
                print(Color.OKBLUE + '[+] T3 Handshake Successful. Weblogic Version: {}'.format(versionInfo) + Color.ENDC)
                return True
            else:
                print(Color.OKBLUE + '[+] ' + res[:-1] + Color.ENDC)
                print(Color.FAIL + '[-] Target Weblogic T3 Handshake Failed.' + Color.ENDC)
        except Exception as e:
            print(Color.FAIL + '[-] Target Weblogic T3 Handshake Failed.' + Color.ENDC)

    def run(self, ip, port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(10)
        server_addr = (ip, port)
        return self.t3handshake(sock, server_addr)
