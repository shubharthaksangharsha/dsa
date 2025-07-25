from mylink import MyLinkedList, Node
from typing import Optional, List
from middle_of_list import find_middle_optimize
from reverse_linkedlist import reverse

def check_pallindrome_array(array: List) -> bool: 
    start, end = 0, len(array) - 1 
    while start <= end: 
        if array[start] != array[end]:
            return False 
        start += 1 
        end -= 1 
    return True 
def brute_force(head:  None) -> bool: 
    temp, array = head, []
    
    while temp: 
        array.append(temp.data)
        temp = temp.next 
    return check_pallindrome_array(array)

def check_pallindrome_list(head: Node) -> bool: 

    if head == None or head.next == None: 
        return True 
    # return brute_force(head) 
    temp = head
    middle = find_middle_optimize(head)
    temp2 = reverse(middle.next)
    while temp2: 
        if temp.data != temp2.data:
            return False 
        temp = temp.next 
        temp2 = temp2.next 
    return True 


if __name__ == '__main__':
    head = Node(1) 
    head.next = Node(2); head.next.next = Node(2) 

    print(check_pallindrome_list(head))
