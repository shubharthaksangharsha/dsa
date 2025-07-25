from mylink import MyLinkedList, Node
from typing import Optional

def merge(head: Node) -> Optional[Node]: 
    pass 

if __name__ == '__main__':
    head = Node(1); head.next = Node(5); head.next.next = Node(1); head.next.next.next = Node(1) 
    MyLinkedList().printlist(head)
    # MyLinkedList().printlist(head=(remove_duplicates_sorted(head=Node(2))))
    # head = remove_duplicates_sorted(head)
    head = remove_duplicates_unsorted(head)
    MyLinkedList().printlist(head)
    # print(check_circular_list(head=head))
    # print(check_circular_list(head=dummy))
    