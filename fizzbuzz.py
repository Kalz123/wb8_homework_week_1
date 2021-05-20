'''412. Fizz Buzz      Easy
Given an integer n, return a string array answer (1-indexed) where:
answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i if non of the above conditions are true.

Example 1:
Input: n = 3
Output: ["1","2","Fizz"]
Example 2:
Input: n = 5
Output: ["1","2","Fizz","4","Buzz"]
Example 3:
Input: n = 15
Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]

Constraints:
1 <= n <= 104
'''


class Solution:
    def fizzBuzz(self, n):
        #     # Solution1
        #     ans = []
        #     for i in range(1, n+1):
        #         if i % 15 == 0:
        #             ans.append("FizzBuzz")
        #         elif i % 3 == 0:
        #             ans.append("Fizz")
        #         elif i % 5:
        #             ans.append("Buzz")
        #         else:
        #             ans.append(str(i))
        #     return ans
        #
        # # solution 2
        # ans = [""]*n
        # for i in range(n):
        #     if (i+1) % 15 == 0:
        #         ans[i] = "FizzBuzz"
        #     elif (i+1) % 3 == 0:
        #         ans[i] = "Fizz"
        #     elif (i+1) % 5 == 0:
        #         ans[i] = "Buzz"
        #     else:
        #         ans[i] = str(i+1)
        #
        #     # solution 3
        #     return ["FizzBuzz" if i % 15 == 0 else "Fizz" if i % 3 == 0 else "Buzz" if i % 5 == 0 else str(i+1) for i in range(1, n+1)]

        # solutiion 4
        def is_fizzbuzz(n):
            if n % 15 == 0:
                return "FizzBuzz"
            elif n % 3 == 0:
                return "Fizz"
            elif n % 5 == 0:
                return "Buzz"
            else:
                return str(n)
        return list(map(is_fizzbuzz,  range(1, n+1)))
