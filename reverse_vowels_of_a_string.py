"""
345. Reverse Vowels of a String           Easy
Given a string s, reverse only all the vowels in the string and return it.
The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both cases.

Example 1:
Input: s = "hello"
Output: "holle"
Example 2:
Input: s = "leetcode"
Output: "leotcede"

Constraints:
1 <= s.length <= 3 * 105
s consist of printable ASCII characters.
"""


class Solution:
    def reverseVowels(self, s):
        new = list(s)

        v = "aeiouAEIOU"
        l, r = 0, len(new)-1

        while l < r:
            if new[l] in v and new[r] in v:
                new[l], new[r] = new[r], new[l]
                l += 1
                r -= 1
            if new[l] not in v:
                l += 1
            if new[r] not in v:
                r -= 1
        return "".join(new)
