from Crypto.Cipher import AES
import base64
import binascii

# Python3 版本的 AES 解密脚本
# 安装依赖：pip install pycryptodome
# 运行：python3 aes_decrypt.py

# 提供的密钥和IV
crypt_key = 'l36DoqKUYQP0N7e1'
crypt_iv = '131b0c8a7a6e072e'

# 待解密的Base64字符串
encrypted_str = 'KGM7NI0/WvKswK+PlmFIhO4gqe8jJzRdOi02GQ0wZoo='

# 转换密钥和IV为字节
key = crypt_key.encode('utf-8')
iv = crypt_iv.encode('utf-8')

# Base64解码
ciphertext = base64.b64decode(encrypted_str)

# 创建AES解密器（CBC模式，Pkcs7填充）
cipher = AES.new(key, AES.MODE_CBC, iv)

# 解密并去除填充
decrypted_bytes = cipher.decrypt(ciphertext)

# 处理PKCS7填充
pad_len = decrypted_bytes[-1]
decrypted_bytes = decrypted_bytes[:-pad_len]

# 转换为字符串
decrypted_str = decrypted_bytes.decode('utf-8')

print(f"解密后的字符串: {decrypted_str}")
print(f"解密的十六进制表示: {binascii.hexlify(decrypted_bytes).decode('utf-8')}")
