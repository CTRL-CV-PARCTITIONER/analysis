# docker常用命令

## 帮助命令

```shell
docker version	#docker版本信息
docker info	#docker的系统信息，包括镜像和容器的数量
docker 指令 --help	#万能命令

```

文档 ： https://docs.docker.com/reference/

## 镜像命令

**docker images** 查看所有本地的主机上的镜像

```shell
[root@localhost ~]# docker images -a
REPOSITORY                             TAG       IMAGE ID       CREATED        SIZE
registry.gitlab.cn/omnibus/gitlab-jh   latest    825c75508151   6 days ago     3.23GB
hello-world                            latest    d2c94e258dcb   7 months ago   13.3kB

#column含义
REPOSITORY	镜像的仓库源
TAG			镜像的标签
IMAGE ID	镜像的id
CREATED		镜像的创建时间
SIZE		镜像的大小

#可选项
	-a, --all	列出所有镜像
	-q, --quiet	只显示镜像的id
```

**docker search** 搜索镜像

```shell
[root@localhost ~]# docker search mysql
NAME                            DESCRIPTION                                     STARS     OFFICIAL   AUTOMATED
mysql                           MySQL is a widely used, open-source relation…   14726     [OK]
mariadb                         MariaDB Server is a high performing open sou…   5619      [OK]
percona                         Percona Server is a fork of the MySQL relati…   623       [OK]
phpmyadmin                      phpMyAdmin - A web interface for MySQL and M…   916       [OK]
bitnami/mysql                   Bitnami MySQL Docker Image                      105                  [OK]

```

**docker pull** 下载镜像

```shell
#下载镜像 docker pull 镜像名[:tag]
[root@localhost ~]# docker pull mysql
Using default tag: latest	#如果不写镜像，默认下载最新版本
bce031bc522d: Pull complete	#分层下载
cf7e9f463619: Pull complete
105f403783c7: Pull complete
878e53a613d8: Pull complete
2a362044e79f: Pull complete
6e4df4f73cfe: Pull complete
69263d634755: Pull complete
fe5e85549202: Pull complete
5c02229ce6f1: Pull complete
7320aa32bf42: Pull complete
Digest: sha256:4ef30b2c11a3366d7bb9ad95c70c0782ae435df52d046553ed931621ea36ffa5	#签名
Status: Downloaded newer image for mysql:latest
docker.io/library/mysql:latest	#真实地址

### docker pull mysql == docker pull docker.io/library/mysql:latest

#指定版本下载
[root@localhost ~]# docker pull mysql:5.7
5.7: Pulling from library/mysql
20e4dcae4c69: Pull complete
1c56c3d4ce74: Pull complete
e9f03a1c24ce: Pull complete
68c3898c2015: Pull complete
6b95a940e7b6: Pull complete
90986bb8de6e: Pull complete
ae71319cb779: Pull complete
ffc89e9dfd88: Pull complete
43d05e938198: Pull complete
064b2d298fba: Pull complete
df9a4d85569b: Pull complete
Digest: sha256:4bc6bc963e6d8443453676cae56536f4b8156d78bae03c0145cbe47c2aad73bb
Status: Downloaded newer image for mysql:5.7
docker.io/library/mysql:5.7
```

**docker remove** 删除镜像

```shell
[root@localhost ~]# docker rmi -f 5107333e08a8
Untagged: mysql:5.7
Untagged: mysql@sha256:4bc6bc963e6d8443453676cae56536f4b8156d78bae03c0145cbe47c2aad73bb
Deleted: sha256:5107333e08a87b836d48ff7528b1e84b9c86781cc9f1748bbc1b8c42a870d933
Deleted: sha256:37fd5f1492d4e9cb540c52c26655f220568050438f804275e886200c8807ffb4
Deleted: sha256:1105a50d3483cb9f970e70cf5163e3352f0b2fe2ff07c6abcca6f34228e76dc5
Deleted: sha256:94187496c18bb11b78e71017f2774ad3c0a734da9749a46e917c4239504e9322
Deleted: sha256:ae59716eae3be604a4fd43e86fd2ad504cb06c89cc064c73c78eee651e675805
Deleted: sha256:97d26ca29ec287ff4bd09a49602c44cbcabcf3303ddc726b3b94cbe26dfe1c94
Deleted: sha256:27303974d12144264b32b8936ca7c90d72bdba939a9e791010201b3b1717c4c4
Deleted: sha256:4d4483f06dbe01282c10cb9e429a0be826c18c61048f7860dad49ae7f6bac927
Deleted: sha256:3b73a6f6b3298c568dcfb8fa5e96c581a1b5c0ad395b0c38f9addd0c79703124
Deleted: sha256:46446bf265a411a4a13a4adc86f60c9e0479a2e03273c98cafab7bc4151dd2bc
Deleted: sha256:1d5264146b09a27a8fc6801dc239a4962582ed27dd2fbd8ee708463a1857b06b
Deleted: sha256:cff044e186247f93aa52554c96d77143cc92f99b2b55914038d0941fddeb6623

docker rmi -f (imgage id) (imgage id) (imgage id) #删除指定容器
docker rmi -f &(docker images -aq) #删除所有容器
```

## 容器命令

**有了镜像才可以创建容器，linux，下载一个centos镜像测试学习**

```shell
docker pull centos
```

**新建容器并启动**

```shell
docker run [可选参数] image

#参数说明
--name="Name"	容器名字，用来区分容器
-d				后台方式运行
-it				使用交互方式运行
-p				指定容器端口 -p 8080:8080
	-p ip:主机端口:容器端口
	-p 主机端口:容器端口(常用)
	-p 容器端口
-P(大写)		   随机指定端口

#启动并进入容器
[root@localhost ~]# docker run -it centos /bin/bash
[root@a31b9ef8ad7c /]# ls
bin  etc   lib    lost+found  mnt  proc  run   srv  tmp  var
dev  home  lib64  media       opt  root  sbin  sys  usr

#从容器中推出到主机
[root@a31b9ef8ad7c /]# exit
exit
[root@localhost ~]# ls
anaconda-ks.cfg  jenkins_project  --name     --restart   --volume
--hostname       jenkins.war      --publish  --shm-size

```

**列出所有运行的容器**

```shell
#docker ps 当前正在运行的容器
	-a 包含历史运行的容器
	-n=n 显示最近n个运行的容器
	-q 只显示容器的编号

[root@localhost ~]# docker ps
CONTAINER ID   IMAGE                                         COMMAND             CREATED        STATUS                  PORTS                                                                              NAMES
da8fc9759c2e   registry.gitlab.cn/omnibus/gitlab-jh:latest   "/assets/wrapper"   42 hours ago   Up 42 hours (healthy)   0.0.0.0:80->80/tcp, :::80->80/tcp, 22/tcp, 0.0.0.0:443->443/tcp, :::443->443/tcp   gitlab

[root@localhost ~]# docker ps -a
CONTAINER ID   IMAGE                                         COMMAND             CREATED         STATUS                     PORTS                                                                              NAMES
a31b9ef8ad7c   centos                                        "/bin/bash"         4 minutes ago   Exited (0) 2 minutes ago                                                                                      inspiring_clarke
da8fc9759c2e   registry.gitlab.cn/omnibus/gitlab-jh:latest   "/assets/wrapper"   42 hours ago    Up 42 hours (healthy)      0.0.0.0:80->80/tcp, :::80->80/tcp, 22/tcp, 0.0.0.0:443->443/tcp, :::443->443/tcp   gitlab
```

**退出容器**

```shell
exit #容器停止并退出
Ctrl + P + Q #容器不停止退出
```

**删除容器**

```shell
docker rm 容器id					   #删除指定容器
docker ps -a -q | xargs docker rm 	#删除指定容器
docker rm -f $(docker ps -aq)	 	#删除所有容器
```

**启动和停止容器的操作**

```shell
docker start 容器id		#启动容器
docker restart 容器id		#重启容器
docker stop 容器id		#停止当前正在运行的容器
docker kill 容器id		#强制停止当前容器
```

## 常用其他命令

**后台启动容器**

```shell
#通过docker run -d 镜像名！
[root@localhost ~]# docker run -d centos
7c4353d97d08618d04a40e8a6d1f008ffdfde2d6eb25d0c17710dddeafcea419
[root@localhost ~]# docker ps
CONTAINER ID   IMAGE                                         COMMAND             CREATED        STATUS                  PORTS                                                                              NAMES
da8fc9759c2e   registry.gitlab.cn/omnibus/gitlab-jh:latest   "/assets/wrapper"   42 hours ago   Up 42 hours (healthy)   0.0.0.0:80->80/tcp, :::80->80/tcp, 22/tcp, 0.0.0.0:443->443/tcp, :::443->443/tcp   gitlab

#问题 docker ps 发现centos停止了
#常见的坑，docker 容器使用后台运行，必须要有一个前台进程（-it）
```

**查看日志**

```shell
docker logs -ft --tail 10 87eed01a72ba（容器id）
-ft #显示日志
--tail number 显示最后几行日志

[root@localhost ~]# docker run -d centos /bin/bash -c "while true;do echo weidong;sleep 1;done"
87eed01a72ba648f63ce243f2e39ec8737daa0f18f7488cb12803d10870d2dca

[root@localhost ~]# docker logs -f -t --tail 10 87eed01a72ba
2023-12-23T09:26:21.208610737Z weidong
2023-12-23T09:26:22.220469507Z weidong
2023-12-23T09:26:23.225986235Z weidong
2023-12-23T09:26:24.232344362Z weidong
2023-12-23T09:26:25.238813398Z weidong
2023-12-23T09:26:26.253730709Z weidong
2023-12-23T09:26:27.265965503Z weidong
2023-12-23T09:26:28.272734242Z weidong
2023-12-23T09:26:29.280703823Z weidong
2023-12-23T09:26:30.282131644Z weidong
```

**查看容器中的进程信息**

```shell
# docker top 容器id
[root@localhost ~]# docker top 87eed01a72ba
UID                 PID                 PPID                C                   STIME               TTY                 TIME                CMD
root                28988               28970               0                   17:24               ?                   00:00:00            /bin/bash -c while true;do echo weidong;sleep 1;done
root                29542               28988               0                   17:29               ?                   00:00:00            /usr/bin/coreutils --coreutils-prog-shebang=sleep /usr/bin/sleep 1
```

**查看镜像元数据**

```shell
docker inspect 容器id

[root@localhost ~]# docker inspect 87eed01a72ba
[
    {
        "Id": "87eed01a72ba648f63ce243f2e39ec8737daa0f18f7488cb12803d10870d2dca",
        "Created": "2023-12-23T09:24:37.876942612Z",
        "Path": "/bin/bash",
        "Args": [
            "-c",
            "while true;do echo weidong;sleep 1;done"
        ],
        "State": {
            "Status": "running",
            "Running": true,
            "Paused": false,
            "Restarting": false,
            "OOMKilled": false,
            "Dead": false,
            "Pid": 28988,
            "ExitCode": 0,
            "Error": "",
            "StartedAt": "2023-12-23T09:24:38.308770678Z",
            "FinishedAt": "0001-01-01T00:00:00Z"
        },
        "Image": "sha256:5d0da3dc976460b72c77d94c8a1ad043720b0416bfc16c52c45d4847e53fadb6",
        "ResolvConfPath": "/var/lib/docker/containers/87eed01a72ba648f63ce243f2e39ec8737daa0f18f7488cb12803d10870d2dca/resolv.conf",
        "HostnamePath": "/var/lib/docker/containers/87eed01a72ba648f63ce243f2e39ec8737daa0f18f7488cb12803d10870d2dca/hostname",
        "HostsPath": "/var/lib/docker/containers/87eed01a72ba648f63ce243f2e39ec8737daa0f18f7488cb12803d10870d2dca/hosts",
        "LogPath": "/var/lib/docker/containers/87eed01a72ba648f63ce243f2e39ec8737daa0f18f7488cb12803d10870d2dca/87eed01a72ba648f63ce243f2e39ec8737daa0f18f7488cb12803d10870d2dca-json.log",
        "Name": "/recursing_hermann",
        "RestartCount": 0,
        "Driver": "overlay2",
        "Platform": "linux",
        "MountLabel": "",
        "ProcessLabel": "",
        "AppArmorProfile": "",
        "ExecIDs": null,
        "HostConfig": {
            "Binds": null,
            "ContainerIDFile": "",
            "LogConfig": {
                "Type": "json-file",
                "Config": {}
            },
            "NetworkMode": "default",
            "PortBindings": {},
            "RestartPolicy": {
                "Name": "no",
                "MaximumRetryCount": 0
            },
            "AutoRemove": false,
            "VolumeDriver": "",
            "VolumesFrom": null,
            "ConsoleSize": [
                41,
                77
            ],
            "CapAdd": null,
            "CapDrop": null,
            "CgroupnsMode": "host",
            "Dns": [],
            "DnsOptions": [],
            "DnsSearch": [],
            "ExtraHosts": null,
            "GroupAdd": null,
            "IpcMode": "private",
            "Cgroup": "",
            "Links": null,
            "OomScoreAdj": 0,
            "PidMode": "",
            "Privileged": false,
            "PublishAllPorts": false,
            "ReadonlyRootfs": false,
            "SecurityOpt": null,
            "UTSMode": "",
            "UsernsMode": "",
            "ShmSize": 67108864,
            "Runtime": "runc",
            "Isolation": "",
            "CpuShares": 0,
            "Memory": 0,
            "NanoCpus": 0,
            "CgroupParent": "",
            "BlkioWeight": 0,
            "BlkioWeightDevice": [],
            "BlkioDeviceReadBps": [],
            "BlkioDeviceWriteBps": [],
            "BlkioDeviceReadIOps": [],
            "BlkioDeviceWriteIOps": [],
            "CpuPeriod": 0,
            "CpuQuota": 0,
            "CpuRealtimePeriod": 0,
            "CpuRealtimeRuntime": 0,
            "CpusetCpus": "",
            "CpusetMems": "",
            "Devices": [],
            "DeviceCgroupRules": null,
            "DeviceRequests": null,
            "MemoryReservation": 0,
            "MemorySwap": 0,
            "MemorySwappiness": null,
            "OomKillDisable": false,
            "PidsLimit": null,
            "Ulimits": null,
            "CpuCount": 0,
            "CpuPercent": 0,
            "IOMaximumIOps": 0,
            "IOMaximumBandwidth": 0,
            "MaskedPaths": [
                "/proc/asound",
                "/proc/acpi",
                "/proc/kcore",
                "/proc/keys",
                "/proc/latency_stats",
                "/proc/timer_list",
                "/proc/timer_stats",
                "/proc/sched_debug",
                "/proc/scsi",
                "/sys/firmware",
                "/sys/devices/virtual/powercap"
            ],
            "ReadonlyPaths": [
                "/proc/bus",
                "/proc/fs",
                "/proc/irq",
                "/proc/sys",
                "/proc/sysrq-trigger"
            ]
        },
        "GraphDriver": {
            "Data": {
                "LowerDir": "/var/lib/docker/overlay2/6b39f90dfd5e3f1b27eb593f9cde5a04c1796df54137af3102f8be7683b5e26d-init/diff:/var/lib/docker/overlay2/816f8d9ca14f4a211f83acf844cb639d17a3a97f2ceb1a7384e2a68b9caad71d/diff",
                "MergedDir": "/var/lib/docker/overlay2/6b39f90dfd5e3f1b27eb593f9cde5a04c1796df54137af3102f8be7683b5e26d/merged",
                "UpperDir": "/var/lib/docker/overlay2/6b39f90dfd5e3f1b27eb593f9cde5a04c1796df54137af3102f8be7683b5e26d/diff",
                "WorkDir": "/var/lib/docker/overlay2/6b39f90dfd5e3f1b27eb593f9cde5a04c1796df54137af3102f8be7683b5e26d/work"
            },
            "Name": "overlay2"
        },
        "Mounts": [],
        "Config": {
            "Hostname": "87eed01a72ba",
            "Domainname": "",
            "User": "",
            "AttachStdin": false,
            "AttachStdout": false,
            "AttachStderr": false,
            "Tty": false,
            "OpenStdin": false,
            "StdinOnce": false,
            "Env": [
                "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
            ],
            "Cmd": [
                "/bin/bash",
                "-c",
                "while true;do echo weidong;sleep 1;done"
            ],
            "Image": "centos",
            "Volumes": null,
            "WorkingDir": "",
            "Entrypoint": null,
            "OnBuild": null,
            "Labels": {
                "org.label-schema.build-date": "20210915",
                "org.label-schema.license": "GPLv2",
                "org.label-schema.name": "CentOS Base Image",
                "org.label-schema.schema-version": "1.0",
                "org.label-schema.vendor": "CentOS"
            }
        },
        "NetworkSettings": {
            "Bridge": "",
            "SandboxID": "67a9072cb1ea4e73bf0d6394cfbf8308ca7332fb2c11415f00c296b5c12ad726",
            "HairpinMode": false,
            "LinkLocalIPv6Address": "",
            "LinkLocalIPv6PrefixLen": 0,
            "Ports": {},
            "SandboxKey": "/var/run/docker/netns/67a9072cb1ea",
            "SecondaryIPAddresses": null,
            "SecondaryIPv6Addresses": null,
            "EndpointID": "6c589a9dcb0d975835dd0abdd757adf50df5748275f8225df5fb0aa9a56d2b75",
            "Gateway": "172.17.0.1",
            "GlobalIPv6Address": "",
            "GlobalIPv6PrefixLen": 0,
            "IPAddress": "172.17.0.3",
            "IPPrefixLen": 16,
            "IPv6Gateway": "",
            "MacAddress": "02:42:ac:11:00:03",
            "Networks": {
                "bridge": {
                    "IPAMConfig": null,
                    "Links": null,
                    "Aliases": null,
                    "NetworkID": "ec343ffc545a0a0e9f52dcf483cf755fe076232280f71b5a08d372f639321971",
                    "EndpointID": "6c589a9dcb0d975835dd0abdd757adf50df5748275f8225df5fb0aa9a56d2b75",
                    "Gateway": "172.17.0.1",
                    "IPAddress": "172.17.0.3",
                    "IPPrefixLen": 16,
                    "IPv6Gateway": "",
                    "GlobalIPv6Address": "",
                    "GlobalIPv6PrefixLen": 0,
                    "MacAddress": "02:42:ac:11:00:03",
                    "DriverOpts": null
                }
            }
        }
    }
]
```

**进入当前正在进行的容器**

```shell
#通常容器都是通过后台方式运行的，需要进入容器，修改一些配置
#方式1
docker exec -it 容器id bashShell

[root@localhost ~]# docker exec -it 87eed01a72ba /bin/bash
[root@87eed01a72ba /]# ps -ef
UID         PID   PPID  C STIME TTY          TIME CMD
root          1      0  0 09:24 ?        00:00:00 /bin/bash -c while true;do
root        662      0  0 09:35 pts/0    00:00:00 /bin/bash
root        682      1  0 09:35 ?        00:00:00 /usr/bin/coreutils --coreut
root        683    662  0 09:35 pts/0    00:00:00 ps -ef


#方式2 进入正在执行的代码
docker attach 容器id

docker exec #请入容器后进入一个新的终端，可以在里面操作
docker attach #请入容器正在执行的终端，不会启动新的终端
```

**从容器内拷贝文件到主机**

```shell
docker cp 容器id:容器内路径 目的地主机路径
#不管容器是否启动，只要容器存在数据就存在
[root@localhost ~]# docker cp 71585c62be5d:/home/test.java ~
Successfully copied 1.54kB to /root
```



## Docker安装Nginx

```shell
1. 搜索镜像 docker search nginx
2. 下载镜像 docker pull nginx
3. 启动nginx
[root@localhost ~]# docker run -d nginx --name nginx01 -p 3344:80
7473507bdd8c0fb7689ed7118a0f544d1b258343913e2b436b9e53af592ffb47
```

## dockerfile

```shell
dockerfile 是用来构建docker镜像的文件！ 命令参数脚本！
#构建步骤
1. 编写一个dockerfile
2. docker build 构建成为一个镜像
3. docker run 运行镜像
4. docker push 发布镜像（DockerHub、阿里云镜像仓库等）
```

### dockerfile 构建过程

**基础知识**：

1.每个保留关键词（指令)都必须是大写字母

2.执行从上到下顺序执行

3.#表示注释

4.每一个指令都会创建提交一个新的镜像层，并提交！

##### 三部曲：

DockerFile: 构建文件，定义了一切的步骤，源代码

DockerImages: 通过DockerFile构建生成的镜像，最终发布和运行的产品！

Docker容器： 容器就是镜像运行起来提供服务器

##### 指令：

Docker Hub 中99%的镜像都是从scratch这个基础镜像过来的 FROM scratch

```shell
FROM 			# 基础镜像，一切从这里开始构建 centos
MAINTAINER		# 镜像开发者，姓名+邮箱
RUN				# 镜像构建的时候需要运行的命令
ADD				# 步骤：python镜像, python压缩包
WORKDIR			# 镜像工作目录
VOLUME			# 挂在的目录
EXPOSE			# 保留端口配置
CMD				# 指定这个容器启动的时候要运行的命令,只有最后一个会生效，可被替代
ENTRYPOINT		# 指定这个容器启动的时候要运行的命令，可以追加命令
ONBUILD			# 当构建一个被继承的DockerFile,这个时候就会运行ONBUILD，出发指令
COPY			# 类似ADD， 将文件拷贝到镜像中
ENV				# 构建的时候设置环境变量
```



