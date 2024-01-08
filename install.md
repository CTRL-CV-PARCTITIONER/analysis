```shell
#### 网易邮箱POP3授权密码
ADEUTQXAJQRQXPJH
```

```shell
#查看jdk版本
yum search java | grep jdk
#安装java sdk
yum install -y java-11-openjdk
yum install -y java-11-openjdk-devel
#删除jdk
 yum remove -y java-1.8.0-openjdk*
#Jenkins war包下载
https://get.jenkins.io/war-stable/
https://www.jenkins.io/zh/download/
#查看8080端口是否开放
firewall-cmd --query-port=8080/tcp
#开放如果8080端口
firewall-cmd --zone=public --add-port=8080/tcp --permanent
#重启防火墙激活端口配置
firewall-cmd --reload
#关闭防火墙
systemctl status firewalld  查看防火墙状态
systemctl start firewalld.service   打开防火墙
systemctl stop firewalld.service   停止防火墙
systemctl disable firewalld.service   关闭防火墙
#启动jenkins
java -jar jenkins.war --httpPort=8081
#查看jenkins进程
ps -ef|grep jenkins
```

```shell
#安装docker相关依赖
sudo yum install -y yum-utils
#添加docker源
sudo yum-config-manager --add-repo http://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo
sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
#查看docker版本
yum list docker-ce --showduplicates | sort -r
#安装指定docker镜像
sudo yum install docker-ce-20.10.9-3.el7
#启动docker
sudo systemctl start docker
#测试docker是否安装成功
sudo docker run hello-world
#查看docker版本
docker version
```

```shell
#maven安装 选择Binary tar.gz archive
https://maven.apache.org/download.cgi
#解压maven
tar -xvf apache-maven-3.9.6-bin.tar.gz
#转移目录
mv apache-maven-3.9.6/ /usr/local/maven
#测试是否可以运行并查看版本
/usr/local/maven/bin/mvn
/usr/local/maven/bin/mvn -version
```

```shell
# jenkins
# 启动服务
java -jar jenkins.war --httpPort=8080
# 修改内容, 创建时先什么都不要选择进行安装
# Advanced settings URL改为下面
https://mirrors.tuna.tsinghua.edu.cn/jenkins/updates/update-center.json
# Available plugins 点击刷新 等待页面所有的工具加载出来
# 修改本地文件内容
vim ~/.jenkins/updates/default.json
:%s#www.google.com#www.baidu.com#g
:%s#https://updates.jenkins.io/download/#https://mirrors.tuna.tsinghua.edu.cn/jenkins/#g
#Installed plugins 选择下面插件安装
Folders
OWASP Markup Formatter
Build Timeout
Credentials Binding
Timestamper
Workspace Cleanup
Ant
Gradle
Pipeline
GitHub Branch Source
Pipeline: Stage View
Pipeline: GitHub Groovy Libraries
SSH Build Agents
Matrix Authorization Strategy
PAM Authentication
LDAP
Email Extension
Localization Support
Localization: Chinese (Simplified)
Maven Integration
```

```shell
# gitlab 8088
# 卸载所有于gitlab相关的服务
sudo gitlab-ctl stop
sudo apt-get remove gitlab-ce
sudo apt-get autoremove -y
sudo rm -rf /opt/gitlab
sudo rm -rf /etc/gitlab
sudo apt-get remove gitlab-runner
#docker 创建gitlab 容器
docker run --detach  --hostname 192.168.162.156  --publish 443:443 --publish 80:80 --name gitlab  --restart always  --volume $GITLAB_HOME/config:/etc/gitlab:Z  --volume $GITLAB_HOME/logs:/var/log/gitlab:Z  --volume $GITLAB_HOME/data:/var/opt/gitlab:Z  --shm-size 256m registry.gitlab.cn/omnibus/gitlab-jh:latest
```

```shell
# nexus ip:8081
export MAVEN_HOME=/home/maven
export NEXUS_HOME=/home/nexus
export PATH=$MAVEN_HOME/bin:$NEXUS_HOME/bin:$PATH
source /etc/profile
nexus start
[root@localhost bin]# nexus start
WARNING: ************************************************************
WARNING: Detected execution as "root" user.  This is NOT recommended!
WARNING: ************************************************************
Starting nexus
# 需要等待一会才能启动, 查看端口使用情况
netstat -anp | grep 8081
#用户名admin 密码
cat sonatype-work/nexus3/admin.password
[root@localhost home]# cat sonatype-work/nexus3/admin.password 
3694f361-aa37-41c8-9329-23971dd32cda

```

```shell
# Harbor 192.168.162.156
yum install lrzsz
#安装docker-compos
sudo curl -L "https://github.com/docker/compose/releases/download/1.24.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose/
# 使用迅雷下载 https://github.com/docker/compose/releases/tag/v2.23.3/docker-compose-linux-x86_64  上传到/usr/bin  mv docker-compose-linux-x86_64 docker-compose
# 将可执行权限应用于二进制文件
sudo chmod +x /usr/bin/docker-compose
#配置habar文件
tar -xvf Habar.tar.gz
cd harbor
cp harbor.yml.tmpl harbor.yml
vim harbor.yml
	hostname: 192.168.162.156
	https部分注释掉
#修改配置文件， /etc/docker/daemon.json
{
 "insecure-registries":["192.168.162.156"]
}
#重启docker
systemctl docker restart
#启动harbar
cd harbar目录
./install.sh
#验证harbar登录名密码
docker login 192.168.162.156
#输入用户名和密码
#
```

```shell
# ssh
ssh-keygen -t rsa
```

