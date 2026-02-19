# def isAnagram(s: str, t: str) -> bool:
#     if len(s) != len(t):
#         return False

#     count = {}

#     for char in s:
#         count[char] = count.get(char, 0) + 1

#     for char in t:
#         if char not in count:
#             return False
#         count[char] -= 1
#         if count[char] < 0:
#             return False

#     return True



# if __name__ == "__main__":
#     s = input("Enter first string: ")
#     t = input("Enter second string: ")

#     result = isAnagram(s, t)

#     if result:
#         print("Valid Anagram ✅")
#     else:
#         print("Not an Anagram ❌")



# def climbStairs(n: int) -> int:
#     if n <= 2:
#         return n
    
#     a, b = 1, 2
#     for i in range(3, n + 1):
#         a, b = b, a + b
#     return b

# if __name__ == "__main__":
#     n = int(input("Enter number of stairs: "))
#     ways = climbStairs(n)
#     print(f"Number of ways to climb {n} stairs: {ways}")

# def fizzBuzz(n: int) -> list[str]:
#     result = []
#     for i in range(1, n + 1):
#         if i % 3 == 0 and i % 5 == 0:
#             result.append("FizzBuzz")
#         elif i % 3 == 0:
#             result.append("Fizz")
#         elif i % 5 == 0:
#             result.append("Buzz")
#         else:
#             result.append(str(i))
#     return result

# if __name__ == "__main__":
#     n = int(input("Enter a number: "))
#     output = fizzBuzz(n)
#     print(output)



# a = input("Enter first binary number: ")
# b = input("Enter second binary number: ")


# sum_binary = bin(int(a, 2) + int(b, 2))[2:]


# print("Sum:", sum_binary)

# class Solution:
#     def majorityElement(self, nums: list[int]) -> int:
#         candidate = None
#         count = 0
        
#         for num in nums:
#             if count == 0:
#                 candidate = num
#             count += (1 if num == candidate else -1)
        
#         return candidate

# def arraySign(nums: list[int]) -> int:
#     sign = 1
#     for num in nums:
#         if num == 0:
#             return 0
#         elif num < 0:
#             sign *= -1
#     return sign

# if __name__ == "__main__":
#     nums = list(map(int, input("Enter numbers separated by space: ").split()))
#     result = arraySign(nums)
#     print("Sign of the product:", result)

# def lengthOfLastWord(s: str) -> int:
#     words = s.strip().split()
#     return len(words[-1])

# if __name__ == "__main__":
#     s = input("Enter a string: ")
#     length = lengthOfLastWord(s)
#     print("Length of last word:", length)

# from typing import List

# class Solution:
#     def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
#         set1 = set(nums1)
#         set2 = set(nums2)
        
      
#         intersect = set1 & set2
        
       
#         return list(intersect)

# sol = Solution()
# nums1 = [1, 2, 2, 1]
# nums2 = [2, 2]
# print(sol.intersection(nums1, nums2))  

# class Solution:
#     def strStr(self, haystack: str, needle: str) -> int:
#         if not needle:
#             return 0  # Empty needle case
        
#         n, m = len(haystack), len(needle)
        
#         for i in range(n - m + 1):
#             if haystack[i:i+m] == needle:
#                 return i
#         return -1


# def longestCommonPrefix(strs):
#     if not strs:
#         return ""
    

#     prefix = strs [0]
#     for s in strs[1:]:
#         while not s.startswith(prefix):
#             prefix = prefix[:-1]
#             if not prefix:
#                 return ""
#     return prefix
            
# word = ["fower", "flow", "flight"]
# print("Longest Common Prefix:",  )


# def reverse_string(s: str) -> str:
#     return s[::-1]

# print(reverse_string("hello"))

# def singleNumber(nums):
#     result = 0
#     for num in nums:
#         result ^= num    
#     return result


# nums = [4, 1, 2, 1, 2]
# print(singleNumber(nums))

# class Solution:
#     def addDigits(self, num: int) -> int:
#         if num == 0:
#             return 0
#         return 1 + (num - 1) % 9


def moveZeroes(nums):
    left = 0
    
    for right in range(len(nums)):
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1

# Example
nums = [0,1,0,3,12]
moveZeroes(nums)
print(nums)
