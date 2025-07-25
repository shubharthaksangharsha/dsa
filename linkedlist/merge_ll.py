from mylink import MyLinkedList, Node
from typing import Optional

def merge(head1: Optional[Node], head2: Optional[Node]) -> Optional[Node]: 
    if not head1:
        return head2 
    if not head2:
        return head1 
    temp_a, temp_b = head1, head2 
    while temp_a and temp_b: 
        if temp_a.data <= temp_b.data:  
            temp
            temp_a = temp_a.next  
        else: 
            temp_b = temp_b.next 

        


if __name__ == '__main__':
    mylink, mylink2  = MyLinkedList(), MyLinkedList()
    mylink.populate(start=1, end=5)
    mylink2.populate(start=7, end=10)   
    mylink.printlist()
    mylink2.printlist()