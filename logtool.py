import datetime as dt
import os

from engine.tool import datetool
from engine.conf import param

SINGLE_SEP_LINE = '\n' + '-'*30


cache = []


def doLog(msg):
    """

    :rtype : None
    """
    current_time = datetool.fmt2str(dt.datetime.now())
    content = "{0} : \t{1}".format(current_time, msg)
    print(content)

    global cache
    cache.append(content + '\n')

    if len(cache) >= 10:
        toDisk()


def toDisk():
    global cache
    if len(cache) > 0:
        with open(os.path.join(param.BASE_PATH, 'log.txt'), 'a') as f:
            f.writelines(cache)
            cache = []


def printProgress(i, N, p0, p1):  # p0% - p1% progress
    doLog('>> PROGRESS(%): {0}\n'.format(int((p1-p0) * i / N) + p0))