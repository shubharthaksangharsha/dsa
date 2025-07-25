from mylink import MyLinkedList, Node
from typing import Optional

def populate(attach_node: Node, tail: Node) -> None: 
    tail.next = attach_node
    tail = tail.next

def sort_012(head: Node) -> Optional[Node]:
    #using data 
    # zeros, ones, twos, temp = 0, 0, 0, head 
    # while temp: 
    #     if  temp.data == 0:
    #         zeros += 1 
    #     elif temp.data == 1: 
    #         ones += 1 
    #     else: 
    #         twos += 1 
    #     temp = temp.next 

    # temp = head
    # while zeros: 
    #     temp.data = 0 
    #     temp = temp.next 
    #     zeros -= 1 
    # while ones: 
    #     temp.data = 1 
    #     temp = temp.next 
    #     ones -= 1
    # while twos: 
    #     temp.data = 2
    #     temp = temp.next 
    #     twos -= 1 
    # return head 
    #without data replacement 
    temp, zero_head, one_head, two_head = head, Node(-1), Node(-1), Node(-1) 
    zero_tail, one_tail, two_tail = zero_head, one_head, two_head 
    while temp: 
        print('temp: ', temp.data)
        print('beffore****')
        MyLinkedList().printlist(head=zero_head)
        MyLinkedList().printlist(head=one_head)
        MyLinkedList().printlist(head=two_head)
        if temp.data == 0:
            populate(temp, zero_tail)
        elif temp.data == 1:
            populate(temp,  one_tail)
        else:
            populate(temp, two_tail)
        temp = temp.next  
        print('after****')
        MyLinkedList().printlist(head=zero_head)
        MyLinkedList().printlist(head=one_head)
        MyLinkedList().printlist(head=two_head)

    print('loops ends')
    MyLinkedList().printlist(head=zero_head)
    MyLinkedList().printlist(head=one_head)
    MyLinkedList().printlist(head=two_head)
    
    if one_head != None: 
        zero_tail.next = one_head.next 
    else:  
        zero_tail.next = two_head.next 

    one_tail.next = two_head.next 
    two_tail.next = None 
    # head = zero_head.next 
    # del one_head, two_head, zero_head
    return head 



if __name__ == '__main__':
    head = Node(1); head.next = Node(0); head.next.next = Node(2); head.next.next.next = Node(1) 
    MyLinkedList().printlist(head)
    head = sort_012(head)
    MyLinkedList().printlist(head)