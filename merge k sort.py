import heapq
class ListNode:
    def__init__(self,val=0
next=none):  
        self.val =Val           
        self.next =next
        
class solution:
    def mergelists(self,lists):
        heap =[]
        for i, node in emulator(lists):
            if node:
                haepq.heappus(heap,node,val,node)
                dummy =ListNode(0)
                current = dummy
                
                while heap:
                    val, i, node =heapq.heapop(heap)
                    current.next=node
                    current =current.next
                    if node.next:heapq.heappush(heap)(node,next,val,i,node.next)
 return dummy.next                   
                
                