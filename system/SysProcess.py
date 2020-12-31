import psutil
import json
import requests
import time

# 导入配置文件信息
from conf import config


# 此方法为查看系统中所有的进程
def show_system_pid(processname):
    # 获取当前系统的所有进程的PID
    full_pid = psutil.pids()

    # 循环PID函数取值
    for pid in full_pid:
        # 获取没个PID的程序名 进行判断 监控的进程是否存在
        if psutil.Process(pid).name() == processname:
            return pid


# 此方法为 校验配置文件中定义的进程是否存在
def check_servername():
    # 循环 当前配置文件中的服务列表
    if len(config.server_name):

        for server in config.server_name:
            if isinstance(show_system_pid(server), int):
                pass
            else:
                # 获取当前时间
                date = time.strftime("%Y-%m-%d %H:%M:%S")
                headers = {'content-type': 'application/json'}
                data = {
                    "msgtype": "markdown",
                    "markdown": {
                        "title": "%s" % config.keyName,
                        "text": "#进程监控\n\n" +
                                ">时间：%s\n\n" % date +
                                ">主机名：%s\n\n" % config.hostname +
                                ">主机IP：%s\n\n" % config.ipaddr +
                                ">当前[%s]进程不存在 \n\n" % server

                    }

                }
                # 封装信息提交到钉钉API
                requests.post(config.webhook, headers=headers, data=json.dumps(data))
        else:
            return None

if __name__ == '__main__':
    check_servername()
