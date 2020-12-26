import socket
import json
import requests
import time

from conf import config


# 创建测试端口类
class listen():
    # Tcp 检测方法
    def Tcp_Connect(self):

        # 从配置文件中循环本地端口列表
        for port in config.tcp_port:
            # 创建套接字对象
            tcpsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # 设置等待时间
            tcpsocket.settimeout(3)
            # 获取状态
            status = tcpsocket.connect_ex(('localhost', int(port)))

            if status == 0:
                print('TCP端口正常-> %s' % port)
            elif status == 10061:
                print('TCP端口不正常-> %s' % port)
                # 关闭套接字
                tcpsocket.close()

                date = time.strftime("%Y-%m-%d %H:%M:%S")
                headers = {'content-type': 'application/json'}
                data = {
                    "msgtype": "markdown",
                    "markdown": {
                        "title": "%s" % config.keyName,
                        "text": "#端口监控\n\n" +
                                ">时间：%s\n\n" % date +
                                ">主机名：%s\n\n" % config.hostname +
                                ">主机IP：%s\n\n" % config.ipaddr +
                                ">当前TCP端口：->%s<- 异常 \n\n" % port

                    }

                }
                # 封装信息提交到钉钉API
                requests.post(config.webhook, headers=headers, data=json.dumps(data))


if __name__ == '__main__':
    listen().Tcp_Connect()
