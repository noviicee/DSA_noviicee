"""
This file demonstartes the implementation of a queue by use of inbuilt module named 'Queue'.
The queue class in Queue module can be used to implement a queue.
"""


import queue
"""
Queue module-
->queue
->lifoqueue
->priorityqueue
"""
q3=queue.Queue() #by defalut, size of queue=infinite
#
q3.put(10)
q3.put(20)
q3.put(30)
"""
>>> print(q3)
<queue.Queue object at 0x0000009FFAFFF970>
"""
q3.get() #10
q3.get() #20
q3.get() #30

""""
>>> g3.get()
blocks and waits until an element is available
"""

"""
To prevent from such conditions we use get_nowait()
"""




"""
Some more methods which can be used in this implemnting queue from queue class.
* queuesize() ->  to get the size of the queue #q.size()
* q.empty() -> to check if the queue is empty or not
* q.full() -> to check if the queue is full or not

* q.put() -> to put items in the queue
->> q.put(item,block=True,timeout)
if block is True, and  timeout is None, it will block the addition of elements if the queue is full until free slot is available.

To prevent this kind of thing, we can-
-set block=False
-set timeout
-use another method called 'Put_nowait(item)'

*Put_nowait(item)-> it does not wait for an empty slot, but gives a message that the queue is full.

Note:- We will encounter the condition of a full queue only if we set the maxsize for the queue; maxsize>0
By default, the maxsize for the queue is infinite.

*q.get(block=True,timeout=None)
*q.get_nowait(item)

Note:- get() works in the same way as put()
"""
