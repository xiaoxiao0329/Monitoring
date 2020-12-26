# 导入监控脚本
from system import Disk
from system import SysProcess
from system import ListenPort

# ================================================ 配置区 ================================================
# TODO:以下配置根据需求选择开启

if __name__ == '__main__':
    # TODO:硬盘监控
    Disk.showDisk().disk_info()

    # TODO:进程监控 建议与supervisor 进行使用 此功能不涉及进程重启 只监控状态
    SysProcess.check_server().checkprocess()

    # TODO:端口监控
    ListenPort.listen().Tcp_Connect()
