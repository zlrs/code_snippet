### 递归获取用户目录下所有的Word文档
```powershell
Get-ChildItem -Path $home -Filter *.doc* -Recurse
```
### 如果你想将它们全部都打打印，可以使用下面的脚本：
```powershell
Get-ChildItem -Path $home -Filter *.doc* -Recurse |
ForEach-Object {
Start-Process -FilePath $_.FullName -Verb Print -Wait
}
```
这里有一个关键点是参数–Wait，如果没有它PowerShell就会尝试并行打印全部的Word文档，然后每一个文档都会开启一个Word应用程序实例，最终耗尽系统资源。有了-Wait，这所有的文档都会被按顺序打印。
### 打印纯文本文件
```powershell
Start-Process -FilePath notepad -ArgumentList '/P C:\windows\WindowsUpdate.log'
```
替换 C:\windows\WindowsUpdate.log 为纯文本文件的路径
