# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pq = []

        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(pq,(lists[i].val,i,lists[i]))

        dummynode = ListNode()
        temp = dummynode
        while pq:
            val , i , node = heapq.heappop(pq)
            temp.next = node
            temp = temp.next

            if node.next:
                heapq.heappush(pq,(node.next.val,i, node.next))
        return dummynode.next

        
