# 退出终端后，所有子进程会受到SIGHUP，SIGHUP的默认行为是终止进程
# nohup命令：使命令忽略SIGHUP
nohup ping www.bing.com &
