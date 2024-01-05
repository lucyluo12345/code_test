# # 使用Unicode字符直接表示字符串  
# s = '你好，世界！'  
# print(s)  
  
# # 使用转义序列表示Unicode字符  
# s = 'Hello,\u0041\u0042\u0043\u0044\u0045 world!'  
# print(s) # 输出：Hello,ABCD world! 

# # 使用Unicode编码表示希腊字母表  
# print('\u0391\u0392\u0393\u0394\u0395\u0396\u0397\u0398\u0399\u039a\u039b\u039c\u039d\u039e\u039f\u03a0\u03a1\u03a3\u03a4\u03a5\u03a6\u03a7\u03a8\u03a9') # 输出：ABCDEFGHIJKLMNOPQRSTUVWXYZ


import sys
  
# 定义一个包含UTF-8编码的字符串
# text = "你好，python！"
#
# # 将字符串转换为UTF-8编码的字节序列
# encoded_text = text.encode("utf-8")
#
# # 打印转换后的字节序列
# print('encoded_text')
# print(encoded_text)
# print('encoded_text')
#
# # # 将UTF-8编码的字节序列解码为字符串
# decoded_text = encoded_text.decode("utf-8")
# print('------------')
# print(decoded_text)
# print('------------')



# # 导入必要的库  
# import codecs  
# # 要编码的字符串  
# text = "你好，python！"  
  
# # 将字符串编码为GB2312编码  
# encoded_text = codecs.encode(text, 'gb2312')  
  
# # 输出编码后的字符串  
# print('----------------')
# print(encoded_text)
# print('----------------')



# text ='Hello,学习'
# # ASCII编码将字符串转换为字节码，无法处理忽路错误
# text1 = text.encode('ascii', errors='ignore')
# print(text1)
# # ASCII编码将字符串转换为字节码，无法编码的字符时用问号代者
# text2 = text.encode('ascii', errors='replace')
# print(text2)
#


# import codecs
#
# # 打开包含中文字符的文件，并指定UTF-8编码
# # 使用vscode需要注意路径问题，需要在对应文件前添加./
# with codecs.open('./test.txt', encoding='utf-8') as file:
#     # 读取文件内容
#     content = file.read()
#
# # 输出文件内容
# print(content)

import codecs
#
# # 打开包含二进制数据的文件,先执行写入操作
# # binary_data需要在操作前创建
# with codecs.open('./binary_data.bin', mode='wb') as file:
#     # 写入二进制数据
#     binary_data = b'Hello World\x00This is binary data\x01\x02\x03\x8D'
#     # 用于写入文件操作
#     file.write(binary_data)
#
#
# 以二进制模式打开包含二进制数据的文件，并指定编码方式为None
# with codecs.open('././././binary_data.bin', mode='rb', encoding=None) as file:
#     # 读取文件内容
#     binary_data = file.read()
#
# # 输出二进制数据
# print(binary_data)







# # 类型错误案例-1
# s = "hello"
# i = 5
# # TypeError: can only concatenate str (not "int") to str
# result = s + i
# print(result)



# # 类型错误-2
# my_list = [1, 2, 3]
# # IndexError: list index out of range
# print(my_list[0])
# print(my_list[1])
# print(my_list[2])
# print(my_list[4])


# try……exacpt

# try:  
#     # 尝试执行的代码  
# except ExceptionType:  
#     # 当异常发生时执行的代码


# def divide_numbers(dividend, divisor):
#     try:
#         result = dividend / divisor
#         print("The result is:", result)
#     except ZeroDivisionError:
#         print("Error: Division by zero is not allowed.")
#     except TypeError:
#         print("Error: Invalid operand types for '/' operation.")
#     except Exception as e:
#         print("Error:", str(e))
#
#
# # 调用函数并传入参数
# divide_numbers(10, 2)  # 这将正常执行并输出结果
# divide_numbers(10, 0)  # 这将引发 ZeroDivisionError
# divide_numbers(10, '2')  # 这将引发 TypeError








# try-except-else案例
# try:
#     # 尝试执行的代码
# except ExceptionType:
#     # 当异常发生时执行的代码
# else:
#     # 没有异常发生时执行的代码

def calculate_sum(numbers):
    try:
        result = sum(numbers)
        print("The sum is:", result)
    except TypeError:
        print("Error: Invalid operand types for '+' operation.")
    else:
        print("No error occurred.")
  
# 调用函数并传入参数
calculate_sum([1, 2, 3])  # 这将正常执行并输出结果
calculate_sum([1, '2', 3])  # 这将引发 TypeError









# try+except+finally案例
# try:  
#     # 尝试执行的代码  
# except ExceptionType:  
#     # 当异常发生时执行的代码  
# finally:  
#     # 无论是否发生异常都会执行的代码


# def divide_numbers(dividend, divisor):
#     try:
#         result = dividend / divisor
#         print("The result is:", result)
#     except ZeroDivisionError:
#         print("Error: Division by zero is not allowed.")
#     finally:
#         print("This is the finally block.")
#
# # 调用函数并传入参数
# divide_numbers(10, 2)  # 这将正常执行并输出结果
# divide_numbers(10, 0)  # 这将引发 ZeroDivisionError，并输出相应的错误消息



# raise案例
# try:
#     # 可能引发异常的代码
#     x = 1 / 0
# except Exception as e:
#     # 处理 Exception 异常
#     print("Error:", str(e))
#     raise  # 手动引发异常