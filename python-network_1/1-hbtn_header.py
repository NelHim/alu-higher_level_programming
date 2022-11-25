#!/usr/bin/python3
"""I documented you"""

import urllib.request
import sys

if __name__ == '__main__':
    with urllib.request.urlopen(sys.argv[1]) as response:
        header = response.info()
<<<<<<< HEAD
        print(header["X-Request-Id"]
=======
        print(header["X-Request-Id"])
>>>>>>> fb8bf7acf98a3771b9e02155953beaae03be43c6
