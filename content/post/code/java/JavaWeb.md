---
title: JavaWeb
description: 一遍文章让你快速入门JavaWeb
slug: JavaWeb
date: 2024-08-08 00:00:00+0000
toc: true
categories:
    - 学习笔记
tags:
    - Java
    - JavaWeb
    - SQL
    - Tomcat
    - Maven
    - HTTP
---

# JavaWeb

***

## Web程序是什么

- 可以提供浏览器访问的网页
- 程序 = 数据结构+算法

##  Tomcat

> Apache Tomcat 是一个开源的实现了 Java Servlet、JavaServer Pages（JSP）、Java Expression Language（EL）和 Java WebSocket 技术的 web 服务器和 servlet 容器

### 下载并启动Tomcat

- **注意tomcat10以上注意版本问题**

- 配置Java环境：在本机上配置一个JAVA_HOME的变量

  ![image-20221129140528956](img/image-20221129140528956.png)

- 在bin文件内点startup.bat

  ![image-20221228120857316](img/image-20221228120857316.png)

- 访问地址localhost:8080

### Tomcat配置文件

#### 修改主机名称

Tomcat只能启动通过localhost去访问？ 可以修改在C:\Windows\System32\drivers\etc目录下host文件中有映射主机名称步骤如下

1. 修改改主机名称：在conf\service文件中改成自己想要的域名如`www.xxl.com`还要把自己主机的名称一起改掉在C:\Windows\System32\drivers\etc目录下host文件把本来映射localhost的改成www.xxl.com**注意是加映射**

    ```xml
    <!-- tomcat配置文件  -->
    <Host name="localhost" appBase="webapps" unpackWARs="true" autoDeploy="true" />
    ```

#### 修改端口

Tomcat目录中conf\service.xml文件中

```xml
<!-- tomcat配置文件  -->
<Connector port="8080" protocol="HTTP/1.1" connectionTimeout="20000" redirectPort="8443"/>
```

**Tip:**
1. mysql【默认3306】
2. http【默认80】.
3. https【默认端口443】


##### 相关面试题

- 请你谈谈网站是如何进行访问的！
  - 输入一个域名：回车
  - 检查本机的C:\Windows\System32\driv ers\etc\hosts配置文件有没有这个域名映射

    1. 有：直接返回对应的ip地址

    ![image-20221129141843038](img/image-20221129141843038.png)

    2. 没有：去dns服务器找，能找到就返回，找不到就返回找不到

    ![img](img/L377CV890TBGA{904_F26.png)

##### 相关面试题

- 请你谈谈网站是如何进行访问的！
  - 输入一个域名：回车
  - 检查本机的C:\Windows\System32\driv ers\etc\hosts配置文件有没有这个域名映射

    1. 有：直接返回对应的ip地址

    ![image-20221129141843038](img/image-20221129141843038.png)
  
    2. 没有：去dns服务器找，能找到就返回，找不到就返回找不到

    ![img](img/L377CV890TBGA{904_F26.png)

#### 发布一个web网站

将自己写的网站放到服务器【tomcat】中指定的web应用的文件夹下【webapps】，就可以访问了网站该有的的结构

```text
webapps : Tomcat服务器的web目录
    -ROOT
    -XXLStudy ：网站的目录名
    	-WEB-INF
    		-classes xx：Java程序
            -lib ： web应用所依赖的jar包
            -web.xml : 网站配置文件
        -index.html ： 默认的首页（注意名字index）
        -static
            -css
                -style.css
            -js
            -img
```

##### IDEA控制台乱码问题

在IDEA编辑器中help中自定义vm option加上这一句`-Dfile.encoding=UTF-8`其余的在tomcat log配置文件改  

### HTTP

> - 超文本传输协议（Hyper Text Transfer Protocol，HTTP）是一个简单的**请求-响应协议**，它通常运行在[TCP](https://baike.baidu.com/item/TCP/33012?fromModule=lemma_inlink)之上
>   - 文本：html，字符....
>   - 超文本：图片，音乐，视频，定位，地图.....

#### 两个时代

- HTTP/1.0：客户端与web夫区其连接后，只能获得一个web资源，然后断开连接
- HTTP/1.1：客户端与web夫区其连接后，可以获得多个web资源

#### Request & Response

##### Request(请求)

请求用于处理用户的网络动作大概流程：客户端 ➡️ 发请求 ➡️ 服务器

**请求头部分参数介绍**
  
```text
Request URL: https://www.baidu.com/?tn=15007414_pg 请求地址
Request Method: GET    请求方法
Status Code: 200 OK     状态码
Remote Address: 14.215.177.38:443   远程地址实际ip和端口
Accept: text/html 请求能够携带的数据类型
Accept-Encoding: gzip, deflate, br 支持那种编码
Accept-Language: zh-CN,zh;q=0.9 语言环境
Cache-Control: max-age=0 缓存控制
Connection: keep-alive   请求完成还是保持连接
   ```

##### Response(响应)

处理完请求之后就会回应给客户端大概流程为：服务器 ➡️  客户端

**响应体部分参数介绍**

```text
Accept: 告诉浏览器，他所支持的数据类型
Accept-Encoding:  支持那种编码  GBK UTF-8   GB2312
Accept-Language: 告诉浏览器，它的语言环境
Cache-Control:    缓存控制
Connection:    告诉浏览器，请求完成还是保持连接
HOST：主机
cache-control(缓存控制):private     
Connection(连接): keep-alive   保持连接
Content-Encoding(编码): gzip     
Content-Type(内容类型): text/html; charset=utf-8   
Refresh: 告诉客户端，多久刷新一次
Locatuion：让网页重新定位
```

- 响应状态码

  - 200：请求响应成功  200
  - 3xx：请求重定向
    - 重定向：重新到我给你找的新位置去
  - 4xx：找不到资源    404
  - 5xx：服务器代码错误    500 ：服务器代码错误   502：网关错误

##### 请求方法的区别

主要分为两种get和post，其余的delete/put...都是在get和post基础上扩展，为了满足Restful风格

1. `get`：请求能够携带的参数大小有限制，会在浏览器的url地址栏显示数据内容，不安全。但高效
2. `post`：请求能够携带的参数有限制，但是比get请求大，不会在浏览器的url地址栏显示数据内容，安全。但相对不高效

## Maven

>  Apache Maven 是一个软件项目管理和理解工具。基于项目对象模型 (POM) 的概念，Maven 可以通过中央信息来管理项目的构建、报告和文档。

简而言之就是包管理工具/项目架构管理工具

### 下载安装Maven

- 官网网址：[Maven – Welcome to Apache Maven](https://maven.apache.org/)
- 安装后解压即可
- 配置环境变量，如果你的Maven下载在`E:\Program Files (x86)\TomcatAndMaven\apache-maven-3.8.6`目录下
  - M2_HOME：`E:\Program Files (x86)\TomcatAndMaven\apache-maven-3.8.6-bin\apache-maven-3.8.6\bin`
  - MAVEN_HOME：`E:\Program Files (x86)\TomcatAndMaven\apache-maven-3.8.6-bin\apache-maven-3.8.6`
  - 还需要在Path环境变量中增加：`E:\Program Files (x86)\TomcatAndMaven\apache-maven-3.8.6-bin\apache-maven-3.8.6\bin`   

  ![image-20221228164932271](img/image-20221228164932271.png)

### 修改Maven配置文件的镜像

修改conf/setting.xml文件，修改镜像仓库地址为国内镜像仓库地址，目的下载jar包速度快

```xml
<mirrors>
  <mirror>
    <id>alimaven </id > 
    <name>aliyun maven</name>
    <!-- 阿里云仓库   -->
    <url>http://maven.aliyun.com/nexus/content/groups/public/</url> 			 
    <mirrorOf>central</mirrorOf>
  </mirror> 
</mirrors>
```

### 配置本地仓库
修改conf/setting.xml文件，默认项目依赖都会下载在`C:\Users\用户\.m2`中
```xml
<!--本地仓库,修改下载的地方为自定义创建的仓库-->
<localRepository>D:\Program Files (x86)\Maven\maven-repo</localRepository>   
```

### IDEA配置Maven

修改在IDEA的maven为我们自己的下载

![image-20221228172129655](img/image-20221228172129655.png)

在设置中设置自动下载源代码

![image-20221228182122799](img/image-20221228182122799.png)

**Tip: ** 以上配置如不想要每个项目都配置一次，则在在IDEA默认全局配置设置

### IDEA配置Tomcat

1. 点击当前文件进行配置

    ![image-20221228190143133](img/image-20221228190143133.png)

2. 配置上下文路径映射，也就是url地址会显示

    ![image-20221228190810818](img/image-20221228190810818.png)

    ![image-20221228191139999](img/image-20221228191139999.png)

3.  启动Tomcat，默认首页是index.jsp

    ![image-20221228191236459](img/image-20221228191236459.png)

4.  项目的结构

    ![微信图片_20221228191616](img/微信图片_20221228191616.jpg)

### POM文件

pom.xml是maven核心配置文件

```xml
<!--maven版本和头文件-->
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/maven-v4_0_0.xsd">
  <modelVersion>4.0.0</modelVersion>

<!--  我们配置的GAV-->
  <groupId>com.james.aks</groupId>
  <artifactId>javaweb01-maven</artifactId>
  <version>1.0-SNAPSHOT</version>
<!--  项目的打包方式：jar：Java应用，war：javaweb应用-->
  <packaging>war</packaging>

<!--  项目配置-->
  <properties>
<!--    项目默认构建编码-->
    <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
<!--    编码版本-->
    <maven.compiler.source>1.8</maven.compiler.source>
    <maven.compiler.target>1.8</maven.compiler.target>
  </properties>

<!--  项目依赖-->
  <dependencies>
<!--    具体依赖的jar包配置文件-->
    <dependency>
      <groupId>junit</groupId>
      <artifactId>junit</artifactId>
      <version>4.13.2</version>
      <scope>test</scope>
    </dependency>
<!--  maven的高级之处,它会帮你导入jar包其他所以依赖的jar包-->
    <dependency>
      <groupId>org.springframework</groupId>
      <artifactId>spring-webmvc</artifactId>
      <version>6.0.3</version>
    </dependency>
  </dependencies>

<!--  项目构建用的东西-->
  <build>
    <finalName>javaweb01-maven</finalName>
  </build>

</project>

```

出现配置无法生效、导出xml文件问题,解决方案在build中添加resource

```xml
<build>
  <resources>
    <resource>
      <directory>src/main/resources</directory>
      <includes>
        <include>**/*.properties</include>
        <include>**/*.xml</include>
      </includes>
      <filtering>true</filtering>
    </resource>
    <resource>
      <directory>src/main/java</directory>
      <includes>
        <include>**/*.properties</include>
        <include>**/*.xml</include>
      </includes>
      <filtering>true</filtering>
    </resource>
  </resources>
</build>
```

IDEA默认的web.xml版本太低问题：把Tomcat的web.xml文件版本复制过去

```xml
<?xml version="1.0" encoding="UTF-8"?>
<web-app xmlns="https://jakarta.ee/xml/ns/jakartaee"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="https://jakarta.ee/xml/ns/jakartaee
                      https://jakarta.ee/xml/ns/jakartaee/web-app_5_0.xsd"
         version="5.0"
         metadata-complete="true">
</web-app>

```

### 最简单的JavaWeb示例

1. 继承HttpServlet，重写doget，doPost()方法
2. 在web.xml文件中配置如下

    ```xml
    <?xml version="1.0" encoding="UTF-8"?>
    <web-app xmlns="https://jakarta.ee/xml/ns/jakartaee"
             xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
             xsi:schemaLocation="https://jakarta.ee/xml/ns/jakartaee
                          https://jakarta.ee/xml/ns/jakartaee/web-app_5_0.xsd"
             version="5.0"
             metadata-complete="true">
    <!--web.xml中配置我们的web核心应用   -->
    <!--    注册Servlet，一个Servlet标签对应一个类-->
        <servlet>
            <servlet-name>helloServlet</servlet-name>
    <!--        类的路径-->
            <servlet-class>com.xxl.HelloServlet</servlet-class>
        </servlet>
    <!--    一个Servlet对应一个Mapping：映射-->
        <servlet-mapping>
            <!--这个的名字要跟上面的servlet标签名字一致 -->
            <servlet-name>helloServlet</servlet-name>
    <!--        请求路径-->
            <!--tomcat10必须加斜杠“/”，而且在第一位-->
            <url-pattern>/helloServlet</url-pattern>
        </servlet-mapping>
    </web-app>
    ```

为什么要映射：我们通过url地址访问，每一个地址需要相应的Servlet类处理

#### Servlet-Mapping

匹配URL请求分发到对应的Servlet类处理,如下将介绍匹配规则

##### 1对1
一个Servlet对应一个Mapping
```xml
<!--    映射-->
<servlet-mapping>
  <servlet-name>HelloServlet</servlet-name>
  <url-pattern>/helloServlet</url-pattern>
</servlet-mapping>    
```

##### 1对多

一个Servlet对应多个Mapping

```xml
<!--    映射-->
<servlet-mapping>
  <servlet-name>HelloServlet</servlet-name>
  <url-pattern>/helloServlet</url-pattern>
</servlet-mapping><!--    映射-->
<servlet-mapping>
    <servlet-name>HelloServlet</servlet-name>
    <url-pattern>/hello</url-pattern>
</servlet-mapping>
 ```

##### 通用路径

一个Servlet可以指定通用路径

```xml    
<!--    映射-->    
<servlet-mapping>    
    <servlet-name>HelloServlet</servlet-name>    
    <url-pattern>/*</url-pattern>    
</servlet-mapping>        
```    
 
一个Servlet可以自定义后缀Mapping

```xml
<!--    映射-->
<servlet-mapping>
  <servlet-name>HelloServlet</servlet-name>
  <url-pattern>*.xxl</url-pattern>
</servlet-mapping>      
```

#### 优先级

映射优先级：固定匹配规则 > 通用匹配规则
