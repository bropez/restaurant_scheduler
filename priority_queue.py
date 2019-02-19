class Node:
    def __init__(self, _value, _weight, _name):
        self.value = _value
        self.weight = _weight
        self.name = _name
        self.next = None

    def set_next(self, _next):
        self.next = _next

    def return_next(self):
        return self.next


def print_nodes(_head):
    while _head:
        print(_head.value, _head.weight, _head.name)
        _head = _head.next


def insert_node(_head, insertee):
    dummy = Node(0, 0, "dummy")
    dummy.next = _head
    prev = dummy
    curr = _head

    while curr:
        if insertee.weight <= curr.weight:
            insertee.next = curr
            prev.next = insertee
            return dummy.next
        elif insertee.weight >= curr.weight and not curr.next:
            curr.next = insertee
            return dummy.next
        prev = curr
        curr = curr.next


def remove_node(_head, _name):
    dummy = Node(0, 0, "dummy")
    dummy.next = _head
    prev = dummy
    curr = _head

    while curr:
        if curr.name is _name:
            prev.next = curr.next
            curr.next = None
            return dummy.next

        prev = curr
        curr = curr.next


if __name__ == "__main__":
    # This is all to test if this is working as should be
    # creating the nodes
    node1 = Node(1, 4, "First")
    node2 = Node(2, 5, "Second")
    node3 = Node(3, 2, "Third")
    node4 = Node(4, 1, "Fourth")
    node5 = Node(5, 9, "Fifth")

    # testing the insert method and creation of list
    head = node1
    head = insert_node(head, node2)
    head = insert_node(head, node3)
    head = insert_node(head, node4)
    head = insert_node(head, node5)
    print_nodes(head)
    print("break")

    # testing the remove method
    head = remove_node(head, "Fourth")
    print_nodes(head)


