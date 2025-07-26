from mylink import MyLinkedList, Node
from reverse_linkedlist import reverse
from typing import Optional,  Tuple
 
def insert_in_ans(head: Node, tail: Node, val: int) -> Tuple[Node]: 
   temp = Node(val) 
   if head is None: 
      head = temp 
      tail = temp  
      return head, tail 
   tail.next = temp 
   tail = temp  
   return head, tail 


def add(first: Node, second: Node) -> Node: 
   if first is None:
      return second
   if second is None:
      return first
   ans_head, ans_tail = None, None
   
   carry = 0 
   while first or  second or carry: 
      val = carry
      if first:
         val  += first.data 
         first  = first.next 
      if second: 
         val += second.data 
         second = second.next
      digit = val % 10 
      ans_head, ans_tail = insert_in_ans(ans_head, ans_tail, digit) #create node and add ans in list 
      carry = val // 10 
   return ans_head 

def add_two_numbers(first: Node, second: Node) -> Node: 
   first_reverse = reverse(first) 
   second_reverse = reverse(second) 

   ans = add(first_reverse, second_reverse) 

   return reverse(ans)


if __name__ == '__main__':
   head_1 = Node(1); head_1.next  = Node(2); head_1.next.next  = Node(3)
   head_2 = Node(1); head_2.next  = Node(2); #head_2.next.next  = Node(3) 
   MyLinkedList().printlist(head=head_1); MyLinkedList().printlist(head=head_2)
   ans = add_two_numbers(head_1, head_2)
   MyLinkedList().printlist(head=ans)
   
