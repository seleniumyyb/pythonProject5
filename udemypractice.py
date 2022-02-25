"""dict = {}
dict["first name"] = "kanti"
dict["last name"] = "prajapati"
print(dict)
greet = "good morning"
a = 4
if a>3:
    print("this condition is right")
else:
    print("this condition is wrong")

for k in range(100):
    print(k)

it = 4
while it>1:
    if it != 3:
        print(it)           # don't want to print 3
    it = it-1
print(it)
print("while loop execution is done")

it = 10
while it>1:
    if it == 3:
        break
    print(it)           # using break at equal to 3 then run it stop 3
    it = it-1
#print(it)
print("while loop execution is done")


it = 10
while it>1:
    if it ==9:
        it=it-1
        continue

    if it == 3:
        break
    print(it)           # using break at equal to 3 then run it stop 3
    it = it-1
#print(it)
print("while loop execution is done")
# using function
def GreetMe(name):
    print("good morning"+ name)

def AddIntegers(a,b):
    print(a+b)

GreetMe(" kanti prajapati ")
AddIntegers(2,3)"""
#using classes

class calculator():
    num = 100               #class variables
    def __init__(self, a,b):       # default constructor
         self.firstNumber = a        # a or b are intances variables
         self.secondNumber=b
         print(" i m called automatically when object is created")
    def getData(self):
        print("i m execution as method in class")
    def summation(self):
        return self.firstNumber + self.secondNumber+calculator.num         # or we can put self.num or class name calculator.num either


obj = calculator(2,3)
obj.getData()
print(obj.summation())

obj1 = calculator(4,5)
obj1.getData()
print(obj1.summation())
