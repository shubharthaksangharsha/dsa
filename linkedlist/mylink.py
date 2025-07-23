#This is my Linked List class anyone can use 
from  typing  import Optional

class Node():
    """
    Node class use to create Linked list 
    """ 
    def __init__(self, data):
        self.data = data 
        self.next = None 

class MyLinkedList():
    def __init__(self):
        self.head = None 

    def populate(self, start: int = 1, end: int =10, is_return: bool =True) -> Optional[Node]:
        """
        populate the linked list with from start index till end index 

            start: starting index = int 
            end: ending index = int  
            is_return: shall return the head of the list = bool
        """
        if self.head  is None:
            self.head = Node(start)
        temp = self.head 
        for i in range(start+1, end + 1):
            temp.next = Node(i)
            temp = temp.next 
        
        if is_return:
            return self.head 
    
    def printlist(self, head: Node = None) -> None:
        """
        Print the linked list with head(provided) else internal head 
            args:
                head: provided starting head = Node 
        """
        if head: 
            temp = head 
        else:
            temp = self.head 
            
        while(temp):
            print(f"{temp.data} -> ", end = " ")
            temp = temp.next 
        print()
      
    
    def reverse(self, is_return: bool =True) -> Optional[Node]:
        """
        reverse the linked list
            args: 
                is_return: shall return the head of the list = bool
        """
        #empty check 
        if self.head is None and is_return: 
            return None
        
        prev, curr, forward = None, self.head, None 
        while(curr):
            forward = curr.next 
            curr.next = prev 
            prev = curr 
            curr = forward
        self.head = prev  
        if is_return:
            return prev #as curr and forward will be None at last 


if __name__ == '__main__':
    mylinklist = MyLinkedList()
    mylinklist.populate(start=1, end=5, is_return=False)
    mylinklist.printlist()
    mylinklist.reverse()
    mylinklist.printlist()
