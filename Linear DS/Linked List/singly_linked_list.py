#18-01-2021
#Singly Linked List
#NOTE:- LL means Linked List (Singly/Simple Linked List)

class Node:
	def __init__(self,data):
		self.data=data
		self.ref=None

class LinkedList:
	def __init__(self):
		self.__head=None
		self.__size=0

	def isEmpty(self):
		return(self.__head==None)

	def display(self):
		if self.isEmpty():
			print("LL is empty.")
		else:
			n=self.__head
			while n is not None:
				print(n.data,'--->',end=' ')
				n=n.ref
		print()
		self.size_of_LL()

	def size_of_LL(self):
		print("Size of the LL:",self.__size)

	def add_at_begin(self,data):
		new_node=Node(data)
		new_node.ref=self.__head
		self.__head=new_node
		self.__size+=1

	def del_from_beg(self):
		if self.isEmpty():
			print("Can't delete elements, LL is empty.")
		else:
			n=self.__head
			self.__head=n.ref
			n.ref=self.__head
			self.__size-=1

	def add_at_end(self,data):
		if self.isEmpty():
			print("The given element was not found, since the list is empty.")
		else:
			n=self.__head
			while n.ref is not None:
				n=n.ref
			new_node=Node(data)
			n.ref=new_node
			self.__size+=1

	def del_at_end(self):
		if self.isEmpty():
			print("Can't delete elements, LL is empty.")
		elif self.__head.ref==None:
			self.__head=None
			self.__size-=1
			print("LL has become empty, after deleting the last element from the end.")
		else:
			n=self.__head
			while n.ref.ref is not None:
				n=n.ref
			n.ref=None
			self.__size-=1


	def add_after_node(self,data,x):
		if self.isEmpty():
			print("Can't add after specified node",x,"Since, the LL is empty.")
			return
		n=self.__head
		while n is not None:
			if n.data==x:
				break
			n=n.ref
		if n is None:
			print("Given node",x,"not found in LL.")
			return
		elif n.ref==None: #add after the last node
			new_node=Node(data)
			n.ref=new_node			
		else:
			new_node=Node(data)
			new_node.ref=n.ref
			n.ref=new_node
		self.__size+=1


	def del_after_node(self,x):
		if self.isEmpty():
			print("Can't delete elements, LL is empty.")
		else:
			n=self.__head
			while n.ref is not None:
				if n.data==x:
					break
				n=n.ref
			if n.ref is None:
				print("Given node",x,"not found in the LL.")
				return
			else:
				n.ref=n.ref.ref
				#n.ref=None
			self.__size-=1
				

	def add_before_node(self,data,x):
		if self.isEmpty():
			print("LL is empty, so can't perform the add_before_node method.")
		elif self.__head.data==x: #adding before first node
			new_node=Node(data)
			new_node.ref=self.__head
			self.__head=new_node
			self.__size+=1
		else:
			n=self.__head
			while n.ref is not None: #if n.ref is None, it means that we have to insert before the last node
				if n.ref.data==x:
					break
				n=n.ref
			if n.ref is None:
				print("Given node",x,"was not found in the LL")
				return
			else:
				new_node=Node(data)
				new_node.ref=n.ref
				n.ref=new_node
		self.__size+=1

	def del_before_node(self,x):
		if self.isEmpty():
			print("LL is empty, so can't perform the del_before_node method.")
			return
		if self.__head.data==x: #deleting before the first node; not possible
			print("Can't delete anything before the FIRST node.")
			return
		n=self.__head
		while n.ref.ref is not None:
			if n.ref.data==x:
				break
			n=n.ref
		if n.ref is None:
			print("Given node",x,"not present in the LL.")
		else:
			self.del_by_value(n.data)
		self.__size-=1


	def del_by_value(self,x):
		if self.isEmpty():
			print("LL is empty, so cannot delete anything.")
			return
		if self.__head.data==x: #deleting the fist node
			self.__head=self.__head.ref
			return
		n=self.__head
		while n.ref is not None:
			if n.ref.data==x:
				break
			n=n.ref
		if n.ref is None: #we have reached to the last node
			print("Given node",x,"not found in the LL.")
		else:
			n.ref=n.ref.ref
		self.__size-=1





LL1=LinkedList()
'''LL1.add_at_begin(15)
LL1.add_at_begin(35)
LL1.add_after_node(1500,15)
LL1.add_after_node(3500,35)
LL1.add_after_node(3500,385)
LL1.add_at_end(456)
LL1.add_before_node(7800,15)
LL1.add_before_node(7811,35)
LL1.add_before_node(7822,456)
LL1.add_before_node(92793,6387)'''
'''LL1.del_by_value(7811)
LL1.del_by_value(456)
LL1.del_by_value(900)
LL1.del_before_node(15)
LL1.del_by_value(15)
LL1.del_after_node(7811)
LL1.del_after_node(456)
LL1.del_after_node(7822)
LL1.del_from_beg()
LL1.del_at_end()'''
'''LL1.del_at_end()
LL1.del_at_end()
LL1.del_at_end()'''

print("\nFrom first node:")
LL1.display()
