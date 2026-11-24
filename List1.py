#A List in Python is a collection of multiple elements stored in a single variable.
l = [10,20,30,40,50,"hello"]
print(l[3], l[5])   # 40 hello
print(l[0:2])      # 10 20
print(l[0::2])    #10 30 50
print(l[3:])   # 40 50 'hello'
# Reberse list
print(l[-1::-1]) #['hello', 50, 40, 30, 20, 10]
print(l[::-1])  #['hello', 50, 40, 30, 20, 10]