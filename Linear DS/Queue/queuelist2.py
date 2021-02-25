"""This file demonstartes the implementation of a queue by use of array/list in python by using classes and methods"""

"""Using Concepts of Advanced Python"""

class queue():
	def __init__(self):
		self.__queue=[]
		self.__size=0
		self.__front=0
	#initially we define the size of the queue to be 0, and the front to the initial postion that is 0

	"""
	q=queue()
	"""

	def enqueue(self,data):
		self.__queue.append(data)
		self.__size+=1
		#self.display()
	"""
	>>> q.enqueue(1)
	    1 --->
	>>> q.enqueue(11)
	    1 --->11 --->
	>>> q.enqueue(10)
	    1 --->11 --->10
	"""


	def dequeue(self):
		if self.__size==0:
			print("Queue is empty, returning -1")
			return -1
		else:
			self.__queue.pop(0)
			self.__size-=1

	"""
	>>> q.dequeue()
	1
	"""

	def peek(self):
		if self.__size==0:
			print("Queue is empty. Returning -1")
			return -1
		return(self.__queue[0])
	"""
	>>> q.peek()
	11
	"""

	def display(self):
		for i in self.__queue:
			print(i,"--->",end='')
		print()
	#this method is for dispaying the queue
	
	"""
	>>> q.display()
	11 --->10
	"""

	def size(self):
		return self.__size
	#returns the current size of the queue
	
	"""
	>>> print(q.size())
	2
	"""

	def isEmpty(self):
		return self.__size==0
	"""
	>>> print(q.isEmpty())
	False
	"""

"""
q=queue()
q.enqueue(1)
q.enqueue(11)
q.enqueue(10)
q.dequeue()
print(q.peek())
q.display()
print(q.size())
print(q.isEmpty())
"""

if __name__ == "__main__":

    import doctest

    doctest.testmod()
