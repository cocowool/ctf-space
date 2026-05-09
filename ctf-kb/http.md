# HTTP 协议知识


通过 Header 中修改 相关属性，绕过一些检查。

HTTP 的几种请求方式
* GET
* POST
* HEAD
* PUT
* DEL

## 重要的Header

`X-Forwarded-For` ，表示请求来自哪个IP。部分后台用这个属性判断请求客户端 IP，可通过修改来绕过。另外还有 `X-Real-IP` 和 `Client-IP` 可能被利用。

```
X-Forwarded-For: 127.0.0.1 
```

`Referer` ，表示请求来自哪个网站，部分后台对这个属性有校验和检查。典型场景用于防盗链、访问统计、基础来源校验、日志分析。
```
Referer: www.google.com
```

`Origin` ，表示请求的源。典型的场景用于 CORS预检、WebSocket、跨域安全校验。

## git 信息泄漏


`.git` 是使用 Git 进行源代码管理的一个工作目录，保存了很多敏感信息，如果不慎泄漏出来，可以获取项目的完整代码、历史提交记录、配置文件等敏感信息。


简单的泄漏题目，只要用 `GitHack` 或者 `git-dumper` 类的工具，把代码拖下来就能找到 flag，排查思路参考。

```sh
# 1. 查看所有分支/标签（可能有隐藏分支）
git branch -a
git tag

# 2. 查看完整提交链（包括被 reset 的）
git reflog

# 3. 如果有 stash，检查暂存区
git stash list
git stash show -p stash@{0} 2>/dev/null

# 方法1：用 git grep 遍历所有提交对象（推荐⭐）
git rev-list --all | xargs git grep -iE "flag\{|CTF\{|KEY\{"

# 方法2：用 log -p + grep（你已看过，但加上 --all 更全面）
git log -p --all --no-pager | grep -iE "flag\{|CTF\{"

# 方法3：直接搜索 .git/objects 底层（应对 pack 文件）
find .git/objects -type f | grep -v pack | while read f; do 
  git cat-file -p $(echo $f | sed 's|.git/objects/||;s|/||') 2>/dev/null | grep -iE "flag\{"
done

```

## 参考资料