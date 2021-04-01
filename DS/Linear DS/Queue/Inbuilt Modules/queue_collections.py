"""
This file demonstartes the implementation of a queue by use of inbuilt module named 'collections'.
The deque class in the module named collection can be used to implement a queue.
It provides methods which allow us to enter and remove elements/data from both sides of the queue, unlike in lists/arrays.
"""

"""
To implement a queue, we must follow FIFO/LILO order.
Since here we are able to append as well as remove elemenys from both the sides of the queue, we can use two methods-
(by default, we consider that append takes place from the right side)
1. append() and popleft()
2.appendleft() and pop()
"""

#Method-1
from collections import deque
q1=deque()
"""
>>> print(q1)
deque([])
"""

q1.append(10)
q1.append(20)
"""
>>> print(q1)
deque([10,20])
"""
while q1:
	q1.popleft()
"""
>>> print(q1)
deque([])
"""

"""
For the above method, we can use index to access elements at the front as well as rear side
>>> q1.append(20)
>>> q1.append(10)
>>> q1.append(15)
>>> print(q1[-1]
5
>>> print(q1[0])
20
"""


#Method-2
from collections import deque
q2=deque()
"""
>>> print(q2)
deque([])
"""

q2.appendleft(15)
q2.appendleft(25)
"""
>>> print(q2)
deque([15,25])
"""
while q2:
	q2.pop()
"""
>>> print(q2)
deque([])
"""

"""
For the above method, we can use index to access elements at the front as well as rear side
>>> q2.append(20)
>>> q2.append(10)
>>> q2.append(15)
>>> print(q2[-1]
5
>>> print(q2[0])
20
"""

if __name__ == "__main__":
    import doctest
    doctest.testmod()






