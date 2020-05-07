#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import argparse

from app.main import pentest, pentestmore
from app.platform import Color

version = "1.3.1"
banner = '''
__        __   _     _             _        ____                  
\ \      / /__| |__ | | ___   __ _(_) ___  / ___|  ___ __ _ _ __  
 \ \ /\ / / _ \ '_ \| |/ _ \ / _` | |/ __| \___ \ / __/ _` | '_ \ 
  \ V  V /  __/ |_) | | (_) | (_| | | (__   ___) | (_| (_| | | | |
   \_/\_/ \___|_.__/|_|\___/ \__, |_|\___| |____/ \___\__,_|_| |_|
                             |___/ 
      From WeblogicScan V1.2 Fixed by Ra1ndr0op: drops.org.cn | V {} 
'''.format(version)

print(Color.OKYELLOW + banner + Color.ENDC)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-u", "--url", help="URL (e.g. 'http://127.0.0.1:7001/')")
    group.add_argument("-f", "--file", help="FILE (e.g. 'targets.txt')")
    args = parser.parse_args()
    if args.url:
        pentest(args.url)
    elif args.file:
        with open(args.file) as f:
            urls = f.read().splitlines()
        # pentestmore(targets)
        for url in urls:
            pentest(url)
    else:
        print("error: missing a mandatory option (-u or -f), use -h for basic help")
