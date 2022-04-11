from linked_list import LinkedList


def loop_detection(ll):
    fast = slow = ll.head

    while fast and fast.next:
        # move fast at a rate of 2 step
        fast = fast.next.next
        # move slow at the rate of 1
        slow = slow.next
        # break at the point where fast meets slow in the loop
        if fast is slow:
            break

    if fast is None or fast.next is None:
        return None

    # assign slow to head and fast is at the point of intersection of slow and fast in the loop
    slow = ll.head
    while fast is not slow:
        # move both fast and slow with 1 step
        # the point of intersection of fast and slow is the starting point of  the loop
        fast = fast.next
        slow = slow.next

    return fast


def test_loop_detection():
    looped_list = LinkedList(["A", "B", "C", "D", "E", "F", "G"])
    # assume loop starting point is C
    loop_start_node = looped_list.head.next.next
    looped_list.tail.next = loop_start_node
    print("loop start node: ", loop_start_node)
    tests = [
        (LinkedList(), None),
        ((LinkedList((1, 2, 3))), None),
        (looped_list, loop_start_node),
    ]

    for ll, expected in tests:
        assert loop_detection(ll) == expected

test_loop_detection()