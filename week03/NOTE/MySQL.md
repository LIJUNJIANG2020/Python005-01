学习笔记

# MySQL

[下载地址](https://dev.mysql.com/downloads/)

## 企业级MySQL部署需要重点注意以下几点：

- 注意操作系统的平台(32位、64位)
- 注意MySQL版本(MySQL企业版、社区版、MariaDB)
- 注意安装后避免yum 自动更新
- 注意数据库的安全性

## 安装

> CentOS 7  x86_64 
>
> >  注意： CentOS7 自待的mysql 版本为mariadb   
>
> [MySQL-Compatibility-5.7](https://dev.mysql.com/downloads/mysql/5.7.html)

### 1. yum 安装

> [MySQL Yum Repository](https://dev.mysql.com/downloads/repo/yum/)
>
> [MySQL Yum Repository for 7](https://dev.mysql.com/get/mysql80-community-release-el7-3.noarch.rpm)

~~~shell
# 下载yum源 rpm安装包
wget https://dev.mysql.com/get/mysql80-community-release-el7-3.noarch.rpm

# 安装
yum install mysql80-community-release-el7-3.noarch.rpm

# 修改yum源文件
vim /etc/yum.repos.d/mysql-community.repo    
    # 将mysql57-community enabled设置为1
    #	mysql80-community enabled设置为0
    [mysql57-community]
    name=MySQL 5.7 Community Server
    baseurl=http://repo.mysql.com/yum/mysql-5.7-community/el/7/$basearch/
    enabled=1
    gpgcheck=1
    gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-mysql
    ...
    [mysql-cluster-8.0-community]
    name=MySQL Cluster 8.0 Community
    baseurl=http://repo.mysql.com/yum/mysql-cluster-8.0-community/el/7/$basearch/
    enabled=0
    gpgcheck=1
    gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-mysql

# 更改yum仓库
yum clean all && yum makecache

# 安装 mysql 57
yum install mysql-community-server

##############################################################
## 安装完成移除或禁有mysql yum源，防止系统更新时更新mysql版本
# 方法1-移除：
yum remove mysql80-community-release-el7-3.noarch.rpm
# 方法2 -禁用
vim /etc/yum.repos.d/mysql-community.repo
	# 将mysql57-community enabled设置为0
	[mysql57-community]
    name=MySQL 5.7 Community Server
    baseurl=http://repo.mysql.com/yum/mysql-5.7-community/el/7/$basearch/
    enabled=0
    gpgcheck=1
    gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-mysql
   
##############################################################
## mysql 启动、停止、查看状态
systemctl start | stop | status mysqld
~~~

## 配置

1. 首次启动后mysql 5.7会自动生成一个随机密码，保存于/var/log/mysqld.log

    > 获取随机密码  grep 'password' /var/log/mysqld.log

    ```shell
    [root@geekbang ~]# grep 'password' /var/log/mysqld.log 
    2020-11-26T10:53:04.830371Z 1 [Note] A temporary password is generated for root@localhost: -r.bc#33/He&
    ```

2. 登陆 

    > mysql -u USER -p

    ```sql
    [root@geekbang ~]# mysql -uroot -p
    Enter password: 
    Welcome to the MySQL monitor.  Commands end with ; or \g.
    Your MySQL connection id is 3
    Server version: 5.7.32
    
    Copyright (c) 2000, 2020, Oracle and/or its affiliates. All rights reserved.
    
    Oracle is a registered trademark of Oracle Corporation and/or its
    affiliates. Other names may be trademarks of their respective
    owners.
    
    Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.
    
    mysql> show 
    ```

3. 修改用户密码

    >ALTER USER 'root@localhost' IDENTIFIED BY 'new_password';

    ```sql
    mysql> ALTER USER 'root'@'localhost' IDENTIFIED BY 'new_password';
    ERROR 1819 (HY000): Your password does not satisfy the current policy requirements
    
    mysql> ALTER USER 'root'@'localhost' IDENTIFIED BY 'New&Pwd2020';
    Query OK, 0 rows affected (0.00 sec)
    ```

4. 修改密码复杂度限制

    > 查看：SHOW VARIABLES LIKE 'validate_password%';

    ```sql
    mysql>  SHOW VARIABLES LIKE 'validate_password%';
    +--------------------------------------+--------+
    | Variable_name                        | Value  |
    +--------------------------------------+--------+
    | validate_password_check_user_name    | OFF    |
    | validate_password_dictionary_file    |        |
    | validate_password_length             | 8      |
    | validate_password_mixed_case_count   | 1      |
    | validate_password_number_count       | 1      |
    | validate_password_policy             | MEDIUM |
    | validate_password_special_char_count | 1      |
    +--------------------------------------+--------+
    7 rows in set (0.01 sec)
    ```

    > 设置: SET GLOBAL validate_password_policy=0 ;

    ```sql
    # 除低密码复杂度要求
    mysql> SET GLOBAL validate_password_policy=0 ;       
    Query OK, 0 rows affected (0.00 sec)
    
    mysql> SHOW VARIABLES LIKE 'validate_password%';
    +--------------------------------------+-------+
    | Variable_name                        | Value |
    +--------------------------------------+-------+
    | validate_password_check_user_name    | OFF   |
    | validate_password_dictionary_file    |       |
    | validate_password_length             | 8     |
    | validate_password_mixed_case_count   | 1     |
    | validate_password_number_count       | 1     |
    | validate_password_policy             | LOW   |
    | validate_password_special_char_count | 1     |
    +--------------------------------------+-------+
    7 rows in set (0.01 sec)
    
    mysql> ALTER USER 'root'@'localhost' IDENTIFIED BY '12345678';
    Query OK, 0 rows affected (0.00 sec)
    ```

## 字符集设置

> 1. MySQL 中的utf8 不是utf-8字符集， 
> 2. 因字符集问题造成的乱码，是不法修复的，故在使用之前必须做好字符集设置

1. 查看字符集

    > 查看字符集：	show variables like '%character%';
    >
    > 查看校对规则: 	show variables like '%collation_%';
    >
    > > 在字符集里用于字符比较和排序的一套规则
    > >
    > > \*\_\*\_ci  大小写不敏感
    > >
    > > \*\_\*\_cs  大小写敏感

    ```mysql
    mysql> show variables like '%character%';
    +--------------------------+----------------------------+
    | Variable_name            | Value                      |
    +--------------------------+----------------------------+
    | character_set_client     | utf8                       |
    | character_set_connection | utf8                       |
    | character_set_database   | latin1                     |
    | character_set_filesystem | binary                     |
    | character_set_results    | utf8                       |
    | character_set_server     | latin1                     |
    | character_set_system     | utf8                       |
    | character_sets_dir       | /usr/share/mysql/charsets/ |
    +--------------------------+----------------------------+
    8 rows in set (0.00 sec)
    
    mysql> show variables like '%collation_%';
    +----------------------+-------------------+
    | Variable_name        | Value             |
    +----------------------+-------------------+
    | collation_connection | utf8_general_ci   |
    | collation_database   | latin1_swedish_ci |
    | collation_server     | latin1_swedish_ci |
    +----------------------+-------------------+
    3 rows in set (0.01 sec)
    
    ```

2. 配置字符集

    > 配置文件： /etc/my.cnf

    ```shell
    ######
    ## 设置客户端字符集
    [client]   
    default_character_set = utf8mb4
    
    ##
    [mysql]
    default_character_set = utf8mb4
    
    ## 服务设置
    [mysqld]
    bind-address=0.0.0.0
    character_set_server = utf8mb4 # MySQL字符集设置
    init_connect = 'SET NAMES UTF8MB4' # 服务器为每个连接的客户端执行的字符串
    collation_server = utf8mb4_unicode_ci  # 校对规则
    character_set_client_handshake = FALSE 
    
    
    interactive_timeout = 28800 # 针对交互式连接超时时间
    wait_timeout = 28800		# 针对非交互式连接超时时间
    max_connections = 1000		# MySQL 的最大连接数
    #######
    # 重启服务使配置生效
    systemctl restart mysqld
    
    ##  查看
    mysql> show variables like '%character%' ;
    +--------------------------+----------------------------+
    | Variable_name            | Value                      |
    +--------------------------+----------------------------+
    | character_set_client     | utf8mb4                    |
    | character_set_connection | utf8mb4                    |
    | character_set_database   | utf8mb4                    |
    | character_set_filesystem | binary                     |
    | character_set_results    | utf8mb4                    |
    | character_set_server     | utf8mb4                    |
    | character_set_system     | utf8                       |
    | character_sets_dir       | /usr/share/mysql/charsets/ |
    +--------------------------+----------------------------+
    8 rows in set (0.01 sec) 
    
    mysql> show variables like '%collation_%';
    +----------------------+--------------------+
    | Variable_name        | Value              |
    +----------------------+--------------------+
    | collation_connection | utf8mb4_unicode_ci |
    | collation_database   | utf8mb4_unicode_ci |
    | collation_server     | utf8mb4_unicode_ci |
    +----------------------+--------------------+
    3 rows in set (0.00 sec)
    
    
    ```

3. 在mysql 中 utf8 和 utf8mb4 的区别

    > utf8 占用3字节
    >
    > utf8mb4 占用4字节

    ```mysql
    # 查看与utf8相关字符集
    mysql>  SHOW CHARACTER SET WHERE Charset="utf8";
    +---------+---------------+-------------------+--------+
    | Charset | Description   | Default collation | Maxlen |
    +---------+---------------+-------------------+--------+
    | utf8    | UTF-8 Unicode | utf8_general_ci   |      3 |
    +---------+---------------+-------------------+--------+
    1 row in set (0.00 sec)
    
    mysql> SHOW CHARACTER SET LIKE "utf8%";
    +---------+---------------+--------------------+--------+
    | Charset | Description   | Default collation  | Maxlen |
    +---------+---------------+--------------------+--------+
    | utf8    | UTF-8 Unicode | utf8_general_ci    |      3 |
    | utf8mb4 | UTF-8 Unicode | utf8mb4_general_ci |      4 |
    +---------+---------------+--------------------+--------+
    2 rows in set (0.00 sec)
    
    # 查看MYSQL支持的字符集
    SHOW CHARACTER SET;
    mysql> SHOW CHARACTER SET;
    +----------+---------------------------------+---------------------+--------+
    | Charset  | Description                     | Default collation   | Maxlen |
    +----------+---------------------------------+---------------------+--------+
    | big5     | Big5 Traditional Chinese        | big5_chinese_ci     |      2 |
    | dec8     | DEC West European               | dec8_swedish_ci     |      1 |
    | cp850    | DOS West European               | cp850_general_ci    |      1 |
    | hp8      | HP West European                | hp8_english_ci      |      1 |
    | koi8r    | KOI8-R Relcom Russian           | koi8r_general_ci    |      1 |
    | latin1   | cp1252 West European            | latin1_swedish_ci   |      1 |
    | latin2   | ISO 8859-2 Central European     | latin2_general_ci   |      1 |
    | swe7     | 7bit Swedish                    | swe7_swedish_ci     |      1 |
    | ascii    | US ASCII                        | ascii_general_ci    |      1 |
    | ujis     | EUC-JP Japanese                 | ujis_japanese_ci    |      3 |
    | sjis     | Shift-JIS Japanese              | sjis_japanese_ci    |      2 |
    | hebrew   | ISO 8859-8 Hebrew               | hebrew_general_ci   |      1 |
    | tis620   | TIS620 Thai                     | tis620_thai_ci      |      1 |
    | euckr    | EUC-KR Korean                   | euckr_korean_ci     |      2 |
    | koi8u    | KOI8-U Ukrainian                | koi8u_general_ci    |      1 |
    | gb2312   | GB2312 Simplified Chinese       | gb2312_chinese_ci   |      2 |
    | greek    | ISO 8859-7 Greek                | greek_general_ci    |      1 |
    | cp1250   | Windows Central European        | cp1250_general_ci   |      1 |
    | gbk      | GBK Simplified Chinese          | gbk_chinese_ci      |      2 |
    | latin5   | ISO 8859-9 Turkish              | latin5_turkish_ci   |      1 |
    | armscii8 | ARMSCII-8 Armenian              | armscii8_general_ci |      1 |
    | utf8     | UTF-8 Unicode                   | utf8_general_ci     |      3 |
    | ucs2     | UCS-2 Unicode                   | ucs2_general_ci     |      2 |
    | cp866    | DOS Russian                     | cp866_general_ci    |      1 |
    | keybcs2  | DOS Kamenicky Czech-Slovak      | keybcs2_general_ci  |      1 |
    | macce    | Mac Central European            | macce_general_ci    |      1 |
    | macroman | Mac West European               | macroman_general_ci |      1 |
    | cp852    | DOS Central European            | cp852_general_ci    |      1 |
    | latin7   | ISO 8859-13 Baltic              | latin7_general_ci   |      1 |
    | utf8mb4  | UTF-8 Unicode                   | utf8mb4_general_ci  |      4 |
    | cp1251   | Windows Cyrillic                | cp1251_general_ci   |      1 |
    | utf16    | UTF-16 Unicode                  | utf16_general_ci    |      4 |
    | utf16le  | UTF-16LE Unicode                | utf16le_general_ci  |      4 |
    | cp1256   | Windows Arabic                  | cp1256_general_ci   |      1 |
    | cp1257   | Windows Baltic                  | cp1257_general_ci   |      1 |
    | utf32    | UTF-32 Unicode                  | utf32_general_ci    |      4 |
    | binary   | Binary pseudo charset           | binary              |      1 |
    | geostd8  | GEOSTD8 Georgian                | geostd8_general_ci  |      1 |
    | cp932    | SJIS for Windows Japanese       | cp932_japanese_ci   |      2 |
    | eucjpms  | UJIS for Windows Japanese       | eucjpms_japanese_ci |      3 |
    | gb18030  | China National Standard GB18030 | gb18030_chinese_ci  |      4 |
    +----------+---------------------------------+---------------------+--------+
    41 rows in set (0.00 sec)
    ```

4. 创建库、表时字符集继承规则

    > 不指定字符集创建库：create database db1;
    >
    > > 继承MySQL 服务设置的字符集,
    > >
    > > 表继承库，库继承服务设置， 查找时也是这样 表-->库-->服务

    ```mysql
    mysql> create database db1;
    Query OK, 1 row affected (0.00 sec)
    
    mysql> show create database db1;
    +----------+--------------------------------------------------------------------------------------------+
    | Database | Create Database                                                                            |
    +----------+--------------------------------------------------------------------------------------------+
    | db1      | CREATE DATABASE `db1` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci */ |
    +----------+--------------------------------------------------------------------------------------------+
    1 row in set (0.00 sec)
    ```

    

