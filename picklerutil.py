import pickle
def loadFromFile(fileName):
    dataDict = {}
    try:
        with open(fileName, 'rb') as f:
            dataDict = pickle.load(f)
    except:
        print("file doesnt exist")
    return dataDict

def saveToFile(fileName, dataDict):
    with open(fileName, 'wb') as f:
        pickle.dump(dataDict, f)
        print("saved to {0}".format(fileName))
