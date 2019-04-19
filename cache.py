from picklerutil import *
filename = "request_cache.pkl"
class RequestCache:
    def __init__(self):
        self.request_dict = loadFromFile(filename)

    def saveResponse(self, url, text):
        self.request_dict[url] = text
        saveToFile(filename, self.request_dict)

    def getCachedResponse(self, url):
        return self.request_dict[url]

    def isInCache(self, url):
        return url in self.request_dict

reqCache = RequestCache()
