import os
import datetime as dt

from engine.tool import logtool
from engine.tool import dumptool


def isExpired(fn, validDuration):
    #logtool.doLog(">> [cachetool] -- os.path.getmtime({0}) = {1}".format(fn, dt.datetime.fromtimestamp(os.path.getmtime(fn))))
    #logtool.doLog(">> [cachetool] -- dt.datetime.now() = {0}".format(dt.datetime.now()))
    iExpired = False
    #iExpired = dt.datetime.now() - dt.datetime.fromtimestamp(os.path.getmtime(fn)) > validDuration
    return iExpired

def dump(result, cacheName):
    cacheRoot = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    cacheFile = os.path.join(cacheRoot, r'cache\{0}'.format(cacheName))  # cache file path
    dumptool.dump(result, '', cacheFile)


def load(cacheName, loadFunction=None, loadParam=None, forceRetrive=0):
    cacheRoot = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    cacheFile = os.path.join(cacheRoot, r'cache\{0}'.format(cacheName))  # cache file path

    is_retrive = 0 # retrive from source data
    if loadFunction:
        if os.path.exists(cacheFile):
            if forceRetrive:
                is_retrive = 1
            else:
                is_retrive = 0
        else:
            is_retrive = 1
    else:
        is_retrive = 0


    if not is_retrive:
        result = dumptool.retrieve('', cacheFile)
    else:
        msg = ">> [cachetool] -- No cache, invoking loadFunction ..."
        logtool.doLog(msg)
        result = loadFunction() if loadParam is None else loadFunction(loadParam)
        dumptool.dump(result, '', cacheFile)

    return result