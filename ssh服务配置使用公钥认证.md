OS ubunru 18.04
## 安装sshd
```bash
sudo apt install openssh-client  # 安装 ssh 客户端
sudo apt install openssh-server  # 安装 sshd 服务
```
## 配置端口号和公钥认证登录
OpenSSH 服务器缺省配置文件： `/etc/ssh/sshd_config`
以下是您可能更改配置语句的范例:

要设置您 OpenSSH 在 TCP 2222 端口而不是缺省的 TCP 20 端口监听，可以如下使用改变 Port 语句：

`Port 2222`

要让 sshd 允许基于公钥登录证书，可以简单添加或修改该行语句：

`PubkeyAuthentication yes`

If the line is already present, then ensure it is not commented out.

要使您的 OpenSSH 服务器显示 `/etc/issue.net` 文件的内容以作为预登录 Banner，只需简单地将下行添加或修改：

`Banner /etc/issue.net`

在 `/etc/ssh/sshd_config` 文件中。

在修改 `/etc/ssh/sshd_config` 文件之后，保存该文件并重启 sshd 服务器应用程序以使之生效。可以在终端提示符后使用下列命令：

`sudo systemctl restart sshd.service`

## 如何配置公钥登录
- 方法一：在服务器上生成密钥对，把公钥保存到`.ssh/authorized_keys`，私钥传到运行ssh client的主机上。在运行`sshd`的 Ubuntu 主机上，`.ssh`目录应具备的内容如下所示
```
ubuntu@yourUserName:~/.ssh$ ls -l
total 16
-rw-rw-r-- 1 ubuntu ubuntu  404 Apr 30 10:44 authorized_keys
-rw------- 1 ubuntu ubuntu 1675 Apr 30 10:17 id_rsa
-rw-r--r-- 1 ubuntu ubuntu  404 Apr 30 10:17 id_rsa.pub
-rw-r--r-- 1 ubuntu ubuntu  444 Apr 30 10:16 known_hosts
```

- 方法二：在运行ssh client的主机上生成密钥对，把公钥传到运行sshd的主机上，并保存到其`.ssh/authorized_keys`文件中。

## 如何使用公钥登录
1. 使用`ssh`命令登录，`-i` 指定私钥的路径
```
PS C:\Users\yourUserName> ssh ubuntu@10.4.79.19 -p 2222 -i .ssh\id_rsa_ubuntu
Welcome to Ubuntu 18.04.1 LTS (GNU/Linux 4.15.0-47-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage


 * Canonical Livepatch is available for installation.
   - Reduce system reboots and improve kernel security. Activate at:
     https://ubuntu.com/livepatch

322 packages can be updated.
15 updates are security updates.

Last login: Tue Apr 30 10:57:02 2019 from 10.4.79.19
ubuntu@yourUserName:~$
```
2. 使用XShell等 ssh client GUI软件登录
在连接配置中指定登录方法为PublicKey, 并指定私钥路径

## .ssh文件夹目录
Windows 10:  C:\Users\yourUserName\.ssh

Ubutnu    :  ~/.ssh

## Windows 10 安装 sshd
https://docs.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse

## Reference
- https://help.ubuntu.com/lts/serverguide/openssh-server.html.zh-CN
