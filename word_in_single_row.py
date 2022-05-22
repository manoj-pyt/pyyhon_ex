wordslist1=["Hello","Alaska","Dad","Peace"]
wordslist=set(wordslist1)
firstrow="qwertyuiop"
secondrow="asdfghjkl"
thirdrow="zxcvbnm"
mylist=[]
# only second
print(wordslist)
for mystr in wordslist:
   for mychar in mystr:
       if mychar  in firstrow:
           break
       if mychar  in secondrow:
            break
       if mychar  in thirdrow:
            break


print(mylist)