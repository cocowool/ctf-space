from Cryptodome.Cipher import DES
import binascii

# DES 算法的加密/解密
# 在CTF比赛中往往利用DES加密算法的密钥较短、弱密钥等安全问题获取FLAG。如果在渗透测试中发现拦截的数据包被DES加密，因为DES是对称加密算法，可以考虑在前端JavaScript代码中寻找对应的 Key 值进行解密。

def des_encode(str, key):
    key = b'abcdefgh'                # key的长度须为8字节
    des = DES.new(key, DES.MODE_ECB)      # ECB模式
    text = 'ms08067.com'
    text = text + (8 - (len(text) % 8)) * '='
    encrypt_text = des.encrypt(text.encode())
    encryptResult = binascii.b2a_hex(encrypt_text)
    print(text)
    print(encryptResult)

def des_decode(str, key):
    key = b'abcdefgh'              # key的长度须为8字节
    des = DES.new(key, DES.MODE_ECB)     # ECB模式
    encryptResult = b'b81fcb047936afb76487dda463334767'
    encrypto_text = binascii.a2b_hex(encryptResult)
    decryptResult = des.decrypt(encrypto_text)
    print(decryptResult)