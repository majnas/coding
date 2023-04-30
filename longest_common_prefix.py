"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
"""

from prettytable import PrettyTable

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """        

        lcp = strs[0]
        for idx in range(1, len(strs)):
            llcp = len(lcp)
            if llcp:
                new_lcp = ""
                for i in range(min(llcp, len(strs[idx]))):
                    if lcp[i] == strs[idx][i]:
                        new_lcp += lcp[i]
                    else:
                        break
                lcp = new_lcp
            else:
                break
        return lcp



if __name__ == "__main__":
    sol = Solution()
    inputs = [["flower", "flow", "flight"],
              ["dog", "racecar", "car"],
              ["ab", "a"],
              ["cir","car"]]

    x = PrettyTable()
    x.field_names = ["Input", "Output"]
    x.align["Input"] = "l"
    x.align["Output"] = "c"
    
    for input in inputs:
        r = sol.longestCommonPrefix(input)
        x.add_row([f"{input}", f"{r}"]) 

    print(x)