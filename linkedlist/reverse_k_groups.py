from mylink import MyLinkedList, Node
from typing import Optional

def reverse_k(head: Node, k: int) -> Optional[Node]:
    #base case 
    if head is None:
        return None 
    
    #Step1. Reverse first k group 
    i, curr, prev, forward = 0, head, None, None

    while curr and i < k: 
        i += 1 
        forward = curr.next 
        curr.next = prev 
        prev = curr 
        curr = forward 
    # print(prev.data, curr.data, forward.data, head.data ) #debug line for understanding the game 
    # #Step2.  Reverse rest of k groups using recursion 
    if forward is not None: 
        head.next = reverse_k(forward, k)
    
    #Step3. Return head of reverse list i.e prev (as first k group will be the new head)
    return prev
    

if __name__ == '__main__':
    mylink = MyLinkedList()
    mylink.populate()
    mylink.printlist()
    reverse_link = reverse_k(mylink.head, 2)
    mylink.printlist(head=reverse_link)
    