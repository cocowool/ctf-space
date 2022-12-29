import hashlib
import itertools

# 构建符合要求的 md5 字符串

str = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

def md5match(match_str, direction='right'):
    pass

len = 2

mylist=("".join(x) for x in itertools.product("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", repeat=16))

while True:
# for i in str:
    # print(i)

    # try:
        # print("len="+len)
    ori_str = next(mylist)
    md5str = hashlib.md5(ori_str.encode('utf-8')).hexdigest()
    print(ori_str)
    print(md5str)

    
    # if md5str[-6:] == "a91cd9":
    #     print(md5str[-6:])
    #     break


    if md5str[-6:] == "8b184b":
        print(md5str[-6:])
        break

    # print(hashlib.md5(i.encode('utf-8')).hexdigest())    
    # except:
    #     len = len + 1
        # mylist=("".join(x) for x in itertools.product("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", repeat=len))
        # print(next(mylist))
    # print(hashlib.md5(i.encode('utf-8')).hexdigest())