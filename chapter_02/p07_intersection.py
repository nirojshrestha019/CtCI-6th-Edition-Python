from linked_list import LinkedList


def intersection(list1, list2):
    # check if the tails are similar not by value but by reference
    if list1.tail is not list2.tail:
        return False

    shorter = list1 if len(list1) < len(list2) else list2
    longer = list2 if len(list1) < len(list2) else list1

    diff = len(longer) - len(shorter)

    shorter_node, longer_node = shorter.head, longer.head

    """
    chop off the longer node so that when we traverse through two linked list,
    the collision of two is the starting point of the intersection
    """
    for _ in range(diff):
        longer_node = longer_node.next

    while shorter_node is not longer_node:
        shorter_node = shorter_node.next
        longer_node = longer_node.next

    return longer_node


def test_linked_list_intersection():
    shared = LinkedList()
    shared.add_multiple([1, 2, 3, 4])

    a = LinkedList([10, 11, 12, 13, 14, 15])
    b = LinkedList([20, 21, 22])

    # link a to shared linkedlist
    a.tail.next = shared.head
    a.tail = shared.tail
    # link b to shared linkedlist
    b.tail.next = shared.head
    b.tail = shared.tail
    
    print(a)
    print(b)
    # should be 1

    print(intersection(a, b))
    # hardcoded assert: insersection value == begining of the shared linked list by refernce
    # if we find the collision point not by value but by reference then this is intersection
    assert intersection(a, b).value == 1

test_linked_list_intersection()