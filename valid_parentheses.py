"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""

from prettytable import PrettyTable

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        buff = []
        for c in s:
            if c == "(":
                buff.append(c)
            elif c == "[":
                buff.append(c)
            elif c == "{":
                buff.append(c)
            elif c == ")":
                if buff:
                    if buff[-1] == "(":
                        buff.pop()
                    else:
                        return False
                else:
                        return False
            elif c == "]":
                if buff:
                    if buff[-1] == "[":
                        buff.pop()
                    else:
                        return False
                else:
                        return False
            elif c == "}":
                if buff:
                    if buff[-1] == "{":
                        buff.pop()
                    else:
                        return False
                else:
                        return False
            
        return not buff




if __name__ == "__main__":
    sol = Solution()
    inputs = ['()[]{}',
              '()[]{',
              '}()[]{',
              '()[]{[()]}',
              '()[]{[()]}{[()]}',
              '('
              ]

    x = PrettyTable()
    x.field_names = ["Input", "Output"]
    x.align["Input"] = "l"
    x.align["Output"] = "c"
    
    for input in inputs:
        r = sol.isValid(input)
        x.add_row([f"{input}", f"{r}"]) 

    print(x)