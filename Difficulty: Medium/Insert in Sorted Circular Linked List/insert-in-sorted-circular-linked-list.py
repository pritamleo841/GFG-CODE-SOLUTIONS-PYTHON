
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
        
class Solution:
    def sortedInsert(self, head, data):
        '''
        Edge Cases to Handle
            1.Empty list → Create a single-node circular list.
            2.New node is smallest → Insert before head, and update head if needed.
            3.New node is largest → Insert at the end (before head).
            4.Normal insertion between two nodes.
        '''
        new_node = Node(data)
        # Case 1: Empty list
        if not head:
            new_node.next = new_node
            return new_node
        current = head
        while True:
            # Case 2: Normal position to insert between two nodes
            if current.data <= data <= current.next.data:
                break
            # Case 3: At the turning point (end of list to start)
            if current.data > current.next.data:
                # data is either the new smallest or largest
                if data >= current.data or data <= current.next.data:
                    break
            current = current.next
            # Came full circle
            if current == head:
                break
        # Insert new node between current and current.next
        new_node.next = current.next
        current.next = new_node
        # If inserting before head (new smallest), return new node as head
        if data < head.data:
            return new_node
    
        return head
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
        