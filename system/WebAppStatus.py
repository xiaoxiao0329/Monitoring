import requests
import time
import json
from conf import config


# 创建校验网站类
class check:

    def status_url(self):
        # 循环配置文件列表
        for url in config.weburl:
            try:

                requests.get(url, timeout=4).status_code
                print('正常', url)

            except (requests.exceptions.ConnectTimeout, requests.exceptions.ConnectionError,
                    requests.exceptions.ReadTimeout) as e:

                print('异常', url)

                # 获取当前时间
                date = time.strftime("%Y-%m-%d %H:%M:%S")
                headers = {'content-type': 'application/json'}
                data = {
                    "msgtype": "markdown",
                    "markdown": {
                        "title": "%s" % config.keyName,
                        "text": "#网站监控\n\n" +
                                ">时间：%s\n\n" % date +
                                ">当前：%s 异常连接超时 \n\n" % url

                    }

                }
                # 封装信息提交到钉钉API
                requests.post(config.webhook, headers=headers, data=json.dumps(data))


if __name__ == '__main__':
    check().status_url()
