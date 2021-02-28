#!/usr/bin/env python

import asyncio, time

async def main() :
    print (f"{time.ctime()} Hello")
    await asyncio.sleep(1.0)
    print (f"{time.ctime()} Goodbye ")

x = main()
print (type(x))
asyncio.run(x)

