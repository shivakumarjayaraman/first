#!/usr/bin/env python

from sqlalchemy import *
from dbcore import *

columns = [orders.c.order_id, users.c.username, users.c.phone,
           cookies.c.cookie_name, line_items.c.quantity,
           line_items.c.extended_cost]
cookiemon_orders = select(columns)
cookiemon_orders = cookiemon_orders.select_from(orders.join(users).join( 
                        line_items).join(cookies)).where(users.c.username ==
                            'cookiemon')
print (str(cookiemon_orders))
result = connection.execute(cookiemon_orders).fetchall()
for row in result:
    print(row)

print ("***** OUTER JOIN query *******")

columns = [users.c.username, func.count(orders.c.order_id)]
all_orders = select(columns)
all_orders = all_orders.select_from(users.outerjoin(orders)) 
all_orders = all_orders.group_by(users.c.username)
result = connection.execute(all_orders).fetchall()
print (str(all_orders))
for row in result:
    print(row)
