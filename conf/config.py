import socket

# TODO:获取当前主机名以及IP地址 请勿删除
hostname = socket.getfqdn(socket.gethostname())
ipaddr = socket.gethostbyname(socket.gethostname())

# TODO:钉钉配置 webhook 设置钉钉的关键字 此配置参数为全局引用
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

# TODO:此参数为监控网站是否正常访问 以列表形式写入逗号分割 请以 https//或http:// 开头
# TODO:此配置参数被 system/WebAppStatus.py 所引用
weburl = ['']

# TODO:此参数为多台机器多端口进行批量Telnet
# TODO:此配置参数被 system/TelnetPort.py 所引用
telnet_data = {
    "static": [
        {"host": ['localhost'], "port": [135, 445, 7680, 49664, 443]},
        {"host": ['127.0.0.1'], "port": [2222, 22, 3306, 5432, 6379]}
    ]
}
