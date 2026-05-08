# PHP 题目相关

## PHP语言介绍


## PHP RCE

如果有执行 php 代码的入口，通常需要掌握哪些函数能够获取文件内容或更多内部信息，同时要掌握绕过 安全狗 / WAF 的技巧。

常用的命令
```php
system('ls');
//下面几个原生的php函数，用来绕过对cat、more等linux命令的过滤
file_get_contents('filename');
highlight_file('filename');
readfile('filename');
```



## PHP 弱类型比较

* 弱类型比较 

```php
1a == 1，! is_numeric(1a)

$$args，变量泄漏 _REQUEST\_SERVER\GLOBALS
  
md5弱类型比较
QNKCDZO
240610708
s878926199a
s155964671a
s214587387a
s214587387a
# 这些字符串的 md5 值都是 0e 开头，在 php 弱类型比较中判断为相等
```

## 文件包含

PHP中的文件包含，一般是通过 `include` 或者 `require` 函数触发。可以利用 `/etc/passwd` 和 `../../../etc/passwd` 等进行探测。

文件包含检查的绕过。