from mylink import MyLinkedList, Node
from typing import Optional

#1. Detect,  2. Beginning node of the  loop.      3. Remove Cycle  

#1. Detect the loop 
def detect_cycle(head: Node) -> bool: 
    if head is None: 
        return False 
    
    #USING SET - Taking extra space 
    # temp, visited = head, set()
    # while temp: 
    #     if temp in visited:
    #         return True 
    #     visited.add(temp) 
    #     temp = temp.next  
    # return False 

    #USING FLOYD CYCLE DETECTION 
    slow, fast = head, head 
    while fast and fast.next: 
        slow = slow.next 
        fast = fast.next.next 
        if slow == fast:  
            return True 

    return False  

def get_starting(head: None) -> Optional[Node]:
    def helper(head) -> Optional[Node]:
        slow, fast = head, head 
        while fast and fast.next: 
            slow = slow.next 
            fast = fast.next.next 
            if (slow == fast):
                return slow 
        return None 
    
    slow, temp = head, helper(head) 
    if temp is None: 
        return None

    #extra check for edge case - 1 node with loop
    if slow == temp: 
        return slow 
    
    while slow != temp: 
        slow = slow.next 
        temp = temp.next 
        if slow == temp:
            return slow 
    
    return None 

def remove_loop(head: Node) -> None: 
    if head is None:
        return 
    start_loop = get_starting(head)
    temp = start_loop 

    while temp.next != start_loop: 
        temp = temp.next 
    temp.next = None     

if __name__ == '__main__':
    # head = Node(1); head.next = Node(2); head.next.next = Node(3); head.next.next.next = Node(4);
    # head.next.next.next.next = head.next 
    head = Node(1); head.next = head 
    # MyLinkedList().printlist(head=head) 
    print(detect_cycle(head=head))
    # print(get_starting(head).data)
    remove_loop(head)
    print(detect_cycle(head=head))

    