
# 打开文件操作
# with open('test.txt', 'r') as f:  
#     content = f.read()
#     print(content)
    

# 写入文件操作
# with open('test.txt', 'w') as f:  
#     f.write('Hello, world!')
#     f.write('Hello, python!')
    
# # 换行写入
# with open('test.txt', 'w') as f:  
#     f.write('第一行\n')  
#     f.write('第二行\n')  
#     f.write('第三行\n')

# # 读取文件的行
with open('test.txt', 'r') as f:  
    for line in f:  
        print(line)
        
        
# # 关闭文件
with open('test.txt', 'r') as f:  
    content = f.read()  
f.close()