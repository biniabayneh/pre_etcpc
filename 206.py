class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


class Solution(object):
    def reverse_linked_list(head: ListNode) -> ListNode:
        prev = None
        current = head

while current is not None:
        # Store the next node
    next_node = current.next
        # Reverse the link
    current.next = prev
        # Move one step forward
    prev = current
    current = next_node

return prev  # New head of the reversed list


