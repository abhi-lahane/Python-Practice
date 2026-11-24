# del() -  delete using index
li1 = [10,20,30,40]
del li1[2]
print(li1)    # 30 del


# pop() - delete and return element
li2 = [10,20,30,40,50]
print(li2.pop(2))    #pop 30
print(li2)      

# remobe() - using value
li3 = [10, 20, 30, 40, 50]
li3.remove(30)
print(li3)    #30

# clear() - deleye all element
li4 = [10, 20, 30, 40, 50]
li4.clear()
print(li4)    #[]