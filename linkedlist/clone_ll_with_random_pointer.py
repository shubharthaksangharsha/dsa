from typing import Optional
class Node:
    def __init__(self, data, next, random):
        self.data = data 
        self.next = next 
        self.random = random 


def print_list(head: Node) -> None: 
    temp = head 
    while temp: 
        print(f"{temp.data} -> ", end="")
        temp = temp.next 
    print() 

def setting_next_ptr(head: Node) -> Optional[Node]: 
    if head is None:
        return head

    dummy_node = Node(-1, None, None)
    temp_head = dummy_node  
    temp = head 
    while temp: 
        temp_head.next = temp 
        temp = temp.next 
        temp_head = temp_head.next
    return dummy_node.next     

def clone_list(head: Node) -> Optional[Node]:
    #creating  clone list 
    clone_head = setting_next_ptr(head=head)
    return clone_head



    
    
if __name__ == '__main__': 
    head = Node(1, None, None); head.next = Node(2, None, None) 
    head.next.next = Node(3, None, None)    
    print_list(head)
    clone_head = clone_list(head) 
    print_list(clone_head)