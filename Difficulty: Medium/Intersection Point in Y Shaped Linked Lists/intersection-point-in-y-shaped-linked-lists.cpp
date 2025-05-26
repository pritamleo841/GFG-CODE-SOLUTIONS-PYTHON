/* Linked List Node
struct Node {
  int data;
  struct Node *next;
  Node(int x) {
    data = x;
    next = NULL;
  }
}; */

class Solution {
  public:
    Node* intersectPoint(Node* head1, Node* head2) {
        // Your Code Here
        // Use two pointers that traverse both lists. When a pointer reaches the end of a list, redirect it to the head of the other list.
        // If there's an intersection, the pointers will meet there.
        // Key Idea:Both pointers will traverse exactly the same number of nodes (n + m) and thus meet at the intersection point.
        if (!head1 || !head2) return NULL;

        Node* ptr1 = head1;
        Node* ptr2 = head2;

        while (ptr1 != ptr2) {
            ptr1 = ptr1 ? ptr1->next : head2;
            ptr2 = ptr2 ? ptr2->next : head1;
        }

        return ptr1;
    }
};
