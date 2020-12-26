import psutil
import json
import requests
import time

# 导入配置文件信息
from conf import config


# 创建监控进程的方法
class check_server:

    def checkprocess(processname):
        """

        :param processname: 从配置文件server_name 中获取
        :return:
        """
        # 获取当前系统的所有进程的PID
        full_pid = psutil.pids()

        # 循环PID函数取值
        for pid in full_pid:
            # 获取没个PID的程序名 进行判断 监控的进程是否存在
            if psutil.Process(pid).name() == processname:
                return pid

    # 循环 当前配置文件中的服务列表

    for server in config.server_name:
        if isinstance(checkprocess(server), int):
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


if __name__ == '__main__':
    check_server().checkprocess()
