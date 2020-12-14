# SQL

## SQL语言功能划分：

- DQL: Data Query Language, 数据查询语言，开发工程师学习的重点
- DDL: Data Definition Language, 数据定义语言，操作库和表结构
- DML: Data Mamipulation Language, 数据操作语言，操作表中的记录
- DCL: Data Control Language, 数据控制语言，安全和访问权限控制



## 创建库



## 创建表

> 建议：
>
> 1. 创建数据表的个数和表中字段，越少越好且相互独立，使之简洁
> 2. 联合主键字段越少越好
> 3. 对于外键，内部系统性能要求不高可以使用（适用于单机），对于外部系统，所有外键建议在应用层解决（适用于并发和分布式等对性能要求较高的场景）

```mysql
# 使用反引号可避免与双单引号冲突， 与mysql 保留字段进行区别
CREATE TABLE `book` (
	`book_id` int(11) NOt NULL AUTO_INCREMENT,
	`book_name` varchar(255),
    PRIMARY KEY(`book_id`)
)ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_cl;
```

## 查询

> 1. 注意：
>     1. 生产环境下因为列数相对较多，一般禁用 SELECT *
>     2. WHERE字段为避免全表扫描，一般需要增加索引



> 2. SELECT查询时关键字顺序
>
> 书写顺序： SELECT ... FROM ... WHERE ... GROUP BY ... HAVING ... ORDER BY ... LIMIT
>
> 执行顺序：

```mysql
SELECT DISTINCT book_id, book_name, count(*) as number   # 5
FROM book JOIN author ON book.sn_id = author.sn_id       # 1
WHERE pages > 500										 # 2
GROUP BY book.book_id									 # 3
HAVING number > 10										 # 4	
ORDER BY number											 # 6
LIMIT 5													 # 7
```

## SQL函数

> 包括 算术函数、字符串函数、日期函数、转换函数、聚合函数

### 聚合函数

> 聚合函数忽略空行
>
> 运行在行组上，计算和返回单个值的函数	

- COUNT()

    > 行数

- MAX()

    > 最大值

- MIN()

    > 最小值

- SUM()

    > 求和

- AVG()

    > 平均值
    
- 示例：

```mysql
mysql> select count(*) from t1;
+----------+
| count(*) |
+----------+
|      570 |
+----------+
1 row in set (0.01 sec)


mysql> select count(*), avg(n_star), max(n_star) from t1 where id < 10;
+----------+-------------+-------------+
| count(*) | avg(n_star) | max(n_star) |
+----------+-------------+-------------+
|        9 |      2.8889 |           5 |
+----------+-------------+-------------+
1 row in set (0.00 sec)


mysql> select count(*), n_star from t1 group by n_star;
+----------+--------+
| count(*) | n_star |
+----------+--------+
|        9 |      1 |
|       56 |      2 |
|      315 |      3 |
|      150 |      4 |
|       40 |      5 |
+----------+--------+
5 rows in set (0.01 sec)

mysql> select count(*), n_star from t1 group by n_star having n_star > 3 order by n_star desc;
+----------+--------+
| count(*) | n_star |
+----------+--------+
|       40 |      5 |
|      150 |      4 |
+----------+--------+
2 rows in set (0.00 sec)

mysql> select count(*), n_star from t1 group by n_star having n_star > 3 order by n_star;
+----------+--------+
| count(*) | n_star |
+----------+--------+
|      150 |      4 |
|       40 |      5 |
+----------+--------+
2 rows in set (0.00 sec)

mysql> SELECT AVG(n_star) from t1;
+-------------+
| AVG(n_star) |
+-------------+
|      3.2737 |
+-------------+
1 row in set (0.00 sec)

```



## 子查询

> 需要从查询结果集中再次进行查询，才能得到想要的结果

- 关联子查询和非关联子查询

    - 非关联子查询

        ```mysql
        mysql> select count(*), n_star from t1 group by n_star having n_star > (select avg(n_star) from t1) order by n_star desc;
        +----------+--------+
        | count(*) | n_star |
        +----------+--------+
        |       40 |      5 |
        |      150 |      4 |
        +----------+--------+
        2 rows in set (0.00 sec)
        ```

    - 关联子查询

        ```mysql
        # 使用IN
        SELECT * FROM TABLE_A WHERE condition IN (SELECT condition FROM TABLE_B)
        
        # 使用EXIST
        SELECT * FROM TABLE_A WHERE EXIST(SELECT condition FROM B WHERE B.condition=A.condithon)
        ```

        ```python
        # IN
        for i in TABLE_B:
        	for j in TABLE_A:
        		if TABLE_B.condition == TABLE_A.condition:
        			...
        			
        # EXIST
        for i in TABLE_A:
        	for j in TABLE_B:
        		if TABLE_A.condition == TABLE_B.condition:
        			...
        ```

        

- 何时使用IN， 何时使用EXIST

    > 小表驱动大表
    >
    > 表a 小于表 b时EXISTS ,反之用IN

## 常见连接(JOIN)

- 自然连接 

    > SELECT <SELECT_LIST> FROM T_A A INNER JOIN T_B B ON A.KEY = B.KEY

- ON 连接  

- USING 连接

- 外连接

    - 左外连接

        > SELECT <SELECT_LIST> FROM T_A A LEFT JOIN T_B B ON A.KEY = B.KEY

    - 右外连接

        > SELECT <SELECT_LIST> FROM T_A A RIGHT JION T_B B  ON A.KEY = B.KEY

    - 全外连接(MySQL不支持)

 ## 事务

> 在 MySQL 中只有使用了 Innodb 数据库引擎的数据库或表才支持事务。
>
> 事务处理可以用来维护数据库的完整性，保证成批的 SQL 语句要么全部执行，要么全部不执行。
>
> 事务用来管理 insert,update,delete 语句

### 事务的特性  -- ACID

- A   原子性(Atomicity)

    > 不可分割 

- B   一致性(Consistency)

    > 状态只有成功与不成功

- I    隔离性 (Isolation)

    > 每一个事务比此间是独立的

- D   持久性(Durability)

    > 事务提交后对数据的修改是持久的

### 隔离级别

- 读未提交

    > 允许读到未提交的数据

- 读已提交

    > 只能读到已提交的内容

- 可重复读 (MySQL 默认)

    > 同一事务在相同查询条件下两次查询得到的数据结果一致

- 可串行化

    > 事务进行串行化，但是牺牲了并发性能



在mysql中事务默认是自动进行提交（隐式提交）的可能过下面的方法进行关闭

```mysql
# 查看
mysql> show variables like 'autocommit';
+---------------+-------+
| Variable_name | Value |
+---------------+-------+
| autocommit    | ON    |
+---------------+-------+
1 row in set (0.02 sec)

# 修改
mysql> set autocommit=0;
Query OK, 0 rows affected (0.00 sec)

mysql> show variables like 'autocommit';
+---------------+-------+
| Variable_name | Value |
+---------------+-------+
| autocommit    | OFF   |
+---------------+-------+
1 row in set (0.00 sec)


```



事务关键字：

- BEGIN     

    > 开启一个事务

- COMMIT

    > 提交事务

- ROLLBACK 

    > 回滚

- SAVEPOINT

    > 保存点

