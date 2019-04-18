from urllib import urlopen
import sys
cmd_arguments = sys.argv
base_url = "http://en.wikipedia.org/wiki/{0}"
if len(cmd_arguments) == 2:
    query = cmd_arguments[1]
    print(query)
    res = urlopen(base_url.format(query))
    print(res.read())
    res.close()
else:
    print("enter a query string")
