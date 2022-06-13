class Node:

    def __init__(self, number: int):
        self.number = number
        self.next = None

    def __str__(self):
        return str(self.number)


class LinkedList:

    def __init__(self, node: Node):
        self.head = node

    def add(self, node: Node):
        current = self.head
        while True:
            if not current.next:
                current.next = node
                break
            current = current.next


class LinkedListIterator:

    def __init__(self, linked_list: LinkedList):
        self.linked_list = linked_list

    def iterate(self):
        current = self.linked_list.head
        while current:
            print(f"{current}")
            current = current.next


if __name__ == '__main__':
    linked_list = LinkedList(Node(5))
    linked_list.add(Node(6))
    linked_list.add(Node(7))
    linked_list.add(Node(8))
    iterator_linked_list = LinkedListIterator(linked_list)
    iterator_linked_list.iterate()
