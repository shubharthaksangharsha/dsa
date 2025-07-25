from mylink import MyLinkedList, Node
from typing import Optional

def remove_duplicates_sorted(head:Node) -> Optional[Node]: 
    if head is None: 
        return None 
    curr = head  
    while curr: 
        if curr.next != None and curr.data == curr.next.data: 
            temp = curr.next 
            curr.next = curr.next.next 
            del temp 
        else: 
            curr = curr.next 
        
    return head 

def remove_duplicates_unsorted(head: Node) -> Optional[Node]:
    if head is None: 
        return None 
    #3. Approaches - a) 2 loops b) sorting c) hashmaps) 
    #2 loops - O(N^2)
    # curr = head 
    # while curr: 
    #     temp = curr
    #     while temp: 
    #         if temp.next != None  and curr.data == temp.next.data: 
    #             delete_node = temp.next 
    #             temp.next = temp.next.next  
    #             del delete_node
    #         else: 
    #             temp = temp.next 

    #     curr = curr.next 
    # return head  

    #sorting #TODO - first will learn sorting then will come  back 
    # return remove_duplicates_sorted(sort(head))

    #hashmaps - O(N), SC: O(N)
    curr, prev, vis = head.next, head, set() 
    vis.add(prev.data)
    while curr: 
        if curr.data in vis: 
            prev.next = curr.next 
            delete_node = curr  
            curr = curr.next 
            del delete_node #optional as handle by GC in python 
        else: 
            vis.add(curr.data) 
            prev = curr  
            curr  = curr.next 
    return head 
    
if __name__ == '__main__':
    head = Node(1); head.next = Node(5); head.next.next = Node(1); head.next.next.next = Node(1) 
    MyLinkedList().printlist(head)
    # MyLinkedList().printlist(head=(remove_duplicates_sorted(head=Node(2))))
    # head = remove_duplicates_sorted(head)
    head = remove_duplicates_unsorted(head)
    MyLinkedList().printlist(head)
    # print(check_circular_list(head=head))
    # print(check_circular_list(head=dummy))
    