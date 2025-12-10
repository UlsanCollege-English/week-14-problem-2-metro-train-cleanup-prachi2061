"""
HW02 — Metro Train Cleanup (Linked List Filter)

Implement a singly linked list Node class and a function remove_cars(head, target)
that removes all nodes with value == target and returns the new head.
"""


class Node:
    """
    Simple singly linked list node.

    value: the car ID (int or any value)
    next: the next Node in the list, or None
    """

    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def remove_cars(head, target):
    """
    Remove all nodes whose value == target from the list starting at head.

    :param head: Node or None, the head of the list
    :param target: value to remove from the list
    :return: new head Node (or None if list becomes empty)
    """
    dummy = Node(None, head)
    current = dummy

    while current.next is not None:
        if current.next.value == target:
            current.next = current.next.next
        else:
            current = current.next

    return dummy.next


if __name__ == "__main__":
    n4 = Node(3)
    n3 = Node(2, n4)
    n2 = Node(2, n3)
    n1 = Node(1, n2)

    new_head = remove_cars(n1, 2)
    curr = new_head
    values = []
    while curr is not None:
        values.append(curr.value)
        curr = curr.next
    print(values)
