from urllib import request
# urlopen: Open a web info
# resp = request.urlopen('http://www.baidu.com')
# print (resp.read())
# print (resp.read(10))
# print (resp.readline())
# print (resp.readlines()) #Data type is a list
# print (resp.getcode())
# print (type(resp)) #http.client.HTTPResponse

# urlretrieve: Download the web info
# request.urlretrieve('http://www.baidu.com', 'baidu.html') #Download image or something


from urllib import parse
# urlencode: Encode special characters or other languages than English
# params = {"name": "张三", "age": 18, "greet": "Hello World"}
# result = parse.urlencode(params)
# print (result)
# url = 'http://www.baidu.com/s'
# params = {"wd":"刘德华"}
# qs = parse.urlencode(params)
# url = url + "?" + qs
# resp = request.urlopen(url)
# print (resp.read())


# urlparse_qs: The other way around of encode
# params = {"name": "张三", "age": 18, "greet": "Hello World"}
# qs = parse.urlencode(params)
# result = parse.parse_qs(qs)
# print (qs)
# print (result)

# urlparse vs urlsplit
# url = 'http://www.baidu.com/s?wd=python&username=abc#1'
# result1 = parse.urlparse(url)
# print (result1)
# print (result1.netloc)
# result2 = parse.urlsplit(url)
# print (result2)

# request.Request: User-Agent
# url = 'https://www.lagou.com/wn/jobs?cl=false&fromSearch=true&labelWords=sug&suginput='
# # resp = request.urlopen(url)
# # print (resp.read())
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'}
# req = request.Request(url,headers=headers)
# resp = request.urlopen(req)
# print (resp.read())

from urllib.request import urlopen
# Prepare a different IP address for data crawling: ProxyHandler
# httpbin.org/ip   kuaidaili.com
# url = 'http://httpbin.org/ip'
# resp1 = request.urlopen(url)
# print (resp1.read())
# # 1. Use ProxyHandler to build a handler
# handler = request.ProxyHandler({"http":"47.92.113.71:80",
#                                 "http":"47.92.113.71:80"
#                                 })
#
# # 2. Used the handler to build a opener
# opener = request.build_opener(handler)
# # 3. Use opener to ask
# resp2 = opener.open(url)
# print (resp2.read())

