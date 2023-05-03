"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

 

Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
 

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
"""


from prettytable import PrettyTable

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self) -> str:
        s = f"{self.val}"
        if self.next is not None:
            s += "," + str(self.next)
        return s
    
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        if (list1 is None) or (not list1):
            return list2
        elif (list2 is None) or (not list2):
            return list1
        else:
            out = []
            while(True):
                if (list1.val is None) or (list2.val is None):
                    break

                if list1.val < list2.val:
                    out.append(list1.val)
                    list1 = list1.next
                    if list1 is None:
                        while(list2 is not None):
                            out.append(list2.val)
                            list2 = list2.next
                        break
                else:
                    out.append(list2.val)
                    list2 = list2.next
                    if list2 is None:
                        while(list1 is not None):
                            out.append(list1.val)
                            list1 = list1.next
                        break

            r = ListNode(val=out[-1])
            lo = len(out)
            for i in range(1,lo):
                r = ListNode(val=out[lo-1-i], next=r)
            return r


if __name__ == "__main__":
    sol = Solution()

    inputs = []

    inputA = ListNode(val=4)
    inputA = ListNode(val=2, next=inputA)
    inputA = ListNode(val=1, next=inputA)
    inputB = ListNode(val=4)
    inputB = ListNode(val=3, next=inputB)
    inputB = ListNode(val=1, next=inputB)
    inputs.append((inputA, inputB))


    inputA = ListNode(val=6)
    inputA = ListNode(val=5, next=inputA)
    inputA = ListNode(val=1, next=inputA)
    inputB = ListNode(val=6)
    inputB = ListNode(val=3, next=inputB)
    inputB = ListNode(val=2, next=inputB)
    inputs.append((inputA, inputB))


    inputA = []
    inputB = []
    inputs.append((inputA, inputB))

    inputA = ListNode(val=0)
    inputB = []
    inputs.append((inputA, inputB))
    inputs.append((inputB, inputA))

    x = PrettyTable()
    x.field_names = ["Input1", "Input2", "Output"]
    x.align["Input1"] = "l"
    x.align["Input2"] = "l"
    x.align["Output"] = "c"
    
    for (A,B) in inputs:
        r = sol.mergeTwoLists(A, B)
        x.add_row([f"{A}", f"{B}", f"{r}"]) 


    print(x)