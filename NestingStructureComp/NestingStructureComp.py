import re

def recursiveHandler(l, f):
    try:
        for n, i in enumerate(l):
            if type(i) is list:
                l[n] = recursiveHandler(l[n], f)
            elif type(i) is str:
                l[n] = f(i)
            else:
                l[n] = f(str(i))
    except TypeError:
        pass
    return l

def NestingStructureComp(list1, list2):
    func = lambda s: re.sub(r'[0-9a-zA-Z-;,.\[\]\'\"]+', s, '')
    return recursiveHandler(list1, func) == recursiveHandler(list2, func)

print(NestingStructureComp([ 1, 1, 1 ], [ 2, 2, 2 ])) # true
print(NestingStructureComp([ 1, [ 1, 1 ] ], [ 2, [ 2, 2 ] ])) # true
print(NestingStructureComp([ 1, [ 1, 1 ] ], [ [ 2, 2 ], 2 ])) # false
print(NestingStructureComp([ 1, [ 1, 1 ] ], [ [ 2 ], 2 ])) # false
print(NestingStructureComp([ [ [ ], [ ] ] ], [ [ [ ], [ ] ] ])) # true
print(NestingStructureComp([ [ [ ], [ ] ] ], [ [ 1, 1 ] ])) # false
