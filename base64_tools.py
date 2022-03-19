import base64
import os.path

# base64 tools for encode and decode

def decode_str(str):
    decode_str = base64.decodebytes(str.encode('utf-8'))

    return decode_str

def encode_str(str):
    encode_str = base64.encodebytes(str)
    
    return encode_str

def decode_file(filename):
    decode_content = ''
    with open(filename, 'rb') as f:
        # # 全部一次性读取内容
        # file_content = f.read()
        # # print(f.read())
        # decode_content = base64.decodebytes( file_content )
        # f.close()

        # 逐行读取内容
        for line_conente in f:
            decode_content = base64.decodebytes( line_conente )
            print(decode_content)

        f.close()

    return decode_content

str = "bGluZyBhbmQgY29tZm9ydGFibGUuDQoNCi0tDQpodHRwOi8vZW4ud2lraXBlZGlhLm9yZw=="

print(decode_str(str))

filename = '/Users/shiqiang/Downloads/CTF_Tools/2022-practice/xctf-misc/stego.txt'
print(decode_file(filename))