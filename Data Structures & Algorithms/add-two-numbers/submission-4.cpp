/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        uint8_t remainder = 0;
        ListNode *head = new ListNode;
        ListNode *curr = nullptr;
        while (l1 || l2 || remainder){
            if (curr == nullptr) {
                curr = head;
            } else {
                curr->next = new ListNode;
                curr = curr->next;
            }
            unsigned int sum = remainder;
            if (l1) {
                sum += l1->val;
                l1 = l1->next;
            }
            if (l2) {
                sum += l2->val;
                l2 = l2->next;
            }
            curr->val = sum % 10;
            remainder = sum / 10;
        } 
        return head;
    }
};
