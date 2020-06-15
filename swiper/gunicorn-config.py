# -*- coding: utf-8 -*-

from multiprocessing import cpu_count

bind = ["127.0.0.1:9000"]  # 线上环境不会开启在公网 IP 下，一般使用内网 IP
daemon = True  # 是否开启守护进程模式
pidfile = 'logs/gunicorn.pid'

workers = cpu_count() * 2
worker_class = "gevent"  # 指定一个异步处理的库
worker_connections = 65535   #单个进程的网络连接数

keepalive = 60  # 服务器保持连接的时间，能够避免频繁的三次握手过程
timeout = 30   #访问之后一直没回应的访问超时时间
graceful_timeout = 10  #重启超时时间
forwarded_allow_ips = '*'

# 日志处理
capture_output = True  #重定向标准输出
loglevel = 'info'
errorlog = 'logs/error.log'
