"""
Stack   ----->   List
---------------------
push    ----->   append
pop     ----->   pop
"""

class Stack:
	def __init__(self):
		self.__stack=[]
	"""
	initialising stack
	"""

	def push(self,item):
		"""
		push() method for stack
		appending elements in the stack
		"""
		self.__stack.append(item)

	def pop(self):

		"""
		pop() method for stack
		"""
		if self.__stack:
			element=self.__stack.pop()
			print("Removed element after calling pop: ",element)
		else:
			print("Stack is empty!")
		"""
		removes the last item inserted in the stack
		if stack is not empty
		same as FILO/LIFO order follows
		"""

	def peek(self):
		"""
		displays the top element of the stack
		"""
		print("Topmost element in the stack is:",self.__stack[-1])

	def isEmpty(self):
		"""
		returns True if the stack is empty, else returns false
		"""
		result=len(self.__stack)==0
		print(result)

	def display(self):
		for i in self.__stack[::-1]:
			print(i)

# Driver Code:
if __name__=="__main__":


	st1=Stack()
	st1.push(10)
	st1.push(100)
	st1.push(15)
	st1.display()
	st1.pop()
	st1.display()
	st1.peek()
	st1.isEmpty()
	
