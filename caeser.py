#!/usr/bin/env python

def enc(s, n) :
    return "".join(chr(((ord(c) + n - ord('a')) % 26) + ord('a')) for c in s.lower())

def dec(s, n) :
    return "".join(chr(ord(c) - n)  if  ord(c)-n >= ord('a') else chr(ord(c) - n + 26) for c in s.lower())

print (enc("matrix", 3))
print (dec("pdwula", 3))


