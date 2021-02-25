#Queue
*******

Queue is a [Linear Data Structutre](#) where the elements are inserted from one side and are removed from the other side.

The queue is an abstract datatype (called as 'interface' in [Java](#))


![basic structure of a queue](https://www.etutorialspoint.com/images/ds/doubly-ended_queue.png)


* A queue can basically be said t be opene from both the ends
   * This is the reason why insertion and removal is done at different ends of a queue.

   * The end at which elememts are added are called as **rear/back/tail**
   * The end at which elements are removed from is known as **head/front**

* Queue follows FIFO or LILO methodology
   * *FIFO: First In First Out*
   * *LILO: Last In Last Out*
   * This means that the elements inserted first will leave the queue first,and the elements inserted last will leave the queue last. (It is very similar to a  rael queue)

##Basic Operations of a simple Queue data structure:
----------------------------------------------------

-> enqueue:
-----------

The `enqueue()` method is used for adding data to the queue. The data can be of any data type- be it string, integers, float, etc.

We can say that a queue is 'heterogeneous' in nature.


->dequeue:
----------

The `dequeue()` method is used in order to remove items from a queue.

In short and exact words, **accessing the content while removing it from the front end of the queue**, is known as a Dequeue Operation.

->peek:
-------

The`peek()` method can be used to get the value of the first item from the queue.

->isFull:
---------

The `isFull()` methid can be used to check whether the queue is full or not.

The `isFull()` method is applicable only if we specify the size of the queue before-hand. In that case the `isFull()` method can be implemented as-

```Python
def isFull():
	return size==max_size
```

;where size is the current size of the queue, and max_size is the size fixed for the queue.

The function will return a boolean value.

->isEmpty:
----------

This method is very similar to the isFull() method. It can be used to check if the queue is empty or not.


##Applications of the Queue data structure:
-------------------------------------------

* When an appplication is shared with several consumers(threads), we store them in a queue.

   E.g:- CPU Scheduling

* When data is transferred asynchronously(recieving rate isn't always the same), between two processes.

   E.g:- I/O buffers

* Optional research applications or stochastic models reliy heavily on queues

* Queue is very important as far as Operating Systems are concerned.

   E.g:- Android O.S- maintains a queue, in order to track the processes it has to make

   Tasks are stored in queue ADT in O.S to enable the operating system to amke it in a sequential order.
   Also, the tasks follow FIFO order priority-wise.


##Implementation of Queue Abstract Data Type:
----------------------------------------------

Queue can also be implemented with dynamic arrays, as well as with Linked Lists.

1. By using [Array](#) (or List in python)

2. By using [Linked Lists](#)

3. By using inbuilt modules

4. From [Stacks](#)


##Complexity:
-------------

1. Enqueue: O(1)
2. Dequeue: O(1)
