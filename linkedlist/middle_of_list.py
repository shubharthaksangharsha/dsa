from typing import Optional
class Node: 
    def __init__(self, data):
        self.data = data 
        self.next = None
         

def display(head: Node) -> None:
    temp = head 
    while temp: 
        print(f"{temp.data} -> ", end=" ")
        temp = temp.next 
    print()

def populate() -> Node:
    head = Node(1)
    temp = head 
    for i in range(2, 10):
        temp.next = Node(i) 
        temp = temp.next 
    return head

def length(head: Node) -> int: 
    count, temp = 0, head
    while(temp):
        count += 1 
        temp = temp.next 
    return count

def find_middle_len(head: Node) -> Optional[Node]: 
    temp, ans, count = head, (length(head) // 2), 0
    while count < ans: 
        temp = temp.next 
        count += 1 
    return temp 

def find_middle_optimize(head: Node) -> Optional[Node]:  
    slow, fast = head, head 
    while fast and fast.next: 
        slow = slow.next 
        fast = fast.next.next 
    return slow 

if __name__ == '__main__':
    
    head = populate() 
    display(head)
    print(find_middle_len(head).data)
    print(find_middle_optimize(head).data)
    print(find_middle_optimize(None))
