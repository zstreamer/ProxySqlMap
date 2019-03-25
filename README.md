# ProxySqlMap


### 安装

Python3.5+

```
python3 -m pip install requests,mitmproxy
```

### 配置

conf.py
	1. ContentType 过滤的文件类型
	2. sqlmapapi_url SqlMap地址
	
### 使用

服务器:
```
sqlmapapi.py -h "ip" -P "端口" -s

```

浏览器设置代理127.0.0.1:8080

会将所有经过浏览器的宝发送到远程SqlMapapi上进行扫描
	
### 联系
	http://www.tysec.org
