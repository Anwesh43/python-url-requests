import requests
from arg_parser import parseArgs
from constants import wiki_url
from cache import reqCache

def parseTag(respTxt, tag):
    firstTitleParts = respTxt.split("<{0}>".format(tag))
    if len(firstTitleParts) > 1:
        secondTitleParts = firstTitleParts[1].split("</{0}>".format(tag))
        if len(secondTitleParts) > 0:
            return secondTitleParts[0]

    return ""

def getWikiResp(args):
    query = args[0]
    url = wiki_url.format(query)
    if reqCache.isInCache(url):
        print("getting from cache \n")
        respTxt = reqCache.getCachedResponse(url)
        title = parseTag(respTxt, "title")
        print("the title of the page is")
        print(title)
    else:
        print("making fresh request \n \n")
        resp = requests.get(url)
        text = resp.text
        print(text)
        print("saving in cache")
        reqCache.saveResponse(url, text)

def printError():
    print("enter a query param")
if __name__ == "__main__":
    parseArgs(1, getWikiResp, printError)
