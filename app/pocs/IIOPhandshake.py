#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import socket
import time

from ..platform import ManageProcessor, Color


@ManageProcessor.poc_register('IIOPhandshake')
class IIOPhandshake(object):
    def process(self, ip, port, scheme):
        return self.run(ip, port)

    def iiophandshake(self, sock, server_addr):
        try:
            sock.connect(server_addr)
            sock.send(bytes.fromhex('47494f50010200030000001700000002000000000000000b4e616d6553657276696365'))
            time.sleep(1)
            res = sock.recv(1024)
            if b'GIOP' in res:
                print(Color.OKBLUE + '[+] Target Weblogic IIOP Handshake Success.' + Color.ENDC)
                return True
            else:
                print(Color.FAIL + '[-] Target Weblogic IIOP Handshake Failed.' + Color.ENDC)
                return False
        except Exception as e:
            print(Color.FAIL + '[-] Target Weblogic IIOP Handshake Failed.' + Color.ENDC)
            return False

    def run(self, ip, port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(10)
        server_addr = (ip, port)
        return self.iiophandshake(sock, server_addr)
