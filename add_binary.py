a="101"
b="11"
a1=list(a)
b1=list(b)
for i in a1[::-1]:
    for j in b1[::-1]:
        nums=i+j
        if  nums == "00":
            sum=0
        elif nums =='01':
            sum=1
        elif nums =='10':
            sum =1
        elif nums == '11':
            sum=10



