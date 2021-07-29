import json
import sys

fname = sys.argv[1]
fd = open(fname)
dalist = json.load(fd)
fd.close()

for i, ele in enumerate(dalist):
    print(ele[1])
    print(f"Tweet {i}, Length {len(ele[1])} characters")
    print('----------------')