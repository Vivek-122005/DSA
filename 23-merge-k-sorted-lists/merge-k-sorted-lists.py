# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        import heapq
        # intitalize heap. 
        # heap item tuple = (value, )
        heap = []
        counter = 0
        merged = ListNode()
        curr = merged
        for li in range(len(lists)):
            if lists[li] == None:
                continue
            counter +=1 
            heapq.heappush(heap,(lists[li].val, counter, lists[li]) )
            

        # now we take out one element from the heap and store it in new list, and do this till heap becomes empty
        # counter is just for doing tie breaks for cases where velues of items in heap are same. since they increase everytime a new item is added to heap, it is unique. 
        while not len(heap)==0:
            item = heapq.heappop(heap)
            if item[2] != None:
                curr.next = item[2]
                curr = curr.next
                if item[2].next != None:
                    counter +=1 
                    heapq.heappush(heap, (item[2].next.val,counter,item[2].next))
                else:
                    # actually nothing is required to be done. 
                    continue
            else:
                pass

        merged = merged.next
        return merged
