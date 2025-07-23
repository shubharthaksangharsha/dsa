(head: Node) -> Node: 
#     #base
#     if head is None or head.next is None: 
#         return head 
    
#     small_head = reverse_recursive(head.next) 
#     head.next.next = head 
#     head.next = None 
#     return small_head