#!/usr/bin/env python

import asyncio

async def main(f: asyncio.Future) :
    await asyncio.sleep(1)
    f.set_result('I am done')

loop = asyncio.get_event_loop()
fut = asyncio.Future()
print (fut.done())
f = loop.create_task(main(fut))
print (f, fut)
print (f == fut)
loop.run_until_complete(fut)
print (fut.done())
print (fut.result())
