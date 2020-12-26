import psutil
import json
import requests
import time

# 导入配置文件信息
from conf import config


# 创建收集硬盘信息类
class showDisk():

    def __init__(self, ):

        # 获取当前系统所有硬盘信息
        self.disk = psutil.disk_partitions()

        # 获取盘符或分区

    def disk_info(self):
        for name in self.disk:
            """
            变量说明 获取的数值进行了四舍五入
            disk_name   盘符名称或挂载点
            disk_full   硬盘总大小
            disk_used   硬盘使用大小
            disk_free   硬盘剩余大小
            percent     硬盘使用百分比
            threshold   设置硬盘阈值 硬盘总容量的百分之几的数值
            date        当前时间
            """

            disk_name = name[0]
            disk_full = round(psutil.disk_usage(disk_name).total / 1024 / 1024 / 1024)
            disk_used = round(psutil.disk_usage(disk_name).used / 1024 / 1024 / 1024)
            disk_free = round(psutil.disk_usage(disk_name).free / 1024 / 1024 / 1024)
            percent = psutil.disk_usage(disk_name).percent
            threshold = config.threshold
            date = time.strftime("%Y-%m-%d %H:%M:%S")

            #   判断使用空间是否大于总容量的百分之几
            if str(disk_used) > str(disk_full * threshold):
                headers = {'content-type': 'application/json'}
                data = {
                    "msgtype": "markdown",
                    "markdown": {
                        "title": "%s" % config.keyName,
                        "text": "#硬盘剩余空间不足\n\n" +
                                ">时间：%s\n\n" % date +
                                ">主机名：%s\n\n" % config.hostname +
                                ">主机IP：%s\n\n" % config.ipaddr +
                                ">分区名称: %s\n\n" % disk_name +
                                ">分区总大小: %sG\n\n" % disk_full +
                                ">分区使用大小: %sG\n\n" % disk_used +
                                ">分区剩余大小: %sG\n\n" % disk_free +
                                ">使用百分比: %s%%\n\n" % percent

                    }

                }
                # 封装信息提交到钉钉API
                requests.post(config.webhook, headers=headers, data=json.dumps(data))


if __name__ == '__main__':
    showDisk().disk_info()
