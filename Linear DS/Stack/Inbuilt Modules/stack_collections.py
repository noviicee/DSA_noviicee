"""
This file demonstartes the implementation of a stack by use of inbuilt module named 'collections'.
The deque class in the module named collection can be used to implement a stack.
It provides methods which allow us to enter and remove elements/data from both sides,
but for implementing a stack, we need just one side.
[queque] : 'double-ended-queue'
"""

"""
To implement a stack, we must follow FILO/LIFO order.
This means elements must be inserted and removed from the same end
(unlike queue, where elements are added at one end, and removed from another end)
1. append() and pop()
2.appendleft() and popleft()
By default, we consider that append takes place from the right side.
So we use append() and pop()
"""

from collections import deque
stack=deque()
"""
>print(stack)
<class 'collections.deque'>
"""

def push(element):
	stack.append(element)
def pop():
	e=stack.pop()
	print("Removed element after calling pop:",e)
def peek():
	print("The top element in the stack is:",stack[-1])
def isEmpty():
	result=len(stack)==0
	print(result)
def display():
	for i in range(1,len(stack)+1):
		print(stack[-i])

# Driver Code:
if __name__=="__main__":

	push(10)
	push(100)
	push(15)
	display()
	pop()
	display()
	peek()
	isEmpty()
	
