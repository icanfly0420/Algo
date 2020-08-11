class Node:
    def __init__(self, elem, _next=None):
        self._elem = elem
        self._next = _next


def reserve(node):
    one = None
    next = node._next
    node._next = one
    one = node
    node = next
    return one


if __name__ == '__main__':
    node1 = Node(1)
    node2 = Node(2)
    node1._next = node2
    print(node2._next)