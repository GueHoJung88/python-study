result = 0


def add(num):
    global result
    result  += num
    return result


class Calulation:
    def __init__(self):
        self.result =0


    def add(self, num):
        self.result += num
        return self.result
    
    def sub(self, num):
        self.result -= num
        return self.result    

cal1 = Calulation()


class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    
    def setdata(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result
    
    def mul(self):
        result = self.first * self.second
        return result
    
    def sub(self):
        result = self.first - self.second
        return result
    
    def div(self):
        result= self.first / self.second
        return result
    



class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result

a = MoreFourCal(4,2)
add_result = a.add()

print(f"add_result : {add_result}")


class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second
        

b = SafeFourCal(3,0)
div_result = b.div()

print(f"div_result : {div_result}")


class Family:
    lastname = "김"