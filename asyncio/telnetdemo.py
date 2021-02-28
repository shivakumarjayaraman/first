#!/usr/bin/env python

import asyncio
from asyncio import StreamReader, StreamWriter

async def echo(reader: StreamReader, writer: StreamWriter) :
    print ("New Connection")
    try :
        while True:
            data = await reader.readline()
            if (not data) : break
            writer.write(data.upper())
            await writer.drain()
        print ("Leaving connection")
    except asyncio.CancelledError :
        print ("Connection Dropped")

async def main(host='127.0.0.1', port=8888) :
    server = await asyncio.start_server(echo, host, port)
    async with server : 
        await server.serve_forever()

try :
    asyncio.run(main())
except KeyboardInterrupt :
    print ("Bye")
