# def generate(numRows):
#     triangle = []

#     for i in range(numRows):
#         row = [1] * (i + 1)

#         for j in range(1, i):
#             row[j] = triangle[i-1][j-1] + triangle[i-1][j]

#         triangle.append(row)

#     return triangle



# numRows = int(input("Enter number of rows: "))
# result = generate(numRows)

# for row in result:
#     print(row)


# def romanToInt(s):
#     roman = {
#         'I': 1, 'V': 5, 'X': 10, 'L': 50,
#         'C': 100, 'D': 500, 'M': 1000
#     }
    
#     total = 0
    
#     for i in range(len(s)):
#         if i < len(s) - 1 and roman[s[i]] < roman[s[i + 1]]:
#             total -= roman[s[i]]
#         else:
#             total += roman[s[i]]
    
#     return total


# print(romanToInt("MCMXCIV"))

# def maximumProduct(nums):
#     nums.sort()
    
#     return max(
#         nums[-1] * nums[-2] * nums[-3],
#         nums[0] * nums[1] * nums[-1]
#     )

# print(maximumProduct([-10, -10, 5, 2]))

# nums = list(map(int, input("Enter sorted numbers (space separated): ").split()))

# if not nums:
#     print("0")
# else:
#     i = 0
#     for j in range(1, len(nums)):
#         if nums[j] != nums[i]:
#             i += 1
#             nums[i] = nums[j]

#     print("Array after removing duplicates:", nums[:i+1])
#     print("Count of unique elements:", i + 1)



# word = input("Enter a word: ")

# if word.islower():
#     print("Small letters (lowercase)")
# elif word.isupper():
#     print("Big letters (uppercase)")
# else:
#     print("Mixed letters")