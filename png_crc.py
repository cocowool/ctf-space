import os
import binascii
import struct

# 根据PNG图片 CRC 计算高度与宽度
# 如果不相符则尝试修改图片尺寸
filename = '/Users/shiqiang/Downloads/ctf-2023/719af25af2ca4707972c6ae57060238e.png'
crcbp = open(filename, "rb").read()
for i in range(2000):
    for j in range(2000):
        data = crcbp[12:16] + struct.pack('>i', i) + struct.pack('>i',j) + crcbp[24:29]
        crc32 = binascii.crc32(data) & 0xffffffff
        if( crc32 == 0x376FA9F0):
            print(i,j)
            print('hex :' , hex(i), hex(j))
