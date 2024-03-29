#!/usr/bin/env python

def to_str(bytes_or_str) :
    if isinstance(bytes_or_str, bytes) :
        return bytes_or_str.decode('utf-8')
    return bytes_or_str

def to_bytes(bytes_or_str) :
    if isinstance(bytes_or_str, str) :
        return bytes_or_str.encode('utf-8')
    return bytes_or_str
