
import requests
import json
# 整个请求中常用的：get post
# 利用post取抓去一些数据-》返回的翻译数据
# 做补充：关于get的params和close
# 思维探索，做自己的一个翻译器

# get:参数拼接在url
# http://aaa?a=1&b=2&c=3
# url='https://www.baidu.com/s'
# params={
#     "wd":'你好'
# }
# result = requests.get(url,params=params)
# print(result.text)
# print(result.url)
def postTest(text):
    search=input('想查一个什么单词呀？')
    print(text)
    url='https://fanyi.baidu.com/sug'
    dataP={
        'kw':search
    }
    postD=requests.post(url,data=dataP)
    # print(type(postD.json()))
    print(postD.json())
# 想知道请求的结果
    # print(postD.json()['errno'])
# 数据转化的格式json
    print(type(postD.text))
def fyTest(txt):
    # 整个功能设计
    # 1、想要达到的目的
        # 输入查询的中文或者英文可以返回结果
        # 对于呈现形式考虑周全（实现data中的第一个内呈现）
    # 2、可能会遇到的问题
        # 查不到？做一个有好处理
        # 捕错，对于错误的处理也是尤为的重要
    # 3、遇到问题我们怎么去处理
        # 如何友好的处理错误，提升体验
    # 4、涉及到大数据？or高并发（先不考虑）
    print(txt)
    see=input('请输入你要查询的内容')
    url='https://fanyi.baidu.com/sug'
    dataP={
        'kw':see
    }
    result=requests.post(url,data=dataP)
    # print(result.json())
    searchResult=result.json()
    # 集合如何取响应内部值
    # print('集合如何取响应内部值')
    # print(searchResult['data'])
    # 注意的点
    # 在呈现结果 请勿忽略数据类型
    # 注意数据类型的转化
    for i in range(len(searchResult['data'])):
        print('第'+str(i + 1)+'项解释:' + searchResult['data'][i]['v'])


if __name__ == "__main__":
    # postTest('测试post')
    fyTest('欢迎来到最牛的翻译器')