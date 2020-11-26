 

学习笔记

# Python版本差异

可通过查询Python[官网](https://www.python.org/doc/versions/)获取详细说明

1. 在Python解释器中  Python 2 和Python 3 版本不完全兼容

2. 第三方库可能对较新版本的Python 存在不兼容问题，需查阅库文档获取支持的Python版本信息

3. Python不同版本存在不同的特性，需查阅具体Python版本[文档](https://docs.python.org/)，以3.7为例:[Python 3.7 有什么新变化](https://docs.python.org/zh-cn/3.7/whatsnew/3.7.html)

# Python安装

- 注意事项：
    1. 安装目录不要有中文、空格、特殊字符
    2. 非必要情况尽可能只安装一个Python解释器
    3. 安装了多个版本的Python需注意PATH环境变量配置

1. 查看系统信息及已有Python版本信息（以CentOS7 x84_64 环境安装[python 3.8.9](https://www.python.org/ftp/python/3.7.9/Python-3.7.9.tgz)为例）

    ~~~shell
    [root@geekbang ~]# uname -a
    Linux geekbang 3.10.0-957.el7.x86_64 #1 SMP Thu Nov 8 23:39:32 UTC 2018 x86_64 x86_64 x86_64 GNU/Linux
    [root@geekbang ~]# which python
    /usr/bin/python
    [root@geekbang ~]# python -V
    Python 2.7.5
    ~~~

2. 根据硬件平台和操系统版本 [下载 ](https://www.python.org/downloads/)适合的Python版本（[python 3.8.9](https://www.python.org/ftp/python/3.7.9/Python-3.7.9.tgz)）

    ~~~shell
    [root@geekbang ~]# wget https://www.python.org/ftp/python/3.7.9/Python-3.7.9.tgz
    ~~~

3. 安装

    ~~~shell
    [root@geekbang ~]# tar zxf Python-3.7.9.tgz 
    [root@geekbang ~]# cd Python-3.7.9
    [root@geekbang Python-3.7.9]# ./configure --prefix="/usr/local/python3.7.9"
    [root@geekbang Python-3.7.9]# make && make install
    ~~~

    > 1、编译时可能存在依赖：
    >
    > ​			yum groupinstall Development Tools -y
    >
    > ​			yum install zlib-devel -y
    >
    > 2、./configure --prefix="/usr/local/python3.7.9" ： 
    >
    > ​			 --prefix="/usr/local/python3.7.9"  指定安装目录
    >
    > 3、此安装采用默认配置选项，安装后可能会存在问题，如需指定请 ./configure -h 查看帮助文档，自行添加，并外理相关依赖

4. 设置并处理yum问题

    > 采用更改系统PATH的方法, 使python3.7.9 成为默认python

    ~~~shell
    [root@geekbang Python-3.7.9]# cd /usr/local/python3.7.9/
    [root@geekbang bin]# ln -s python3 python
    
    # 临时修改只对当前shell有效，测试无误后可修改至文件
    [root@geekbang bin]# export PATH=/usr/local/python3.7.9/bin:$PATH   
    [root@geekbang bin]# echo $PATH
    /usr/local/python3.7.9/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/root/bin
    
    # 查看修改PATH后python指向
    [root@geekbang bin]# which python
    /usr/local/python3.7.9/bin/python
    
    # 查看yum命令调用python位置
    [root@geekbang bin]# head /usr/bin/yum 
    #!/usr/bin/python
    import sys
    try:
    
    # 查看yum调用Python版本
    [root@geekbang bin]# /usr/bin/python -V
    Python 2.7.5
    
    # 测试yum是否正常运行
    [root@geekbang bin]# yum install tree
    Failed to set locale, defaulting to C
    Loaded plugins: fastestmirror
    Loading mirror speeds from cached hostfile
     * base: mirror.bit.edu.cn
     * epel: ftp.iij.ad.jp
     * extras: mirrors.tuna.tsinghua.edu.cn
     * updates: mirrors.tuna.tsinghua.edu.cn
    Package tree-1.6.0-10.el7.x86_64 already installed and latest version
    Nothing to do
    
    ~~~

    > pip 设置
    >
    > 1、CentOS 7 下 Python2.* 版本没有安装 pip , 如需安装执行： yum install python-pip
    >
    > 2、在该例中，不安装python 2.* 的pip

    ~~~shell
    [root@geekbang bin]# pwd
    /usr/local/python3.7.9/bin
    [root@geekbang bin]# ln -s pip3 pip
    [root@geekbang bin]# ll -d pip
    lrwxrwxrwx 1 root root 4 Nov 26 11:14 pip -> pip3
    
    [root@geekbang bin]# which pip
    /usr/local/python3.7.9/bin/pip
    
    [root@geekbang bin]# pip -V
    pip 20.1.1 from /usr/local/python3.7.9/lib/python3.7/site-packages/pip (python 3.7)
    
    ~~~

    > 当前设置下各版本 python pip 位置

    ~~~shell
    [root@geekbang bin]# which python
    /usr/local/python3.7.9/bin/python
    
    [root@geekbang bin]# which python2
    /usr/bin/python2
    
    [root@geekbang bin]# which pip
    /usr/local/python3.7.9/bin/pip
    
    [root@geekbang bin]# which pip2
    /usr/bin/pip2
    ~~~

5. 更多版本Python安装

    > 虚拟环境工具进行安装，避免版本和第三方库管理混乱

# REPL(交互式解释器)

- pthon

    > 该程序可以交互执行也可采用文件形式加载执行

- ipthon

    > 可以扩展python的交互功能

- bpython


# pip命令

- 配置加速

    国内常用镜像源

    ​	[阿里云]( http://mirrors.aliyun.com/pypi/simple/)、[中国科技大学]( https://pypi.mirrors.ustc.edu.cn/simple/)、[豆瓣(douban)]( http://pypi.douban.com/simple/)、[清华大学]( https://pypi.tuna.tsinghua.edu.cn/simple/)、[中国科学技术大学]( http://pypi.mirrors.ustc.edu.cn/simple/)

    更换pip源方法

     - 临时方法：

        可以在使用pip的时候在后面加上-i参数，指定pip源 

        >pip install  -i pip源地址 [包名]
        >
        >或
        >
        >pip config set global.index-url pip源地址 [包名]

    -	永久方法：

        修改 pip.conf 文件 (没有就创建一个)

        >vim $HOME/.pip/pip.conf
        >
        >​	[global]
        >
        >​	index-url = pip源地址-url pip源地址

        

- 常用命令

    安装:	pip install NAME      

    安装指定版本:	pip install NAME==VERSION

    升级pip: 	pip install pip -U

    查看已安装： pip list

# Python IDE

- [VSCode](https://code.visualstudio.com/)

    - 插件

    - 功能

    - 快捷键

        > option + shift + f ： 格式化代码

        > option + 左/右： 光标移动一个单词
        >
        > option + 上/下： 对光标所在行进行上下位置调换

        > command + 上/下： 光标快速移动到代码块开头/结尾
        >
        > command + 左/右： 光标快速移动到当前行的开头/结尾

        

- [Pycharm](https://www.jetbrains.com/pycharm/download/#section=mac)

- [Jupyter Notebook](https://jupyter.org/)

# Python开发流程

1. 搞清需求 (明白需求十分重要，是后续步骤开展的必要条件)
2. 编写源代码 (.py)
3. 使用Python解释器转换为目标代码（.pyc  一般情况下与步骤4同步完成）
4. 运行程序
5. 测试
6. 修复错误
7. 再运行、测试
8. 测试完成迁移部署

# Python [虚拟环境](https://docs.python.org/zh-cn/3.7/tutorial/venv.html)

-  [virtual environment](https://docs.python.org/zh-cn/3/glossary.html#term-virtual-environment)，

    一个目录树，其中安装有特定Python版本，以及许多其他包。

- 作用

    为每个项目或每个应用各自建立一套“独立、隔离”的Python运行环境，包括Python版本、第三方库版本，

    避免在同一个系统中多个Python版本及各Python版本对应第三方库版本管理混乱

    同时也方便项目的迁移、部署，保持生产环境和测试环境一致

- python 3.* 版本 默认自带 venv 模块

- venv （**使用对应版本的python命令创建对应的该版本的虚拟环境**）

    

    > 创建虚拟环境 myvenv1：	python3.7 -m venv myvenv1
    >
    > 激活 myvenv1虚拟环境:   	sourct myvenv1/bin/activat
    >
    > 退出当前虚拟环境：			deactivate

