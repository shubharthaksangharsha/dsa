from mylink import MyLinkedList, Node
from typing import Optional
 

def check_circular_list(head: Node) -> bool: 
    #1. empty 
    if head is None:
        return True 
    #3. Multiple nodes 
    temp = head.next 
    while temp and temp != head: 
        temp = temp.next 
    return temp == head  

def check_circular_list_map(head: Node) -> bool: 
    if head is None:
        return True  
    temp, visited = head, set()
    while temp: 
        if temp in visited:
            return True 
        visited.add(temp)
        temp = temp.next 
    return False  



if __name__ == '__main__':
    head = Node(1)
    head.next = Node(2) 
    head.next.next = Node(3) 
    # head.next.next.next = head 
    # MyLinkedList().printlist(head)
    dummy = Node(1)
    dummy.next = dummy 
    # print(check_circular_list(head=head))
    # print(check_circular_list(head=dummy))
    print(check_circular_list_map(head=head))
    print(check_circular_list_map(head=dummy))