---
title: Redis
description: 快速带你入门Redis
# 默认url路径是title如果不写slug
slug: Redis
date: 2024-08-15 14:16:54+0000
toc: true
categories:
  - 学习笔记
tags:
  - Redis
---

## Redis

> 基于Redis 7.0.11学习，
> Redis（Remote Dictionary Server )，即远程字典服务，是一个开源的使用ANSI [C语言](https://baike.baidu.com/item/C语言?fromModule=lemma_inlink)编写、支持网络、可基于内存亦可持久化的日志型、Key-Value[数据库](https://baike.baidu.com/item/数据库/103728?fromModule=lemma_inlink)，并提供多种语言的API。

**多用于缓存，官网如下解释，因为所有数据都存放在内存中，访问很快**

> Redis 是一种开源（BSD 许可）内存**数据结构存储**，用作**数据库、缓存、消息代理和流引擎**。Redis 提供[数据结构，](https://redis.io/docs/data-types/)例如 [字符串](https://redis.io/docs/data-types/strings/)、[散列](https://redis.io/docs/data-types/hashes/)、[列表](https://redis.io/docs/data-types/lists/)、[集合](https://redis.io/docs/data-types/sets/)、带范围查询的排序[集合、](https://redis.io/docs/data-types/sorted-sets/)[位图](https://redis.io/docs/data-types/bitmaps/)、[hyperloglogs](https://redis.io/docs/data-types/hyperloglogs/)、[地理空间索引](https://redis.io/docs/data-types/geospatial/)和[流](https://redis.io/docs/data-types/streams/)。Redis 具有内置[复制](https://redis.io/topics/replication)、[Lua 脚本](https://redis.io/commands/eval)、[LRU 逐出](https://redis.io/docs/reference/eviction/)、[事务](https://redis.io/topics/transactions)和不同级别的[磁盘持久性](https://redis.io/topics/persistence)[，并通过Redis Sentinel](https://redis.io/topics/sentinel)和[Redis Cluster 的](https://redis.io/topics/cluster-tutorial)自动分区提供高可用性。

### 存储架构分析

**以前，如果数据存储量大、访问多。就是使用【缓存+MySQL+垂直拆分(读写分离)】**

![image-20230516173957952](img/redis/image-20230516173957952.png)

**现在，如果数据存储量大、访问多。就是使用【缓存＋分库分表+水平拆分(数据库集群[主-从]】**

![image-20230516174601262](img/redis/image-20230516174601262.png)

###  什么是NoSQL

> not only SQL不仅仅是SQL，泛指非关系型数据库

1. **关系型数据库：**
   1. 基于关系模型，使用表（表格）来组织和存储数据。
   2. 数据以结构化的方式存储，每个表都有预定义的列和数据类型。
   3. 使用 SQL（Structured Query Language）进行数据查询和操作。
   4. 支持事务处理，具备 ACID（原子性、一致性、隔离性和持久性）特性。
   5. 数据之间可以建立关系，通过外键来实现数据的关联。
   6. 典型的关系型数据库包括MySQL、Oracle、SQL Server等。
2. **非关系型数据库：**
    1. 不基于传统的关系模型，以键值对、文档、列族或图等形式存储数据。
    2. 数据以非结构化或半结构化的方式存储，不需要预定义的模式。
    3. 查询语言多样，有些使用类似SQL的查询语言，有些使用API进行数据操作。
    4. 可扩展性强，能够处理大规模数据和高并发访问。
    5. 对于某些应用场景（如分布式系统、大数据存储和实时数据处理等）具有更好的性能和灵活性。
    6. 典型的非关系型数据库包括MongoDB、Redis、Cassandra等。

在程序设计中有一句出名的话：**没有什么是加一层解决不了的**

### NoSQL的四大分类

1. **键值对存储**：Redis
2. **文档型数据库(bson格式和json差不多 只不过是二进制的)**：MongoDB
3. **列存储**：HBase
4. **图存储：** 适用与广告推荐，朋友圈社交网络

![image-20230516204330944](img/redis/image-20230516204330944.png)

### Redis能干嘛

1. 内存存储
    - rdb
    - aof
2. 效率高，可以用于缓存
3. 发布订阅系统
4. 地图信息分析

### 特性

1. 事务的控制
2. 持久化
3. 多样的数据类型
4. 集群

### redis线程问题

**命令处理模块还是单线程，只是网络模块(IO)是多线程的**

> 一般来说，一个 redis `请求`有两大模块，**网络模块 + 命令处理模块**。我们常说的 redis 单线程模型，其实主要就指的是一个正常请求涉及的**网络模块**和**命令处理模块**。
> 当执行一个特别慢的命令时，比如删除一个百万级的字典，可能会造成暂时的卡顿，导致 QPS 骤降；基于此，在 redis 4.0 出现专门处理这种 **Lazy Free** 模型的`后台线程`。
> 另外，正常情况下，redis 单线程模型中，网络模块往往成为瓶颈高发地；因此，redis 6.0 引入`多线程`模型，解决**网络模块**的问题。也就是说**命令处理模块还是单线程，只是网络模块是多线程的**



## Linux安装Redis

> 官网的网址：https://redis.io

**注意这里是从源开始安装，需要手动启动和安装**

1. 进入官网找到下载页面

2. 下载稳定版：注意下载页面两个版本需要向下翻，**点击http连接会先下载一个.gz包需要在Linux下解压**，一个Redis和Redis-stack：

    - Redis是一个开源的内存数据结构存储库，通常用作数据库、缓存和消息代理。它被广泛地使用在Web应用程序、移动应用程序和游戏等领域中，具有极高的性能和可扩展性。
    - Redis-stack则是一个基于Redis的应用程序堆栈，它为企业提供了一个综合的解决方案，包括Redis和其他必需的组件，如HAProxy、Sentinel等。Redis-stack旨在简化Redis的安装、配置和管理，并提供强大的监控、警报和灾难恢复功能。

   ![image-20230516215557546](img/redis/image-20230516215557546.png)

3. 把下载好的安装包放到Linux环境上可以使用xftp7，解压

4. 到解压后的目录

   ```shell
   # 我这里解压后的目录是redis-stable
   cd redis-stable
   
   # 下载相关的依赖
   make
   
   # 确认是否完整下载依赖
   make install     
   ```

5. 启动Redis

   ```shell
    # 移动到src目录下
    cd src
    
    # 加&表示在Linux系统中后端运行
    redis-server  &  //可以在配置文件设置，启动时带上配置文件redis-server redis.conf
    
    # 查询是否启动
    ps -aux | grep redis
   ```

    - 这里有个注意点可以使用`redis-server`启动，启动后 就一直是Redis的页面不能打命令了

      ![image-20230516220950622](img/redis/image-20230516220950622.png)

6. 使用Redis，`redis-cli  -h 127.0.0.1 -p 6379`，这里地配置可以在redis.conf 文件中查看，本地服务器可以不写-h，这里是为了演示就加上了

   ![image-20230516221721443](img/redis/image-20230516221721443.png)

7. 在Redis服务器内关闭 Redis

   ```shell
   # 关闭
   shutdown
   # 退出    
   quit
   ```

8. 在Redis服务器外关闭redis

   ```shell
    # 查询6379端口是被那个进程占用了，因为默认redis启动端口是6379 
    netstat  -anop | grep 6379
        
   # 杀死进程
   kill -9  xxx[上个命令查询地pid]
        
   # 或者
   redis-cli shutdown
   ```

## 测试性能

**在`/usr/Program-File/Redis/redis-stable/src`下的`redis-benchmark`就是**

### 性能测试工具可选参数

![image-20230516223329063](img/redis/image-20230516223329063.png)

### 示例

- **测试：1000个连接  1000000请求**：` redis-benchmark -c 1000 -n 1000000`

    - 测试讲解

      ![image-20230516224742019](img/redis/image-20230516224742019.png)

      ![image-20230516224902433](img/redis/image-20230516224902433.png)

## Redis数据类型

### 五大基本类型

1. **String**
2. **List**
3. **Set**
4. **Hash**
5. **Zset**

### 三种特殊数据类型

1. **geospatial：地理空间的**
2. **hyperloglog：估计一个集合中元素数量的数据结构**
3. **bitmaps：位图**

## Redis常用命令

### 数据库

#### 切换数据库

- ` SELECT 1[dbID]`：默认有16个

#### 查看数据库大小

- ` DBSIZE`

#### 清空当前数据库

- `FLUSHDB `

#### 清空所有数据库的数据

- `FLUSHALL `

###  类型

**设置成功返回1，设置失败返回0**

**其实redis存储的始终是key-value形式，value可以是set、list、map(hash)、string**

#### Keys 相关命令：

- KEYS pattern: 查找与指定模式匹配的所有键。    
    - keys * ：查看数据库所有的键    
- exists [keyName]：查看键是否存在    
- move [keyName] [DataBaseIndex] :移动键到指定的数据库不可使当前数据库    
- expire [keyName] [seconds]：指定某个键过期时间    
- ttl [keyName] ：查看你某个键的过期时间,**获取键的剩余生存时间**    
    - 该命令将返回以秒为单位的剩余生存时间,如果键存在且没有设置过期时间，TTL 命令将返回 -1。    
- ptll [keyName]:**以毫秒为单位获取键的剩余生存时间（PTTL）**    
- PERSIST key：移除键的过期时间，使其成为永久有效的键。    
- type [keyName] ：查看键类型    
- DEL key: 删除指定键。    

#### String 相关命令：

- SET key value: 设置指定键的值。重复设置就是替换    
- GET key: 获取指定键的值。list也可以用    
- DEL key: 删除指定键。    
- INCR key: 将指定键的值增加 1。    
    - incrby  [keyName]  [number] :增加指定的number    
- DECR key: 将指定键的值减少 1。    
    - decrBy[keyName]  [number] :减少指定的number    
- append [keyName]  [keyValue]：拼接某个键的value    
- strlen [keyName]：查看键value的长度    
- GETRANGE [keyName] [startIndex] [endIndex]：查看字符串指定的长度,endindex为-1就是查看整个字符串    
    - GETRANGE username -1 -1：获取最后一个字符    
- SETRANGE  [keyName] [offset] [value]:替换也可以是拼接，根据需要替换的字符串来替换，超过则拼接    
- SETEX [key] [seconds] [value]：设置键的过期时间，时间到了直接删除，expire设置过期时间不会删除    
- setnx [key] [value ]：键不存在则创建    
- mset key value key value ... ：批量设值键    
    - MSET user:1:name xxl user:1:age 13：字符串存储对象  [对象​：:id:：​属性]    
- mget key... :批量查看键值    
- msetnx key value key value ... ：批量设置键值对，如果设置失败，则全失败，是一个原子性操作    
    - MSETNX k4 v4 k4 v4：k4设置成功的后面都失败了    
- getset：先get再set，不存在则创建，存在则先取值再更新键的value    
-  HSETNX  [key] [field] [value]：key不存在则创建，field不存在则创建，value存在没有任何动作    

#### Hash 相关命令：

   **想象key是map变量名value是一个key-value形式，相关的命令一般是h开头**

- HSET key field value: 在指定哈希表中设置字段的值。**field就是java中的map集合的key，只不过redis在最外层有一个key名字了**    
- HGET key field: 获取指定哈希表中字段的值。    
- HDEL key field1 [field2 ...]: 删除指定哈希表中的一个或多个字段。    
-  HMSET [key] [field] [value] [field]  [value]...：设置多个key-value    
- hmget  [key] [filed]...：获取key的多个filed    
-  HGETALL [key]：获取key的所有field(key-value形式)    
-   HDEL [key] [field]...：删除key里面的field值    
-   HGETALL [key]：查看key有多少个field    
-    HEXISTS [key] [field]：查看key的field是否存在    
-    HKEYS  [key]：查看key的所有field不带value    
-    HVALS [key]：查看key所有field的value    
-   hlen [key]：查看key中有多少field    
-   HINCRBY  [key] [field] [number]：key的field的value增加number，number可以是负数，并且必须要指定跟String类型有区别的，并且filed的value是integer类型才可以    

#### List 相关命令：

   **所有list相关的命令，基本带一个l，相当于链表，可以做队列，栈**

- LPUSH key value1 [value2 ...]: 将一个或多个值推入列表的左侧。    
- RPUSH key value1 [value2 ...]: 将一个或多个值推入列表的右侧。    
- LPOP key [count]: 移出并获取列表的最左边元素。默认count为1    
- RPOP key [count]: 移出并获取列表的最右边元素。    
- LRANGE [keyName]  [startIndex] [endIndex] : 展示list中的元素    
    - LRANGE myList 0 -1：注意使用lpush存发元素获取时从list尾部开始(**栈：先进后出**)，rpush存放的元素，展示时则是从头开始(**队：先进先出**)，如果一个列表的是两种方式混合加入的，就按照最后一次加入的方式来查询    
- lindex [key] [index]：查看集合特定下标的的位置    
- LLEN [key]：查看集合的长度    
- lrem [key] [count] [element]：移除集合特定的值，可以指定数量(用在元素重复的场景)    
-  LTRIM [key] [startIndex] [endIndex]：裁剪list，注意原list是改变的    
-  RPOPLPUSH [key1] [key2]：把key1右边的元素pop出来，放在key2，key1必须存在，key2无所谓    
- lset  [key] [index] [element]：(更新集合)设置list特定下标的元素，key不能为空，下标必须存在，就是设置不能超过集合大小    
-  LINSERT [key]  before|after element1 element2：更新集合，key要存在，element1 要存在element2才会插入成功    
- LINSERT list1 before xxl hello：在list集合中的xxl元素前面插入hello元素    

#### Set 相关命令：

   **set命令开头一般是s，注意元素无序，不重复**

- SADD key member1 [member2 ...]: 向集合中添加一个或多个成员。    
- SMEMBERS key: 返回集合中的所有成员。    
- SREM key member1 [member2 ...]: 从集合中移除一个或多个成员。    
- sismeber [key] [number]：查看特定的值是否存在集合中    
- SCARD [key]：查看set集合中有多少元素个数，必须set集合    
- SREM [key] [number...]：移除集合中的元素，不是原子型操作，前面没移除，后面继续    
-  SRANDMEMBER [key] [number]：查看指定数量的元素，元素返回是随机的，可以做随机的游戏    
- SPOP [key] [count]：随机弹出某个集合的元素，不写count默认是1    
- SMOVE  [key1] [key2] [element]：把key1的元素element移动到key2    
- SDIFF  [set...]：查看多个set的差集(返回其他集合中不存在的元素，第一个set为参照)，注意返回的是第一个set集合中的元素    

   ```redis
   SADD set1 a b c
   SADD set2 e d f    
   SDIFF set1 set2  //返回 a b c
   SDIFF set2 set1  //返回e d f  
     ``` 

- SINTER [set...]：查看多个集合的交集(返回集合中都有的元素)
- SUNION [set...]：查看多个集合的并集(返回所有的集合的元素，重复的只保留一份)

#### ZSet 相关命令：

   **有序不重复集合，命令一般带个Z**

- ZADD key score1 member1 [score2 member2 ...]: 向有序集合中添加一个或多个成员。**score1是一个标志到时候排序就会根据这个来**
- ZRANGE key start stop [WITHSCORES]: 获取有序集合中指定范围的成员，**返回的结果会根据排序从小到大来**
- ZRANGE mset1 0 -1获取所有元素，**大部分的range都可以是0 -1就可以获取所有元素**
- ZREM key member1 [member2 ...]: 从有序集合中移除一个或多个成员。
-  ZRANGEBYSCORE [zset] [start] [end]：通过排序查看指定zset
-  ZRANGEBYSCORE zset1 -inf +inf(**获取zset的正无穷到负无穷的范围的元素，按score1从小到大排序 **)
- ZRANGEBYSCORE zset1 -inf +inf  withscores**获取zset的正无穷到负无穷的范围的元素，按score1从小到大排序 ，返回结果是带着score**
- ZREVRANGE  [zset] [start]  [end]：返回倒序排的结果
-   ZREVRANGE zset1 0 -1 withscores返回zset1所有元素按着倒序排(**从大到小排序**），会展示标识符(score)
-  ZCARD [zset]：获取有序集合中元素的个数
-  ZRANGE  [zset] [minScore] [maxScore]：查看zset中的minScore标识符和maxScore标识符之间有多少元素，返回个数注意可以等于minScore和maxScore**[minScore,maxScore]区间**

#### Pub/Sub 相关命令：

- PUBLISH channel message: 将消息发布到指定的频道。
- SUBSCRIBE channel1 [channel2 ...]: 订阅一个或多个频道的消息。

#### bitmaps 相关命令：

   **这个key的value像list<Map<offset,value>>集合**

- `SETBIT key offset value`: 设置指定key中指定偏移量上的位的值。`offset`表示偏移量，`value`表示位的值（0或1）。
- `GETBIT key offset`: 获取指定key中指定偏移量上的位的值。返回值为0或1。
- `BITCOUNT key [start end]`: 统计指定key中指定范围内（默认整个字符串）的位为1的个数，**如果是key是bit类型的就计算么个offset位置为1的数量**。
- `BITOP operation destkey key [key ...]`: 对一个或多个key进行位运算，并将结果保存到`destkey`中。支持的位运算操作有：AND（与）、OR（或）、XOR（异或）、NOT（非）。
- `BITFIELD key [GET type offset] [SET type offset value] [INCRBY type offset increment]`: 对指定key中的位进行多种操作。支持的位操作类型有：u（无符号整数）、i（有符号整数）、f（浮点数）。可用于获取位的值、设置位的值、增加位的值。

#### 事务相关命令：

- MULTI: 标记一个事务块的开始。
- EXEC: 执行所有事务块内的命令。
- DISCARD: 取消事务，放弃执行所有事务块内的命令。

## 事务

**事务本质：一组操作有序的执行,要么都成功，要么都失败**

### ACID

- **原子性，一致性、隔离性、持久性**

- **线程安全的三大条件：原子性，有序性，可见性**

###  Redis事务

- **Redis是单线程执行命令能保证原子性，但是事务不保证原子性，同时Redis事务没有隔离级别的概念**
- Redis的事务流程：
    1. **开启事务：multi**
    2. **命令入队**
    3. **执行事务：exec**
- **只有第三步被执行了才会执行命令，如果命令队列中有命令出错还是会继续执行(详细看下面)，不保证原子性，一次事务结束就结束了**
- **取消事务**
    1. **取消事务：DISCARD，就是命令队列不会被执行**

#### 命令错误/检查异常

- **java中代码写错了会触发检查异常，这里对应redis命令写错,同时Redis在事务中命令写错也会报错，执行事务失败**

#### 命令错误/非检查错误

- **java中代码出现 1/0 会触发非检查异常，这里对应redis命令用错,同时Redis在事务中命令没写错但是用错了，执行事务成功**

####  java项目中Redis事务

**事务执行失败**

```java
@Bean
public   Jedis redis() {
    Jedis jedis = new Jedis("47.94.211.12",6379);
    jedis.auth("root123456");
    jedis.flushDB();
    Transaction multi = jedis.multi();
    
    multi.set("username","xxl");
    //会报错因为事务中必须使用multi操作redis，整个过程必须在没在discard或者exec都有效
    //最终执行事务失败
    jedis.set("username","xxl");
    multi.exec();
    //关闭连接
    jedis.close();
    return jedis;
}
```

**正确使用方式1：**

```java
@Bean    
public   Jedis redis() {    
    Jedis jedis = new Jedis("47.94.211.12",6379);    
    jedis.auth("root123456");    

    jedis.flushDB();    

    Transaction multi = jedis.multi();    
    try {    
        multi.set("username","xxl");    
        //以下事务执行失败    
        int i = 1 / 0;    
        multi.exec();    
    } catch (Exception e) {    
        //放弃事务    
        multi.discard();    
    }finally {    
        System.out.println(jedis.get("username"));    
    }    
    //关闭连接    
    jedis.close();    
    return jedis;    
}    
```

**正确使用方式2：**

```java
@Bean
public   Jedis redis() {    
    Jedis jedis = new Jedis("47.94.211.12",6379);    
    jedis.auth("root123456");    

    //解锁    
    jedis.unwatch();    
    //获取锁    
    jedis.watch("user");    
    Transaction multi = jedis.multi();    
    try {    
        //Thread.sleep(5000);    
        multi.lset("user",0,"18");    
        /*    
            以下会出错因为multi没有执行exec命令不可以获取结果，multi只是缓存一组命令    
            Response<List<String>> user = multi.lrange("user", 0, -1);    
            user.get();    
        */    
        multi.get("user");    
        /*    
            以下集合是保存命令是否执行成功的结果集，Ok    
            List<Object> exec = multi.exec();    
        */    
        List<Object> exec = multi.exec();    
        exec.forEach(System.out::println);    
    } catch (Exception e) {    
        System.out.println(e);    
        System.out.println("事务出问题");    
        //放弃事务    
        multi.discard();    
    }finally {    
          List<String> list = jedis.lrange("user", 0, -1);//  
          list.forEach(System.out::println);//  
    }    
    //关闭连接    
    jedis.close();    
    return jedis;    
}    
```

### 乐观锁

```java
@Bean
public   Jedis redis() {    
    Jedis jedis = new Jedis("47.94.211.12",6379);    
    jedis.auth("root123456");    

    //解锁    
    jedis.unwatch();    
    //获取锁    
    jedis.watch("user");    
    Transaction multi = jedis.multi();    
    try {    
        Thread.sleep(5000);    
        multi.lset("user",0,"18");    
        //如果其他线程更新user键，这里就会失败，并且结果集为空    
        List<Object> exec = multi.exec();    
        if (ObjectUtil.isNotNull(exec)) {    
            exec.forEach(System.out::println);    
        }    
    } catch (Exception e) {    
        System.out.println(e);    
        System.out.println("事务出问题");    
        //放弃事务    
        multi.discard();    
    }    
    //关闭连接    
    jedis.close();    
    return jedis;    
}    
```

### redisTemplate事务

**最接近redis本来的事务的模样**

```java
@Bean
public  void sentinel(){      
    Object execute = redisTemplate.execute(new SessionCallback<>() {      
        //想实现回滚，不仅代码层次错误实现      
        @Override      
        public <K, V> Object execute(RedisOperations<K, V> operations) throws DataAccessException {      
            List<Object> exec = null;      
            try {      
                operations.multi();      
                operations.opsForHash().put((K) "map1","map2","xxl1");      
                //operations.opsForValue().get("map1");    事务成功      
                //System.out.println(1/0);  //事务失败      
            } catch (Exception e) {      
                operations.discard();  //discard和exec只能执行一次，不管那个执行都会关闭当前事务连接      
            }finally {      
                exec = operations.exec();      
            }      
            return exec;      
        }      
    });      
  
    System.out.println(execute);      
}      
  ```

## Redis锁

### 悲观锁

- **很悲观，认为什么时候都会出问题，无论做什么都会加锁**

## 乐观锁

- **很乐观，认为什么时候都会出问题，无论做什么都不会加锁！更新数据的时候去判断一下，在此期间是否有人修改过这个数据(加个version判断，流程如下：先获取version ---> 比较version )**
- **CAS（Compare-And-Swap）**

### Redis监视

- 命令：
    1. **watch [key...]：监视某个键**
    2. **unwatch :解除监视，先解除监视再watch获取最新的值**

- **watch命令不可用在事务中!A线程监视了某个键并开启了事务修改此键但是没有提交事务，此时B线程修改了此键，A线程再提交事务就会返回nil，也就是事务修改失败**

- **watch命令相当于乐观锁**

## 集成Redis

### IDEA连接

**远程连接需要在redis.conf配置密码否则报错，以后命令行登录为`redis-cli -h localhost -p 6379 -a root123456`**

### 测试连接

```java
@Bean
public   Jedis redis() {    
    Jedis jedis = new Jedis("47.94.211.12",6379);    
    jedis.auth("root123456");    
    System.out.println(jedis.get("username"));    
    System.out.println(jedis.ping());    
    return jedis;    
}    

//xxl
//pong
```

### SpringBoot集成redis

**yml配置**

```yml
spring:
  data:
    redis:
      host: 47.94.211.12
      port: 6379
      password: root123456
      database: 0
      client-type: lettuce
      jedis:
        pool:
          enabled: true
```

**导入依赖**

```xml
<!-- spring boot集成redis依赖 为什么不用jedis，因为是直连线程可能不安全BIO，
        而lettuce是同netty，异步调用线程安全NIO -->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-data-redis</artifactId>
        </dependency>
```

**测试**

```java
@Resource    
RedisTemplate<Object,Object> redisTemplate;    
@Bean    
public void test(){    
    //常用的命令直接使用，不同类型的键值对通过opsForxxx来操作    
    redisTemplate.opsForList();  //list    
    redisTemplate.opsForSet(); //Set    
    redisTemplate.opsForValue();  //String    
    System.out.println("hello,world");    
    //这里取不到值是因为不是当前的对象存储的    
    Object o = redisTemplate.opsForValue().get("username");    
    System.out.println(o);    
    redisTemplate.opsForValue().set("username","wyx");    
    System.out.println(redisTemplate.opsForValue().get("username"));    
    //获取连接对象    
    RedisConnection connection = redisTemplate.getConnectionFactory().getConnection();    
    //清空resis数据库    
    connection.serverCommands().flushDb();    
}    
```

### Redis在java相关的API

```java
@Bean
public   Jedis redis() {    
    Jedis jedis = new Jedis("47.94.211.12",6379);    
    jedis.auth("root123456");    
    //==============string==================    
    System.out.println("==============string==================");    
    String s = jedis.get("username");    
    System.out.println(s);    
    System.out.println("==============list==================");    
    List<String> list = jedis.lrange("list", 0, -1);    
    list.forEach(System.out::println);    
    System.out.println("==============set==================");    
    Set<String> set = jedis.smembers("set");    
    set.forEach(System.out::println);    
    System.out.println("==============hash(map)==================");    
    Map<String, String> hash = jedis.hgetAll("hash");    
    hash.entrySet().forEach(System.out::println);    
    System.out.println("==============zset==================");    
    List<String> zset = jedis.zrange("zset", 0, -1);    
    zset.forEach(System.out::println);    
    jedis.close();    
    return jedis;    
}    
```

![image-20230627231950765](img/redis/image-20230627231950765.png)

## 序列化问题

- 存储在redis的对象需要实现序列化或者**使用json存储**,否则报错

**redis序列化通用设置**

```java
/**
 * redis序列化
 *
 * @author xxl
 * @since 2023/7/2
 */
@Configuration
public class RedisConfig {
    /**
     * 序列化相关的配置
     */
    @Bean("myRedisTemplate")
    public RedisTemplate<String, Object> redisTemplate(RedisConnectionFactory  factory) {
        RedisTemplate<String, Object> redisTemplate  = new RedisTemplate<>();

        //json方式序列化
        Jackson2JsonRedisSerializer jackson = new Jackson2JsonRedisSerializer<>(Object.class);
        redisTemplate.setConnectionFactory(factory);
        //String方式序列化
        StringRedisSerializer stringRedisSerializer = new StringRedisSerializer();

        //配置序列化的方式不用设置
        /*redisTemplate.setDefaultSerializer();
        redisTemplate.setStringSerializer();
        redisTemplate.setEnableDefaultSerializer();*/

        //设置所有的key为string方式序列化
        redisTemplate.setKeySerializer(stringRedisSerializer);
        redisTemplate.setHashKeySerializer(stringRedisSerializer);
        //设置所有的value为jackson方式序列化
        redisTemplate.setValueSerializer(jackson);
        redisTemplate.setHashValueSerializer(jackson);

        redisTemplate.afterPropertiesSet();
        return redisTemplate;
    }

}
```

## 持久化

### AOF和RDB的区别

Redis中有两种持久化方式：**AOF（Append-Only File）**和**RDB（Redis Database Backup）**。它们解决了不同的问题，下面我会分别介绍它们以及它们的一些问题。

**AOF持久化：** AOF持久化是通过将**每个写操作追加到一个日志文件中来实现的。**Redis在启动时会重新执行这些写操作以还原数据。AOF持久化的优点包括：

1. 数据完整性：AOF日志包含了重放所有写操作的指令，因此可以保证数据的完整性。
2. 可读性：AOF日志是以文本形式记录的，易于阅读和理解。

然而，使用AOF持久化也可能面临以下问题：

1. 文件大小增长：随着写操作的增加，AOF日志文件的大小也会逐渐增长。较大的AOF文件可能会导致磁盘空间占用过多。
2. 恢复时间：在启动时重新执行AOF日志中的所有写操作，可能需要较长的时间来还原数据。

**RDB持久化：** RDB持久化是通过**将Redis在某个时间点的数据快照保存到磁盘上的二进制文件中来实现的**。RDB持久化的优点包括：

1. 快速恢复：RDB文件是一个快照，可以快速加载到内存中恢复数据。
2. 小文件大小：相对于AOF日志，RDB文件通常较小，占用较少的磁盘空间。

然而，使用RDB持久化也可能面临以下问题：

1. 数据丢失风险：由于RDB持久化是定期进行的，如果Redis意外崩溃，最近的更改可能无法保存到RDB文件中，导致数据丢失。

为了解决AOF和RDB各自的问题，你也可以将它们同时使用。这种配置称为"AOF和RDB混合持久化"。在这种情况下，你可以通过AOF来保证数据的完整性和持久化，同时使用RDB来实现快速的恢复。

### RDB(redis database)

- 使用快照机制，**快照是数据存储的某一时刻的状态记录；备份则是数据存储的某一个时刻的副本。这是两种完全不同的概念。**
- **RDB保存的文件叫做dump.rdb，可以在Redis配置文件看见redis启动之初会读取**
- **默认开启**

#### RDB的过程

![image-20230704224535749](img/redis/image-20230704224535749.png)

#### 如何自动恢复rdb文件中所记录的数据

- `CONFIG get dir`查看有效目录

  ```text
  1) "dir"
  2) "/home/redis7.0/redis-stable"  .rbd文件放这俩个目录下就行，redis自动检查并恢复
  ```

#### 优点和缺点

1. 优点：
    - 快速恢复
    - 文件占用较小
2. 缺点
    - 数据丢失风险(如果最后一次修改宕机，就可能没有记录这个数据)
    - 需要一定的时间间隔保存
    - 保存命令时会fork一个子线程会阻塞主线程

### AOF(AppendOnly File)

- **以日志的形式记录每一个写操作，读不记录，只允许追加不可以改写，redis启动之初会读取，恢复数据的时候重新执行所有的保存命令**
- **AOF保存的文件叫做appendonly.aof文件,可以在Redis配置文件看见**
- **默认不开启，需要在配置文件设置**

#### 1图解

![image-20230704232705997](img/redis/image-20230704232705997.png)

#### 如何自动恢复aof文件中所记录的数据

**新的日志文件放在appendonlydir目录下**

![image-20230704235406927](img/redis/image-20230704235406927.png)

#### 优点和缺点

1. 优点
    - 数据完整性，最多只丢一次的写的命令
    - aof可读性
    - redis提供修复恶意破坏aof日志文件的工具
2. 缺点
    - 文件占用较大
    - 数据恢复较慢

### AOF文件安全

- **如果修改了日志文件就会，启动失败！！此时可以借用redis自带的修复aof文件的工具`redis-check-aof  --fix appendonlydir/appendonly.aof.1.incr.aof`-这个修复不是保证所有的数据都被修复，可能修复未破坏的数据**

- **不能随意删除aof文件，否则启动会失败，此时需要设置配置文件**

## Redis发布订阅

- **图解：两个重要的角色，一个最重要的容器**
    1. **消息发布者**
    2. **消息订阅者：等待发布者的信息推送过来，而不是自己获取**
    3. **存放消息的容器**

   ![image-20230705215102114](img/redis/image-20230705215102114.png)

### 相关的命令

![image-20230705215632785](img/redis/image-20230705215632785.png)

1. PSUBSCRIBE [channelName... ] message：发布到某个频道某个信息
2. subscribe [channelName..]：订阅频道
3. UNSUBSCRIBE  [channelName..]：取消订阅
4. PUBSUB CHANNELS [channelName ..]：查看某个订阅的状态
5. PUBSUB NUMSUB [channelName [channelName ...]]：查看订阅者数量
6. PUBSUB NUMPAT：这条命令用于获取当前被订阅模式的数量

### 订阅模式

```text
在Redis的发布订阅模型中，有两种类型的订阅模式：普通订阅和模式订阅。

普通订阅（Normal Subscription）：
普通订阅是指通过订阅具体的频道（channel）来接收消息。订阅者使用SUBSCRIBE命令指定一个或多个频道，并在这些频道上接收发布者发送的消息。

模式订阅（Pattern Subscription）：
模式订阅是一种更灵活的订阅方式，允许订阅者通过使用模式（pattern）来匹配多个频道。模式使用通配符来匹配频道名，可以使用*匹配一个或多个字符，?匹配单个字符，[]匹配指定范围内的字符。订阅者使用PSUBSCRIBE命令指定一个或多个模式，并在匹配的频道上接收消息。

例如，使用SUBSCRIBE news可以订阅名为"news"的频道，而使用PSUBSCRIBE sports:*可以订阅以"sports:"开头的所有频道，如"sports:football"、"sports:basketball"等。

需要注意的是，普通订阅和模式订阅可以同时使用，订阅者可以同时接收指定频道和匹配模式的消息。

这些订阅模式使得Redis的发布订阅模型更加灵活和可扩展，能够满足不同场景下的消息传递需求。
```

### 发布、订阅

1. **发布：在没有订阅者的时候发布的信息，被后来的订阅者订阅的时候，这个信息是不会被订阅者看到的**

   ```redis
   localhost:6379> PUBLISH java  "hello,world"
   (integer) 0
   localhost:6379> PUBLISH java  "hello,world"
   (integer) 1
   localhost:6379> PUBLISH java  "hello,world
   ```

2. **订阅的时候不能退出，这个订阅的过程**

   ```redis
   localhost:6379> PSUBSCRIBE java
   Reading messages... (press Ctrl-C to quit)
   1) "psubscribe"
   2) "java"
   3) (integer) 1
   1) "pmessage"
   2) "java"
   3) "java"
   4) "hello,world"
   ^C(194.28s)
   localhost:6379> PSUBSCRIBE java
   Reading messages... (press Ctrl-C to quit)
   1) "psubscribe"
   2) "java"
   3) (integer) 1
   ```

## 主从复制

**主从：简单理解为一个主人多个奴仆，就是为了分担主机的压力，以及数据过大时主机的读写速度过慢问题，还有一点读写分离**

### 主从复制概念

- **就是将一台Redis服务器的数据库复制到到其他的Redis服务器，前者是主节点，其余的是从节点**

- **数据的复制是单向的，只能有主节点到从节点，并且复制之后数据在从机也有一份**

- **最低的集群：1主3从(单台redis最大使用的内存不应该超过20G）,默认所有redis服务都是主节点，从节点需要修改配置文件，且从节点只能有一个主节点 ,以及没有配置之前每一个redis服务都是主节点**

- **从节点默认是只读，如需要修改就在配置文件中设置**

  ![G](img/redis/image-20230707143254188.png)

1. 缺点：
    - 数据冗余，多了备份
    - 浪费资源
2. 优点：
    - 查询速度快(单个redis缓存过多数据时，其中的查询速度会变慢)
    - 故障恢复(一个redis数据多了可能会宕机)
    - 负载均衡

### 环境配置

**查看配置信息`info replication`**

```redis
info replication
# Replication
role:master
connected_slaves:0
master_failover_state:no-failover
master_replid:d34fa2697a184e428dc7accd7f47a4e0c45a65e6
master_replid2:0000000000000000000000000000000000000000
master_repl_offset:0
second_repl_offset:-1
repl_backlog_active:0
repl_backlog_size:1048576
repl_backlog_first_byte_offset:0
repl_backlog_histlen:0
```

### demo(一主二从)：命令配置

**命令修改都是暂时性的**

1. **第一步需要配置三个服务的配置文件，三个端口6379，6380，6381，修改配置文件：**
    - 修改日志文件：**logfile "redis-6379.log"**
    - 修改端口：**port 6379**
    - 修改rdb文件名字：**dbfilename dump-6379.rdb**
    - 修改为守护进程：**daemonize yes**
    - 修改pid文件名字：**pidfile /var/run/redis_6380.pid**

2. **第二步：启动服务，配置从机认主人**

    - 6380、6381向6379认主人：**SLAVEOF 127.0.0.1  6379,结束之后使用info replication**

      ```text
      role:slave   //从机身份
      master_host:localhost   //主机地址
      master_port:6379   //主机端口
      master_link_status:down       //主机状态  
      master_last_io_seconds_ago:-1
      master_sync_in_progress:0
      slave_read_repl_offset:0
      slave_repl_offset:0
      master_link_down_since_seconds:-1
      slave_priority:100
      slave_read_only:1
      replica_announced:1
      connected_slaves:0
      master_failover_state:no-failover
      master_replid:d118a794da86cf9f4c326d8123f03cfe358b5e2e
      master_replid2:0000000000000000000000000000000000000000
      master_repl_offset:0
      second_repl_offset:-1
      repl_backlog_active:0
      repl_backlog_size:1048576
      repl_backlog_first_byte_offset:0
      repl_backlog_histlen:0
          
          
      查看主机信息
      role:master
      connected_slaves:2   //从机数量
      slave0:ip=127.0.0.1,port=6380,state=online,offset=70,lag=1  //从机详细信息
      slave1:ip=127.0.0.1,port=6381,state=online,offset=70,lag=0
      master_failover_state:no-failover
      master_replid:f69f40190f658a209991ef5c3a539f8b74b04bc3
      master_replid2:0000000000000000000000000000000000000000
      master_repl_offset:70
      second_repl_offset:-1
      repl_backlog_active:1
      repl_backlog_size:1048576
      repl_backlog_first_byte_offset:1
      repl_backlog_histlen:70 
          
      ```

#### demo(一主二从)：配置文件配置

1. **第一步：(6379是主机，6380，6381是从机)**

    - 修改从机配置文件：

      ```text
      #  从机连接主机的地址
      # replicaof <masterip> <masterport>
      # 如果主机有密码就配上
      # masterauth  root123456 
      ```

2. **第二步：启动服务，使用`info replcaition`查看信息**

### 级联复制

- **以下的salve1既是主机又是从机，但是依旧不能写，只能读**

  ```java
  主机   <---   从机(salve1)   <--- 从机(salve2)
  ```

##  哨兵模式

- **以上传统的主从复制，有两个问题(解决方案是手动命令配置)：**

    1. **主机宕机之后，从机不知道，可能会导致数据数据丢失，查询不到，修复则需要费时费力，还会造成一段时间内服务不能用**
    2. **从机宕机之后，主机是知道的，此时如果主机有写操作，从机在启动之后，会去同步主机数据！！同时得出结论只要是从机都能拿到主机信息**

  ![image-20230707163619215](img/redis/image-20230707163619215.png)

- 以上中主机出问题时最麻烦的，此时就可以用哨兵模式(**自动选举主机**)

### 哨兵模式概念

Redis Sentinel（哨兵）模式是Redis提供的一种高可用性解决方案，用于监控和管理Redis主从复制环境中的故障转移和自动故障恢复。下面是Redis Sentinel模式的详细解释过程，包括每个步骤中Redis的行为和使用的组件：

1. **哨兵节点配置**：**首先，您需要配置一组哨兵节点。每个哨兵节点是一个独立的进程**，它们负责监控和管理Redis主从复制环境。配置中指定了哨兵节点的IP地址和端口号。

2. **哨兵选举**：当哨兵节点启动时，它们会通过向其他哨兵节点发送消息来进行选举，以确定哪个哨兵节点将成为领导者（Leader）。选举过程中，哨兵节点会互相交换信息，并根据事先定义的规则进行选举。

3. **主节点监控**：哨兵进程会周期给所有的主库、从库发送 PING 命令，检测机器是否处于服务状态。如果没有在设置时间内收到回复，则判定为下线。哨兵节点监控到主节点超时未响应，主节点不一定是真的宕机。可能是之间的网络拥堵，或者主库自身压力过大，导致响应超时，**此时引入哨兵集群，多个哨兵实例一起判断，降低误判率。判断标准就是，假如 n 个哨兵实例，至少有 n/2+1 个判定一致，才可以定论。**

   ![image-20230707170835820](img/redis/image-20230707170835820.png)

4. **故障检测和故障转移**：当领导者哨兵节点检测到主节点失效时，它会通知其他哨兵节点，并开始进行故障转移过程。在故障转移期间，哨兵节点会尝试选举一个新的主节点。

5. **选举新的主节点**：哨兵节点根据一定的算法选择一个从节点作为新的主节点。选举的依据通常是判断从节点的优先级（replica priority）和复制偏移量（replica offset）等。

6. **重新配置从节点**：一旦新的主节点选举出来，哨兵节点会将其他从节点重新配置为复制新的主节点。从节点会重新连接到新的主节点，并开始进行数据同步。

7. **客户端重定向**：在故障转移过程中，哨兵节点会向客户端发送重定向命令，指示客户端连接到新的主节点。客户端接收到重定向命令后，会更新连接信息，并重新连接到新的主节点。

![image-20230707170415840](img/redis/image-20230707170415840.png)

### 配置哨兵

1. **查看哨兵配置文件`vim sentinel.conf`**

   ```text
   # 命令格式：
   sentinel monitor mymaster 127.0.0.1 6379 2      
       
   sentinel：表示这是一个哨兵配置项。
   monitor：指定了监视的操作，意味着哨兵节点将监视指定的Redis主节点。
   mymaster：是被监视的主节点的名字，您可以自定义这个名字。
   127.0.0.1：表示被监视的主节点的IP地址，这里是本地主机（localhost）的IP地址。您需要将其替换为实际的主节点的IP地址。
   6379：表示被监视的主节点的端口号，这里是默认的Redis端口号。您需要将其替换为实际的主节点的端口号。
   2：表示在主节点失效之前，至少需要有2个哨兵节点达成一致才能进行故障转移。这个数字是可以根据实际需求进行调整的。    
   
   通过这行配置，哨兵节点会监视指定的Redis主节点（通过IP地址和端口号），并在主节点失效时进行故障转移。哨兵节点之间通过交换信息来达成共识，并根据配置中指定的最小数量（2个）来决定是否进行故障转移。
   
   这只是哨兵配置文件中的一行配置，通常配置文件中会有更多的哨兵节点和监视的主节点。哨兵节点之间会形成一个多数派集群，通过交互和协作来监控主节点的状态，并进行故障转移和自动故障恢复，以保证Redis的高可用性。    
   ```

2. 如果主服务器有密码哨兵也需要设置`sentinel auth-pass mymaster root123456`

3. **启动哨兵模式**

    - `redis-sentinel  sentinel.conf  &`，默认是在26379接口
    - **下图是监控主机出问题之后被选举成功的主机，但是用info命令查看也许跟实际对不上但是被选举的主机更新其他的从机也一起更新，即使命令没有展示它属下的从机信息，但是只要从机的主机是谁就会跟着谁**

   ![image-20230707192402733](img/redis/image-20230707192402733.png)

**相关配置**

| 配置项                                      | 参数类型                   | 说明                                                         |
| ------------------------------------------- | -------------------------- | ------------------------------------------------------------ |
| dir                                         | 文件目录                   | 哨兵进程服务的文件存放目录，默认为 /tmp。                    |
| port                                        | 端口号                     | 启动哨兵的进程端口号，默认为 26379。                         |
| sentinel down-after-milliseconds            | <服务名称><毫秒数(整数)>   | 在指定的毫秒数内，若主节点没有应答哨兵的 PING 命令，此时哨兵认为服务器主观下线，默认时间为 30 秒。 |
| sentinel parallel-syncs                     | <服务名称><服务器数(整数)> | 指定可以有多少个 Redis 服务同步新的主机，一般而言，这个数字越小同步时间越长，而越大，则对网络资源要求就越高。 |
| sentinel failover-timeout                   | <服务名称><毫秒数(整数)>   | 指定故障转移允许的毫秒数，若超过这个时间，就认为故障转移执行失败，默认为 3 分钟。 |
| sentinel notification-script                | <服务名称><脚本路径>       | 脚本通知，配置当某一事件发生时所需要执行的脚本，可以通过脚本来通知管理员，例如当系统运行不正常时发邮件通知相关人员。 |
| sentinel auth-pass <master-name> <password> | <服务器名称><密码>         | 若主服务器设置了密码，则哨兵必须也配置密码，否则哨兵无法对主从服务器进行监控。该密码与主服务器密码相同。 |

### 哨兵集群

**像搭建redis集群一样修改配置文件?肯定是启动多个服务!!!**

### 启动哨兵相关的知识

#### 主机宕机，哨兵选出主机，以前的主机在启动还是主机吗？

- **不是，重启之后也不是，并且哨兵重启之后也还是监控选举出的主机(因为配置文件在选举的主机出来之后就自己修改了自己的配置文件)**

### 优缺点

#### 优点

1. 出问题不用手动出切换主机
2. 故障转移，系统的可用性更好

#### 缺点

1. 占用资源大
2. redis不好在线空扩容
3. 哨兵模式配置十分麻烦，而且哨兵集群配置更麻烦

### 识别主机

- **切换了主机之后会修改哨兵配置文件，以及新的主机的配置和旧主机的配置，注意哨兵配置文件最底下的信息，那里面记录了**

### 哨兵模式常用的命令

1. `SENTINEL masters`：获取当前监控的所有主节点的信息，包括名称、IP地址、端口、状态等。
2. `SENTINEL master <master-name>`：获取特定主节点的信息，例如主节点名称、IP地址、端口、当前状态等。
3. `SENTINEL slaves <master-name>`：获取特定主节点的所有从节点信息，包括从节点的名称、IP地址、端口、状态等。
4. `SENTINEL get-master-addr-by-name <master-name>`：获取特定主节点的IP地址和端口。
5. `SENTINEL is-master-down-by-addr <ip> <port>`：检查指定主节点是否处于下线状态。
6. `SENTINEL failover <master-name>`：手动触发指定主节点的故障转移。
7. `SENTINEL ckquorum <master-name>`：检查指定主节点的哨兵选举是否足够多。
8. `SENTINEL flushconfig`：将所有哨兵节点的配置重置为初始状态。
9. `SENTINEL remove <master-name>`：从哨兵监控中移除指定的主节点。

### SpringBoot集成哨兵

- **需要单独给哨兵模式的配置文件设置哨兵密码**
- **以及哨兵配置文件中指定监视的主机地址不可以是localhost/127.0.0.1**

```yaml
# 哨兵模式配置
spring:
  data:
    redis: 
      //host: 47.94.211.12  可以忽略地址，因为sentinel配置文件写了
      //port: 6379  可以忽略端口，因为sentinel配置文件写了
      password: root123456
      sentinel:
        master: myMaster
        nodes:
          - 47.94.211.12:26380
        password:  sentinel123456   //密码可以不写，可以试试
      database: 0
      client-type: lettuce
      jedis:
        pool:
          enabled: true
```

#### 集成的好处

1. **高可用性：Redis Sentinel模式提供了高可用性的解决方案**。通过集成哨兵，您可以实现Redis主节点的自动故障转移和自动发现。当主节点发生故障或下线时，哨兵会自动将从节点晋升为新的主节点，从而保持系统的可用性。
2. **故障转移：哨兵负责监视Redis主节点的健康状态，并在主节点发生故障时执行自动故障转移**。通过集成哨兵，您的Spring Boot应用程序可以自动感知主节点的故障，并切换到新的可用主节点，而无需手动干预。
3. **负载均衡：哨兵可以管理多个Redis主节点，并自动将请求分发到可用的节点上，实现负载均衡。** 通过集成哨兵，您的Spring Boot应用程序可以利用哨兵提供的负载均衡机制，将请求发送到合适的Redis主节点上，从而提高系统的性能和扩展性。
4. **自动发现：通过连接到哨兵，您的Spring Boot应用程序可以自动发现当前可用的Redis主节点**。您不需要手动配置主节点的地址和端口，而是依靠哨兵提供的自动发现机制，动态获取主节点的信息。
5. 配置管理：哨兵允许您管理Redis主节点的配置，包括添加、删除和修改监控的主节点。通过集成哨兵，您可以通过哨兵节点进行配置管理，而无需直接与每个Redis主节点交互。

通过集成Redis Sentinel，您可以确保Redis在面对主节点故障和高负载情况时仍能保持高可用性和性能。您的Spring Boot应用程序将能够更可靠地连接到Redis并实现缓存、分布式锁等功能，同时享受到Redis Sentinel提供的自动故障转移和负载均衡的好处。

#### 操作哨兵

- **操作哨兵可以移除、故障转移某个节点、复制**

**配置类**

```java
@Bean
public RedisSentinelCommands redisSentinelCommands() {    
    return new LettuceSentinelConnection("47.94.211.12",26380);    
}
```

**操作**

```java
@Bean
public  void sentinel(){    
    //打印监控主机信息    
    redisSentinelCommands.masters().forEach(System.out::println);    
    //故障转移    
    redisSentinelCommands.failover();    
    //移除    
    redisSentinelCommands.remove();    
    //复制    
    redisSentinelCommands.replicas()    
}    
```

## 缓存穿透 & 缓存雪崩 & 缓存击穿

### 缓存穿透

**缓存穿透：缓存没命中，大量的请求走数据库，导致负载或者宕机**

简单来说，**缓存穿透是指恶意请求或非常罕见的请求导致缓存无法有效地提供数据，每次请求都需要直接访问数据库，查不到**。这种情况下，**缓存无法发挥其加速访问的作用，而且数据库可能会承受过大的负载。**

**缓存的目的是为了提高数据访问的性能和响应时间。减轻数据库的压力**通常情况下，当一个请求到达时，首先会检查缓存中是否存在相应的数据。如果存在，就可以快速地返回数据给请求方。但是，当缓存中不存在该数据时，正常的流程是从数据库中获取数据，并将数据存储到缓存中，以便后续的请求可以直接从缓存中获取。

然而，如果一个请求频繁地查询不存在于缓存和数据库中的数据，那么每次请求都会触发对数据库的查询，这会导致缓存无法发挥作用，同时增加了数据库的负载。这就是缓存穿透的情况。

#### 解决方案

1. **布隆过滤器（Bloom Filter）**：使用布隆过滤器可以在缓存层面快速判断请求的数据是否存在。布隆过滤器是一种高效的数据结构，可以迅速判断一个元素是否存在于集合中，从而避免对数据库的不必要查询。
2. **缓存空值（Cache Null Values）**：当数据库查询不到某个数据时，可以将这个结果也缓存起来，但设置一个较短的过期时间。这样，在接下来的请求中，如果再次查询相同的数据，缓存就可以快速返回一个空值，避免对数据库的重复查询。

### 缓存击穿

**缓存击穿是指当一个热门的缓存数据过期或被删除时，同时有大量的请求同时访问这个数据，导致请求绕过缓存直接访问数据库。查太多**这会造成数据库负载过高，影响系统的性能和响应时间。

简单来说，缓存击穿发生在一个非常热门的缓存数据失效的瞬间，此时有很多请求同时访问这个数据。由于缓存失效，请求无法从缓存中获取数据，而需要直接访问数据库。这样一来，数据库会承受大量请求的压力，导致性能下降，并可能引起系统崩溃。

**缓存的目的是为了提高系统的性能和响应速度，减轻数据库的负载。** 正常情况下，当一个请求到达时，如果缓存中存在所需的数据，就可以直接从缓存中获取并快速返回给请求方，而无需访问数据库。但是，如果缓存中的数据过期或被删除，而且在这个时刻有很多请求同时访问这个数据，就会出现缓存击穿的情况。

#### 解决方案

1. **设置短暂的热门数据的互斥锁**：当检测到缓存失效时，在查询数据库之前，可以尝试获取一个互斥锁。如果成功获取锁，就去数据库查询并更新缓存；如果获取锁失败，表示其他请求正在更新缓存，当前请求可以等待一段时间再重试或返回默认值。
2. **提前异步刷新缓存**：在缓存数据即将过期之前，异步地进行缓存的刷新。这样可以避免在缓存失效时出现大量请求同时访问数据库。
3. **使用分布式锁**：在缓存失效的情况下，可以使用分布式锁来保证只有一个请求可以访问数据库，并在数据库查询完成后，将结果存储到缓存中。

###  缓存雪崩

**缓存雪崩是指在缓存中存储的大量数据同时过期或失效或者缓存服务器某个节点宕机或者断网，导致大量请求直接访问数据库，造成数据库负载剧增，系统性能下降甚至崩溃。**

简单来说，**缓存雪崩是指当缓存中的大量数据同时过期或失效时，系统无法从缓存中获取数据，而需要直接访问数据库。**由于大量请求同时访问数据库，数据库无法承受如此大的负载，导致系统响应变慢或崩溃。

**缓存的目的是为了提高系统的性能和响应速度，减轻数据库的负载**。正常情况下，当一个请求到达时，如果缓存中存在所需的数据，就可以直接从缓存中获取并快速返回给请求方，而无需访问数据库。但是，如果缓存中的大量数据同时过期或失效，就会出现缓存雪崩的情况。

#### 解决方案

1. **设置合理的缓存过期时间：** 将缓存数据的过期时间分散开，避免大量数据同时过期。可以随机添加一个小的时间差来分散缓存数据的过期时间。
2. **使用热点数据永不过期策略(不建议)：** 对于一些非常热门的数据，可以将其设置为永不过期，确保这些数据始终可用。
3. **实时监控和预热**：定期监控缓存的状态，确保缓存服务的稳定性。在缓存失效之前，可以通过预热的方式提前加载热门数据到缓存中，避免缓存失效时的突发请求。
4. **备份缓存**：采用多级缓存架构，将数据存储在不同的缓存层级中。当一个缓存层级失效时，可以从备份缓存中获取数据，避免直接访问数据库。
5. **多加几个redis缓存服务**

## 基于Redis的分布式锁原理

当客户端需要获取**锁**时，会尝试在**Redis**中设置一个key，如果key不存在，则设置成功，客户端获得**锁**；如果key已存在，则设置失败，客户端未能获得**锁**。 在获得**锁**后，客户端会在**Redis**中为该key设置一个过期时间，以确保在一定时间后**锁**会被自动释放，防止死**锁**现象的发生。
