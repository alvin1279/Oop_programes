class weight:
    Mass=0
    l=[]
    m=0
    def __init__(self,value):
        self.Mass = value
        self.get()

    def get(self):
        print(self.Mass,end=' ')
        print(self.l,end=' ')
        print(self.m)
    def add(self,value):
        self.l+=[1]
        self.m+=1
        weight(value)

a= weight(20)
a.add(10)
a.add(5)
a.get()
print(weight.l)
print(weight.m)
a=[1,2,3]
print(a)
b=a
print(b)
b=b+[4]
print(a,b)
