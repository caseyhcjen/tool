import pickle as cPickle

from engine.tool import logtool


def dump(objToDump, objName, fileName):
    logtool.doLog('>> [dumptool] -- Dumping {0} to {1} ...'.format(objName, fileName))
    with open(fileName, 'wb') as f:
        cPickle.dump(objToDump, f)    


def retrieve(objName, fileName):
    logtool.doLog('>> [dumptool] -- Retrieving {0} from {1} ...'.format(objName, fileName))
    with open(fileName, 'rb') as f:
        result = cPickle.load(f)
    return result
