a =input("First Number : ")
b= input("Second Number : ")

a = int(a)
b= int(b)

if a<b :
    print("a < b")
elif (a==b):
    print(" a=b ")
else :
    print("a > b")

while(a<b):
    a=a+1
    print(a,b)