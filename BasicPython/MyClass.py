class Person():
    def __init__(self,name,score,age):
        self.name = name
        self.score = score
        self.age = age

    def info(self):
        print("my name is {}, age is {}  and score {}".format(self.name,self.age,self.score))


class Player(Person):
    def __init__(self,name,score,age):
        super().__init__(name,score,age)

    def increaseScore(self):
        self.score+=100

class ComplexNumber():
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __str__(self):
        return 'Complex Number (%d)' %self.x +' i'+ '(%d)'%(self.y)
    def __add__(self, other):
        return (self.x+other.x, self.y+other.y)

c1=ComplexNumber(2,9)
c2=ComplexNumber(-11,999)

print(c1+c2)


class Counter():
    __myCount =0

    def count(self):
        self.__myCount+=1
        print("Current Count = "+str(self.__myCount))

a = Counter()
a.count()
a.count()
b= Counter()
b.count()
print(a._Counter__myCount)
print(b._Counter__myCount)