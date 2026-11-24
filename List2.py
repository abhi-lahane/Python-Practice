li = [10, 20, 30, 40, 50]
# simple
for i in li:
    print(i)

print("-"*10)

# using len 
t = len(li)
for i in range(t):
  print(li[i])

print("-"*10)
# using reverse 
li.reverse()
print(li)

# reverse using slicing
# print(li[::-1])

print("-"*10)
# revers list using for loop index
li1 = [1,2,3,4,5]
l = len(li1)
for i in range(l-1,-1,-1):
  print(li1[i])