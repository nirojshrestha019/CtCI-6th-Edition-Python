from linked_list import LinkedList


def partition(ll, x):
    current = ll.tail = ll.head

    while current:
        next_node = current.next
        current.next = None
        # elements smaller than the pivot element are put at the head
        if current.value < x:
            current.next = ll.head
            ll.head = current
        # elements bigger than the pivot element are put at the tail
        else:
            ll.tail.next = current
            ll.tail = current
        current = next_node

    # Error check in case all nodes are less than x
    if ll.tail.next is not None:
        ll.tail.next = None


def example():

    ll = LinkedList.generate(10, 0, 99)
    print(ll)
    # here head value is the pivot element
    partition(ll, ll.head.value)
    print(ll)


if __name__ == "__main__":
    example()
    print("Local test")
    ll = LinkedList()
    ll.add_multiple([1, 13, 22, 2, 3, 7, 1, 3, 4])
    print(ll)
    partition(ll, 13)
    print(ll)
