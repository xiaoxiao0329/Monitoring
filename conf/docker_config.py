###########################################################
# TODO:以下配置为docker监控相关配置
###########################################################
# TODO:钉钉配置 webhook 设置钉钉的关键字 此配置参数为全局引用
webhook = ""
keyName = ""

# TODO: 设置docker的api地址和监控的容器短ID
docker_Api = {
    "static": [
        {"docker_host": ['qingran.ltd:2375'], "container_id": ['d18a6995031b', 'f5ad2dc29915', 'a17b62069bea']}
    ]
}
