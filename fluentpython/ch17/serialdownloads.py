#!/usr/bin/env python

import requests
import os
from concurrent import futures
import time


urls = ['http://www.rediff.com', 'http://www.cisco.com', 'http://www.hp.com', 'http://www.cnn.com', 'http://www.hindustantimes.com']
files = ['rediff.html', 'cisco.html', 'hp.html', 'cnn.html', 'ht.html']


def downloadurl(url, fname) :
    res = requests.get(url)
    f = os.path.join("/tmp", fname)
    with open(f, "wb") as fp :
        fp.write(res.content)

def downloadAll() :
    t = time.time()
    for u, f in zip(urls, files) :
        downloadurl(u, f)
    elapsed = time.time() - t
    return elapsed

if __name__ == "__main__" :
    print (downloadAll())


