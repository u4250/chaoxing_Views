import requests,base64,time,json
url="https://passport2.chaoxing.com/fanyalogin"#登录
num=''#账号一般是手机号
psw=''#密码
psw=base64.b64encode(psw.encode('utf-8'))#base64加密
data={
    'fid': '-1',
    'uname': num,
    'password': psw,
    'refer': 'http%3A%2F%2Fi.chaoxing.com',
    't': 'true'
}
s = requests.Session()
rep =s.post(url=url,data=data)
cookie_value = ''#登录获取cookie
for key, value in rep.cookies.items():
    if key=="_uid":
        uid=value
    cookie_value += key + '=' + value + ';'
result=json.loads(rep.text)#将str转换为字典
url2="https://fystat-ans.chaoxing.com/log/setlog?personid=67970259&courseId=205365066&classId=24598573&encode=0fbc260bb3d44bb03e339f1ddb207e20&chapterId=173084313"
#url2进入学习页面时记录次数的地址，对此地址发送请求即可刷浏览量
headers = {
    "Cookie":cookie_value ,
    "User-Agent": "Mozilla/5.0 (iPad; CPU OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 ChaoXingStudy/ChaoXingStudy_3_4.3.2_ios_phone_201911291130_27 (@Kalimdor)_11391565702936108810",
   
}
if(result['status']):
    for i in range(60):
        res=s.get(url=url2,headers=headers)
        print(f'第{i+1}次访问')
        print(res.text)
        time.sleep(5)
else:
    print("账号密码错误")