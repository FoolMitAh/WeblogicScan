#!/usr/bin/env python
# _*_ coding:utf-8 _*_

from concurrent import futures
from .platform import ManageProcessor

MAX_WORKERS = 10


def pentest(target):
    processor = ManageProcessor()
    # print(processor.PLUGINS)
    # {'plugin1': <class '__main__.CleanMarkdownBolds'>}
    processor.process(target)
    # processed = processor.process(text="**foo bar**", plugins=('plugin2',))


def pentestmore(targets):
    processor = ManageProcessor()
    with futures.ProcessPoolExecutor(max_workers=MAX_WORKERS) as executor:
        executor.map(processor.process, targets)
