#!/usr/bin/env python

import asyncio, time

async def main() :
    print (f"{time.ctime()} Hello")
    print (asyncio.get_running_loop())
    await asyncio.sleep(1.0)
    print (f"{time.ctime()} Goodbye ")

x = main()
loop = asyncio.get_event_loop()
task = loop.create_task(x)
print (type(x), type(loop), type(task))
print (x, loop,  task)
loop.run_until_complete(task)
pending = asyncio.all_tasks(loop=loop)
print (type(pending))
for task in pending :
    print ("Cancelling ", type(task))
    task.cancel()
group = asyncio.gather(*pending, return_exceptions=True)
print (type(group))
loop.run_until_complete(group)
loop.close()



