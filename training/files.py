__author__ = 'ja'

import json

# f = open("config.json")
with open("config.json") as f:
    try:
        res = json.load(f)
    except ValueError as ex:
        print(ex)
        res = {}
    # finally:
    #     f.close()

print(res)
