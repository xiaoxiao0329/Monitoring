import socket

# TODO:获取当前主机名以及IP地址 请勿删除
hostname = socket.getfqdn(socket.gethostname())
ipaddr = socket.gethostbyname(socket.gethostname())

# TODO:钉钉配置 keyname 设置钉钉的关键字 此配置参数为全局引用
webhook = ""
keyName = ""

# TODO:设置硬盘监控上限 如 硬盘总和的 15% 写 0.15 默认为设置 85%
# TODO:此配置参数被 system/Disk.py 所引用
threshold = 0.85

# TODO:设置监控程序的名 以列表形式写入逗号分割服务名
# TODO:此配置参数被 system/SysProcess.py 所引用
server_name = ['']

# TODO:监控本机端口是否运行 以列表形式写入逗号分割 以下为默认监控端口 根据需求进行更改
# TODO:此配置参数被 system/ListenPort.py 所引用
tcp_port = [80, 3306, 6379, 5432, 8080, 22]
