class student:
    def __init__(self,name,reg):
        self.n=name
        self.r=reg
    def showName(self):
        print(self.n)
    def showReg(self):
        print(self.r)
s1=student("vaish",111)
s2=student("reva",112)
s1.showName()
s2.showName()

class student:
    def __init__(self,name,reg,mark1,mark2,mark3):
        self.n=name
        self.r=reg
        self.m1=mark1
        self.m2=mark2
        self.m3=mark3

    def showAvg(self):
        return(self.m2+self.m2+self.m3)/3
    def compare(self,other):
        if self.showAvg()>other.showAvg():
            print(self.n)
        else:


