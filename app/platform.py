#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import logging
from urllib.parse import urlparse

logging.basicConfig(filename='Weblogic.log',
                    format='%(asctime)s %(message)s',
                    filemode="w", level=logging.INFO)


class ManageProcessor(object):
    POCS = {}
    EXPS = {}

    def process(self, target, pocs=(), cmd=None):
        o = urlparse(target)
        scheme = o.scheme
        ip = o.hostname
        if o.port is None:
            port = 443 if scheme == "https" else 80
        else:
            port = o.port
        # print(scheme, ip, port)
        if pocs is ():
            for poc_name in self.POCS.keys():
                self.check(poc_name, ip, port, scheme)
        else:
            if cmd is None:
                for poc_name in pocs:
                    if poc_name in self.POCS:
                        self.check(poc_name, ip, port, scheme)
                    else:
                        print(Color.WARNING + "[-] {} 暂不支持该漏洞检测".format(poc_name) + Color.ENDC)
            else:
                for exp_name in pocs:
                    if exp_name in self.EXPS:
                        self.exploit(exp_name, ip, port, scheme, cmd)
                    else:
                        print(Color.WARNING + "[-] {} 暂不支持该漏洞利用".format(exp_name) + Color.ENDC)
        return

    def check(self, poc_name, ip, port, scheme):
        try:
            print(Color.OKYELLOW + "[*] 开始检测", ip, port, poc_name + Color.ENDC)
            if self.POCS[poc_name]().process(ip, port, scheme):
                logging.info("[+] {} {} {}".format(ip, port, poc_name))
                print(Color.OKGREEN + "[+]", ip, port, poc_name + Color.ENDC)
        except BaseException:
            print(Color.WARNING + "[-] {} 未成功检测，请检查网络连接或或目标存在负载中间件".format(poc_name) + Color.ENDC)

    def exploit(self, exp_name, ip, port, scheme, cmd):
        try:
            print(Color.OKYELLOW + "[*] Start Exploit", ip, port, exp_name + Color.ENDC)
            if self.EXPS[exp_name]().process(ip, port, scheme, cmd):
                print(Color.OKGREEN + "[+]", ip, port, exp_name + Color.ENDC)
        except BaseException:
            print(Color.WARNING + "[-] {} Exploit Failed. 请检查漏洞是否存在".format(exp_name) + Color.ENDC)

    @classmethod
    def poc_register(cls, poc_name):
        def wrapper(poc):
            cls.POCS.update({poc_name: poc})
            return poc
        return wrapper

    @classmethod
    def exp_register(cls, exp_name):
        def wrapper(exp):
            cls.EXPS.update({exp_name: exp})
            return exp
        return wrapper


class Color:
    HEADER = '\033[95m'
    OKBLUE = '\033[90m'
    OKGREEN = '\033[92m'
    OKYELLOW = '\33[93m'
    WARNING = '\033[91m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
