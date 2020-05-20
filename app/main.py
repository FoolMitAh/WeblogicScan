#!/usr/bin/env python
# _*_ coding:utf-8 _*_

from concurrent import futures
from .platform import ManageProcessor

MAX_WORKERS = 10


def pentest(target, poc=None, cmd=None):
    processor = ManageProcessor()
    # print(processor.POCS)
    if poc is not None:
        processor.process(target, pocs=(poc,), cmd=cmd)
    else:
        processor.process(target)


def pentestmore(targets):
    processor = ManageProcessor()
    with futures.ProcessPoolExecutor(max_workers=MAX_WORKERS) as executor:
        executor.map(processor.process, targets)
