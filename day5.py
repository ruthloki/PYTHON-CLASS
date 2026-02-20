# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# def isSameTree(p, q):
#     if not p and not q:
#         return True
#     if not p or not q:
#         return False
#     if p.val != q.val:
#         return False
    
#     return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

# # Example
# tree1 = TreeNode(1, TreeNode(2), TreeNode(3))
# tree2 = TreeNode(1, TreeNode(2), TreeNode(3))

# print(isSameTree(tree1, tree2))

# def containsDuplicate(nums):
#     return len(nums) != len(set(nums))

# # Example
# print(containsDuplicate([1,2,3,1]))

# def combine(n, k):
#     result = []

#     def backtrack(start, path):
#         if len(path) == k:
#             result.append(path[:])
#             return

#         for i in range(start, n + 1):
#             path.append(i)
#             backtrack(i + 1, path)
#             path.pop()

#     backtrack(1, [])
#     return result

# # Example
# print(combine(4, 2))

# def mySqrt(x):
#     l, r = 0, x
#     while l <= r:
#         m = (l + r) // 2
#         if m * m <= x < (m + 1) * (m + 1):
#             return m
#         elif m * m > x:
#             r = m - 1
#         else:
#             l = m + 1

# print(mySqrt(8))
# def isPowerOfFour(n):
#     if n <= 0:
#         return False
#     while n % 4 == 0:
#         n //= 4
#     return n == 1

# print(isPowerOfFour(16))

# def maxProfit(prices):
#     min_price = float('inf')
#     max_profit = 0
    
#     for price in prices:
#         min_price = min(min_price, price)
#         max_profit = max(max_profit, price - min_price)
    
#     return max_profit

# print(maxProfit([7,1,5,3,6,4]))



#oops(object oriented programming stem)

# def func(a,b):
#     return a+b
# result = func(5,8)
# print(result)



# lass Student:
#     def datails(self,name,marks):
#         if marks>=40:
#              result="pass"
#              print(result)
#              print(name,marks)
#         else:
#             print("Fail")
# s1=Student()
# s2=Student()

# s1.details("rvs",88)

# #syntax
# class ClassName:
#     def method_name(self):
#         print("message")

# #with cinstrcutor
# class ClassName:
#     def __init
    


class Student:
    def __int__(self, name, marks):
        self.name=name
        self.marks=marks
    def show_result(self):
        if self.marks>=40:
            result ="Passs"
        else:
            result="Fail"
        print("/n Student Name:",self.name)
        print("Marks",self.marks)
        print("result",result)

name=input("enter name ")
marks=int(input("enter marks"))
s1=Student(name,marks)
s1.show_result()