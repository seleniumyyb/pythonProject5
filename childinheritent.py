from udemypractice import calculator


class childinheri(calculator):
    def __init__(self):
        calculator.__init__(self,2,10)
    num2 = 200
    def getcompletedData(self):
        return self.num2+self.num+self.summation()

obj= childinheri()
print(obj.getcompletedData())
