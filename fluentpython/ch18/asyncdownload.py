#!/usr/bin/env python

import asyncio
import aiohttp

urls = ['http://www.rediff.com', 'http://www.cisco.com', 'http://www.hp.com', 'http://www.cnn.com', 'http://www.hindustantimes.com']
files = ['rediff.html', 'cisco.html', 'hp.html', 'cnn.html', 'ht.html']

async def savefile(f, c) :
    f = os.path.join("/tmp", f)
    with open(f, "wb") as fp :
        fp.write(c)

async def downloadurl(url, fname) :
    res = await aiohttp.request('GET', url)
    await savefile(fname, res.content)
    return "Done"

def downloadAll() :
    loop = asyncio.get_event_loop()
    todo = [await downloadurl(u, f) for u, f in zip(urls, files)]
    res, _ = loop.run_until_completion(todo)

    loop.close()
    return len(result)

if __name__ == "__main__" :
    print (downloadAll())

