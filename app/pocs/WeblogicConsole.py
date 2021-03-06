#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import requests
from ..platform import ManageProcessor, Color

url = "http://192.168.3.32:7001/"


@ManageProcessor.poc_register('weblogic-console')
class WeblogicCosole(object):
    headers = {'user-agent': 'ceshi/0.0.1'}

    def process(self, ip, port, scheme):
        return self.run(ip, port, scheme)

    def islive(self, ip, port, scheme):
        url = str(scheme) + '://' + str(ip) + ':' + str(port) + '/console/login/LoginForm.jsp'
        r = requests.get(url, headers=self.headers)
        return r.status_code

    def run(self, ip, port, scheme):
        if self.islive(ip, port, scheme) == 200:
            u = str(scheme) + '://' + str(ip) + ':' + str(port) + '/console/login/LoginForm.jsp'
            print(Color.OKBLUE + "[+] The target Weblogic console address is exposed!\n[+] The path is: {}\n[+] Please try weak password blasting!".format(u) + Color.ENDC)
            return True
        else:
            print(Color.FAIL + "[-] Target Weblogic console address not found!" + Color.ENDC)
            return False
