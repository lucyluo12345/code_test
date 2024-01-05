
class Person:  
    """  
    表示一个人的类。  
  
    属性:  
    name -- 人的姓名。  
    age -- 人的年龄。  
  
    方法:  
    say_hello -- 打印问候语。  
    """  
    def __init__(self, name, age):  
        self.name = name  
        self.age = age  
  
    def say_hello(self):  
        """  
        打印问候语。  
        """  
        print("Hello, my name is " + self.name + ".")
        
        
def add(a, b):  
    """  
    这个函数接受两个参数，返回它们的和。  
      
    参数:  
    a -- 数字或字符串  
    b -- 数字或字符串  
      
    返回:  
    返回两个参数的和。  
    """  
    return a + b


"""  
这个模块提供了一些常用的函数和类。  
"""  
import math  
  
def square_root(num):  
    """  
    这个函数返回一个数的平方根。  
      
    参数:  
    num -- 数字类型  
      
    返回:  
    返回输入数字的平方根。  
    """  
    return math.sqrt(num)



class Car:  
    """  
    这个类表示一辆汽车，具有以下属性：  
    color -- 汽车的颜色  
    brand -- 汽车的牌子  
    speed -- 汽车的速度（单位：km/h）  
    """  
    def __init__(self, color, brand, speed):  
        self.color = color  
        self.brand = brand  
        self.speed = speed