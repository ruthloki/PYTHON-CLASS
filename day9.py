#priority queue
#remove elements based on priorty instead of order

#highest priority removed first
#not normal fifo
#smaller numbershghest priorty

#task-1
#task-3
#task-2


#reak-time eg:
# hospital emergency room
# cpu task scheduling
# printer task proority
# network packet routing

# normal queue vs priority queue

#heap
#smallest number=highest priority
#automatic sorting
#uses heapq module


# import heapq

# pq=[]

# heapq.heappush(pq,3)
# heapq.heappush(pq,1)
# heapq.heappush(pq,2)


# print("priority Queue",pq)

# print("removed",heapq.heappop(pq))
# print("removed",heapq.heappop(pq))
# print("removed",heapq.heappop(pq))


#missing number:
# num=[0,1,2,3,4,5]
# n=len(num)
# total = n *(n+1)//2
# missing = total - sum(num)

# print("missing number is:",missing)

# nums = list(map(int, input("Enter sorted numbers: ").split()))

# result = []

# for num in nums:
#     if num not in result:
#         result.append(num)

# print("After removing duplicates:")
# print(*result)

#reverse wed in sting111

# Reverse Words in a String III - VS Version

s = input("Enter a sentence: ")

words = s.split()
result = []

for word in words:
    result.append(word[::-1])

output = " ".join(result)

print("Output:", output)