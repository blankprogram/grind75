class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return False

        slow = head  # Slow pointer moves one step at a time
        fast = head  # Fast pointer moves two steps at a time

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                # Cycle detected
                return True

        return False
