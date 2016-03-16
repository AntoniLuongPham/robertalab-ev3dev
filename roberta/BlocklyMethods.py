import math
import os


class BlocklyMethods:
    GOLDEN_RATIO = (1 + math.sqrt(5)) / 2

    @staticmethod
    def isEven(number):
        return (number % 2) == 0

    @staticmethod
    def isOdd(number):
        return (number % 2) == 1

    @staticmethod
    def isPrime(number):
        for i in xrange(2, math.sqrt(number)):
            remainder = number % i
            if remainder == 0:
                return False
        return True

    @staticmethod
    def isWhole(number):
        return number % 1 == 0

    @staticmethod
    def isPositive(number):
        return number > 0

    @staticmethod
    def isNegative(number):
        return number < 0

    @staticmethod
    def isDivisibleBy(number, divisor):
        return number % divisor == 0

    @staticmethod
    def remainderOf(divident, divisor):
        return divident % divisor

    @staticmethod
    def clamp(x, min_val, max_val):
        return min(max(x, min_val), max_val)

    # note: we don't use the random module since it is large
    @staticmethod
    def randInt(min_val, max_val):
        b = os.urandom(4)
        val = ord(b[0]) << 24 | ord(b[1]) << 16 | ord(b[2]) << 8 | ord(b[3])
        if min_val < max_val:
            return min_val + (val % (max_val - min_val))
        else:
            return max_val + (val % (min_val - max_val))

    @staticmethod
    def randDouble():
        b = os.urandom(4)
        val = ord(b[0]) << 24 | ord(b[1]) << 16 | ord(b[2]) << 8 | ord(b[3])
        return float(val) / 0xffffffff

    @staticmethod
    def textJoin(*args):
        return "".join(args)

    @staticmethod
    def length(_list):
        return len(_list)

    @staticmethod
    def isEmpty(_list):
        return not _list

    @staticmethod
    def createListWith(*args):
        return list(args)

    @staticmethod
    def createListWithItem(item, times):
        return [item] * times

    @staticmethod
    def listsGetSubList():
        # FIXME:
        pass

    @staticmethod
    def findFirst(_list, item):
        try:
            return _list.index(item)
        except:
            return -1

    @staticmethod
    def findLast(_list, item):
        try:
            _list[::-1].index(item)
        except:
            return -1

    @staticmethod
    def listsIndex():
        # FIXME:
        pass

    @staticmethod
    def sumOnList():
        # FIXME:
        pass

    @staticmethod
    def minOnList():
        # FIXME:
        pass

    @staticmethod
    def maxOnList():
        # FIXME:
        pass

    @staticmethod
    def averageOnList():
        # FIXME:
        pass

    @staticmethod
    def medianOnList():
        # FIXME:
        pass

    @staticmethod
    def standardDeviatioin():
        # FIXME:
        pass

    @staticmethod
    def randOnList():
        # FIXME:
        pass

    @staticmethod
    def modeOnList():
        # FIXME:
        pass
