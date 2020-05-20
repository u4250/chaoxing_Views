import requests,base64,time
from lxml import etree
from bs4 import BeautifulSoup
from selenium import webdriver
url="https://passport2.chaoxing.com/fanyalogin"
a='zhang1127'
psw=base64.b64encode(a.encode('utf-8'))
data={
    'fid': '-1',
    'uname': '17660456791',
    'password': psw,
    'refer': 'http%3A%2F%2Fi.chaoxing.com',
    't': 'true'
}
s = requests.Session()
rep =s.post(url=url,data=data)
cookie_value = ''
for key, value in rep.cookies.items():
    if key=="_uid":
        uid=value
    cookie_value += key + '=' + value + ';'
# print (cookie_value)
# print(rep.text)
url2="https://fystat-ans.chaoxing.com/log/setlog?personid=67970259&courseId=206796988&classId=13691456&encode=6950e901fd028077846af2dad4d1594b&chapterId=207495033&_=1589932972517"
headers = {
    "Cookie":cookie_value ,#"k8s=4bf984dad45790f834e27caa0edadb2f2755be52; jrose=13D2E3D38844D80A0903EF3300407584.mooc-270763880-d9cc5; route=1ab934bb3bbdaaef56ce3b0da45c52ed; source=""; uname=""; userinfo=6cb2606b4382afd11196e168534eedf346a85347a16b2b60d6976e7aed0a7a8879305d568c35e6246c3150c53f446f2514fad946ff8d40d04835edc35b90808af16c27f380da6cbec7d140093c24619f84befd42facf430469e531e857e6745ae92e670968c3f5ca8211ac30df2c1aa0d4869624c1f1b8b605f3d63656e1cac0b82da84b8db37f8855608af792552c037a668956f4b79d93c3ddde98ce384969ab5cf8273134ffd400d2bff5f203fca5305ea45302c3eb2b95e54a2d0e600ba1e0a5ec2e00e2ac22a25bcf04af5e9c16fc590c58d700f1aa7ab681595b44bb6cf9866f9a46b7062256e35b7ee475a41e68d5de85bb3d8340028401393201b2304515b39b9fafebe6c8006e7b624be7de8c187d029b5e09b1d7b33289b577e5f217a3131c5323ef2618d0f4498d98b265c33b99687076f2cba93c942bad56cb58b3506c776ad318be8476f393d0dd391bec04d1180da6146e06074d8248ea0d0f4eb923252e8a0bcc87428f11c7997b2ab76b66fe8e3956a64587326423368438d50b4070bb33a84cc33b99687076f2cb466bdad075ceeb68a1d232552011a6be5a854fb7919ebd9656f5c0cfcde71bad38aff4ccf253fbd416d54d5fb9377543618d50726f656ce704bf6213f8a37ab739884059f9fde9fa; spaceFid=12; tl=1; thirdRegist=0; lv=1; fid=122; _uid=82516740; uf=b2d2c93beefa90dc7a30b6ccb4ba9cd715a9d8994cd42cb9d25fea51b08d3367a8f44b56dc42b9c5f171c43e0c3e7f82d807a544f7930b6abeaaa6286f1f175421bf281950a4046400726a3426cc7f6c6d0502e283b9e33444a64bf1906306d43da591c57cf4c790; _d=1589856677816; UID=82516740; vc=078D82DA228CE555A71558BAC2F4B000; vc2=CF712923D873BA0C0DB79330B8592385; vc3=GNyCmY4kSlgMMfnAOWhzEFMaDTEL3gB1X02hpvPeDVhzRdBW1SKPTYP4aO9EhHDLT8bWt1WA0bMfSwW%2FfjNXWioaKZr%2B49aHTjFH9g18Y0%2F0JuF2%2Ft%2FPNqpWEUAkKR68j9ziewowyq8f6uYW6uSR1HADcshllNyKO4orJVPSDv4%3De51df3ce6356d74685b0eac0eba784d0; xxtenc=a95ebaab1af5a20c824583a61a8b8686; DSSTASH_LOG=C_38-UN_668-US_82516740-T_1589856677817; videojs_id=7364483",
    "User-Agent": "Mozilla/5.0 (iPad; CPU OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 ChaoXingStudy/ChaoXingStudy_3_4.3.2_ios_phone_201911291130_27 (@Kalimdor)_11391565702936108810",
    # 'Referer': 'https://mooc1-1.chaoxing.com/mycourse/studentcourse?courseId=206796988&clazzid=13691456&ut=s&enc=bed0d17f3912f3e84881874997256c65&cpi=67970259&openc=d19d09f395c6f649e5c14b2314faf1c3'
}
url3="http://mooc1-1.chaoxing.com/visit/courses/study?isAjax=true&fileId=0&debug=false"
r=s.get(url=url3,headers=headers)
h1 = etree.HTML(r.text)
geturl = h1.xpath('//div[@class = "Mcon1img httpsClass"]/a/@href')
name = h1.xpath('//h3[@class = "clearfix"]/a/text()')
print(geturl)
# data2={
#     'courseId': '206796988',
#     'clazzid': '13691456',
#     'chapterId': '207495027',
#     'cpi': '67970259',
#     'verificationcode': ''
# }
# res=s.post(url=url2,data=data2,headers=headers)
# # print(res.text)
# for i in range(30):
#     res=s.get(url=url2,headers=headers)
#     print(f'第{i+1}次访问')
#     print(res)
#     time.sleep(5)