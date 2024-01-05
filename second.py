

# 导入必要的库  
import codecs  
  
# 定义一个包含中文字符的Unicode字符串  
text = u'你好，世界1！'  
  
# 打印该字符串  
print(text)  
  
# 将该字符串写入文件  
with codecs.open('output.txt', 'w', encoding='utf-8') as file:  
    file.write(text)