import sys
from main import go

if (len(sys.argv) > 1):
    go(state=sys.argv[1])

else:
    go()

