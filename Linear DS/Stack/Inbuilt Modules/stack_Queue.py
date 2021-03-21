"""
This file demonstartes the implementation of a stack by use of inbuilt module named 'queue'.
The LifoQueue class in queue module can be used to implement a stack.
"""

import queue

"""
Stack   ----->   queue Module
push    ----->   put
pop     ----->   get
"""

stack=queue.LifoQueue()
"""
>print(stack)
<queue.LifoQueue object at 0x000000AB1A1DFE50>
"""

"""
LifoQueue(x) can be used to limit the size of the stack to x
"""

def push(element):
	stack.put(element)
def pop():
	e=stack.get(timeout=1)
	print("Removed element is:",e)
	"""
	The get method in LifoQueue when applied on an empty LifoQueue object,
	will block the process, creatind an infinite loop until it finds an element.

	To solve this problem, 
	we can use the 'timeout' parameter in both get() and put() functions.
	
	It is useful in case of put(), if the size of the stack has been specified.
	"""
def isEmpty():
	result=stack.empty()
	print(result)

'''
def display():
	while stack:
		pop()
'''

# Driver Code:
if __name__=="__main__":

	push(10)
	push(100)
	push(15)
	#display()
	pop()
	#display()
	#peek()
	isEmpty()