"""
14. Longest Common Prefix       Easy
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
strs[i] consists of only lower-case English letters.
"""


class Solution:
    def longestCommonPrefix(self, strs):
        #         minlen = min([len(s) for s in strs])

        #         res = ""
        #         for i in range(1, minlen+1):
        #             prefix = strs[0][:i]

        #             for el in strs:
        #                 if el[:i] != prefix:
        #                     return res
        #             res = prefix
        #         return res

        res = ""
        for i in zip(*strs):
            # print(i)
            if len(set(i)) == 1:
                res += i[0]
            else:
                return res
        return res
