
def add(*num):
    sum=0
    for n in num:
        sum +=n
    return sum

l = [1,2,2,3]

print(add(1,2,2,2,88,67))

def detail(**kwargs):
    for k,v in kwargs.items():
        print('{}:{}'.format(k,v))

def about(name,age,likes):
    info = "Hi I am {}, my age is {}, I like {}".format(name,age,likes)
    return info

dic = {"name":"cm",'likes':'maths','age':23}

print(about(**dic))


print(detail(pt='1',qt=2))

s='hello'
#s[1]='o'
print(s)





