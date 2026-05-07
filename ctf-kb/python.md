## Python相关

### Flash SSTI

SSTI Server-Side Template Injection，由于接受用户输入处理不完善而造成的安全问题。

首先找到页面中可以接受用户输入的位置，可能是 GET / POST 参数，也可能是页面 Javascript 触发的后端请求。

使用 `{{ 7*7 }}` 判断是否能注入，如果能计算出结果，则存在诸如的可能。

使用 `{{config}}` 尝试获取配置信息。

再进一步的通过执行命令，获取保存在服务器文件中的 flag 信息。

## Burpsuite 插件

可以使用 SSTI Hunter 来扫描是否存在注入点

## 参考资料
1. https://github.com/ogtirth/SSTI/blob/main/Payloads%20Cheat%20Sheet.md