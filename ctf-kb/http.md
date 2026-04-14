# HTTP 协议知识


通过 Header 中修改 相关属性，绕过一些检查。

HTTP 的几种请求方式
* GET
* POST
* HEAD
* DEL

部分系统用这个属性判断请求客户端 IP，可通过修改来绕过。

```
X-Forwarded-For: 127.0.0.1 
```


## 参考资料