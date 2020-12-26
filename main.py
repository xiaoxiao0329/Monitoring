# 导入配置模块
from conf import config
# 导入监控脚本
from system import Disk
from system import SysProcess

# ================================================配置区=========================================
# 以下配置区根据需求选择开启

if __name__ == '__main__':
    # 硬盘监控 -> 发送信息给钉钉
    Disk.ShowDisk(webhook=config.webhook, keyName=config.keyName).disk_info()
    # 进程监控
    SysProcess.check_server().checkprocess()
