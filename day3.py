# # # # # # #fibonacci series


# # # # # # class Solution:
# # # # # #     def fib(self, n: int) -> int:
# # # # # #         if n == 0:
# # # # # #             return 0
# # # # # #         if n == 1:
# # # # # #             return 1
        
# # # # # #         a, b = 0, 1
# # # # # #         for _ in range(2, n + 1):
# # # # # #             a, b = b, a + b
        
# # # # # #         return b


# # # # # def tribonacci(n):
# # # # #     if n == 0:
# # # # #         return 0
# # # # #     if n == 1 or n == 2:
# # # # #         return 1

# # # # #     a, b, c = 0, 1, 1

# # # # #     for i in range(3, n + 1):
# # # # #         a, b, c = b, c, a + b + c

# # # # #     return c


# # # # # print(tribonacci(6))

# # # # #list
# # # # # list indices
# # # # # list string 
# # # # # list method
# # # # # list operations 
# # # # # mapping

# # # # # #list
# # # # # list =[1,3,4,45,3]
# # # # # print(list[4])
# # # # # #lisst slicing  makes a new data
# # # # # #syntax#[start index(includes): end index (excluded)]
# # # # # print(list[:4])


# # # # #list opertors
# # # # #1 concatenation operator(+) (repetition*) (mwmbership opertors (in,not-in))
# # # # a=[1,2,3]
# # # # b=[4,5]
# # # # print(a+b)

# # # # num=[1,2]
# # # # print(num*8)

# # # # fruits=["apple","banana","citrus"]
# # # # print("apple" in fruits)
# # # # print("graps"  not in fruits)

# # # # #co,persion opr
# # # # listone=[1,2,3]
# # # # listtwo=[1,2,4]
# # # # print(listone==listtwo)
# # # # print(listone<listtwo)


# # # # a=[1,23,4,5]
# # # # b=[44,6,7,88,0]



# # # # print(a+b)
# # # # print(list[:4])
# # # # print(a*2,b*4)
# # # # # print(a<b)

# # # #LIST METHODS (VERY IMPORTANT)
# # # #1) APPEND 
# # # num=[1,2,3,4]
# # # num.append(4)
# # # print(num)


# # # #synyax
# # # #insert(index,item)
# # # num.insert(3,5)
# # # print(num)

# # # #extend() (a gulla b value use pannau
# # # a=[1,2]
# # # b=[3,4]
# # # a.extend(b)
# # # print(a)

# # # # remove
# # # num=[1,2,3,4]
# # # num.remove(2)
# # # print(num)

# # #pop usinf in delete
# # num=[1,2,3,45,67]
# # num.pop(2)
# # print(num)
# # # clear
# # num.clear()
# # print(num)

# # index(
# num=[10,2,3,4,5]
# print(num.index(2))# return index
# num[2] # return index value
# #count()
# print(num.count(2))
# #sort
# a=[4,6,34,9,23]
# a.sort()
# print(a)
# a.sort(reverse=True)
# print(a)

# #reverse
# a.reverse()
# print(a)

# #copy()
# b=a.copy()
# print(b)

#map, filter and list--> functional programminh-->iterates

#should use it on list
# num=[1,2,3,4]
# def func(x):
#     return x*2
# result=list(map(func,num))
# print(result)
  

# numone=[1,2,3,4,5,6,7,8,9]
# resultone=list(filter(lambda x:x%2==0,numone))
# print(resultone)

#reduce-->convert into a sinhle balue--/>functional module
#syntax
#reduce(func,iterable)
# from functools import reduce
# num=[1,2,3,4]
# result=reduce(lambda a,b:a+b,num)
# print(result)



# num=[1,2,3,4,5,6,7,8,9,10]
# odd=list(filter(lambda x:x%2!=0,num))
# even=list(filter(lambda x:x%2==0,num))
# print(odd)
# print(even)


#palindrome--->a value that reads the same backward and forward

#list methos-->sliching

# word=input("enter a word")
# if word==word[::-1]:
#     print("palindrome")
# else:
#     print("not a palindrome")

word=input("enter a word")
rev=""
for ch in word:
    rev=ch+rev

if word==word[::-1]:
    print("palindrome")
else:
    print("not a palindrome")

