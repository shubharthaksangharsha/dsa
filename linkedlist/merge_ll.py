from mylink import MyLinkedList, Node
from typing import Optional

def merge(head1: Optional[Node], head2: Optional[Node]) -> Optional[Node]: 
    if not head1:
        return head2 
    if not head2:
        return head1 
    
        


if __name__ == '__main__':
    mylink, mylink2  = MyLinkedList(), MyLinkedList()
    mylink.populate(start=1, end=5)
    mylink2.populate(start=7, end=10)   
    mylink.printlist()
    mylink2.printlist()