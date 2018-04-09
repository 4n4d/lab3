Lab 3: Abstraction: implement two stack classes

Implement a stack

Implement a class Stack with the operations is_empty(), push(x), and pop().
The class should have double support for the iterator interface: there should be one "regular" iterator,
leaving the data structure intact, and one destructive iterator, which empties the stack during iteration. 

The regular iterator works like the iterators you are used to from lists and dictionaries in Python. 
The destructive iterator is to be invoked using a separate method destructive_iterator. Having a separate method 
to get an alternative iterator is a common "trick", compare with the items() method on Python dictionaries.


Constraints

Use the builtin list datastructure for the internal representation, but the internal implementation should not be exposed to the user.
The Stack class should be put into its own module, stack.py.

Your implementation must work together with the code given in the program, usingstack.py, which imports Stack,
downloadable from the course web.


To report

The implemented class.
Demonstration of your solution working with the test code.


Hints

Use a separate class for an iterator, which is instantiated when an iteration is requested. Ideally, the iterator class does
not need to access the internals of Stack. Having separate iterator classes is the norm in languages like C++ and Java. 
It is good if you iterate from the top of the stack to the bottom. 





Reimplement a stack

In this assignment, you are to change the internal stack representation of the Stack class, but retain the same interface 
so users of Stack do not need to change their code. 


Copy your file stack.py to tuplestack.py and make the changes in the latter file.

In tuplestack.py, the internal representation is done using tuples. For example, the empty stack is () and after pushing an element 7, 
the stack is (7,()). Pushing 11, the stack is (11, (7, ())).


Constraints

The reimplemented Stack should be found in a file tuplestack.py.
The new version of Stack must have the same interface as the first implementation.
Your reimplementation of Stack should work as the same way as your first implementation and it should work together with using stack.py 
when you start using the commented line at the top, importing from tuplestack.py instead of from stack.py.


To report

The implemented class.
Demonstration of your solution working with the test code.


Hint
Remember that tuples can be unpacked. That means that if we have the tuple x=(1,2), then the assignment a, b = x will let a=1 and b=2.

