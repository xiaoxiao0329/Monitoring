import docker
import requests
import json
import time

from conf import docker_config


class Container:

    def Docker_status(self):

        # 从配置文件读取JSON信息
        for dcoker_list in docker_config.docker_Api['static']:

            # 获取主机IP或域名
            for docker_api in dcoker_list['docker_host']:

                # 容器id
                for docker_id in dcoker_list['container_id']:

                    try:
                        # 遍历配置问价中的docker_api 进行连接
                        docker_client = docker.DockerClient(base_url=docker_api)
                        # 获取配置文件中监控的容器id运行状态 运行为True 退出为False
                        status = docker_client.containers.get(docker_id).attrs['State']['Running']
                        docker_name = docker_client.containers.get(docker_id).attrs['Name']
                    except docker.errors.DockerException:
                        break

                    # 判断状态
                    if status:
                        print(docker_name, '容器Running.....', 'ip: %s' % docker_api)
                    else:
                        print(docker_name, '容器exit.....', 'ip: %s' % docker_api)

                        date = time.strftime("%Y-%m-%d %H:%M:%S")
                        headers = {'content-type': 'application/json'}
                        data = {
                            "msgtype": "markdown",
                            "markdown": {
                                "title": "%s" % docker_config.keyName,
                                "text": "#docker容器状态监控\n\n" +
                                        ">时间:%s\n\n" % date +
                                        ">DockerAPI: %s\n\n" % docker_api +
                                        ">容器名称: %s\n\n" % docker_name +
                                        ">容器状态: %s" % status

                            }

                        }
                        # 封装信息提交到钉钉API
                        requests.post(docker_config.webhook, headers=headers, data=json.dumps(data))


if __name__ == '__main__':
    Container().Docker_status()
