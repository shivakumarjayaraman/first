#!/usr/bin/env python

import asyncio

async def f() :
    pass

coro = f()
loop = asyncio.get_event_loop()

task = loop.create_task(coro)
print (coro, task)
assert isinstance(task, asyncio.Task)

new_task = asyncio.ensure_future(coro)
assert isinstance(new_task, asyncio.Task)

mystery_meat = asyncio.ensure_future(task)
assert mystery_meat is task
print (task, mystery_meat, new_task)


