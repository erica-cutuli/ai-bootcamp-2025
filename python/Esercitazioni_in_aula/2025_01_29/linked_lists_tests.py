from linked_lists import LinkedList, Node

# Part 1 - tests for the nodes of a linked list

head_node = Node("Napoli")

assert head_node.next is None

head_node.next = Node("Rome")
head_node.next.next = Node("Milan")

# Part 2 - tests for the linked list

my_list = LinkedList()

assert len(my_list) == 0
assert my_list.head is None

my_list.add_node(data="Napoli")

assert len(my_list) == 1
assert my_list.head.data == "Napoli"

my_list.add_node(data="Milan")

assert len(my_list) == 2

# Check that we have two objects of type Node
assert [type(el) for el in my_list] == [Node, Node]

