#!/usr/bin/env python

import struct

fmt = "<3s3sHH"

with open("example.gif", "rb") as gif :
    #img = memoryview(gif.read())
    img = gif.read()

header = img[:10]
print (bytes(header))

tup = struct.unpack(fmt, header)
print (f"Dimensions are {tup[2]}x{tup[3]}")


