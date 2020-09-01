#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import socket
import time
import re

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
            sock.send(bytes.fromhex('74332031322E312E320A41533A323034380A484C3A31390A0A'))
            time.sleep(1)
            res = sock.recv(1024)
            # print(res)
            res = res.decode('utf-8')
            # versionInfo = res.splitlines()[0].replace("HELO:", "").replace(".false", "")
            versionInfo = re.match(r'.*?([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)', res).group(1)
            if versionInfo:
                if versionInfo == "12.1.2":
                    sock.send(bytes.fromhex('74332031312E312E320A41533A323034380A484C3A31390A0A'))
                    time.sleep(1)
                    res = sock.recv(1024)
                    res = res.decode('utf-8')
                    versionInfo = re.match(r'.*?([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)', res).group(1)
                    if versionInfo == "11.1.2":
                        # Server just echoes whatever version we send.
                        print(Color.OKBLUE + '[-] T3 protocol in use (Unknown WebLogic version).' + Color.ENDC)
                        return
                print(Color.OKBLUE + '[+] T3 protocol in use (Weblogic Version: {})'.format(versionInfo) + Color.ENDC)
                return True
            else:
                print(Color.OKBLUE + '[+] ' + res[:-1] + Color.ENDC)
                print(Color.OKBLUE + '[-] Unknown response received.' + Color.ENDC)
        except Exception as e:
            print(Color.FAIL + '[-] Target Weblogic T3 Handshake Failed.' + Color.ENDC)

    def run(self, ip, port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(10)
        server_addr = (ip, port)
        return self.t3handshake(sock, server_addr)
