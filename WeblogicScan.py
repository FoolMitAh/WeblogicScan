#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import argparse

from app.main import pentest, pentestmore
from app.platform import Color

banner = '''
__        __   _     _             _        ____                  
\ \      / /__| |__ | | ___   __ _(_) ___  / ___|  ___ __ _ _ __  
 \ \ /\ / / _ \ '_ \| |/ _ \ / _` | |/ __| \___ \ / __/ _` | '_ \ 
  \ V  V /  __/ |_) | | (_) | (_| | | (__   ___) | (_| (_| | | | |
   \_/\_/ \___|_.__/|_|\___/ \__, |_|\___| |____/ \___\__,_|_| |_|
                             |___/ 
'''

print(Color.OKYELLOW + banner + Color.ENDC)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-u", "--url", help="URL (e.g. 'http://127.0.0.1:7001/')")
    group.add_argument("-f", "--file", help="FILE (e.g. 'targets.txt')")
    parser.add_argument("-n", "--name", help="NAME (e.g. 'CVE-2019-2729')")
    parser.add_argument("-e", "--exec", help="EXEC (e.g. 'whoami')")
    args = parser.parse_args()
    if args.url:
        pentest(args.url, poc=args.name, cmd=args.exec)
    elif args.file:
        with open(args.file) as f:
            urls = f.read().splitlines()
        # pentestmore(targets)
        for url in urls:
            pentest(url)
    else:
        print("error: missing a mandatory option (-u or -f), use -h for basic help")
