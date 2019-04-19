import sys
def parseArgs(n, cb, notfoundcb):
    if len(sys.argv) == n + 1:
        cb(sys.argv[1:])
    else:
        notfoundcb()
