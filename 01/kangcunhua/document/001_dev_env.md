

## root命令清单
```shell
1  vi /etc/sysconfig/i18n
2  echo $LANG
3  . /etc/sysconfig/i18n
4  echo $LANG
5  mv /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo.backup
6  ls -la /etc/yum.repos.d/
7  wget -O /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-6.repo
8  ls -la /etc/yum.repos.d/
9  yum makecache
10  python -V
11  df -k
12  cd vagrant_data
13  cd /vagrant_data/
14  ls 
15  tar -xzf Python-2.7.11.tgz
16  cd Python-2.7.11
17  ./configure 
18  ./configure --prefix=/usr/local/python27
19  make
20  make install
21  python -V
22  cd ..
23  ls
24  tar -xzf setuptools-20.10.1.tar.gz
25  cd setuptools-20.10.1
26  /usr/local/python27/bin/python setup.py install
27  /usr/local/python27/bin/pip install virtualenv
28  cd ..
29  ls
30  tar -xzf pip-8.1.1.tar.gz
31  cd pip-8.1.1
32  /usr/local/python27/bin/python setup.py build
33  /usr/local/python27/bin/python setup.py install
34  /usr/local/python27/bin/pip install virtualenv
35  mkdir /data
36  /usr/local/python27/bin/virtualenv /data/python27env
37  source /data/python27env/bin/activate
38  pip list
39  pip install ipython
40* 
41  python -V
42  exit
43  history 100 >1.txt
```


##添加镜像报错和修订log
```log
F:\per5\Dev_envsoft\vagrant>vagrant box add "centos-6.6-x86_64" centos-6.6-x86_64.box
==> box: Box file was not detected as metadata. Adding it directly...
==> box: Adding box 'centos-6.6-x86_64' (v0) for provider:
    box: Unpacking necessary files from: file://F:/per5/Dev_envsoft/vagrant/cent
os-6.6-x86_64.box
    box: Progress: 100% (Rate: 7003k/s, Estimated time remaining: --:--:--)
==> box: Successfully added box 'centos-6.6-x86_64' (v0) for 'virtualbox'!

```
###添加镜像报错
```log
F:\Dev_Soft\vagrant>vagrant box add "centos6.6"  centos-6.6-x86_64.box
==> box: Box file was not detected as metadata. Adding it directly...
==> box: Adding box 'centos6.6' (v0) for provider:
    box: Unpacking necessary files from: file://F:/Dev_Soft/vagrant/centos-6.6-x86_64.box
    box:
An error occurred while downloading the remote file. The error
message, if any, is reproduced below. Please fix this error and try
again.
```
###解决
缺少一个.net 32位环境包
>Please install C++ redistributable 32bit.
>Some versions of Win10 doesn’t have it installed.
>32 bit, even if OS is 64bit does the trick:
>https://www.microsoft.com/en-nz/download/details.aspx?id=5555
###查看当前管理镜像

```shell
F:\per5\Dev_envsoft\vagrant>vagrant box list
centos6.6 (virtualbox, 0)
```


##启动镜像log
```log
F:\per5\Devops_centos\reboot>vagrant up
Bringing machine 'default' up with 'virtualbox' provider...
==> default: Importing base box 'centos-6.6-x86_64'...
==> default: Matching MAC address for NAT networking...
==> default: Setting the name of the VM: reboot_default_1462692489358_22114
==> default: Clearing any previously set forwarded ports...
==> default: Clearing any previously set network interfaces...
==> default: Preparing network interfaces based on configuration...
    default: Adapter 1: nat
==> default: Forwarding ports...
    default: 22 (guest) => 2222 (host) (adapter 1)
==> default: Booting VM...
==> default: Waiting for machine to boot. This may take a few minutes...
    default: SSH address: 127.0.0.1:2222
    default: SSH username: vagrant
    default: SSH auth method: private key
    default: Warning: Remote connection disconnect. Retrying...
    default: Warning: Remote connection disconnect. Retrying...
    default:
    default: Vagrant insecure key detected. Vagrant will automatically replace
    default: this with a newly generated keypair for better security.
    default:
    default: Inserting generated public key within guest...
    default: Removing insecure key from the guest if it's present...
    default: Key inserted! Disconnecting and reconnecting using new SSH key...
==> default: Machine booted and ready!
==> default: Checking for guest additions in VM...
    default: The guest additions on this VM do not match the installed version of
    default: VirtualBox! In most cases this is fine, but in rare cases it can
    default: prevent things such as shared folders from working properly. If you see
    default: shared folder errors, please make sure the guest additions within the
    default: virtual machine match the version of VirtualBox you have installedon
    default: your host and reload your VM.
    default:
    default: Guest Additions Version: 4.3.28
    default: VirtualBox Version: 5.0
==> default: Mounting shared folders...
    default: /vagrant => F:/per5/Devops_centos/reboot
```
##通过ssh连接虚拟机log
```log
F:\per5\Devops_centos\reboot>vagrant ssh
Last login: Sat May 30 12:27:44 2015 from 10.0.2.2
Welcome to your Vagrant-built virtual machine.
[vagrant@bogon ~]$ ls
base.sh  cleanup.sh  puppet.sh  vagrant.sh  virtualbox.sh  zerodisk.sh
[vagrant@bogon ~]$ ls -la
insgesamt 60
drwx------. 3 vagrant vagrant 4096 30. Mai 2015  .
drwxr-xr-x. 3 root    root    4096 30. Mai 2015  ..
-rwxr-xr-x. 1 vagrant vagrant  444 30. Mai 2015  base.sh
-rw-r--r--. 1 vagrant vagrant   18 16. Okt 2014  .bash_logout
-rw-r--r--. 1 vagrant vagrant  176 16. Okt 2014  .bash_profile
-rw-r--r--. 1 vagrant vagrant  124 16. Okt 2014  .bashrc
-rwxr-xr-x. 1 vagrant vagrant  339 30. Mai 2015  cleanup.sh
-rwxr-xr-x. 1 vagrant vagrant  360 30. Mai 2015  puppet.sh
drwx------. 2 vagrant root    4096  8. Mai 09:31 .ssh
-rwxr-xr-x. 1 vagrant vagrant  674 30. Mai 2015  vagrant.sh
-rw-------. 1 vagrant vagrant    7 30. Mai 2015  .vbox_version
-rw-------. 1 vagrant vagrant    1 30. Mai 2015  .veewee_params
-rw-------. 1 vagrant vagrant    8 30. Mai 2015  .veewee_version
-rwxr-xr-x. 1 vagrant vagrant  260 30. Mai 2015  virtualbox.sh
-rwxr-xr-x. 1 vagrant vagrant  105 30. Mai 2015  zerodisk.sh
[vagrant@bogon ~]$ df -k
Filesystem           1K-blocks      Used Available Use% Mounted on
/dev/mapper/VolGroup-lv_root
                       8561112    892036   7227528  11% /
tmpfs                   510144         0    510144   0% /dev/shm
/dev/sda1               487652     27666    434386   6% /boot
vagrant              218143768 182565016  35578752  84% /vagrant
[vagrant@bogon ~]$ exit
Abgemeldet
Connection to 127.0.0.1 closed.
```
##关闭虚拟机log
```log
F:\per5\Devops_centos\reboot>vagrant halt
==> default: Attempting graceful shutdown of VM...

```





##安装依赖包的log
```log
[root@OpsDev2 ~]# yum -y install gcc gcc-c++ zlib-devel openssl-devel readline-devel
Loaded plugins: fastestmirror
Setting up Install Process
Loading mirror speeds from cached hostfile
 * base: mirrors.aliyun.com
 * extras: mirrors.aliyun.com
 * updates: mirrors.aliyun.com
base                                                        | 3.7 kB     00:00     
extras                                                      | 3.4 kB     00:00     
updates                                                     | 3.4 kB     00:00     
Package zlib-devel-1.2.3-29.el6.x86_64 already installed and latest version
Package readline-devel-6.0-4.el6.x86_64 already installed and latest version
Resolving Dependencies
--> Running transaction check
---> Package gcc.x86_64 0:4.4.7-11.el6 will be updated
---> Package gcc.x86_64 0:4.4.7-16.el6 will be an update
--> Processing Dependency: libgomp = 4.4.7-16.el6 for package: gcc-4.4.7-16.el6.x86_64
--> Processing Dependency: cpp = 4.4.7-16.el6 for package: gcc-4.4.7-16.el6.x86_64
--> Processing Dependency: libgcc >= 4.4.7-16.el6 for package: gcc-4.4.7-16.el6.x86_64
---> Package gcc-c++.x86_64 0:4.4.7-11.el6 will be updated
---> Package gcc-c++.x86_64 0:4.4.7-16.el6 will be an update
--> Processing Dependency: libstdc++-devel = 4.4.7-16.el6 for package: gcc-c++-4.4.7-16.el6.x86_64
--> Processing Dependency: libstdc++ = 4.4.7-16.el6 for package: gcc-c++-4.4.7-16.el6.x86_64
---> Package openssl-devel.x86_64 0:1.0.1e-30.el6.8 will be updated
---> Package openssl-devel.x86_64 0:1.0.1e-42.el6_7.4 will be an update
--> Processing Dependency: openssl = 1.0.1e-42.el6_7.4 for package: openssl-devel-1.0.1e-42.el6_7.4.x86_64
--> Running transaction check
---> Package cpp.x86_64 0:4.4.7-11.el6 will be updated
---> Package cpp.x86_64 0:4.4.7-16.el6 will be an update
---> Package libgcc.x86_64 0:4.4.7-11.el6 will be updated
---> Package libgcc.x86_64 0:4.4.7-16.el6 will be an update
---> Package libgomp.x86_64 0:4.4.7-11.el6 will be updated
---> Package libgomp.x86_64 0:4.4.7-16.el6 will be an update
---> Package libstdc++.x86_64 0:4.4.7-11.el6 will be updated
---> Package libstdc++.x86_64 0:4.4.7-16.el6 will be an update
---> Package libstdc++-devel.x86_64 0:4.4.7-11.el6 will be updated
---> Package libstdc++-devel.x86_64 0:4.4.7-16.el6 will be an update
---> Package openssl.x86_64 0:1.0.1e-30.el6.8 will be updated
---> Package openssl.x86_64 0:1.0.1e-42.el6_7.4 will be an update
--> Finished Dependency Resolution

Dependencies Resolved

===================================================================================
 Package               Arch         Version                    Repository     Size
===================================================================================
Updating:
 gcc                   x86_64       4.4.7-16.el6               base           10 M
 gcc-c++               x86_64       4.4.7-16.el6               base          4.7 M
 openssl-devel         x86_64       1.0.1e-42.el6_7.4          updates       1.2 M
Updating for dependencies:
 cpp                   x86_64       4.4.7-16.el6               base          3.7 M
 libgcc                x86_64       4.4.7-16.el6               base          103 k
 libgomp               x86_64       4.4.7-16.el6               base          134 k
 libstdc++             x86_64       4.4.7-16.el6               base          295 k
 libstdc++-devel       x86_64       4.4.7-16.el6               base          1.6 M
 openssl               x86_64       1.0.1e-42.el6_7.4          updates       1.5 M

Transaction Summary
===================================================================================
Upgrade       9 Package(s)

Total download size: 23 M
Downloading Packages:
(1/9): cpp-4.4.7-16.el6.x86_64.rpm                          | 3.7 MB     01:27     
(2/9): gcc-4.4.7-16.el6.x86_64.rpm                          |  10 MB     01:26     
(3/9): gcc-c++-4.4.7-16.el6.x86_64.rpm                      | 4.7 MB     00:40     
(4/9): libgcc-4.4.7-16.el6.x86_64.rpm                       | 103 kB     00:00     
(5/9): libgomp-4.4.7-16.el6.x86_64.rpm                      | 134 kB     00:00     
(6/9): libstdc++-4.4.7-16.el6.x86_64.rpm                    | 295 kB     00:02     
(7/9): libstdc++-devel-4.4.7-16.el6.x86_64.rpm              | 1.6 MB     00:12     
(8/9): openssl-1.0.1e-42.el6_7.4.x86_64.rpm                 | 1.5 MB     00:12     
(9/9): openssl-devel-1.0.1e-42.el6_7.4.x86_64.rpm           | 1.2 MB     00:09     
-----------------------------------------------------------------------------------
Total                                               94 kB/s |  23 MB     04:13     
Running rpm_check_debug
Running Transaction Test
Transaction Test Succeeded
Running Transaction
  Updating   : libgcc-4.4.7-16.el6.x86_64                                     1/18 
  Updating   : libstdc++-4.4.7-16.el6.x86_64                                  2/18 
  Updating   : libstdc++-devel-4.4.7-16.el6.x86_64                            3/18 
  Updating   : openssl-1.0.1e-42.el6_7.4.x86_64                               4/18 
  Updating   : cpp-4.4.7-16.el6.x86_64                                        5/18 
  Updating   : libgomp-4.4.7-16.el6.x86_64                                    6/18 
  Updating   : gcc-4.4.7-16.el6.x86_64                                        7/18 
  Updating   : gcc-c++-4.4.7-16.el6.x86_64                                    8/18 
  Updating   : openssl-devel-1.0.1e-42.el6_7.4.x86_64                         9/18 
  Cleanup    : gcc-c++-4.4.7-11.el6.x86_64                                   10/18 
  Cleanup    : libstdc++-devel-4.4.7-11.el6.x86_64                           11/18 
  Cleanup    : openssl-devel-1.0.1e-30.el6.8.x86_64                          12/18 
  Cleanup    : gcc-4.4.7-11.el6.x86_64                                       13/18 
  Cleanup    : libstdc++-4.4.7-11.el6.x86_64                                 14/18 
  Cleanup    : libgcc-4.4.7-11.el6.x86_64                                    15/18 
  Cleanup    : cpp-4.4.7-11.el6.x86_64                                       16/18 
  Cleanup    : libgomp-4.4.7-11.el6.x86_64                                   17/18 
  Cleanup    : openssl-1.0.1e-30.el6.8.x86_64                                18/18 
  Verifying  : libgomp-4.4.7-16.el6.x86_64                                    1/18 
  Verifying  : gcc-c++-4.4.7-16.el6.x86_64                                    2/18 
  Verifying  : gcc-4.4.7-16.el6.x86_64                                        3/18 
  Verifying  : libstdc++-4.4.7-16.el6.x86_64                                  4/18 
  Verifying  : libstdc++-devel-4.4.7-16.el6.x86_64                            5/18 
  Verifying  : cpp-4.4.7-16.el6.x86_64                                        6/18 
  Verifying  : openssl-devel-1.0.1e-42.el6_7.4.x86_64                         7/18 
  Verifying  : libgcc-4.4.7-16.el6.x86_64                                     8/18 
  Verifying  : openssl-1.0.1e-42.el6_7.4.x86_64                               9/18 
  Verifying  : openssl-1.0.1e-30.el6.8.x86_64                                10/18 
  Verifying  : gcc-4.4.7-11.el6.x86_64                                       11/18 
  Verifying  : gcc-c++-4.4.7-11.el6.x86_64                                   12/18 
  Verifying  : libstdc++-4.4.7-11.el6.x86_64                                 13/18 
  Verifying  : openssl-devel-1.0.1e-30.el6.8.x86_64                          14/18 
  Verifying  : libstdc++-devel-4.4.7-11.el6.x86_64                           15/18 
  Verifying  : libgomp-4.4.7-11.el6.x86_64                                   16/18 
  Verifying  : libgcc-4.4.7-11.el6.x86_64                                    17/18 
  Verifying  : cpp-4.4.7-11.el6.x86_64                                       18/18 

Updated:
  gcc.x86_64 0:4.4.7-16.el6                     gcc-c++.x86_64 0:4.4.7-16.el6     
  openssl-devel.x86_64 0:1.0.1e-42.el6_7.4     

Dependency Updated:
  cpp.x86_64 0:4.4.7-16.el6                 libgcc.x86_64 0:4.4.7-16.el6          
  libgomp.x86_64 0:4.4.7-16.el6             libstdc++.x86_64 0:4.4.7-16.el6       
  libstdc++-devel.x86_64 0:4.4.7-16.el6     openssl.x86_64 0:1.0.1e-42.el6_7.4    

Complete!
```


## log of 修改LANG和YUM源

```log
Xshell 5 (Build 0446)
Copyright (c) 2002-2014 NetSarang Computer, Inc. All rights reserved.

Type `help' to learn how to use Xshell prompt.
[D:\reboot]$ 
Connection closed by foreign host.
[D:\reboot]$ ssh 127.0.0.1 2222


Connecting to 127.0.0.1:2222...
Connection established.
To escape to local shell, press 'Ctrl+Alt+]'.

Last login: Sat May 14 19:47:06 2016 from 10.0.2.2
Welcome to your Vagrant-built virtual machine.

[vagrant@bogon vagrant_data]$ sudo su -
[root@bogon ~]# vi /etc/sysconfig/i18n
[root@bogon ~]# echo $LANG
de_DE.UTF-8
[root@bogon ~]# . /etc/sysconfig/i18n
[root@bogon ~]# echo $LANG
en_US.UTF-8
[root@bogon ~]# mv /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo.backup
[root@bogon ~]# ls -la /etc/yum.repos.d/
total 32
drwxr-xr-x.  2 root root 4096 May 14 20:10 .
drwxr-xr-x. 64 root root 4096 May 14 17:59 ..
-rw-r--r--.  1 root root 1991 Oct 23  2014 CentOS-Base.repo.backup
-rw-r--r--.  1 root root  647 Oct 23  2014 CentOS-Debuginfo.repo
-rw-r--r--.  1 root root  289 Oct 23  2014 CentOS-fasttrack.repo
-rw-r--r--.  1 root root  630 Oct 23  2014 CentOS-Media.repo
-rw-r--r--.  1 root root 5394 Oct 23  2014 CentOS-Vault.repo
[root@bogon ~]# wget -O /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-6.repo
--2016-05-14 20:11:04--  http://mirrors.aliyun.com/repo/Centos-6.repo
Resolving mirrors.aliyun.com... 112.124.140.210, 115.28.122.210
Connecting to mirrors.aliyun.com|112.124.140.210|:80... connected.
HTTP request sent, awaiting response... 200 OK
Length: 2572 (2.5K) [application/octet-stream]
Saving to: “/etc/yum.repos.d/CentOS-Base.repo”

100%[=========================================>] 2,572       --.-K/s   in 0s      

2016-05-14 20:11:04 (112 MB/s) - “/etc/yum.repos.d/CentOS-Base.repo” saved [2572/2572]

[root@bogon ~]# ls -la /etc/yum.repos.d/
total 36
drwxr-xr-x.  2 root root 4096 May 14 20:11 .
drwxr-xr-x. 64 root root 4096 May 14 17:59 ..
-rw-r--r--.  1 root root 2572 May 15  2015 CentOS-Base.repo
-rw-r--r--.  1 root root 1991 Oct 23  2014 CentOS-Base.repo.backup
-rw-r--r--.  1 root root  647 Oct 23  2014 CentOS-Debuginfo.repo
-rw-r--r--.  1 root root  289 Oct 23  2014 CentOS-fasttrack.repo
-rw-r--r--.  1 root root  630 Oct 23  2014 CentOS-Media.repo
-rw-r--r--.  1 root root 5394 Oct 23  2014 CentOS-Vault.repo
[root@bogon ~]# yum makecache
Loaded plugins: fastestmirror
Determining fastest mirrors
 * base: mirrors.aliyun.com
 * extras: mirrors.aliyun.com
 * updates: mirrors.aliyun.com
base                                                        | 3.7 kB     00:00     
base/group_gz                                               | 219 kB     00:00     
base/filelists_db                                           | 6.3 MB     00:06     
base/primary_db                                             | 4.6 MB     00:04     
base/other_db                                               | 2.8 MB     00:02     
extras                                                      | 3.4 kB     00:00     
extras/filelists_db                                         |  38 kB     00:00     
extras/prestodelta                                          | 1.7 kB     00:00     
extras/primary_db                                           |  37 kB     00:00     
extras/other_db                                             |  51 kB     00:00     
updates                                                     | 3.4 kB     00:00     
updates/filelists_db                                        | 3.9 MB     00:03     
updates/prestodelta                                         | 563 kB     00:00     
updates/primary_db                                          | 5.2 MB     00:04     
updates/other_db                                            |  62 MB     01:01     
Metadata Cache Created

```



##待整理 by kch


## source命令
附：Linux中source命令的用法 
source命令： 
source命令也称为“点命令”，也就是一个点符号（.）。source命令通常用于重新执行刚修改的初始化文件，使之立即生效，而不必注销并重新登录。 
用法： 
source filename 或 . filename 
source命令除了上述的用途之外，还有一个另外一个用途。在对编译系统核心时常常需要输入一长串的命令，如： 
make mrproper 
make menuconfig 
make dep 
make clean 
make bzImage 
………… 
如果把这些命令做成一个文件，让它自动顺序执行，对于需要多次反复编译系统核心的用户来说会很方便，而用source命令就可以做到这一点，它的作用就是把一个文件的内容当成shell来执行，先在linux的源代码目录下（如/usr/src/linux-2.4.20）建立一个文件，如make_command，在其中输入一下内容：   www.2cto.com  
make mrproper && 
make menuconfig && 
make dep && 
make clean && 
make bzImage && 
make modules && 
make modules_install && 
cp arch/i386/boot/bzImage /boot/vmlinuz_new && 
cp System.map /boot && 
vi /etc/lilo.conf && 
lilo -v 
文件建立好之后，每次编译核心的时候，只需要在/usr/src/linux-2.4.20下输入： 
source make_command 
即可，如果你用的不是lilo来引导系统，可以把最后两行去掉，配置自己的引导程序来引导内核。 
顺便补充一点，&&命令表示顺序执行由它连接的命令，但是只有它之前的命令成功执行完成了之后才可以继续执行它后面的命令。 

##参考：Python安装与版本管理

http://www.jianshu.com/p/4646dedaaff5

