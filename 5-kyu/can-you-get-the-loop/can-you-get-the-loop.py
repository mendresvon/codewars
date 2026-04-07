def loop_size(node):
    slow = node.next
    fast = node.next.next
    
    # confirm loop
    while fast != slow:
        fast = fast.next.next
        slow = slow.next
    
    # count the length of the loop
    count = 1
    fast = fast.next
    while fast != slow:
        fast = fast.next
        count += 1
    
    return count