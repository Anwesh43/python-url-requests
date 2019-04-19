from urllib import urlopen
from constants import wiki_url
from arg_parser import parseArgs

def call(args):
    query = args[0]
    print("making http request to wiki for {0}".format(query))
    res = urlopen(wiki_url.format(query))
    print(res.read())
    res.close()

def notFound():
    print("enter the word you want")

if __name__ == "__main__":
    parseArgs(1, call, notFound)
