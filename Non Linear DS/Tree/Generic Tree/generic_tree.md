## Generic Trees
---
Generic Trees are also called as N-array Trees.

Generic trees are a collection of nodes where each node is a data structure that consists of records and a list of references to its children (duplicate references are not allowed).


Basically, they are more like the Binary Tress and the BST, But the difference is that in case of Binary Tre, and BST, we knew that the number of children will be two-left child and right chiild.
But in the case of **Generic Trees**, we do not know how many children a node will have. It can have 0, 1, 2, 3,...any number of children.

Unlike the [linked list](https://github.com/noviicee/DSA_noviicee/tree/main/Linear%20DS/Linked%20List), each node of the generic tree stores the address of multiple nodes. THhs is because we clearly don't know the number of children a node will have. Every node stores address of its children and the very first node’s address will be stored in a separate pointer called root.

During Implementation-
<br/>
If the root is *None*, it is treated as the *'Edge-Case'*
>NOTE: Edge Case is NOT the same as *Base Case*. *Base Case* is different from *Edge-Case*.

*  The Generic trees are the N-ary trees which have the following properties: 

            1. Many children at every node.

            2. The number of nodes for each node is not known in advance.

### Example:

![Generic Tree](https://media.geeksforgeeks.org/wp-content/uploads/20190612120758/generic-tree_gfg.png)

For More Resources : [Check This Out](https://www.geeksforgeeks.org/generic-treesn-array-trees/)
