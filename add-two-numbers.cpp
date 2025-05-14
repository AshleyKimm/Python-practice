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
            int digCount{1};
            ListNode* head = new ListNode();
            ListNode * tail = head;
            int carry{};
    
            while (l1 != nullptr || l2 != nullptr || carry != 0) {
    
                int dig1 = (l1 != nullptr) ? l1->val : 0;
                int dig2 = (l2 != nullptr) ? l2->val : 0;
                
                int sum = dig1 + dig2 + carry;
                int dig3 = sum % 10;
                carry = sum / 10;
    
                ListNode* ans = new ListNode(dig3);
                tail->next = ans;
                tail = tail->next;
                
                l1 = (l1 != nullptr) ? l1->next : nullptr;
                l2 = (l2 != nullptr) ? l2->next : nullptr;
            }
            head = head->next;
            return head;
    
    
        }
    };