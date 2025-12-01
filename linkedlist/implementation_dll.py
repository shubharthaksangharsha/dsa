    #What is Linkeed List? 
    #Types of Linked List and when to choose which one and when not?
    #Why Linked List over Arrays? 
    #What are the advantages and disadvantages? 
    #Important considerations when using Linked Lists 

from typing import List, Optional
class DLLNode: 
    def __init__(self, data, next_node=None, prev=None):
        self.data = data 
        self.next = next_node
        self.prev = prev  

def convert_to_dll(arr: List[int]) -> Optional[DLLNode]: 
    if arr == []: 
        return None
    head = DLLNode(arr[0])
    temp = head 
    for i in range(1, len(arr)):
        temp_node = DLLNode(arr[i], None, temp)
        temp.next = temp_node 
        temp = temp_node 
    return head 

def traverse(head: DLLNode) -> None: 
    temp = head 
    while temp:
        print(f'{temp.data} -> ', end = "")
        temp = temp.next 
    print() 

def delete_head(head: Optional[DLLNode]) -> Optional[DLLNode]: 
    #If  LL is empty or 1 ele 
    if head is None or head.next is None: 
        return None 
    #if LL have multi ele 
    new_head = head 
    new_head = head.next 
    head.next = None 
    new_head.prev = None
    return new_head

def delete_tail(head: Optional[DLLNode]) -> Optional[DLLNode]: 
    if  head  is  None or  head.next is None: 
        return None 
    temp = head 
    while temp.next: 
        temp = temp.next 
    #reached  the  last node  
    temp.prev.next = None 
    temp.prev  = None  
    return head 

def delete_kth_node(head: Optional[DLLNode], k: int) -> Optional[DLLNode]: 
    #Assuming 1 <= k <= len(head) 
    if head is None: 
        return None 
    count, temp = 0, head 
    while temp:
        count += 1
        if count == k: 
            break 
        temp = temp.next 
    prev_node, next_node  = temp.prev, temp.next
    #Only 1 ele:
    if  prev_node is None and next_node is None: 
        return None
    #Standing at first node:
    if prev_node is None:
        head = delete_head(head)
        return head 
    #Standing at last node:
    if next_node is None: 
        head = delete_tail(head)
        return head 
    #Standing in between: 
    prev_node.next = next_node 
    next_node.prev = prev_node 
    temp.next = None
    temp.prev = None 
    return head 
if  __name__ == '__main__':
    head = convert_to_dll([1, 2, 3, 4])
    traverse(head)
    # head = delete_head(head)
    # head = delete_tail(head)
    head = delete_kth_node(head, 1)
    traverse(head)