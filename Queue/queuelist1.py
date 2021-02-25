"""This file demonstartes the implementation of a queue by use of array/list in python by simple method"""

"""Using Core Python"""

queue=[]
#created a list of name queue, which will be treated as queue DS

"""
Here we use the following acronyms-

Queue -----> List
enqueue ---> append
dequeue ---> pop
"""

queue.append(10)
"""10 is added to the queue and it stands like-
queue=10"""

queue.append(20)
queue.append(30)
queue.append(40)
""" after adding all these elements, thq queue-
queue= 10,20,30,40 

->we assume that the 'append()' operation adds elements from the right side of the queue
"""

queue.pop(0)
"""by default, the 'pop()' operation removes the elements from the right of the list, but this is opposite in the queue DS. Hence, we have to explixitly pop from the left
So we use pop(0)
Now the queue is like-
queue= 20,30,40"""

queue.pop(0)
#queue= 20,30,40

queue.pop(0)
#queue= 30,40

queue.pop(0)
#queue= 40

queue.pop(0)
#queue = 'Null'

queue.pop(0)
#IndexError: pop() form emoty list

"""
Hence while using this method, we need to make sure that the list is not empty before removig elements
"""