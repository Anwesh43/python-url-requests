from picklerutil import *
dict1 = loadFromFile('a.pickle')
assert dict1 == {}
dict2 = {}
dict2["a"] = 1
dict2["b"] = 2
saveToFile('a.pkl', dict2)
dict3 = loadFromFile('a.pkl')
assert dict3 == dict2
