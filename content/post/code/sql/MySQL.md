---
title: MySQL
description:  学习MySQL基础知识
# 默认url路径是title如果不写slug
slug: MySQL
date: 2024-08-13 12:06:05+0000
toc: true
categories:
  - 学习笔记
tags:
  - SQL
  - MySQL
  - DDL
  - DML
---

#  MySQL

***

##  SQL分类

![image-20230127223703569](img/mysql/image-20230127223703569.png)

##  DDL

这里只讲常用的定义语句

### 创建数据库

```mysql
#创建数据库     CREATE DATABASE  数据库名;
CREATE DATABASE `jdbc_demo02`; 
```

### 删除数据库

```mysql
#删除数据库   DROP DATABASE 数据库名
DROP DATABASE `jdbc_demo02`
```

### 创建表

```sql
CREATE TABLE IF NOT EXISTS users(    #注意一个表用()括起来,`` 这个转义，避免和数据库定义好的关键字发生冲突
    id INT PRIMARY KEY,		     	#一列以，结束，PRIMARY KEY设置主键，主键不可以重复
    `username` VARCHAR(10),			#IF NOT如果没有这张表就创建
    pwd VARCHAR(10),				#每列的数字代表字符，int不需要指定的多少字符的
    email VARCHAR(20),				#列名前面
    birthday DATE                   #在sqlyog执行前要鼠标选中要执行的语句
);
```

### 删除表

```mysql
#删除一张表    DROP TABLE  数据库名.表名
DROP TABLE `jdbc_demo01`.`person`;  
```

### COMMENT

后面加注释信息用单引号

#### 表增加注释

```sql
create table if not exists sys_person (
    name varchar(20) comment '姓名'
) engine = innodb default charset = utf8 comment '个人信息表';
```

#### 表增加注释

```sql
create table if not exists sys_person (
    name varchar(20) comment '姓名'
) engine = innodb default charset = utf8 comment '个人信息表';
```

####  查看注释信息

SHOW FULL COLUMNS FROM 表名;

###  增加/删除/修改列

#### 增加

```mysql
alter table jdbc_demo01.demo10_spring_boot_example
    add 列_name int null;  #这个null是当前的列的位置如First,可以不写
```

#### 删除

```mysql
alter table jdbc_demo01.demo10_spring_boot_example
    drop column promise;
```

#### 修改

- 暂时都可以设置默认值

- **修改列的属性和设置默认值，不可以修改列的名字**

    ```mysql
    #修改不为空且默认值是100
    alter table jdbc_demo01.demo10_spring_boot_example
        modify column twd DEC default '100' ;
    ```

- **使用 CHANGE 子句, 语法有很大的不同。 在 CHANGE 关键字之后，紧跟着的是你要修改的字段名，然后指定新字段名及类型。**
- **可以修改列名和属性和设置默认值**

    ```mysql
     ALTER TABLE testalter_tbl CHANGE i j BIGINT  default 'user' ; #设置默认值
    ```

## DML

### SELECT

查询都需要注意分页

```mysql
#查看表(全部的数据)
SELECT * FROM users ;
#后面可带参数(查符合条件的数据)  返回filed(表的列名)等于value的条目
SELECT * FROM users where filed = value;
#查询表数据的总数   COUNT：把查出来的数量赋值给这个变量
SELECT COUNT(1) AS COUNT FROM smbms_user;
#新型查询
SELECT t.*FROM jdbc_demo01.demo10_spring_boot_example t LIMIT 501  #默认是0-3
```

### INSERT

表中插入数据(insert)：values插入多行/单行  value 插入单行

```mysql
#往表中插入数据
#指定表
INSERT INTO users(id,username,pwd,email,birthday)
#设置值
VALUES(19,'xxl','xxl123456','3578144921@qq.com','20030711');    #; 是结束一条语句，
#多次插入
INSERT INTO demo09_books(book_name,book_counts,description) 
VALUE('java',2,'学习java之道'), 
('C',5,'c语言从入门到放弃'),
('python',10,'python学习');
```

### DELETE

```mysql
#删除表数据
DELETE FROM users WHERE id = 20;   #删除id为20的哪一行数据 
```

### UPDATE

```mysql
# UPDATE 表名  set 字段 where 哪一行
UPDATE `account` SET `balance` = 2000.0  WHERE `id` = 1; 
```

## MySQL关键字

### AUTO_INCREMENT

主键自增长，默认第一个为1，每增加一条数据加1，int类型才可以

### START TRANSACTION

开启事务，写SQL文件的时候可以用上

###  SHOW FULL PROCESSLIST

直接执行的MySQL命令，显示用户正在运行的线程 ，KILL id：杀死进程

### WHERE

条件某某不在某某之间，where后面是条件表达式

```mysql
#where 用户角色(int)  NOT BETWEEN 1 AND 2 :不在1和2 之间
SELECT userName,phone,userRole 
FROM smbms_user 
WHERE userRole 
NOT BETWEEN 1 AND 2 
```

#### not、or、and

and与，两者都为true才是true

```mysql
#条件判断 and:返回同时符合两个条件的条目
SELECT * FROM smbms_user WHERE userRole = 1 AND  gender = '女';
```

or或，其中一个为true就是true

```mysql
#条件判断 or:返回符合两个条件其中之一的条目
SELECT * FROM smbms_user WHERE userRole = 1 OR  userName = 'xxl';
```

not非，返回不符合条件的条目

```mysql
select * from user where  not  age = 1;
```

#### in

```mysql
#条件:  返回userRole = 1 or userRole = 2的条目
SELECT * FROM smbms_user WHERE userRole IN(1,2);
```

###  CONSTRAINT

-  约束用于预防破坏表之间连接的行为。
-  约束也能防止非法数据插入外键列，因为它必须是它指向的那个表中的值之一。

### FOREIGN 

`FOREIGN  KEY `在A表中指向B表的某个列,如果一张表增加外键就使用foreign key,
其实强关联(使用FOREIGN  KEY)，也可以使用弱关联(列就是别的表的一列)但是无法保证数据的完整性

### REFERENCES

跟FOREIGN  KEY连用，用于指向B表的某个列(主键)例如

```mysql
CREATE TABLE IF NOT EXISTS demo08(
    id INT PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(10),
    tid INT ,
    CONSTRAINT  FOREIGN  KEY(tid) REFERENCES demo06(id)  #指向另一个表的列
)ENGINE = INNODB DEFAULT CHARSET=utf8;
```

### BETWEEN

```sql
# 查询ID从1到10的数据
select * from users where id between 1 and 10;
```

### SHOW

- 查看数据库

```mysql
SHOW DATABASES;
```

- 查看数据库表

```mysql
SHOW TABLES
```

### COUNT

返回一个表中的所有数据行数

```sql
SELECT COUNT(*) FROM student_table;
```

### HAVING

HAVING 是 SQL 中用于筛选分组结果的子句。它与 WHERE 子句类似，但主要区别在于 HAVING 是在 GROUP BY 之后对分组的数据进行过滤，而 WHERE 是在分组之前过滤原始数据。
HAVING 子句用于限制 GROUP BY 后的结果集，只返回满足特定条件的分组。它通常与聚合函数（如 COUNT、SUM、AVG、MAX、MIN 等）一起使用。

```sql
/*
假设有一个销售记录表 sales，包含以下字段：
product_id（产品ID）
sale_date（销售日期）
amount（销售金额）*/
# 你想查找销售总额超过 1000 的产品。
SELECT product_id, SUM(amount) as total_sales
FROM sales
GROUP BY product_id
HAVING SUM(amount) > 1000;
```

### DISTINCT

指定某个列，去重

```mysql
select DISTINCT  core_admin.`name` 姓名,conversation.datetime 谈话时间
from core_admin join conversation on core_admin.id = conversation.number where  conversation.datetime > '2022-09-01' GROUP BY core_admin.`name` ;
# 姓名是重复的，时间不重复后面的group by就是去重那个列，相应的时间行也去重
```

## 外键

> MySQL 的外键（Foreign Key）是一种关系型数据库中用于建立表与表之间关联关系的重要工具。 外键定义了两个表之间的引用关系，它连接了两个表，使它们之间建立起一定的联系。 外键用于维护表与表之间的一致性和完整性，确保数据的准确性和可靠性
 
- 把A表中B表ID指定外键（B表的Id是A表一个字段），删除A表一行数据之后，B表中关联A表的字段自动删除


## 索引

> 索引 是数据库中用于提高查询速度的数据结构。它类似于书籍的目录，可以帮助快速定位到所需的数据，而无需扫描整个表。

- 把某个字段变成索引可以让他拥有和主键一样得效果就是不能重复出现

1. 索引的作用
   - 提高数据检索速度，减少数据库查询的 I/O 操作。
   - 常用于加速 SELECT 查询和 WHERE 子句中的条件判断。
2. 索引的使用
   - 创建索引：CREATE INDEX index_name ON table_name(column_name);
   - 删除索引：DROP INDEX index_name ON table_name;
   - MySQL 中，索引自动用于优化查询，无需手动指定。
3. 索引的种类
   - 普通索引（Normal Index）: 最基本的索引类型，没有唯一性限制。
   - 唯一索引（Unique Index）: 索引列的值必须唯一，允许有一个 NULL 值。
   - 主键索引（Primary Key）: 一种特殊的唯一索引，不允许 NULL 值，一个表只能有一个主键索引。
   - 全文索引（Full-text Index）: 用于全文搜索，适合较长文本字段的搜索操作。
   - 组合索引（Composite Index）: 由多个列组合而成的索引，优化多列查询。
4. 注意事项
   - 索引可以加速查询，但也会增加插入、更新、删除操作的时间成本。
   - 不宜对频繁更新的列或小表创建过多索引。

## MYSQL注意点

###  数据长度问题

存的数据超过数据库规定的字符限制就会被截断

###  时间类型问题

```java
LocalDateTime dateTime = LocalDateTime.now();  //精确到秒  对应mysql中timestamp类型
        LocalDate date = LocalDate.now();   //不精确到秒对应MySQL中的date类型
        System.out.println(date);
        System.out.println(dateTime);

//2023-06-25
//2023-06-25T00:18:48.428517600
```

## 联表查询

### 分页

```mysql
#分页    select 选择字段 from 表明 limit 偏移量,条目数
SELECT userName,userPassword FROM smbms_user LIMIT 0,3;
#limit 条目数 offset 偏移量 注意limit放在语句最后
SELECT userName,userPassword FROM smbms_user LIMIT 3 OFFSET 0;
```

### 分页+排序

```mysql
#打印userName,phone字段 ，条件是phone > '25769806700'，根据phone的值降序排，显示三条记录
SELECT userName,phone FROM smbms_user WHERE phone > '25769806700' ORDER BY phone DESC limit 0,3;
```

### 排序

```mysql
#按照字节数升序 排
SELECT userName FROM smbms_user   ORDER BY LENGTH(userName) ASC;
```

### 二级排序(可以多级排序)

```mysql
#根据userRole升序排如果userRole重复就按照phone降序排
SELECT userName,phone,userRole FROM smbms_user ORDER BY  userRole ASC , phone DESC;
```

### 模糊查询

#### 全模糊%%

方式1

```mysql
#WHERE gender LIKE '%女%':条件返回gender的值等于女的条目
SELECT userName,gender FROM smbms_user WHERE gender LIKE '%女%';
```

方式2

```mysql
select * from user_blog ub join user_role ur on ub.user_role_id = ur.user_role_id where ub.user_blog_username like  concat('%',#{username},'%')
```

#### %value%、%value、value%的区别

1. `value%`：这种模式表示以指定的值开头的匹配项。例如，如果使用 `SELECT * FROM table WHERE column LIKE 'abc%'`，它将匹配以 "abc" 开头的所有值，如 "abc123"、"abcdef" 等。
2. `%value%`：这种模式表示包含指定值的匹配项。例如，如果使用 `SELECT * FROM table WHERE column LIKE '%abc%'`，它将匹配任何位置包含 "abc" 的值，如 "123abc456"、"abcdefg" 等。
3. `%value`：这种模式表示以指定的值结尾的匹配项。例如，如果使用 `SELECT * FROM table WHERE column LIKE '%abc'`，它将匹配以 "abc" 结尾的所有值，如 "123abc"、"defabc" 等。

### 多表查询

#### 简单多表查询

以下展示也可以称之为隐式内连接

```mysql
#多表查询   把smbms_user.userRole的每个值与smbms_role.roleCode匹配，相等就返回
#两张表拥有一样的字段需要声明来自那张表；r.creationDate(可以展示一样的字段需要指明是那张表)
SELECT userName,userRole,roleCode,roleName,r.creationDate FROM smbms_user u,smbms_role r WHERE u.`userRole` = r.`roleCode`;
#为了优化思考建议每个字段都声明来自那张表
SELECT u.userName,u.userRole,r.roleCode,r.roleName,r.creationDate FROM smbms_user u,smbms_role r WHERE u.`userRole` = r.`roleCode`;
```

#### 联表写法

有n个表实现多表查询，则至少需要n-1的连接条件，可以有多个

- **非等值连接 vs 等值连接**

  ```mysql
  #等值连接  连接条件等于  = 
  SELECT u.userName,u.userRole,r.roleCode,r.roleName,r.creationDate 
  FROM smbms_user u,smbms_role r 
  WHERE u.`userRole` = r.`roleCode`;
  
  #非等值连接  > < != 
  #第一种写法        条件：返回d3.salary符合在d4.lowSalary和d4.highSalary的之间的条件的条目
  SELECT d3.name,d3.salary,d4.grade FROM demo03 d3,demo04 d4 WHERE d3.salary BETWEEN d4.lowSalary AND d4.highSalary;
  #第二种写法   注意and没有它就会出现笛卡尔积错误
  SELECT d3.name,d3.salary,d4.grade FROM demo03 d3,demo04 d4 WHERE d4.lowSalary <= d3.salary AND d3.salary <= d4.highSalary;
  ```

- **自连接  vs 非自连接**

  ```mysql
  #自连接  自己连接自己  eg：查询自己的上司是谁
  SELECT d3.`name`,d3.boss,d4.`name`,d4.boss FROM demo03 d3,demo03 d4 WHERE d3.name = d4.boss;
  
  #非自连接  和其他表连接
  SELECT d3.name,d3.salary,d4.grade FROM demo03 d3,demo04 d4 WHERE d4.lowSalary <= d3.salary AND d3.salary <= d4.highSalary;
  ```

- **内连接 vs 外连接**

  ```mysql
  #内连接(之前写的都是内连接):合并具有同一列的两个以上的表的行，结果集中不包含一个表于另一个表的不匹配的行 结果集就是红色部分
  SELECT d3.`name`,d3.boss,d4.`name`,d4.boss FROM demo03 d3,demo03 d4 WHERE d3.name = d4.boss;
  ```

  ![image-20230113022809493](img/mysql/image-20230113022809493.png)


```text
/*
  外连接:  红色部分为结果集
  分为：左外连接:合并具有同一列的两个以上的表的行，结果除了包含一个表于另一个表的匹配的行,还查询到左表中不匹配的行
      右外连接:合并具有同一列的两个以上的表的行，结果除了包含一个表于另一个表的匹配的行,还查询到右表中不匹配的行
        满连接:合并具有同一列的两个以上的表的行，结果除了包含一个表于另一个表的匹配的行,还查询到左表和右表中不匹配的行
*/

```

**右连接**

```mysql
#右外连接:合并具有同一列的两个以上的表的行，结果除了包含一个表于另一个表的匹配的行,还查询到右表中不匹配的行
/*
92语法mySQL支持内连接不支持外连接(外连接,左连接)，用SQL99语法JOIN..ON实现右外连接
SQL99语法内连接与外连接
*/
#内连接
SELECT d3.name,d3.salary,d4.grade FROM demo03 d3 INNER JOIN demo04 d4 ON d3.salary BETWEEN d4.lowSalary AND d4.highSalary;
#外连接
SELECT d3.name,d3.salary,d4.grade FROM demo03 d3 RIGHT OUTER JOIN demo04 d4 ON d3.salary BETWEEN d4.lowSalary AND d4.highSalary;
```

![image-20230113022935850](img/mysql/image-20230113022935850.png)


**左连接**

```mysql
#左外连接:合并具有同一列的两个以上的表的行，结果除了包含一个表于另一个表的匹配的行,还查询到左表中不匹配的行
/*
92语法mySQL支持内连接不支持外连接，用SQL99语法JOIN..ON实现左外连接
SQL99语法内连接与外连接
*/
#内连接
SELECT d3.name,d3.salary,d4.grade FROM demo03 d3 JOIN demo04 d4 ON d3.salary BETWEEN d4.lowSalary AND d4.highSalary;
#外连接
SELECT d3.name,d3.salary,d4.grade FROM demo03 d3 LEFT OUTER JOIN demo04 d4 ON d3.salary BETWEEN d4.lowSalary AND d4.highSalary;

```



![image-20230113023000612](img/mysql/image-20230113023000612.png)

**满连接：使用UNION(将多个select语句的结果集合并成一个结果集)关键字**

```mysql
#满连接:合并具有同一列的两个以上的表的行，结果除了包含一个表于另一个表的匹配的行,还查询到左表和右表中不匹配的行
#mySQL不支持99语法满连接FULL OUTER JOIN...ON可以使用union和union all实现满链接
#99语法内连接
SELECT d3.name,d3.salary,d4.grade FROM demo03 d3 INNER  JOIN demo04 d4 ON d3.salary BETWEEN d4.lowSalary AND d4.highSalary;  
#union(两个表同样的部分会去重，效率底下)，union all(不去去重，效率高)
SELECT d3.name,d3.salary,d4.grade 
FROM demo03 d3  
LEFT OUTER JOIN demo04 d4 
ON  d3.salary BETWEEN d4.lowSalary AND d4.highSalary
UNION ALL
SELECT d3.name,d3.salary,d4.grade 
FROM demo03 d3 
RIGHT OUTER JOIN demo04 d4 
ON d3.salary BETWEEN d4.lowSalary AND d4.highSalary
WHERE salary IS NULL ; 
```

![image-20230113023148218](img/mysql/image-20230113023148218.png)

#### join...0N的7 种实现

![image-20230113133819697](img/mysql/image-20230113133819697.png)

- 左一，右一

  ```mysql
  #左上(左连接)，右上(右连接)
  SELECT d3.name,d3.salary,d4.grade FROM demo03 d3 LEFT OUTER JOIN demo04 d4 ON d3.salary BETWEEN d4.lowSalary AND d4.highSalary;
  
  SELECT d3.name,d3.salary,d4.grade FROM demo03 d3 RIGHT OUTER JOIN demo04 d4 ON d3.salary BETWEEN d4.lowSalary AND d4.highSalary;  
  ```

- 左中，右中

  ```mysql
  #左中，右中
  SELECT d3.name,d3.salary,d4.grade 
  FROM demo03 d3 
  LEFT OUTER JOIN demo04 d4 
  ON d3.salary BETWEEN d4.lowSalary AND d4.highSalary 
  WHERE d3.salary IS NULL;
  
  SELECT d3.name,d3.salary,d4.grade 
  FROM demo03 d3 
  RIGHT OUTER JOIN demo04 d4 
  ON d3.salary BETWEEN d4.lowSalary AND d4.highSalary 
  WHERE d3.salary IS NULL;
  ```

- 左下，右下

  ```mysql
  #左下(满链接)，右下
  SELECT d3.name,d3.salary,d4.grade 
  FROM demo03 d3 
  LEFT OUTER JOIN demo04 d4 
  ON d3.salary BETWEEN d4.lowSalary AND d4.highSalary 
  UNION ALL 
  SELECT d3.name,d3.salary,d4.grade 
  FROM demo03 d3 
  RIGHT OUTER JOIN demo04 d4 
  ON d3.salary BETWEEN d4.lowSalary AND d4.highSalary 
  WHERE d3.salary IS NULL;
  
  
  SELECT d3.name,d3.salary,d4.grade 
  FROM demo03 d3 
  LEFT OUTER JOIN demo04 d4 
  ON d3.salary BETWEEN d4.lowSalary AND d4.highSalary 
  WHERE d3.salary IS NULL 
  UNION ALL 
  SELECT d3.name,d3.salary,d4.grade 
  FROM demo03 d3 
  RIGHT OUTER JOIN demo04 d4 
  ON d3.salary BETWEEN d4.lowSalary AND d4.highSalary 
  WHERE d3.salary IS NULL;
  ```

##  子查询

>  子查询(内查询)在主查询之前执行一次查询
> 子查询的结果主查询使用 

### 注意点

1. 子查询要被包括在括号内
2. 将子查询放在比较条件的右侧
3. 单行操作符对应单行子查询(子查询的结果为一个)，多行操作符对应多行子查询(子查询的结果为多个)

### 示例

```mysql
#业务：查出demo03表中比名字为码农1工资高的
#第一种方式自连接+非等值连接
# 92
SELECT d2.`name`,d2.`salary` FROM demo03 d1,demo03 d2 
WHERE  d1.`salary` < d2.`salary` AND  d1.`name` = '码农1';
# 99
SELECT d2.`name`,d2.`salary` FROM demo03 d1 JOIN demo03 d2 
ON  d1.`salary` < d2.`salary` AND d1.`name` = '码农1';

#子查询:查询中又带着查询  
SELECT `name`,salary   #外查询
FROM demo03 WHERE salary > (
		   SELECT salary FROM demo03 WHERE `name` = '码农1'		  #子查询	
		);

```

### 子查询分类

#### 角度1：内查询的结果返回值

- 单行子查询
    - 返回一个结果就为单行子查询
- 多行子查询
    - 返回多个结果就为多行子查询

#### 角度2：内查询是否被执行多次

- 相关子查询
    - 返回的结果为一样
- 不相关子查询
    - 返回的结果不一样

### 6：其他的数据库操作

####  查看表的结构

```mysql
DESC smbms_user;  
```

#### 笛卡尔积

```mysql
# 笛卡尔积错误,错误原因：缺少了多表连接
SELECT userName,roleCode FROM smbms_user,smbms_role;  #每个userName把所有roleCode都匹配了
#笛卡尔积(交叉连接)有两个集合n,m,有多少种交叉结果。答案：n.lenght * m.lenght 种结果
# eg：(x,y)和(a,b) 有四种(x,a),(x,b),(y,a),(y,b)
```

#### char和varchar

```text
数据库char和varchar的区别：
    1、char类型的长度是固定的，而varchar类型的长度是可变的；
    2、char类型每次修改的数据长度相同，效率更高，而varchar类型每次修改的数据长度不同，效率更低。
char存取固定的String
varchar存取可变的String
```

#### varchar(10)和char(10)的区别

##### 存储方式

**CHAR:**

`固定长度：`CHAR 类型的字段总是分配固定长度的存储空间。
如果存储的字符串长度小于定义的长度，MySQL 会在字符串后面自动填充空格以达到固定长度。
例如，定义了 CHAR(10) 的字段，如果你插入了字符串 'abc'，它将被存储为 'abc '（后面有7个空格）。

**VARCHAR:**

`可变长度：`VARCHAR 类型的字段根据实际存储的字符串长度分配存储空间，最多不会超过定义的最大长度。
不会自动填充空格，存储的字符串长度就是实际长度，再加上1个或2个字节用于存储长度信息。
例如，定义了 VARCHAR(10) 的字段，如果你插入字符串 'abc'，它将被存储为 'abc'，不附加空格。

##### 存储效率

**CHAR:**

- 由于是固定长度，存储效率较高，特别适合存储长度一致的数据，如固定格式的代码（如国家代码、邮政编码等）。
- 因为不需要存储长度信息，所以检索时可能比 VARCHAR 更快。

**VARCHAR:**

- 对于长度不确定的字符串，VARCHAR 更节省空间，因为它只存储实际的数据长度。
- 但是由于需要额外的字节来存储字符串的长度信息，性能上在某些情况下可能会略低于 CHAR。


## 数据类型

![image-20230330093820865](img/mysql/image-20230330093820865.png)

VARCHAR和TEXT类型是变长类型，其存储需求取决于列值的实际长度（在前面的表格中用L表示），而不是取决于类型的最大可能尺寸。

假如一个VARCHAR(10)列能保存一个最大长度为10个字符的字符串，实际的存储需要字符串的长度L加上一个字节以记录字符串的长度。对于字符abcd，L是4，而存储要求5个字节。

## E-R图

ER图是一种用于描述实体-关系模型（Entity-Relationship Model）的图形化工具。它由实体、属性和关系三部分组成，能够清晰地表示不同实体之间的关系。

下面是ER图的画法：

1. 确定实体：根据系统需求，确定需要建模的实体，并在ER图中画出它们的框架。
2. 确定属性：在实体框架内写下它们的属性，并用椭圆形将它们圈起来。
3. 确定关系：在实体之间确定关系，并用菱形标记它们。关系可以是一对一、一对多或多对多。
4. 确定关系的基数：在菱形中标记关系的基数，即一个实体在关系中的最小和最大出现次数。可以用“1”表示最小基数，用“*”表示最大基数。
5. 确定外键：在相关的实体之间画出箭头，并在箭头的对应端口写下外键。
6. 检查ER图：检查ER图是否符合设计需求和规范，并进行必要的修改和调整。

在绘制ER图时，需要遵循一些基本的规则，如实体、属性和关系的命名应该清晰明了，关系的基数应该符合实际需求等。同时，还需要注意ER图的简洁性和易读性，避免冗余和复杂的关系。

### 案例：将下图表格合理拆分为表，并画出ER图

![image-20231119145256695](img/mysql/image-20231119145256695.png)

![定额数据建模](img/mysql/定额数据建模.jpg)

## 函数

### 字符串函数

菜鸟教程：[MySQL 函数 | 菜鸟教程 (runoob.com)](https://www.runoob.com/mysql/mysql-functions.html)

```mysql
#只返回字符串第一个字符的ASCII码，数字也是如此
select ASCII(100) test from dual;

#查看字符串长度、字符串占几个位置
#char_length是指字符串的长度，length是指字符在字符集的长度，如utf-8中英文占一个byte，中文占三个
select length('你哈'),char_length('hello'),char_length('你好')  from  dual;

#拼接函数，在适合和mybatis使用注意这个参数个数不是固定的
select concat('你好','，','xxl','hello','world')  test from dual;

#连接字符串
#concat相当于concat_ws('',param1,param2)，第一个是分隔符，连接字符串的分隔符
select  concat_ws('你好','，','xxl','hello','world') from dual;

#替换
#MySQL索引是从1开始,从字符串7的位置，后面的5个字符替换为‘xxl’,注意长度
select insert('Hello,world',7,5,'xxl')  from dual;

#提换
#从字符串匹配‘llo’，如果有则替换为‘x’，没有不替换
select replace('Hello,World','llo','x')  from dual;

#大小写转换注意查询条件可以使用比如select * from user where upper(username) = 'xxl'，也就是
#说查询的数据会经过转化
select  upper('heLLo'),lower('Hello') from  dual;

#取指定的字符串，超过字符串长度则表示全取
#从左边取第一个
#从右边取第一个
select left('Hello',1),right('World',1) from dual;

#左对齐，右对齐,可以使用参数补足空位置
select lpad('Hello',10,'*') from dual; -- *****Hello  字符串长度是否到达10，没有在左边用*补
select rpad('Hello',10,'*') from dual; -- Hello*****

#去掉首尾空格
select length(' Hello,World '),length(trim(' Hello,World ')) from dual;
#去掉头部空格
select length(' Hello,World '),length(ltrim(' Hello,World ')) from dual;
#去掉尾部空格
select length(' Hello,World '),length(rtrim(' Hello,World ')) from dual;
#去掉首尾匹配的字符串
select trim('H' from 'Hello,World') from dual; -- ello,World

#返回特定字符串的重复结果相当于拼接，这个可以指定次数
select repeat('Hello',4) from dual;

#返回n个空格
select length(space(6)) from dual; -- 6

select ASCII('a'),ASCII('A'),ASCII('B') from dual;
#比较两个的大小字符串(如果相等就比较后面的 ), 负数右边大，0相等，正数左边大   ASCII('A') - ASCII('B') =  -1
select strcmp('AB','AC')  from dual;

#比较两个字符串/长度/数字是否相等，相等则返回null，否则返回var1，忽略大小写
select nullif('he','He') from dual; -- null

#从字符串指定位置截取
select substr('Hello,World',7,1) from dual; -- W

#从str找指定字符串(大小写不影响结果)，如果有就返回首次出现的位置，没有则返回0
select locate('l','Hello,World') from dual;

#返回字符串列表指定位置的字符串
select elt(3,'h','e','l','l','o') from dual; -- l

#返回指定字符串在字符串列表的位置(int),注意必须是第一个字符串能匹配上，如果只是其中能匹配上则为0，就是没匹配上
select field('hello','hello','world','hello') from dual; -- 1

#返回特定字符串在一个字符串的第一次出现的位置，这个字符串其中的字符用逗号隔开,忽略大小写，MySQL跟大小写相关的基本忽略
select find_in_set('he','hello,world,He,he') from dual; -- 3

SELECT SUBSTRING_INDEX(CFDD, '/', 1) , COUNT(*)  FROM T_YQ_CXXX GROUP BY CFDD;
```

### 日期函数

#### 获取时间

![image-20230514185228333](img/mysql/image-20230514185228333.png)

**例子**

```mysql
#当前日期、当前时间、系统日期和时间、世界标准日期、世界标准时间
select curdate(),curtime(),now(),utc_date,utc_time  from dual -- 2023-05-14  19:03:54 2023-05-14-19:03:54  ;
```

#### 获取日期和时间戳的转换

![image-20230515163455482](img/mysql/image-20230515163455482.png)

**列子**

```mysql
#当前日期、当前时间、系统日期和时间、世界标准日期、世界标准时间
select curdate(),curtime(),now(),utc_date,utc_time  from dual ;-- 2023-05-14  19:03:54 2023-05-14 19:03:54  ;

# Unix 时间（Unix time）是指从协调世界时 1970 年 1 月 1 日 0 时 0 分 0 秒（UTC，即协调世界时）
# 起经过的秒数，是一种时间表示方式。它也被称为 Epoch 时间（Epoch time）或 POSIX 时间（POSIX time）。
select  unix_timestamp(),unix_timestamp(curdate()),from_unixtime(unix_timestamp()) from dual; -- 1684151385 1684080000  2023-05-15 19:50:52
```

#### 获取月份，星期、星期数、天数

![image-20230515195400073](img/mysql/image-20230515195400073.png)

**例子**

```mysql
#获取年、月、日
select year(now()),month(now()),day(now()) from dual;
#获取时、分、秒
select hour(now()),minute(now()),second(now()) from dual;
#获取月份、返回星期几、返回周几
select  monthname(now()),dayname(now()),weekday(now())  from dual;
#返回季度、返回一年中过去了几周
select  quarter(now()),weekofyear(now())  from dual;
#返回日期在一年中的第几天、返回日期在所在月份的第几天、返回周几(7是星期天)
select dayofyear(now()),dayofmonth(now()),dayofweek(now())  from dual;
```

#### 时间函数计算

![image-20230515201716166](img/mysql/image-20230515201716166.png)

**例子**

```mysql
#时间相加，（秒）
select now(),addtime(now(),86400),subtime(now(),86400)  from dual;  --

#时间相加/相减,注意点
    #1：相加时间和相减时间皆不能超过60秒，等于59秒，否则返回null
    #2：如果想要时分秒都相加的，需要 'xx:xx:xx',相减也是如此
select now(),addtime(now(),59),subtime(now(),59)  from dual;
select now(),addtime(now(),'1:0:0'),addtime(now(),'0:1:0'),addtime(now(),'0:0:10') from dual;  -- 加一年，加一月，加一天，加一时，加一分，加一秒


#天数相减
select curdate(),DATEDIFF('2022-05-15',curdate())  from dual;

#返回时间相减后的时间间隔
select  curtime(),TIMEDIFF('20:36:48',curtime())  from dual;

#返回从0000年1月1日起，n天后的日期
select from_days(366) from dual;
```

#### 日期格式化

![image-20230515205358123](img/mysql/image-20230515205358123.png)

## MySQL小知识点

### myisam和innodb

MyISAM 和 InnoDB 是 MySQL 中的两种存储引擎，它们之间的主要区别如下：

1. 事务支持
   - InnoDB: 支持事务，提供 ACID 特性（原子性、一致性、隔离性、持久性），可以使用 COMMIT 和 ROLLBACK 控制事务。
   - MyISAM: 不支持事务，因此无法回滚或提交多条语句作为一个整体。
2. 外键支持
   - InnoDB: 支持外键约束，保证数据的参照完整性。
   - MyISAM: 不支持外键。
3. 锁机制
   - InnoDB: 使用行级锁（row-level locking），适合高并发的读写操作**myisam：表锁，innodb：行锁**。
   - MyISAM: 使用表级锁（table-level locking），在高并发写操作时容易导致锁争用。
4. 性能
   - InnoDB: 由于支持事务和行级锁，适合需要高并发和数据完整性的应用，但在某些场景下可能会略微影响性能。
   - MyISAM: 由于没有事务和外键支持，性能在简单查询或数据仓库场景中可能会更好。
5. 数据恢复
   - InnoDB: 提供崩溃恢复功能，自动恢复未完成的事务。
   - MyISAM: 不提供自动崩溃恢复，数据损坏后可能需要手动修复。
6. 全文索引
   - InnoDB: 从 MySQL 5.6 开始支持全文索引。
   - MyISAM: 原生支持全文索引，适合全文搜索场景。



### 查询插入

查询出一个结果，并插入到另一个表中

```sql
INSERT INTO quota_group ( group_name, unit, belonging_unit, belonging_system, belonging_category, quota_group_tag, type ) SELECT
group_name,
unit,
belonging_unit,
belonging_system,
belonging_category,
quota_group_tag,
type 
FROM
	(
	SELECT
		belonging_unit,
		belonging_system,
		belonging_category,
		group_name,
		unit,
		quota_group_tag,
		parameter_name_1,
		value_1,
		quota_parameter_key_tag_1,
		parameter_name_2,
		value_2,
		quota_parameter_key_tag_2,
		quota_number,
		quota_tag,
		category,
		item_name,
		item_unit,
		(
		sum( num * price ) / sum( num )) AS price,
		sum( num ) AS num,
		type,
		quota_item_tag 
	FROM
		quota_temp qt 
	GROUP BY
		qt.quota_tag,
		qt.quota_item_tag,
		qt.item_name,
		qt.item_unit 
	) source 
GROUP BY
	group_name,
	unit,
	belonging_unit,
	belonging_system,
	belonging_category,
	quota_group_tag;
```

### 分组增加条件

```sql
--  查看重复的  如果quota_group_tag＋qi.quota_item_tag重复COUNT(1)＋1
SELECT qg.quota_group_tag,qi.quota_item_tag,COUNT(1) from quota_item qi JOIN quota_group qg ON qg.id = qi.group_id JOIN quota_detail qd on qd.quota_item_id = qi.id WHERE qg.belonging_unit = '华宁公司' GROUP BY qg.quota_group_tag,qi.quota_item_tag HAVING COUNT(1) > 1
```

### 分组，重复项合并

```sql
SELECT
		belonging_unit,
		belonging_system,
		belonging_category,
		group_name,
		unit,
		quota_group_tag,
		parameter_name_1,
		value_1,
		quota_parameter_key_tag_1,
		parameter_name_2,
		value_2,
		quota_parameter_key_tag_2,
		quota_number,
		quota_tag,
		category,
		item_name,
		item_unit,
		(
        #  分组求平均价格  
		sum( num * price ) / sum( num )) AS price,
		sum( num ) AS num,
		type,
		quota_item_tag 
	FROM
		quota_temp qt 
	GROUP BY
		qt.quota_tag,
		qt.quota_item_tag,
		qt.item_name,
		qt.item_unit 
```

## 事务

### 隔离级别

当我们进行数据库操作时，有时需要保证数据的一致性和可靠性。MySQL事务的隔离级别就是为了解决多个并发事务之间可能出现的问题。

想象一下你正在和朋友玩一个多人游戏，每个人都在进行自己的操作。事务的隔离级别就是定义了每个人操作时的"可见度"和"影响力"，以确保游戏的公平性和数据的准确性。

MySQL定义了四种事务隔离级别，简单介绍如下：

1.  **读未提交（Read Uncommitted）：** 最宽松的级别。一个事务可以读取另一个事务尚未提交的数据。这可能会导致一些问题，例如读取到不完整或错误的数据。

2.  **读已提交（Read Committed）：** 这个级别要求一个事务只能读取已经提交的数据。这样可以避免读取到未提交的脏数据，但是在同一个事务内部，可能会遇到某个查询在不同时间返回不同结果的问题。

3.  **可重复读（Repeatable Read）：** 这个级别确保同一个事务内部的多个查询会返回一致的结果。即使其他事务在执行期间进行了数据更改，事务内部的查询结果也不会受到影响。

4.  **串行化（Serializable）：** 最严格的级别。它通过强制事务之间的串行执行来避免任何并发问题。这意味着每个事务必须按顺序执行，而不会相互干扰。这种级别可以解决所有并发问题，但可能会影响系统的性能。

## Case When

> 在 MySQL 中，`CASE` 表达式用于实现条件逻辑，从而在查询中返回不同的结果。它类似于编程语言中的 `if-else` 或 `switch-case` 结构。`CASE` 表达式非常灵活，可以在 `SELECT`、`INSERT`、`UPDATE` 和 `DELETE` 语句中使用。

- 列使用：`case when DQZT = '0' then '在籍' when DQZT = '1' then '未在籍' else '未知' end`

```sql
# 简单CASE When
CASE
    WHEN condition1 THEN result1
    WHEN condition2 THEN result2
    ...
    ELSE default_result
END

#  复杂CASE类似于switch 或者 if-else
CASE expression
    WHEN value1 THEN result1
    WHEN value2 THEN result2
    ...
    ELSE default_result
END

```

## With

> 公用表表达式（CTE）是一个命名的临时结果集，它在执行查询时仅存在。CTE通过`WITH`关键字引入，紧接着是CTE名称和作为CTE内容的子查询。
>
> **优点**：
>
> 1. **代码可读性**：使用CTE可以提高查询的可读性和可维护性，特别是当子查询非常复杂或在查询中多次使用时。
> 2. **结构化查询**：CTE允许你将查询分解成更小的部分，使得复杂查询更易于理解和管理。
> 3. **复用查询**：CTE可以在主查询中多次引用，避免重复代码。

```mysql
WITH a AS (
    SELECT *
    FROM system_user
    WHERE username LIKE '%22%'
)
SELECT *
FROM a;

```

## IF

### IF语句

> **`IF` 语句**: 用于存储过程和函数中的流程控制。

### IF函数

```mysql
WITH a AS (
    SELECT if(username > '22222',username,'****')
    FROM system_user
    WHERE username like '%22%'
)
SELECT *
FROM a;

# 上面效果等同于下面case语句
WITH a AS (
    SELECT (case length(username) > 0  when username > '2222222' then username else '****' end)
    FROM system_user
    WHERE username like '%22%'
)
SELECT *
FROM a;
```

