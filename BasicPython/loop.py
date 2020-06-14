# l=[]
#
# while(len(l)<4):
#     name = input("Enter a name : ")
#     l.append(name)
#
# print(l)
#
# for i in range(0,len(l)):
#     print (l.__getitem__(i))

dict={}
s = input()

for i in s:
    dict[i]=dict.get(i,0)+1
print ("\n".join(['%s,%s'%(k,v) for k,v in dict.items()]))

