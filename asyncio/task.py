#!/usr/bin/env python

import asyncio
from contextlib import suppress

async def main(f:asyncio.Future) :
    await asyncio.sleep(1)
    try :
        f.set_result("I have finished")
    except RuntimeError as e :
        print (f"No longer allowed {e}")
        f.cancel()

loop = asyncio.get_event_loop()
fut = asyncio.Task(asyncio.sleep(1_000_000))
print (fut.done())

loop.create_task(main(fut))
with suppress(asyncio.CancelledError) :
    loop.run_until_complete(fut)

print (fut.done())
print (fut.cancelled())


