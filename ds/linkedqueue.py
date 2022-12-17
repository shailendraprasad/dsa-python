class LinkedQueue:
    """
    Queue implementation using the linked list
    """

    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._tail = None
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def enqueue(self, e):
        if self.is_empty():
            self._head = self._Node(e, None)
            self._tail = self._head
        else:
            self._tail._next = self._Node(e, None)
            self._tail = self._tail._next
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            return "Empty Queue, cannot dequeue anymore. Please enqueue"
        else:
            answer = self._head._element
            self._head = self._head._next
            self._size -= 1
            return answer


"""
Some test cases below to make sure the queue and dequeue is working fine
"""
# q = LinkedQueue()
# q.enqueue(1)
# q.enqueue(5)
# q.enqueue(9)
# q.enqueue(0)
# print('length of the queue is : ' + str(len(q)))
# print(q.dequeue())
# print(q.dequeue())
# print(q.dequeue())
# print(q.dequeue())
# q.enqueue(120)
# print(q.dequeue())
