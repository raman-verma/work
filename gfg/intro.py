class Node:
    # Init the node object
    def __init__(self, data):
        self.data = data
        self.next = None


# create LL class contain node object
class LL:
    def __init__(self):
        self.head = None

    def printlist(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


if __name__ == '__main__':
    # start empty list
    ll = LL()

    ll.head = Node(1)
    a = Node(2)
    b = Node(3)

    ll.head.next = a
    a.next = b

    ll.printlist()
