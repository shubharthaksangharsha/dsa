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

def reverse_recursive(head: Node) -> Node: 
    #base case
    if head is None or head.next is None: 
        return head 
    small_head = reverse_recursive(head.next) 
    head.next.next, head.next = head, None 
    return small_head


def reverse(head: Node) -> Node: 
    #empty check 
    if head is None: 
        return None
     
    prev, curr, forward = None, head, None 
    while(curr):
        forward = curr.next 
        curr.next = prev 
        prev = curr 
        curr = forward 
    return prev #as curr and forward will be None at last 

if __name__ == '__main__':
    link = populate()
    display(head=link)
    # reverse_link = reverse(link)
    reverse_link = reverse_recursive(link)
    display(head=reverse_link)