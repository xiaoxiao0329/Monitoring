from conf import config
from system import disk

if __name__ == '__main__':
    # 发送信息给钉钉
    disk.ShowDisk(webhook=config.webhook, keyName=config.keyName).disk_info()
