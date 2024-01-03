from Cryptodome.Cipher import AES
import binascii
key = b'abcdefghabcdefgh'           # key的长度须为8字节
text = 'ms08067.com'               # 被加密的数据需要为8字节的倍数
text = text + (16 - (len(text) % 16)) * '='
aes = AES.new(key, AES.MODE_ECB)     # ECB模式
encrypto_text = aes.encrypt(text.encode())
encryptResult = binascii.b2a_hex(encrypto_text)
print(text)
print(encryptResult)


from Cryptodome.Cipher import AES
import binascii
key = b'abcdefghabcdefgh'             # key的长度须为8字节
encryptResult = b'51d23f9cab201da377c925ac526c4901'
aes = AES.new(key, AES.MODE_ECB)     # ECB模式
encrypto_text = binascii.a2b_hex(encryptResult)
decryptResult = aes.decrypt(encrypto_text)
print(decryptResult)