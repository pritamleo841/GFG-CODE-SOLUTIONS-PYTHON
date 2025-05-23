/*
// structure of the node is as follows

struct Node
{
    int data;
    struct Node* next;

    Node(int x){
        data = x;
        next = NULL;
    }

};

*/
#include <set>
class Solution {
  public:
    struct Node* makeUnion(struct Node* head1, struct Node* head2) {
        // code here
        std::set<int> s;

        // Insert all elements from both lists into the set
        while (head1 != NULL) {
            s.insert(head1->data);
            head1 = head1->next;
        }
        while (head2 != NULL) {
            s.insert(head2->data);
            head2 = head2->next;
        }

        // Create new linked list from sorted set
        Node* dummy = new Node(0);
        Node* tail = dummy;

        for (int val : s) {
            tail->next = new Node(val);
            tail = tail->next;
        }

        return dummy->next;
    }
};