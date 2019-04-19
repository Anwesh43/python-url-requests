import requests
from arg_parser import parseArgs
from constants import wiki_url
def getWikiResp(args):
    query = args[0]
    resp = requests.get(wiki_url.format(query))
    text = resp.text
    print(text)

def printError():
    print("enter a query param")
if __name__ == "__main__":
    parseArgs(1, getWikiResp, printError)
