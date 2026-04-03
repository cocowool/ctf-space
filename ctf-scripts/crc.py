import os
import binascii
import struct

# PNG CRC 校验不匹配情况下，计算文件中 crc 值对应的 宽、高
# 计算后通过 010Editor 修改

# png 文件路径
png_file = "/Users/shiqiang/Downloads/ctf-2026/2.png"

current_crc = 0xcbd6df8a

png_hd = open(png_file, 'rb').read()

for i in range(2000):
    for j in range(2000):
        data = png_hd[12:16] + \
            struct.pack('>i', i) + struct.pack('>i', j) + png_hd[24:29]
        crc = binascii.crc32(data) & 0xffffffff
        if crc == current_crc:
            print(f"crc: {crc}")
            print(f"i: {i}")
            print(f"j: {j}")