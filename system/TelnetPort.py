import socket
import json
import requests
import time

from conf import config


# 创建telnet类
class Telnet:

    def ChekPort(self):

        # 获取JSON中数据的值
        for server_name in config.telnet_data['static']:

            # 获取主机IP或域名
            for host_name in server_name['host']:

                # 获取单个端口或多个端口
                for host_port in server_name['port']:

                    # 创建套接字对象
                    tcpsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

                    # 设置等待时间
                    tcpsocket.settimeout(2)

                    # 获取状态
                    status = tcpsocket.connect_ex((host_name, int(host_port)))

                    if status == 0:
                        print(host_name, host_port, status, 'OK')

                    elif status == 10035:
                        print(host_name, host_port, status, 'TimeOut')

                        date = time.strftime("%Y-%m-%d %H:%M:%S")
                        headers = {'content-type': 'application/json'}

                        data = {
                            "msgtype": "markdown",
                            "markdown": {
                                "title": "%s" % config.keyName,
                                "text": "#Telnet监控\n\n" +
                                        ">时间：%s\n\n" % date +
                                        ">主机IP/域名：%s\n\n" % host_name +
                                        ">当前端口：->%s<- TimeOut \n\n" % host_port

                            }

                        }
                        # 封装信息提交到钉钉API
                        requests.post(config.webhook, headers=headers, data=json.dumps(data))


if __name__ == '__main__':
    Telnet().ChekPort()
