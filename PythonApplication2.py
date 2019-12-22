import requests
r=requests.get('https://home.firefoxchina.cn/')
print(r.status_code)#200 是连接成功   404是失败
#1
#print(r.text)   #结果是一堆看不懂的 码
#r.encoding='utf-8'
print(r.encoding)
#print(r.apparent_encoding)
r.encoding="utf-8"
print(r.text)

