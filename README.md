# 钉钉业务监控说明：

    安装环境:
        1. 环境python3 pip3
        2. pip3 install -r requirements.txt
        3. 配置文件目录conf
        4. 主程序main.py
        5. 使用crontab 设置计划任务

#### 系统监控配置文件说明:

    配置文件：
        Config.py 里面的的配置 全局引用
    参数：
        【钉钉配置】
        webhook = "https://oapi.dingtalk.com/robot/send?access_token=你的Token"
        keyName = "自己在钉钉定义的关键字"

        【监控硬盘】
        设置监控硬盘使用量默认配置 85%

        threshold = 0.85

        【进程监控】
        设置监控的进程名称 区分大小写 要与进程名称一致 多个进程逗号分隔

        server_name = ['mysqld', 'nginx',]

        【本地端口监控】
        设置本机监控的端口 下面是例子

        tcp_port = [5432, 22, 5040, 80, 3306, 8080, 6379]

        【网站监控】
        此参数为监控网站是否正常访问 以列表形式写入逗号分割 请以 https//或http:// 开头

        weburl = ['https://www.baidu.com', 'http://xxx.aaa.com']

        【Telent监控】
        此参数为多台机器多端口进行批量Telnet

        telnet_data = {
                "static": [
                    {"host": ['localhost'], "port": [135, 445, 7680, 49664, 443]},
                    {"host": ['127.0.0.1'], "port": [2222, 22, 3306, 5432, 6379]}
                ]
            }

#### Docker 容器监控配置文件说明:

    配置文件:
        docker_config.py
    参数：
        【钉钉配置】
        webhook -> 钉钉机器人的api地址
        keyName -> 钉钉机器人的关键词

        【docker容器监控】
        设置docker的API地址和监控的容器的短ID 可以设置多个地址和多个容器ID

        docker_Api = {
            "static": [
                {"docker_host": ['localhost:2375'], "container_id": ['d18a6995031b', 'f5ad2dc29915', 'a17b62069bea']},
                {"docker_host": ['192.168.0.1:2375'], "container_id": ['d18a6995031b', 'f5ad2dc29915', 'a17b62069bea']}
            ]
        }

### main.py主程序参数说明根据需求开启

> 硬盘监控
> ```Disk.showDisk().disk_info()```

> 进程监控建议与supervisor进行使用此功能不涉及进程重启只监控状态
> ```SysProcess.check_servername()```

> 本机端口监控
> ```ListenPort.listen().Tcp_Connect()```

> 网站监控
> ```WebAppStatus.check().status_url()```

> Telnet 多台主机多个端口监控
> ```TelnetPort.Telnet().ChekPort()```

> Docker 多台主机多个容器监控
> ```ContainerStatus.Container().Docker_status() ```


