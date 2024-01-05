
class Greeter:  
    def greet(name: str) -> str:  
        """  
        这个方法接受一个字符串参数name。  
        """  
        return name

# print(Greeter.greet(1)) 

# def test():
    # print(Greeter.greet('1'))
    # print(person.name) 
    # print(person.age)
    # print(greet(1))  # 触发类型错误
    
# class Person:  
#     def __init__(self, name: str, age: int):  
#         self.name = name  
#         self.age = age  
          
# person = Person(1, '25') 
# print(person.age) 
# print(person.name) 



# if __name__ == "__main__":
#     test()




#  函数返回值注解
from typing import List  
  
def get_users() -> List[int]:  
    """  
    这个函数不接受任何参数，返回一个字符串类型的列表。  
    """  
    users = '1'  # 将字符串列表改为整数列表  
    return users  
  
print(get_users())  # 触发类型错误


def greet(name: str) -> int:  
    """  
    这个函数接受一个字符串类型的参数name，返回一个整数类型的值。  
    """  
    return len(name)  
  