#!/usr/bin/env python

from sqlalchemy import *
from datetime import datetime
from sqlalchemy.sql import select

from dbcore import *

s = select([cookies])
print (s)
rp = connection.execute(s)
results = rp.fetchall()
for r in results :
    print (r)

print ("*******************")
for r in connection.execute(cookies.select()) :
    print (r.cookie_name, r[cookies.c.cookie_name])

print (rp.keys())
rp = connection.execute(s)
print (rp.first())

s = select([cookies.c.cookie_name, cookies.c.quantity])
s = s.order_by(desc(cookies.c.quantity))
rp = connection.execute(s)
for r in rp :
    print (type(r))
    print (f"{r.quantity} -> {r.cookie_name}")

print ("********")

s = select([func.sum(cookies.c.quantity)])
rp = connection.execute(s)
print (f"# Cookies is {rp.scalar()}")

s = select([func.sum(cookies.c.quantity).label('Avail')]).where(cookies.c.cookie_name == 'chocolate chip')
rp = connection.execute(s)
record = rp.first()
print (record.items())

print ("*****")
s = select([cookies]).where(cookies.c.cookie_name.like('%choco%'))
rp = connection.execute(s)
for r in rp :
    print (r)
