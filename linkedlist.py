class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def follow(self):
        node = self
        while True:
            if node.next is None:
                break
            prev_node = node
            node = node.next
            yield prev_node
        yield node

    def show(self):
        for el in self.follow():
            print(el.val)
        

ll = ListNode(1, ListNode(2, ListNode(3, None)))
ll.show()
