# Node class
class Node:
    def __init__(self, data):
        self.data = data  # stores data
        self.next = None  # pointer to next node

# LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None  # start of list

    # Add a node to the end
    def add_node(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:  # go to the last node
                temp = temp.next
            temp.next = new_node

    # Print the linked list
    def print_list(self):
        if self.head is None:
            print("List is empty.")
            return
        temp = self.head
        print("Linked List:", end=" ")
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    # Delete the nth node 
    def delete_nth_node(self, n):
        try:
            if self.head is None:
                raise Exception("Cannot delete from an empty list.")

            if n <= 0:
                raise Exception("Index should be a positive integer.")

            # Deleting the head node
            if n == 1:
                self.head = self.head.next
                return

            # Traverse to (n-1)th node
            temp = self.head
            for i in range(n - 2):
                if temp.next is None:
                    raise Exception("Index out of range.")
                temp = temp.next

            if temp.next is None:
                raise Exception("Index out of range.")

            # Delete nth node
            temp.next = temp.next.next

        except Exception as e:
            print("Error:", e)

# -------- Testing --------
ll = LinkedList()
ll.add_node(10)
ll.add_node(20)
ll.add_node(30)
ll.add_node(40)
ll.print_list()

print("Deleting 3rd node...")
ll.delete_nth_node(3)
ll.print_list()

print("Trying to delete 10th node (invalid)...")
ll.delete_nth_node(10)

print("Deleting 1st node...")
ll.delete_nth_node(1)
ll.print_list()

print("Deleting all nodes...")
ll.delete_nth_node(1)
ll.delete_nth_node(1)
ll.print_list()

print("Trying to delete from empty list...")
ll.delete_nth_node(1)
