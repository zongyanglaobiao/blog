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
    - Web
    - SQL
    - Tomcat
    - 计算机网络
---

# javaWeb

***

## Web程序是什么

- 可以提供浏览器访问的网页
- 程序 = 数据结构+算法

## Tomcat

> Apache Tomcat 是一个开源的实现了 Java Servlet、JavaServer Pages（JSP）、Java Expression Language（EL）和 Java WebSocket 技术的 web 服务器和 servlet 容器

### 启动Tomcat

- **注意tomcat10以上好多坑时刻注意版本问题**

- 配置Java环境：在本机上配置一个JAVA_HOME的变量

  ![image-20221129140528956](img/image-20221129140528956.png)

- 在bin文件内点startup.bat

  ![image-20221228120857316](../img/image-20221228120857316.png)

  - 访问地址localhost:8080

##### 2.2配置文件：

- 改主机名称：在conf\service文件中改成自己想要的域名【例如www.xxl.com】还要把自己主机的名称一起改掉在C:\Windows\System32\drivers\etc目录下host文件把本来映射localhost的改成www.xxl.com【注意是加一个】

  ```xml
  <Host name="localhost" appBase="webapps" unpackWARs="true" autoDeploy="true">
  ```

  

- 改端口【默认8080】在E:\Program Files (x86)\Tomcat\apache-tomcat-10.0.27-windows-x64\apache-tomcat-10.0.27\conf\service.xml文件中

  ```xml
  <Connector port="8080" protocol="HTTP/1.1" connectionTimeout="20000" redirectPort="8443"/>
  ```

  - mysql【默认3306】
  - http【默认80】.
  - https【默认端口443】

##### 2.3高难度面试题

- 请你谈谈网站是如何进行访问的！

  - 输入一个域名：回车

  - 检查本机的C:\Windows\System32\driv ers\etc\hosts配置文件有没有这个域名映射

    1. 有：直接返回对应的ip地址

    ![image-20221129141843038](../img/image-20221129141843038.png)

      2.没有：去dns服务器找，能找到就返回，找不到就返回找不到

    ​	![img](../img/L377CV890TBGA{904_F26.png)

##### 2.4、发布一个web网站

- 将自己写的网站放到服务器【tomcat】中指定的web应用的文件夹下【webapps】，就可以访问了

- 网站该有的的结构

  - ```
    ---webapps : Tomcat服务器的web目录
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
        -.....
        		
    ```

##### 2.5、idea改乱码

```java
在help中自定义vm option加上这一句
-Dfile.encoding=UTF-8
 
其余的在tomcat log配置文件改    
```

### 3：HTTP

##### 3.1、什么是http

- 超文本传输协议（Hyper Text Transfer Protocol，HTTP）是一个简单的**请求-响应协议**，它通常运行在**[TCP](https://baike.baidu.com/item/TCP/33012?fromModule=lemma_inlink)**之上
  - 文本：html，字符....
  - 超文本：图片，音乐，视频，定位，地图.....
  - 默认端口80，Https安全的超文本传输协议：443

##### 3.2、两个时代

- HTTP/1.0：客户端与web夫区其连接后，只能获得一个web资源，然后断开连接
- HTTP/1.1：客户端与web夫区其连接后，可以获得多个web资源

##### 3.3、Http响应--请求

- 请求

  - 客户端---发请求------服务器

    **general(普遍的，通用)**

    ```java
    请求百度：
    Request URL: https://www.baidu.com/?tn=15007414_pg
    Request Method: GET    请求方法
    Status Code: 200 OK     状态码
    Remote Address: 14.215.177.38:443      远程地址
    ```

    **请求头**request—head

    ```java
    Accept(接收): text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,appl
    Accept-Encoding: gzip, deflate, br
    Accept-Language: zh-CN,zh;q=0.9
    Cache-Control: max-age=0
    Connection: keep-alive
    ```

  - 请求方式get，post，head，delete.....
    
  - **get**：请求能够携带的参数比较少，大小有限制，会在浏览器的url地址栏显示数据内容，不安全。但高效

  - **post**：请求能够携带的参数没有限制，大小没有限制，不会在浏览器的url地址栏显示数据内容，安全。但相对不高效

  - 消息头

    ```java
    Accept: 告诉浏览器，他所支持的数据类型
    Accept-Encoding:  支持那种编码  GBK UTF-8   GB2312
    Accept-Language: 告诉浏览器，它的语言环境
    Cache-Control:    缓存控制
    Connection:    告诉浏览器，请求完成还是保持连接
    HOST：主机
    ```

    

- 响应

  - 服务器---响应---客户端

    **响应头response-head**
    
    ```java
    百度响应;
    cache-control(缓存控制):private     
    Connection(连接): keep-alive   保持连接
    Content-Encoding(编码): gzip     
    Content-Type(内容类型): text/html; charset=utf-8   
    ```
    
  - 响应体

    ```java
    Accept: 告诉浏览器，他所支持的数据类型
    Accept-Encoding:  支持那种编码  GBK UTF-8   GB2312
    Accept-Language: 告诉浏览器，它的语言环境
    Cache-Control:    缓存控制
    Connection:    告诉浏览器，请求完成还是保持连接
    HOST：主机
    Refresh: 告诉客户端，多久刷新一次
    Locatuion：让网页重新定位
    ```

  - 响应状态码

    - 200：请求响应成功  200
    - 3xx：请求重定向
      - 重定向：重新到我给你找的新位置去
    - 4xx：找不到资源    404
    - 5xx：服务器代码错误    500 ：服务器代码错误   502：网关错误

  - 常见面试题：当你的浏览器中地址栏输入地址并回车的一瞬间到页面能够展示回来，经历了什么？

  先去本地host文件中查找地址是否有。没有就去互联网上dhcp解析地址，并发送请求给那个地址相关的服务器，服务器收到请求后会返回相应的一个响应给客户端显示屏

### 4：Maven

##### 4.1、为什么要学这个maven技术

1. 在javaweb开发中，需要使用大量的jar包，我们手动去导入太麻烦了，于是maven出现了，它能自动导入和配置这个jar包

##### 4.2、Maven项目架构管理工具

- 目前就是用来导jar包的
- Maven的核心思想是：**约定大于配置**。maven回规定好你如何和去编写我们的Java代码，且必须按照这个规范来

##### 4.3、下载安装 Maven

- 官网网址：[Maven – Welcome to Apache Maven](https://maven.apache.org/)

- 安装后加压即可    
- 配置环境变量
  - M2_HOME       E:\Program Files (x86)\TomcatAndMaven\apache-maven-3.8.6-bin\apache-maven-3.8.6\bin配M2就是为了后面的学习
  - MAVEN_HOME   E:\Program Files (x86)\TomcatAndMaven\apache-maven-3.8.6-bin\apache-maven-3.8.6
  - path里的maven目录   E:\Program Files (x86)\TomcatAndMaven\apache-maven-3.8.6-bin\apache-maven-3.8.6\bin

![image-20221228164932271](../img/image-20221228164932271.png)

##### 4.4、修改Maven配置文件的镜像

- 修改conf/setting.xml文件，修改镜像方便下载jar包

  ```xml
  <mirrors>
      <mirror>
  	 	<id>alimaven </id > 
  	 	<name>aliyun maven</name>
  	  	<url>http://maven.aliyun.com/nexus/content/groups/public/</url> 			 //阿里云仓库
  	  	<mirrorOf>central</mirrorOf>
  	</mirror> 
    </mirrors>
  ```

##### 4.5、配置本地仓库

- ```xml
  <localRepository>D:\Program Files (x86)\Maven\mavne-repo</localRepository>   //本地仓库
  ```

##### 4.6、在idea使用Maven

- 在idea设置中修改

![image-20221228172129655](../img/image-20221228172129655.png)

- 在设置中设置自动下载源代码

**![image-20221228182122799](../img/image-20221228182122799.png)**

- 不重复配置maven文件方法：在idea默认全局配置设置

##### 4.7、在idea中配置tomcat

- 点击当前文件进行配置

![image-20221228190143133](../img/image-20221228190143133.png)

- 配置上下文路径映射，也就是url地址会显示

  ![image-20221228190810818](../img/image-20221228190810818.png)

  ![image-20221228191139999](../img/image-20221228191139999.png)

- 启动tomcat，这下面的文件就是index.jsp



![image-20221228191236459](../img/image-20221228191236459.png)

- maven的结构

![微信图片_20221228191616](../img/微信图片_20221228191616.jpg)

##### 4.8、pom文件

- pom.xml是maven核心配置文件

```xml
<!--maven版本和头文件-->
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/maven-v4_0_0.xsd">
  <modelVersion>4.0.0</modelVersion>

<!--  我们配置的GAV-->
  <groupId>com.XXL</groupId>
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

- 出现配置无法生效、导出xml文件问题,解决方案在build中添加resource

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

- maven目录树

![image-20221228194212331](../img/image-20221228194212331.png)

- idea默认的web.xml版本太低问题：把tomcat的web.xml文件版本复制过去

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

##### 4.9Maven仓库的使用

- 使用人数多的jar包

![image-20221228200950028](img/image-20221228200950028.png)

### 5：写第一个Servlet(服务小程序)

- 继承HttpServlet，重写doget，doPost()方法
- 在web.xml文件中配置如下

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

- 为什么要映射：我们写的是java程序，需要在浏览器访问，而浏览器需要连接web服务器，所以要在web服务器中注册我们写的Servlet，给浏览器访问的一个路径

- Mapping问题
  - 一个Servlet对应一个Mapping
  
  ```xml-dtd
  <!--    映射-->
      <servlet-mapping>
          <servlet-name>HelloServlet</servlet-name>
          <url-pattern>/helloServlet</url-pattern>
      </servlet-mapping>
  ```
  
  - 一个Servlet对应多个Mapping
  
  ```xml
  <!--    映射-->
      <servlet-mapping>
          <servlet-name>HelloServlet</servlet-name>
          <url-pattern>/helloServlet</url-pattern>
      </servlet-mapping>
      <!--    映射-->
      <servlet-mapping>
          <servlet-name>HelloServlet</servlet-name>
          <url-pattern>/hello</url-pattern>
      </servlet-mapping>
  ```
  
  - 一个Servlet可以指定通用路径
  
    ```xml
    <!--    映射-->
        <servlet-mapping>
            <servlet-name>HelloServlet</servlet-name>
            <url-pattern>/*</url-pattern>
        </servlet-mapping>
    ```
  
  - 一个Servlet可以自定义后缀Mapping
  
  ```xml
  <!--    映射-->
      <servlet-mapping>
          <servlet-name>HelloServlet</servlet-name>
          <url-pattern>*.xxl</url-pattern>
      </servlet-mapping>
  ```

- Mapping优先级：固定的Mapping>通用Mapping

### 6：Servlet

##### 6.1、servlet简介

- Servlet就是sun公司**开发动态web的一门技术**
- 一个请求代表一个servlet
- sun公司在这些API提供了一个接口就做：Servlet，如果要开发一个Servlet程序，需要两个步骤
  - 编写一个类实现Servlet接口
  - 把开发好的Java类部署到web服务器中，实现了Servlet接口的程序叫做**Servlet**
- 可继承官方已经实现Servlet接口的类**HttpServlet**
- **servlet是单例模式**

##### 6.2、HelloServlet

- 构建一个普通的Maven项目，删掉src目录，以后的学习就在这个项目中建立model，这个空工程就是以后创建新项目的时候主工程

  父目录会有子目录的名字

  ```xml
  <modules>
      <module>servlet01</module>
  </modules>
  ```

  子目录会有父目录的AGV

  ```
  <parent>
      <artifactId>javaweb02-maven</artifactId>
      <groupId>com.xxl</groupId>
      <version>1.0-SNAPSHOT</version>
  </parent>
  ```

  **子目录可以直接使用父目录的jar包**，而父目录不可以使用子目录jar包

##### 6.3、servlet原理

- Servlet是由web服务器调用，web服务器在收到浏览器请求之后，会：

  ![image-20221229132501759](img/image-20221229132501759.png) 

自己画的图

![image-20221229133758829](img/image-20221229133758829.png)

### 7：ServletContext

- web容器在启动的时候，他会为每个web程序都创建一个对应的ServletContext对象，他代表当前的web应用

##### 7.1、**可以共享数据**，因为一个web应用只有一个上下文，所有的servlet都可以拿到这个上下文对象


![img](img/C9C66AC0E5979A71CD52AA77490DDD70.png)

- **eg：**

**设置数据**：

```java
//设置数据
String username = "xxl";  //设置的数据
ServletContext servletContext = req.getServletContext();   //注意是请求request拿到的上下文对象/this.getServletContext()
servletContext.setAttribute("username",username);

//response写在下面
/*resp.setCharacterEncoding("utf-8");
resp.setContentType("text/html");*/

String text = "<h1>开始设置数据</h1>";
//流不需要设置type和encoding
ServletOutputStream outputStream = resp.getOutputStream();
outputStream.write(text.getBytes(),0,text.getBytes().length);
outputStream.close();
```

![image-20221229165933759](img/image-20221229165933759.png)

**得到数据：**

```java
ServletContext servletContext = req.getServletContext();
String  username = (String) servletContext.getAttribute("username");
 
resp.setCharacterEncoding("utf-8");
resp.setContentType("text/html");
String name = "姓名：";
//字符流需要设置type和encoding，字节流不需要
PrintWriter writer = resp.getWriter();
writer.print(name+username);
writer.close();
```

![image-20221229165955253](img/image-20221229165955253.png)

##### 7.2、获取初始化参数

```java
ServletContext servletContext = this.getServletContext();
String url = servletContext.getInitParameter("url");//这个就是获得web.xml中设置的context-param参数
//打印出来
String text = "<h1>" + url + "</h1>";
ServletOutputStream outputStream = resp.getOutputStream();
outputStream.write(text.getBytes(),0,text.getBytes().length);
outputStream.close();
```

![image-20221229172428454](img/image-20221229172428454.png)

##### 7.3、**请求转发和重定向：都可以是一个Servlet或者一个.jsp文件**

- **转发：当前文件地址，转发带参数**

```java
ServletContext servletContext = this.getServletContext();
RequestDispatcher requestDispatcher = servletContext.getRequestDispatcher("/demo01");  //还没开始转发
requestDispatcher.forward(req, resp);  //开始转发
```
- **重定向：得带上项目地址，相当于之前重新发起请求，不饿能携带之前的request中参数**

  ```java
  //getContextPath  项目地址不带/
  resp.sendRedirect(req.getServletContext().getContextPath()+"/success/success.jsp");   重定向
  ```

  

  ![image-20221229174355664](img/image-20221229174355664.png)

  

##### 7.4、**读取资源文件**

  - 发现问题在java目录下的properties文件识别不了，解决方案用：在Maven中有写
  - 相对路径：target\servlet-02\WEB-INF\classes，俗称classpath

```java
//设置配置文件第一步加载load(),第二步保存stone()
Properties properties = new Properties();
//加载配置文件
properties.load(servletContext.getResourceAsStream(path));  //getResourceAsStream(path)把资源路径变成一个流
//读取配置文件
String username = (String) properties.get("username");
String pwd = (String) properties.get("pwd");
//设置配置文件
properties.setProperty("username", "wyx");
properties.setProperty("pwd", "wyx12345");
//保存配置文件
properties.store(new FileWriter(path2),null);
```

##### 7.5、ServletContext作用域

![image-20230102121111908](img/image-20230102121111908.png)

##### 7.6：路径问题

```java
this.getServletContext().getRealPath("/WEB-INF/upload")
    等于tomcat服务器所在的位置的webapps中
E:\Program Files (x86)\TomcatAndMaven\apache-tomcat-10.0.27-windows-x64\apache-tomcat-10.0.27\webapps\servlet_09\WEB-INF\upload\
```



### 8：HttpServletRequest

##### 8.1、HttpServletRequest

- HttpServletRequest代表客户端的请求，用户通过http协议访问服务器，http请求中的所有信息都会被封装到HttpServletRequest对象中，通过这个对象的方法可以获得客户端的所有信息

##### 8.2、常用方法

```java
req.getContextPath();  //拿到上下文路径后后面不带/
req.getAuthType();  //作者信息(谁访问的)
req.getHeader();   //拿到请求头信息
req.getHttpServletMapping(); //拿到请求路径
req.getMethod();      //拿到请求方法
req.getQueryString(); //查询信息
req.getRemoteUser();  //拿到远程用户信息
req.getRequestURI(); //拿到请求路径
req.getParameter();  //拿到请求中参数信息
req.getParameterValues();  //拿到请求中参数信息  这个是数组
```

##### 8.3、常见应用

- 登录

```JAVA
//处理请求
String username = req.getParameter("username");
String password = req.getParameter("password");
System.out.println("用户名：" + username + ",密码：" + password);

//登录成功之后，重定向
//重定向一定要记住，要当前的项目路径+页面路径
resp.sendRedirect("/servlet02/loginSuccess.jsp");
```

```JSP
<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
</head>
<body>
<h2>努力学习java中</h2>
<%--表单--%>
  <%--contextPath：当前发布出的路径，后面不带/    --%>  
<form action="${pageContext.request.contextPath}/login" method="get">
    用户名:<input type="text" name="username"><br>
    密码  :<input type="password" name="password"><br>
<%--    提交按钮--%>
    <input type="submit">
</form>
</body>
</html>
```

- 获取参数，请求转发     

  ```java
  String[] hobbies = req.getParameterValues("hobbies");
  String username = req.getParameter("username");
  String password = req.getParameter("password");
  //解决后端乱码问题
          req.setCharacterEncoding("utf-8");
          resp.setCharacterEncoding("utf-8");
  //打印信息
  System.out.println("=====================================");
  System.out.println("用户名" + username);
  System.out.println("密码" + password);
  System.out.println(Arrays.toString(hobbies));
  System.out.println("getContextPath:" + req.getContextPath());
  System.out.println("=====================================");
  
  //请求转发
  if (username.equals("xxl") && password.equals("xxl123456")) {
      //注意不用加上项目路劲，默认是加上的
      req.getRequestDispatcher("/loginSuccess.jsp").forward(req,resp);
  }else {
      //测试这会在那个页面出现
      ServletOutputStream outputStream = resp.getOutputStream();
      String text = "登录失败";
      outputStream.write(text.getBytes(),0,text.getBytes().length);
      outputStream.close();
  }
  ```

  ```jsp
  <%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
  <html>
  <head>
      <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
  </head>
  <body>
  <h2>努力学习java中</h2>
  <%--表单--%>
    <%--重要的是这个action，他表示谁会来那个页面处理这个请求--%>  
  <form action="${pageContext.request.contextPath}/login2" method="post">
      用户名:<input type="text" name="username"><br>
      密码  :<input type="password" name="password"><br>
      <%--    checkbox，name名字要一致--%>
      爱好  :<input type="checkbox" name="hobbies" value="girl">女孩
            <input type="checkbox" name="hobbies" value="code">打代码
            <input type="checkbox" name="hobbies" value="basketball">打篮球
            <input type="checkbox" name="hobbies" value="吃美食">吃美食
      <br>
  <%--    提交按钮--%>
      <input type="submit">
  </form>
  </body>
  </html>
  ```

### 9：HttpServletResponse

#### 9.1、HttpServletResponse的简述

- 响应，web服务器接收端客户端的http请求，针对这个请求，分别创建一个代表请求的HttpServletRequest对象和一个代表响应的HttpServletResponse的对象。
    - HttpServletRequest可以获取请求过来的参数
    - HttpServletResponse可以在这个对象加一些响应的信息

#### 9.2、简单分类

- 负责向浏览器发送数据的方法

  ```java
  public ServletOutputStream getOutputStream() throws IOException;   字节流
  public PrintWriter getWriter() throws IOException;   字符流
  ```

- 负责向浏览器发送的响应头的方法

  ```java
  public void setCharacterEncoding(String charset);
  public void setContentType(String type);
  public void setDateHeader(String name, long date);
  public void addDateHeader(String name, long date);
  public void setHeader(String name, String value)；
  public void addHeader(String name, String value);
  public void setIntHeader(String name, int value)；
  public void addIntHeader(String name, int value);
  ```

- 响应的状态码

  ```java
  public static final int SC_CONTINUE = 100;
  public static final int SC_SWITCHING_PROTOCOLS = 101;
  public static final int SC_OK = 200;    //请求响应成功
  public static final int SC_CREATED = 201;
  public static final int SC_ACCEPTED = 202;
  public static final int SC_NON_AUTHORITATIVE_INFORMATION = 203;
  public static final int SC_NO_CONTENT = 204;
  public static final int SC_RESET_CONTENT = 205;
  public static final int SC_PARTIAL_CONTENT = 206;
  public static final int SC_MULTIPLE_CHOICES = 300;
  public static final int SC_MOVED_PERMANENTLY = 301;
  public static final int SC_MOVED_TEMPORARILY = 302;
  public static final int SC_FOUND = 302;    //重定向
  public static final int SC_SEE_OTHER = 303;
  public static final int SC_NOT_MODIFIED = 304;
  public static final int SC_USE_PROXY = 305;
  public static final int SC_TEMPORARY_REDIRECT = 307;    //转发
  public static final int SC_BAD_REQUEST = 400;
  public static final int SC_UNAUTHORIZED = 401;
  public static final int SC_PAYMENT_REQUIRED = 402;   //找不到资源 
  public static final int SC_FORBIDDEN = 403;
  public static final int SC_NOT_FOUND = 404;
  public static final int SC_METHOD_NOT_ALLOWED = 405;  //方法不被永许
  public static final int SC_NOT_ACCEPTABLE = 406;
  public static final int SC_PROXY_AUTHENTICATION_REQUIRED = 407;
  public static final int SC_REQUEST_TIMEOUT = 408;
  public static final int SC_CONFLICT = 409;
  public static final int SC_GONE = 410;
  public static final int SC_LENGTH_REQUIRED = 411;
  public static final int SC_PRECONDITION_FAILED = 412;
  public static final int SC_REQUEST_ENTITY_TOO_LARGE = 413;
  public static final int SC_REQUEST_URI_TOO_LONG = 414;
  public static final int SC_UNSUPPORTED_MEDIA_TYPE = 415;   //不支持类型
  public static final int SC_REQUESTED_RANGE_NOT_SATISFIABLE = 416;
  public static final int SC_EXPECTATION_FAILED = 417;
  public static final int SC_INTERNAL_SERVER_ERROR = 500;   //服务器代码错误 
  public static final int SC_NOT_IMPLEMENTED = 501;
  public static final int SC_BAD_GATEWAY = 502;   //网关错误
  public static final int SC_SERVICE_UNAVAILABLE = 503;
  public static final int SC_GATEWAY_TIMEOUT = 504;
  public static final int SC_HTTP_VERSION_NOT_SUPPORTED = 505;
  ```

#### 9.3、常见应用

- 下载文件

  ```java
  //文件路径
  String path = "D:\\Program Files (x86)\\idea\\IDEAproject\\javaweb02-maven\\servlet-02\\src\\main\\java\\com\\xxl\\servlet\\response\\女孩.jpeg";
  //上下文拿到的真实路径:  E:\Program Files (x86)\TomcatAndMaven\apache-tomcat-10.0.27-windows-x64\apache-tomcat-10.0.27\webapps\servlet02\迪丽热巴.png
  //显然图片不可能在tomcat下面
  System.out.println("getRealPath拿到的路径："+this.getServletContext().getRealPath("女孩.jpeg"));
  //拿到文件名
  String fileName = path.substring(path.lastIndexOf("\\")+1);
  System.out.println("文件名字：" + fileName);
  //设置响应头用来可以下载文件，如果文件名是中文名下载会出现不显示的情况解决方法：
  resp.setHeader("Content-disposition","attachment;filename="+ URLEncoder.encode(fileName,"utf-8"));
  //输入流-->读取文件   相当于拷贝文件
  BufferedInputStream in = new BufferedInputStream(new FileInputStream(path));
  //输出流-->写出文件
  ServletOutputStream out = resp.getOutputStream();   //写出文件
  //开始写文件
  byte[] bytes = new byte[1024];   //容器
  int len = 0;         //真实容量
  while ((len = in.read(bytes)) != -1) {
      out.write(bytes,0,len);
  }
  in.close();
  out.close();
  ```

- 验证码实现

  ```java
   @Override
      protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
          //准备图片，图片上有我们随机生成的验证码
          BufferedImage bufferedImage = new BufferedImage(100, 20,BufferedImage.TYPE_INT_RGB);
          //画笔
          Graphics2D graphics = (Graphics2D) bufferedImage.getGraphics();
          //设置图片背景颜色
          graphics.setColor(Color.white);
          //设置图片背景填充颜色大小
          graphics.fillRect(0,0,100,20);
          //把验证码画到图片中，准确来说是把图片画到准备到画笔画出的的空间
          graphics.setColor(Color.BLACK);
          graphics.setFont(new Font(null,Font.BOLD,20));
          graphics.drawString(getRandomNUmber(),0,20);
  
          //让验证码3秒刷新一次
          resp.setHeader("refresh","5");
          //告诉浏览器用图片的方式打开
          resp.setContentType("image/png");
          //告诉浏览器不用缓存
          resp.setDateHeader("expires",-1);
          resp.setHeader("Cache-Control","no-cache");
          resp.setHeader("Pragma","no-cache");
  
          //把图片写给浏览器
          boolean io = ImageIO.write(bufferedImage, "png", resp.getOutputStream());
      }
      /**
       *@date:2022/12/31/13:44
       *@explian:  生成随机数，总共八位
       */
      private String getRandomNUmber() {
          Random random = new Random();
          String i  = random.nextInt(999999999) + "";
          StringBuffer stringBuffer = new StringBuffer(i);
          //缺几位就补几位0，实际随机生成的就是8位数
          for (int i1 = 0; i1 < 8 - i.length(); i1++) {
              stringBuffer.append("0");
          }
          return stringBuffer.toString();
      }
  ```

- **重定向**

```java
resp.sendRedirect("/servlet02/code");  //路径要注意还要加上项目路径
```

#### 9.4、面试题

- 请你聊聊重定向和转发的区别
  - 相同点
    - 页面都会跳转
  - 不同点
    - 重定向：url地址栏会 变化   307
    - 转发：url地址栏不会发生变化  302

### 10：cookie

##### 10.1、会话

- **重点：除了服务器创建的cookie，自己增加的cookie只会在你response回去的那个页面（详细信息见下面图解），也就是说转发会携带请求和cookie，而重定向不会**

- **cookie是有作用范围，范围的大小巨顶请求的时候能带哪些cookie所以有的时候明明设置了cookie却无法生效，看下图**

  ![image-20230404143945057](img/image-20230404143945057.png)

- 用户打开浏览器，点击了很多链接，访问多个web资源，然后关闭浏览器，这个过程可以称之为会话

- 一次会话是指： 好比打电话，当A打给B，电话接通了 会话开始，持续到会话结束。 浏览器访问服务器，就如同打电话，浏览器A给服务器发送请求，访问web程序，该次会话就开始，其中不管浏览器发送了多少请求 ，都为一次会话，直到浏览器关闭，本次会话结束。

 ```java
 /*
        解决ajax跨域导致session不一致的问题，由于sessionId是存在cookie,而每次获取getSession()
        都会通过cookie中的sessionId来获取session,如果没有就会创建一个新的session，然后把sessionId存在cookie中
         //把cookie中的sessionId给下一个请求，失败因为跨域原因导致cookie崩创建
        String sessionId = "JSESSIONID";
        Cookie[] cookies = request.getCookies();
        if (cookies != null) {
            log.info("cookie=不为null");
            for (Cookie cookie : cookies) {
                if (cookie.getName().equals(sessionId)) {
                    Cookie cookie1 = new Cookie(sessionId,cookie.getValue());
                    response.addCookie(cookie1);
                }
            }
        }
        */
 ```

##### 10.2、有状态会话

- 第一次去某个网站然后登录，之后会给你标记，下次来的时候，网站识别到这个标记，知道你来过，所以就不用重新登录了

##### 10.3、保存会话的两种技术

- **cookie**：客户端技术 ，存的数据比较少
- **session**：服务器技术，利用这个技术，可以保存用户的会话信息，可以把数据或者信息放在session中

##### 10.4、Cookie的使用方法

- cookie常用的方法

  ```java
  Cookie cookie = new Cookie();
  cookie.getName();  //得到cookie的键
  cookie.setMaxAge();  //设置cookie的存活期
  cookie.getValue(); //得到当前cookie的值
  cookie.setPath();  //设置作用范围
  ```

- 从请求中拿到cookie，再响应一个cookie给客户端

```java
String h1 = "<h1>";
String h1end = "</h1>";
//查看cookie一般从请求中得到
Cookie[] cookies = req.getCookies();   //cookie不止一个
//响应
ServletOutputStream outputStream = resp.getOutputStream();
//判断有没有cookie
if (cookies != null) {
    for (Cookie ck : cookies) {
        if (ck.getName().equals("lastLoginTime")) {
            String text = h1+"上次登录时间："+ck.getValue()+h1end;
            outputStream.write(text.getBytes(),0,text.getBytes().length);
        }
    }
}else {
    String text = h1+"第一次没有cookie"+h1end;
    outputStream.write(text.getBytes(),0,text.getBytes().length);
}
resp.setCharacterEncoding("utf-8");
//添加cookie
Date date = new Date();
SimpleDateFormat format = new SimpleDateFormat("yyyy-MM-dd-hh:mm:ss");
String format1 = format.format(date);
Cookie lastLoginTime = new Cookie("lastLoginTime",format1);
//设置这个cookie存活时间,单位是秒
lastLoginTime.setMaxAge(24*60*60);
Cookie cookie = new Cookie("info", "随便写的");
resp.addCookie(lastLoginTime);
resp.addCookie(cookie);
outputStream.close();
```

- 一个网站的cookie上限：**一个web站点可以给浏览器发送多个cookie，最多存放20个cookie**

- cookie大小有限制：**4kb**

- **300个cookie是一个浏览器的上限**

- 删除cookie

  - 不设置有效期

  - 设置有效期为0

    ```java
     Cookie cookie = new Cookie("name", "xxl");
     //cookie.setMaxAge(0)  //写在这就是这个会话期间就没了，但没什么意义
     resp.addCookie(cookie);
    //cookie.setMaxAge(0);  //写在这跟默认是一样的就是浏览器关闭cookie就没
    ```

- 网络编程时刻注意编码问题

  - ```java
    编码：URLEncoder.encode();
    解码： URLDecoder.decode();
    ```

### 11：session(重点)

- **每个人get的session都不同，只要不是在同一个浏览器**

- **session是存在服务器上，cookie是存在浏览器(每次请求会携带当前页的所有cookie)，session对象在服务器默认存活时间未30分钟**

- 对session来说也是一样的，除非程序通知服务器删除一个session，否则服务器会一直保留。

  > 所以浏览器从来不会主动在关闭之前通知服务器它将要关闭，因此服务器根本不会有机会知道浏览器已经关闭，之所以会有这种错觉，是大部分session机制都使用会话cookie来保存session id，而关闭浏览器后这个session id就消失了，再次连接服务器时也就无法找到原来的session
  > 　恰恰是由于关闭浏览器不会导致session被删除，迫使服务器为seesion设置了一个失效时间，一般是30分钟也就是说这个session可以一直存在，只要服务器不刷新，或者设置一个存话时间(这样浏览器关闭也会存在)，当距离客户端上一次使用session的时间超过这个失效时间时，服务器就可以认为客户端已经停止了活动，才会把session删除以节省存储空间

- 服务器刷新，浏览器关闭/刷新，session就没了，不适合存数据

- cookie可以存  在浏览器，只要还在cookie存活期cookie就一直存在。

- **session和cookie关系**

  ```java
  /*
      场景：通过session里用户判断是否登录
      设置session时间(是这个session对象在服务器的存活时间，一般为30分钟)：如果关闭浏览页，再打开session中还是存着用户信息的.关闭浏览器在打开就要重新登录，
      （注意session是可以跨同个服务器的多个页面这就是保存用户信息的核心(它存在web上下文中)，cookie则不可以，只能在某一页，但是cookie
      是存在请求中的，也就是每次请求都会携带当前页的cookie）
      session是是通过cookie中存的sessionId获得的，但保存sessionId的cookie是服务器自己创建的，一旦关闭浏览器
      再次打开页面就会重新创建cookie同时session也会变化，(想要完成“记住我”这种功能，需要cookie和session一起合作)
      所以需要设置cookie存活期，浏览器默认创建的cookie存活期为一次会话，也就是浏览器不够就心
  */
  ```

##### 11.1、什么是session

- 服务器会给，会每一个用户(浏览器某个app)，创建一个Session对象
- 一个web应用只有一个session并且独占一个浏览器（**也就是session是唯一的**），也就是换了一个浏览器也有session只是不一样，但这个session独占这个浏览器。只要浏览器没有关闭，这个Session就存在。这一点跟cookie一样

##### 11.2、session和cookie的区别

- cookie：是把用户的数据写给用户的浏览器，浏览器保存(可以保存多个)
- session：把用户的数据写给用户独占的session中，服务端保存，**session对象由服务器创建**

##### 11.3、session的普通用法

- **存数据**

  ```java
  //解决乱码问题
  req.setCharacterEncoding("utf-8");
  resp.setCharacterEncoding("utf-8");
  //把文本转为html，但其实不用设置，默认就是这样的
  resp.setContentType("text/html");
  //得到session
  HttpSession session = req.getSession();
  //存数据
  session.setAttribute("name","xxl");
  //存一个对象数据
  session.setAttribute("person",new Person("wyx",18));
  
  //这个session是否是新创建的
  if (session.isNew()) {
      resp.getWriter().write("<h1>session是新创建的</h1>");
  }else {
      //只会走这一步(根据浏览器来，chrome就会走上面的)，因为打开那个页面就自动会创建一个会话session,只要访问就会产生一个session
      resp.getWriter().write("<h1>session不是新创建的，id："+session.getId()+"</h1>");
  }
  //取数据
  String name = (String)session.getAttribute("name");
  System.out.println(name);
  //session创建的时候做了什么
  /*Cookie cookie = new Cookie("JSESSIONID", session.getId());
  resp.addCookie(cookie);*/
  ```

- **servlet与servlet之间的通信用session**

  ```java
  //解决乱码问题
  req.setCharacterEncoding("utf-8");
  resp.setCharacterEncoding("utf-8");
  //把文本转为html，但其实不用设置，默认就是这样的
  resp.setContentType("text/html");
  //取出demo01存的数据
  HttpSession session = req.getSession();
  Person person = (Person) session.getAttribute("person");
  
  String text =  "<h1>demo02:"+session.getAttribute("name")+"</h1>";
  String text1 = "<h1>demo02:" + person.toString() + "</h1>";
  PrintWriter writer = resp.getWriter();
  writer.write(text);
  writer.write(text1);
  writer.close();
  ```

- **手动注销session以及session的存的数据**

  ```java
  HttpSession session = req.getSession();
  //注销session中所存的数据
  session.removeAttribute("name");
  //注销掉整个session
  session.invalidate();
  ```

- **自动注销session在配置文件(web.xml)中设置session存活时间**

  ```xml
  <!--  session配置  -->
  <session-config>
      <!--     设置存活时间，以分钟为单位 设置在服务器的存活时间  -->
      <session-timeout>1</session-timeout>
  </session-config>
  ```

##### 11.4、使用场景

- 保存一个登录用户的时间
- 购物车信息

### 12：多个用户如何共享数据

##### 12.1、多个用户在同一个web应用如何共享数据

- **只能用ServletContext**，cookie不行，session也不行
  - session是因为每个用户都有自己的一个唯一的sessionId
  - cookie是因为无法做到，是因为需要提交cookie

### 13：jsp原理(记住jsp文件其实就是一个类罢了)

##### 13.1、什么是jsp

- jsp(java server pager)：java服务器端页面，和servlet一样，用于动态web技术

- 最大的特点：写jsp就像写html，**同时jsp中可以嵌入java代码**

##### 13.2、jsp原理

- **jsp怎么执行的：jsp最终也会转变成一个java类**

  ![image-20230102132718626](img/image-20230102132718626.png)

  - idea的tomcat工作空间

    ```jav\
    C:\Users\xxl\AppData\Local\JetBrains\IntelliJIdea2022.2\tomcat\e15f62a3-55e4-44b3-b0d0-787c68ff1d5e\work\Catalina\localhost\servlet_04\org\apache\jsp
    ```

- **jsp本质是一个Servlet**

  ```java
  public final class index_jsp extends org.apache.jasper.runtime.HttpJspBase  //HttpJspBase继承了HttpSerlevrt。
      implements org.apache.jasper.runtime.JspSourceDependent,
                   org.apache.jasper.runtime.JspSourceImports {
  ```

- jsp的一些方法

  ```java
  //初始化
  public void _jspInit() {
    }
  //销毁	
  public void _jspDestroy() {
  }
  //jsp服务
    public void _jspService(final jakarta.servlet.http.HttpServletRequest request, final jakarta.servlet.http.HttpServletResponse response)
  ```

- 工作原理：如果jsp中有java代码就原封不动写进去(xxx_jsp.java类)，有html代码就写成字符串，让浏览器去识别

##### 13.3、jsp，_jspService()方法中的内置对象

```java
final jakarta.servlet.jsp.PageContext pageContext;  //页面上下文
jakarta.servlet.http.HttpSession session = null;  //session
final jakarta.servlet.ServletContext application;  //ServletContext
final jakarta.servlet.ServletConfig config;   //配置
jakarta.servlet.jsp.JspWriter out = null;  //写出对象
final java.lang.Object page = this;    //代表当前页
final jakarta.servlet.http.HttpServletRequest request, //请求 
final jakarta.servlet.http.HttpServletResponse response  //响应
```

##### 13.4、输出页面前增加的代码

```java
pageContext = _jspxFactory.getPageContext(this, request, response,
			null, true, 8192, true);
_jspx_page_context = pageContext;
application = pageContext.getServletContext();    //获取servletContext
config = pageContext.getServletConfig();  //获取配置
session = pageContext.getSession();  //获取session
out = pageContext.getOut(); //获取输出对象
_jspx_out = out;
```

##### 13.5、在jsp中写java代码

```java
写java代码必须在<%%>中
<%  out.write();   %>
```

##### 13.6、请求一个jsp页面的流程图

![image-20230102134552563](img/image-20230102134552563.png)

### 14：jsp基础语法和指令

##### 14.1、jsp指令

- **第一种：<%=java%>这是一个输出的语句，里面的内容直接输出，注意不要写分号。所有地方的变量都可以引用**

    **第二种：<%java%>在这里面我们就可以写一些java代码,for循环之类的。**
    
    **第三种：<!%java%>写java代码和方法，不同之处在于这个直接在类中**
    
    **第四种：<%@ %><%@ include file%>将引入的文件和原来的文件合二为一，就是不能有一样的变量....,<jsp:includ/>则相反**
    
    | <%@ page ... %>    | 定义网页依赖属性，比如脚本语言、error页面、缓存需求等等 |
    | ------------------ | ------------------------------------------------------- |
    | <%@ include ... %> | 包含其他文件                                            |
    | <%@ taglib ... %>  | 引入标签库的定义                                        |
    
    **第五种：<jsp:  args   />可以在这里写一些配置代码**

##### 14.2、java代码中嵌入html代码

- **java代码中不能嵌入html代码**，可以伪嵌入，**<%%>不可以嵌入<%%>**

  ```jsp
  <%
      for (int i = 0; i < 5; i++) {
  %>
  <h1>hello,world</h1>   //实际是把java代码拆分了，中间写上html代码
  <%
      }
   %>    
  ```

- html嵌入java代码

  ```jsp
  <h2>姓名：<%=name%></h2>
  ```

##### 14.3、jsp输出的区别

- **<%%>这个里面的表达式和代码都是在_jspService()方法中**

- **<!%%>这个里面的表达式和代码都是在xxx_jsp.java类中**，这叫jsp声明

#####   14.4、注释的区别

```jsp
<!------->   //客户端会显示注释内容
<%---------%>  //客户端不会显示
```

##### 14.5、定制错误页面

- **jsp文件>web.xml文件**

  在jsp文件中

```jsp
<%--定制错误页面，在web.xml文件也可定制--%>
<%@ page errorPage="ErrorPage.jsp" %>
```

​		在web.xml中

```xml
<error-page>
    <error-code>500</error-code>
    <location>/ErrorPage.jsp</location>
</error-page>
```

##### 14.6、jsp9大内置对象

- PageContext  存东西
- response
- request  存东西
- session  存东西
- Application【ServletContext】  存东西
- Config【ServletConfig】    
- out
- page
- exception

- 简单的应用，**四大对象的有效域【pageContext<request<session<application】**

  ```jsp
  <%--注意在<%%>里就是x写java代码，所以注释别搞错了--%>
  <%
      //存数据的四个对象，区别就在于作用域不一样、
      pageContext.setAttribute("name1","xxl1");   //保存的数据只在一个页面有效
      application.setAttribute("name2","xxl2");   //保存的数据在服务器有效，也就是到服务器关闭之前都是有效，或者说在一个web应用有效
      request.setAttribute("name3","xxl3");       //保存的数据在一次请求有效，转发依然有效(因为转发地址不变)
      session.setAttribute("name4","xxl4");       //保存的数据在一次会话中有效，从打开浏览器到关闭浏览器都有效
  %>
  <%
      //取数据通过pageContext,也就是就说只要在这个页面存的数据都可以通过pageContext找到，其余几个存数据则不可以
      String name1 = (String)pageContext.findAttribute("name1");
      String name2 = (String)pageContext.findAttribute("name2");
      String name3 = (String)pageContext.findAttribute("name3");
      String name4 = (String)pageContext.findAttribute("name4");
      String name5 = (String)pageContext.findAttribute("name5");
   	//pageContext可以设置作用域
      /*public static final int PAGE_SCOPE = 1;
      public static final int REQUEST_SCOPE = 2;
      public static final int SESSION_SCOPE = 3;
      public static final int APPLICATION_SCOPE = 4;*/
      pageContext.setAttribute("name5","xxl5",PageContext.SESSION_SCOPE);
      //上面那句 == session.setAttribute("name5","xxl5"); 
  %>
  <%--<%=%>与${}的区别，前者未取到值会显示null，后者未取到值不显示--%>
  <%--
  <h1>姓名：<%=name1%></h1><br>
  <h1>姓名：<%=name2%></h1><br>
  <h1>姓名：<%=name3%></h1><br>
  <h1>姓名：<%=name4%></h1><br>
  <h1>姓名：<%=name5%></h1><br>
  --%>
  <h1>姓名：${name1}</h1><br>
  <h1>姓名：${name2}</h1><br>
  <h1>姓名：${name3}</h1><br>
  <h1>姓名：${name4}</h1><br>
  <h1>姓名：${name5}</h1><br>
  ```

- 转发

  ```jsp
  pageContext.forward("/index02.jsp");
  //上面这句 == request.getRequestDispatcher().forward();
  ```

### 15：jsp标签以及表达式

##### 15.1、EL表达式:${}

- 作用域:**s{} 小于 <%=%>**

- 作用
  - **获取数据**
  - **执行运算(加减乘除，判断)**
  - **获取web常用开发对象**

- 其中之一用法：${arg}等价于<%= arg%>,区别在于：**如果 arg不存在，<%= %>会返回null，而${}不会返回东西**，还有就是**获取变量时变量如果是在html中就用param.参数名，如果是java定义，需要先存起来【session，pageContext，application(ServletContext)，request】然后就直接引用存起来的名字。**

- 所用的依赖

  ```xml
  <!--    jsp表达式依赖   -->
         <dependency>
             <groupId>org.glassfish.web</groupId>
             <artifactId>jakarta.servlet.jsp.jstl</artifactId>
             <version>3.0.1</version>
         </dependency>
  <!--  standard标签库的依赖     -->
         <dependency>
             <groupId>taglibs</groupId>
             <artifactId>standard</artifactId>
             <version>1.1.2</version>
         </dependency>
  
  ```

##### 15.2、jsp标签

- 具体样子

  ```jsp
  <%--这个相当于http://localhost:8080/servlet_04/demo01.jsp?name1=xxl1&name2=xxl2--%>
  <jsp:forward page="demo02.jsp">
    <jsp:param name="name1" value="xxl1"/>
    <jsp:param name="name2" value="xxl2"/>
  </jsp:forward>
  ```

##### 15.3、JSTL表达式

- 为什么使用：为了弥补HTML的不足

- **核心标签(掌握部分即可,其他类型标签基本不使用)**

  使用之前先导入

  ```jsp
  <%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
  ```

  ![image-20230102212714636](img/image-20230102212714636.png)

- **格式化标签**

  使用之前先导入

  ```jsp
  <%@ taglib prefix="fmt" 
             uri="http://java.sun.com/jsp/jstl/fmt" %>
  ```

  ![image-20230102212802668](img/image-20230102212802668.png)

- **sql标签**

  使用之前先导入

  ```jsp
  <%@ taglib prefix="sql" 
             uri="http://java.sun.com/jsp/jstl/sql" %>
  ```

  ![image-20230102212835145](img/image-20230102212835145.png)

- **xml标签**

  使用之前先导入

  ```jsp
  <%@ taglib prefix="x" 
             uri="http://java.sun.com/jsp/jstl/xml" %>
  ```

  ![image-20230102212905284](img/image-20230102212905284.png)

##### 15.4、简单应用

- 核心库if标签应用

```jsp
<%-- 把表单提交给这个页面   --%>
<form action="demo03.jsp" method="get" >
    <%--    value="${param.username}" 这是获取这个名字为username的表单的数据
            获取表单中的数据格式为:${param.参数名}
    --%>
    <input type="text" name="username"  >
    <input type="submit" value="登录" >
</form>
<%--  test：判读语句必须是返回true/false  var(定义变量的意思)：接收这个语句是true/false  表单里面就是true就输出的话--%>
<c:if test="${param.username ==  'admin'}" var="isAdmin" >
    <%--     <c:out value="管理员欢迎你" >输出value里的内容    --%>
    <c:out value="管理员欢迎你" >
    </c:out>
</c:if>

<c:out value="${isAdmin}"></c:out>
```

- 核心库set、when、choose、otherwise标签应用【**注意otherwise，when标签只能在when标签中使用**】

  ```jsp
  <%-- set标签就是定义变量像javascript var:变量  value:变量值 --%>
  <c:set var="score" value="drg" ></c:set>
  <%-- choose相当与ifelse-ifelse --%>
  <c:choose>
      <%--   相当与if，判断会从第一句开始，有一个符合条件就不继续判断了     --%>
      <%--  有一个bug如果是随便输入的话它不走else，走的是第一句if ，可能跟他的比较方式有问题     --%>
      <c:when test="${score >= '90' }">
          <h1>优秀</h1>
      </c:when>
      <c:when test="${score >= '80' }">
          <h1>良好</h1>
      </c:when>
      <c:when test="${score <= '60' }">
          <h1>不及格</h1>
      </c:when>
      <%--   相当与else     --%>
      <c:otherwise>
          <c:out value="不优秀"/>
      </c:otherwise>
  </c:choose>
  ```

- 核心库的**foreach**标签的使用

  ```jsp
  <%
      List<String> people = new ArrayList<>();
      people.add(0,"xxl0");
      people.add(1,"xxl1");
      people.add(2,"xxl2");
      people.add(3,"xxl3");
      people.add(4,"xxl4");
      people.add(5,"xxl5");
      pageContext.setAttribute("list",people);
  %>
  <%--
    for (String person : people) {} 这句相当与  <c:forEach items="${people}" var="person"/>
    for (int i = 0; i < people.size(); i++) {}  这句相当于  <c:forEach items="${people}" var="person" begin="" end=" " step=""/>
    items:要遍历的对象
    var(变量)：遍历出的每一个值
    begin:从那个开始   默认从0
    end：到哪结束      默认到最后
    step：步数        默认是1
    --%>
  <h1>第一种用法</h1>
  <c:forEach items="${list}" var="person">
      <h1>${person}</h1>
  </c:forEach>
  <h1>第二种用法</h1>
  <%--  理想结果：xxl1   xxl3   --%>
  <c:forEach items="${list}" var="person" begin="1" end="${list.size() - 2}" step="2">
      <h1>${person}</h1>
  </c:forEach>
  ```

### 16：JavaBean(实体类)

##### 16.1、javaBean特定的写法

- 必须有一个无参构造
- 属性必须私有化
- 必须有对应的get/set方法

##### 16.2、javaBean能做什么

- 一般用于和数据库的字段做映射

##### 16.3、ORM(Object Relationship  Mapping)：对象关系映射

- 表 --->类
- 字段 ---->属性
- 行记录 --->对象

![image-20230103133657945](img/image-20230103133657945.png)

##### 16.4、用jsp创建一个实体类对象

- **jsp、${}、<%=%>的区别**

```jsp
<h1>用jsp标签写javaBean测试</h1>
<hr>
<%--   创建一个对象     --%>
<%--
    下面的等价与
    People people1 = new People();
    people1.setAddress("山水云间");
    people1.setId(1);
    people1.setName("xxl");
    people1.setAge(19);

    userBean：使用某一个类
    class:类路径
    id：给这个人类一个名字
--%>
<jsp:useBean id="people" class="com.xxl.pojo.People">
    <%--     name：userBean创建的名字(就是实体类名字)   property：类属性   value:设置属性的值   --%>
    <jsp:setProperty  name="people" property="id" value="1"/>
    <jsp:setProperty  name="people" property="address" value="山水云间"/>
    <jsp:setProperty  name="people" property="age" value="19"/>
    <jsp:setProperty  name="people" property="name" value="xxl"/>
</jsp:useBean>
<%
    People people1 = new People();
%>
<%--得到一个对象--%>
<%--
    下面等价于
    People people1 = new People();
    people1.getAddress();
    people1.getAge();
    people1.getName();
    people1.getId();

    name:对象名字
    property:属性
    本身有返回值
 --%>
<h1>通过jsp取对象属性</h1>
<h1>id： <jsp:getProperty name="people" property="id"/></h1><br>
<h1>姓名：<jsp:getProperty name="people" property="name"/></h1><br>
<h1>地址：<jsp:getProperty name="people" property="address"/></h1><br>
<h1>年龄：<jsp:getProperty name="people" property="age"/></h1><br>
<h1>类：<jsp:getProperty name="people" property="class"/></h1>
<hr>
<h1>通过\${}取对象属性</h1>
<h1>id： ${people.id}</h1><br>
<h1>姓名：${people.name}</h1><br>
<h1>地址：${people.address}</h1><br>
<h1>年龄：${people.age}</h1><br>
<hr>
<h1>通过<\%%>取对象属性</h1>
<h1>id： <%=people.getId()%></h1><br>
<h1>姓名：<%=people.getName()%></h1><br>
<h1>地址：<%=people.getAddress()%></h1><br>
<h1>年龄：<%=people.getAge()%></h1><br>
```

### 17：MVC(model view controller 模型视图控制器)三层架构

##### 17.1、原理图

![image-20230103161815860](img/image-20230103161815860.png)

##### 17.2、Web应用MVC原理图

​	![image-20230103163020298](img/image-20230103163020298.png)

- Model
  - 业务处理：业务逻辑(Service)
  - 数据持久层：CRUD(dao)

- View
  - 展示数据
  - 提供链接发起Service请求
  - 监听事件
- Controller(Servlet)
  - 接收用户请求（request，session）
  - 交给业务层处理对应的代码
  - 控制视图的跳转

### 18：Filter(过滤器)

- **来的请求过滤，回应则不过滤**

- 路径说明：

  ```java
  在Spring Boot中，/**和/*是URL模式匹配的表达式，用于配置过滤器的应用范围。
  
  /**：这是一种最广泛的URL模式匹配，表示匹配所有路径，包括多级路径。它会匹配以任意字符开头的路径，直到最后一个路径段，包括子路径和子目录。例如，/user, /user/profile, /user/profile/edit等都会匹配/**。
  
  /*：这是一种比较限定的URL模式匹配，表示匹配单级路径。它只匹配以斜杠(/)开头的路径的第一级路径段，不会匹配子路径和子目录。例如，/user可以匹配/*，但是/user/profile不会匹配/*。
  
  通常情况下，/**用于全局范围的过滤器配置，可以拦截所有的请求。而/*用于特定的路径或模块的过滤器配置，只拦截指定的一级路径。
  ```

  

##### 18.1、作用

- filter：过滤网站的数据

  ![image-20230103164808526](img/image-20230103164808526.png)

##### 18.2、编写过滤器

- 第一步实现过滤器接口，**注意如果是write的话需要指定type，outputStream则不需要，还有转型问题**

  ```java
  public class FilterDemo01 implements Filter {
      //初始化:在web服务器启动就初始化
      public void init(FilterConfig config) throws ServletException {
          System.out.println("filter初始化");
      }
      //销毁：在web服务器关闭时被销毁
      public void destroy() {
          System.out.println("filter销毁");
      }
      //主要方法:
       /*
           1：过滤器中代码，在过滤特殊请求的时候都会被执行
           2：必须让过滤器继续通行   doFilter(request, response);
        */
      @Override
      public void doFilter(ServletRequest request, ServletResponse response, FilterChain chain) throws ServletException, IOException {
          request.setCharacterEncoding("utf-8");
          response.setCharacterEncoding("utf-8");
          response.setContentType("text/html");
          System.out.println("过滤前");
          //这句必须要写，不然程序到这里就被拦截停止！，相当于一个链条(chain)，继续把这个请求，响应转发下去
          chain.doFilter(request, response);
          System.out.println("过滤后");
      }
  }
  ```

- 第二步，web.xml文件中配置过滤器

  ```xml
  <filter>
      <filter-name>f1</filter-name>
      <filter-class>com.xxl.filter.FilterDemo01</filter-class>
  </filter>
  <filter-mapping>
      <filter-name>f1</filter-name>
      <!--   <url-pattern>/*</url-pattern>表示当前项目路径下的所有servlet都过经过这个过滤器     -->
      <!--   <url-pattern>/demo01/demo01/*</url-pattern>表示demo01/demo01下的所有请求才会被过滤     -->
      <!--   也就是说 url-pattern就是Servlet的url-pattern,就是过滤请求路径  -->
      <url-pattern>/demo01/demo01</url-pattern>
  </filter-mapping>
  ```

### 19：监听器

##### 19.1、编写监听器

- 实现监听器接口

  ```java
  /**
   * @author:xxl
   * @date:2023/1/3
   * @ProjectDescription:    监听器例子：统计有多少个用户
   */
  public class ListenerDemo01 implements  HttpSessionListener {
  
      //监听session创建的时候
      @Override
      public void sessionCreated(HttpSessionEvent se) {
          System.out.println("session被创建了");
          ServletContext servletContext = se.getSession().getServletContext();;
          Integer people = (Integer)servletContext.getAttribute("people");
          //第一次重启服务器的时候会出现两个session同时存在，这是tomcat的启动、连接的的原因重新部署一下就行了
          System.out.println("sessionId:"+se.getSession().getId());
          if (people == null) {
              //第一次创建session
              servletContext.setAttribute("people",1);
          }else {
              people += people;
              servletContext.setAttribute("people",people);
          }
      }
      //监听session被销毁的时候
      @Override
      public void sessionDestroyed(HttpSessionEvent se) {
          System.out.println("session被销毁");
          ServletContext servletContext = se.getSession().getServletContext();;
          Integer people = (Integer)servletContext.getAttribute("people");
          if (people != null) {
              //第一次创建session
              people -= 1;
              servletContext.setAttribute("people",people);
          }else {
              people = 0;
              servletContext.setAttribute("people",people);
          }
      }
  }
  ```

- 在web.xml中配置

  ```xml
  <listener>
      <listener-class>com.xxl.listen.ListenerDemo01</listener-class>
  </listener>
  
  <!--  自动销毁  -->
  <session-config>
      <session-timeout>1</session-timeout>
  </session-config>
  ```

### 20：JDBC(java database connect java数据库连接)

##### 20.1、什么是jdbc

​	![image-20230104162838162](img/image-20230104162838162.png)

##### 20.2、需要的jar包

- java.sql

- javax.sql

- mysql-conneter-java连接驱动必须要导入

- 一般在maven中导入就够用了

  ```xml
  <!--数据库连接驱动(必须要导)-->
         <dependency>
             <groupId>mysql</groupId>
             <artifactId>mysql-connector-java</artifactId>
           	<!--8.0.31对应的数据库版本-->  
             <version>8.0.31</version>
         </dependency>
     </dependencies>
  ```

##### 20.2、环境搭建

- 连接数据库

  ```java
  String str = "jdbc:mysql://localhost:3306/jdbc_demo01?useUnicode=true&characterEncoding=utf-8"; //这个格式够用了
  url基本格式如下:
  连接地址+ssl连接关闭+字符集为utf-8+时区设置
  ```

  ```java
  //配置信息
  //characterEncoding=utf-8&useUnicode=true解决中文乱码
  String str = "jdbc:mysql://localhost:3306/jdbc_demo01?useUnicode=true&characterEncoding=utf-8";
  String username = "xxl";
  String password = "xxl123456";
  
  //1、加载驱动
  Class driver = Class.forName("com.mysql.cj.jdbc.Driver");
  //2.连接数据库  connection代表数据库
  Connection connection = DriverManager.getConnection(str, username, password);
  //3、创建statement    statement:向数据库发送sql语句(CRUD)   prepared(准备)Statement(预编译):向数据库发送sql语句(CRUD)
  Statement statement = connection.createStatement();
  //PreparedStatement preparedStatement = connection.prepareStatement();
  //4.编写sql语句
  String sql = "SELECT * FROM users;";
  //5.执行查询sql，返回一个resultSet(结果集)
  ResultSet execute = statement.executeQuery(sql);
  //必须要加上next
  while (execute.next()) {
      System.out.println("id:"+execute.getObject("id"));
      System.out.println("username:"+execute.getObject("username"));
      System.out.println("pwd:"+execute.getObject("pwd"));
      System.out.println("email:"+execute.getObject("email"));
      System.out.println("birthday:"+execute.getObject("birthday"));
      System.out.println("---------------------");
  }
  //关闭连接，释放资源(一定要做)，先开后关
  execute.close();
  connection.close();
  ```

- **增删查改**

  ```java
   //4.编写sql语句
          String sqlCheck = "SELECT * FROM users;";   //查询一张表  查
          String sqlDelete = "DELETE FROM users WHERE id = 20;";   //删除表中数据  删
          String sqlInsert = "INSERT INTO users(id,username,pwd,email,birthday)\n" +
                  "VALUES(20,'xxl1','xxl123456','3578144921@qq.com','20030711');";   //插入   增
           String sqlUpdate = "UPDATE `account` SET `balance` = 2000.0  WHERE `id` = 1; "; //改
  //执行sql语句，返回一个受影响的行数(假如没有成功，就0行受影响，插入一条数据，就1行受影响，这点在sqlyog中比较明显)
          int i = statement.executeUpdate(sqlInsert);//用于增删改
          if (i > 0) {
              System.out.println("删除成功");
          }
  ```

##### 20.3、JDBC固定步骤有两种

- 第一种

1. 加载驱动(不需要了)
2. 连接数据库
3. 创建向数据库发送sql语句的对象
4. 编写sql
5. 执行sql
6. 关闭连接，先开后关

```java
//1.加载驱动
//2.连接数据库
Connection connection = DriverManager.getConnection(url, username, password);
//3.创建发送sql对象
Statement statement = connection.createStatement();
//4。编写sql语句
String sqlInsert = "insert into users(id,username,pwd,email,birthday) value (25,'xxl6','xxl123456','3578144921@qq.com','20030711')";   //插入
//5.执行sql
int i = statement.executeUpdate(sqlInsert);
if (i > 0) {
    System.out.println("执行成功");
}
//5.关闭连接
statement.close();
connection.close();
```

- 第二种

1. 加载驱动
2. 连接数据库
3. 编写sql语句
4. 预编译
5. 执行sql语句
6. 关闭连接

```java
//配置信息
//配置信息
//characterEncoding=utf-8&useUnicode=true解决中文乱码
String url = "jdbc:mysql://localhost:3306/jdbc_demo01?useUnicode=true&characterEncoding=utf-8";
String username = "xxl";
String password = "xxl123456";

//1.加载驱动
//2.连接数据库
Connection connection = DriverManager.getConnection(url, username, password);
//3.编写sql语句
String sqlInsert = "insert into users(id,username,pwd,email,birthday) value (24,'xxl5','xxl123456','3578144921@qq.com','20030711')";   //插入
//4.预编译
PreparedStatement preparedStatement = connection.prepareStatement(sqlInsert);
//5.执行sql语句
int i = preparedStatement.executeUpdate();
if (i > 0) {
    System.out.println("插入成功");
}
//6.关闭连接
preparedStatement.close();
connection.close();
```

##### 20.4、**占位符**

```java
//配置信息
//characterEncoding=utf-8&useUnicode=true解决中文乱码
String url = "jdbc:mysql://localhost:3306/jdbc_demo01?useUnicode=true&characterEncoding=utf-8";
String username = "xxl";
String password = "xxl123456";

//1.连接数据库
Connection connection = DriverManager.getConnection(url, username, password);
//2.编写sql语句
String sqlDelete = "DELETE FROM users WHERE id  = ?;";  //占位符从1开始下标，这就是预编译的好处
//3.预编译
PreparedStatement preparedStatement = connection.prepareStatement(sqlDelete);
preparedStatement.setInt(1,20);  //等同于setObject(1,20)就是效率慢点
//4.执行sql语句
int i = preparedStatement.executeUpdate();
if (i > 0) {
    System.out.println("删除成功");
}
//5.关闭连接
preparedStatement.close();
connection.close();
```

##### 20.5、事务：为了数据安全

- **事务流程**

  > 1. START TRANSACTION 或 BEGIN 开启一个新事务
  > 2. COMMIT 提交当前事务，使其永久化。
  > 3. ROLLBACK 回滚当前事务，取消其变更
  > 4. SET autocommit 为当前会话启用或者禁用默认的自动提交模式

- **事务：要么都成功，要么都失败。ACID原则保证数据的安全**

> 数据库事务ACID四大特点：
>
> 1. 原子性(Atomicity): 原子性是指事务包含的所有操作要么全部成功，要么全部失败回滚
>
> 2. 一致性(Consistency): 一致性是指事务必须使数据库从一个一致性状态变换到另一个一致性状态。例如，银行账户A和B分别有存款5000，一共10000，无论A转账给B，还是B转账给A，两个账户的总额总是为10000
> 3. 隔离性(Isolation): 隔离性是当多个用户并发访问数据库时，比如操作同一张表时，数据库为每一个用户开启的事务，不能被其他事务的操作所干扰，多个并发事务之间要相互隔离。
> 4. 持久性(Durability): 持久性是指一个事务一旦被提交了，那么对数据库中的数据的改变就是永久性的，即便是在数据库系统遇到故障的情况下也不会丢失提交事务的操作。

- **案例**

  > 重要的三句话：
  >
  > 1. ​	connection.setAutoCommit(false);  //开启事务
  > 2. ​    connection.commit(); //提交事务
  > 3. ​    connection.rollback();  //出现异常通知数据库，回滚事务

```java
  Connection connection = null;
       try{
           //配置
           //配置信息
           //characterEncoding=utf-8&useUnicode=true解决中文乱码
           String url = "jdbc:mysql://localhost:3306/jdbc_demo01?useUnicode=true&characterEncoding=utf-8";
           String username = "xxl";
           String password = "xxl123456";
           //1.创建
            connection = DriverManager.getConnection(url, username, password);
           connection.setAutoCommit(false);  //开启事务,出现错误不会执行sql语句
           //2.写sql语句
           String sqlUpdate = "UPDATE `account` SET `balance` = `balance` - 500  WHERE `id` =1;";
           //3.预编译并执行
           connection.prepareStatement(sqlUpdate).executeUpdate();

            /*这里有一个错误，如果不开启事务,sql语句还是会执行成功，不符合数据的安全性，就像取钱一样：你取钱成功了，机子出现错误没扣你账户钱*/
           int i = 1/0;

           //4.关闭连接在final中

           //connection.commit(); //提交事务
       }catch (Exception e){
           System.out.println(e);
           //出现异常通知数据库，回滚事务
           connection.rollback();  
       }finally {
            connection.close();
       }
```

### 21：servlet更换欢迎界面

- 在web.xml文件中配置如下

  ```xml
  <!-- 更换首页文件   -->
      <welcome-file-list>
          <!--     路径默认从webapp下开始   -->
          <welcome-file>login.jsp</welcome-file>
      </welcome-file-list>
  ```


### 22：servlet小技巧

- 不用配置web.xml用注解

  ```java
  @WebServlet(name = "LoginServlet", value = "/longin")
  //name  == <servlet-name>LoginServlet</servlet-name>
  //value == <url-pattern>/login</url-pattern>
  相当于
  <!--  登录servlet  -->
      <servlet>
          <servlet-name>LoginServlet</servlet-name>
          <servlet-class>com.xxl.servlet.LoginServlet</servlet-class>
      </servlet>
      <servlet-mapping>
          <servlet-name>LoginServlet</servlet-name>
          <url-pattern>/login</url-pattern>
      </servlet-mapping>
  
  ```


### 23：文件上传(详细内容见blog中文件上传)

##### 23.1、需要相关依赖

```xml
<!--流相关的工具类-->
       <dependency>
           <groupId>commons-io</groupId>
           <artifactId>commons-io</artifactId>
           <version>2.11.0</version>
       </dependency>
<!--文件上传依赖，为什么要用：处理上传的文件一般通过流来获取，request.getInputStream(),这种原生态的上传流处理起来十分麻烦，因此需要一个工具类-->
       <dependency>
           <groupId>commons-fileupload</groupId>
           <artifactId>commons-fileupload</artifactId>
           <version>1.4</version>
       </dependency>
```

##### 23.1、文件上传的注意事项(上传文件的依赖性)

1. 保证安全，上传的文件的要放在无法访问的目录下，比如web-inf目录
2. 为防止文件覆盖性，要给上传的文件一个唯一的文件名(时间戳，uuid，位运算，-md5算法)
3. 要限制文件上传的大小
4. 可惜限制文件类型

### 24：邮件发送

##### 24.1、邮件发送原理

​	![image-20230123000234280](img/image-20230123000234280.png)

##### 24.2、相关的协议

- **发送邮件：SMTP协议**
- **接受邮件：POP3协议**
- **附件：mime协议**

##### 24.3、相关的依赖

```xml
<!--      邮件依赖 -->
       <dependency>
           <groupId>jakarta.mail</groupId>
           <artifactId>jakarta.mail-api</artifactId>
           <version>2.1.1</version>
       </dependency>
<!--     邮件激活  -->
       <dependency>
           <groupId>jakarta.activation</groupId>
           <artifactId>jakarta.activation-api</artifactId>
           <version>2.1.1</version>
       </dependency>
	   <dependency>
           <groupId>jakarta.mail</groupId>
           <artifactId>jakarta.mail-api</artifactId>
           <version>2.1.0</version>
       </dependency>
       <!-- https://github.com/eclipse-ee4j/angus-mail -->
       <dependency>
           <groupId>org.eclipse.angus</groupId>
           <artifactId>jakarta.mail</artifactId>
           <version>1.0.0</version>
       </dependency>
```

##### 24.5、简单邮件(不带附件，纯文本)

```java
public void easyMail() throws IOException, GeneralSecurityException, MessagingException {
        Properties properties = new Properties();
        //固定写法
        properties.setProperty("mail.host","smtp.qq.com");  //设置qq邮件服务器
        properties.setProperty("mail.transport","smtp");   //邮件发送协议
        properties.setProperty("mail.smtp.auth","true");//需要验证用户名密码

        //关于qq邮箱还要设置ssl加密,大厂都这样
        MailSSLSocketFactory mailSSLSocketFactory= new MailSSLSocketFactory();
        mailSSLSocketFactory.setTrustAllHosts(true);
        properties.put("mail.smtp.ssl.enable", "true");
        properties.put("mail.smtp.ssl.socketFactory", mailSSLSocketFactory);


//1、创建session对象，这个对象是指在发送邮件的整个过程
        //qq才有的
        Session session = Session.getDefaultInstance(properties, new Authenticator() {
            @Override
            protected PasswordAuthentication getPasswordAuthentication() {
                //发件人，授权码
                return new PasswordAuthentication("3578144921@qq.com","prkxrgpngrtccgih");
            }
        });

        //开启debug模式监听session
        session.setDebug(true);
//2、通过session对象拿到transport对象
        Transport transport = session.getTransport();
//3、连接上邮件服务器
        //服务器   用户名  授权码(qq设置中找)
        transport.connect("smtp.qq.com","3578144921@qq.com","prkxrgpngrtccgih");
//4、创建邮件
        MimeMessage mimeMessage = new MimeMessage(session);
        //设置邮件标题主题
        mimeMessage.setSubject("邮件学习");
        //发件人
        mimeMessage.setFrom(new InternetAddress("3578144921@qq.com"));
        //收件人
        mimeMessage.setRecipient(Message.RecipientType.TO,new InternetAddress("1499476208@qq.com"));
        //邮件的内容
        mimeMessage.setContent("<h2 style=\"color: red\">正在学习邮件。。。</h2>","text/html;charset=utf-8");
//5、接收邮件
        transport.sendMessage(mimeMessage,mimeMessage.getAllRecipients());
        transport.close();
    }
```

##### 24.6、复杂邮件(带附件，内容中嵌入照片)

- MimeBodyPart类(组成邮件的某个部分)<MimeMultipart类（相当于整个邮件对象）

![image-20230123114958199](img/image-20230123114958199.png)

```java
 public void difficultyMail() throws GeneralSecurityException, MessagingException {
        Properties properties = new Properties();
        //固定写法
        properties.setProperty("mail.host","smtp.qq.com");  //设置qq邮件服务器
        properties.setProperty("mail.transport","smtp");   //邮件发送协议
        properties.setProperty("mail.smtp.auth","true");//需要验证用户名密码
        //关于qq邮箱还要设置ssl加密,大厂都这样
        MailSSLSocketFactory mailSSLSocketFactory= new MailSSLSocketFactory();
        mailSSLSocketFactory.setTrustAllHosts(true);
        properties.put("mail.smtp.ssl.enable", "true");
        properties.put("mail.smtp.ssl.socketFactory", mailSSLSocketFactory);
//1、创建session对象，这个对象是指在发送邮件的整个过程-------------------------
        //qq才有的
        Session session = Session.getDefaultInstance(properties, new Authenticator() {
            @Override
            protected PasswordAuthentication getPasswordAuthentication() {
                //发件人，授权码(密码)
                return new PasswordAuthentication("3578144921@qq.com","prkxrgpngrtccgih");
            }
        });
        //开启debug模式监听session
        session.setDebug(true);
//2、通过session对象拿到transport对象--------------------------------------
        Transport transport = session.getTransport();
//3、连接上邮件服务器------------------------------------------------------
        //服务器   用户名  授权码(qq设置中找)
        transport.connect("smtp.qq.com","3578144921@qq.com","prkxrgpngrtccgih");
//4、创建邮件-------------------------------------------------------------
        MimeMessage mimeMessage = new MimeMessage(session);
        //准备图片
        MimeBodyPart img = new MimeBodyPart();
        String path = "D:\\Program Files (x86)\\idea\\IDEAproject\\javaweb02-maven\\servlet-09\\src\\main\\resources\\img\\avatar.jpg";
        DataHandler dataHandler = new DataHandler(new FileDataSource(path));
        img.setDataHandler(dataHandler); //在主体中放入图片数据
        img.setContentID("girl.jpg");
        //邮件的内容
        MimeBodyPart textBody = new MimeBodyPart();
        String text = "<h2 style=\"color: red\">正在学习邮件。。。</h2><hr/><img src='cid:girl.jpg'/>";
        //文件节点的设置一定要是setContent()
        textBody.setContent(text,"text/html;charset=UTF-8");
        //将文本节点和图片节点混合在一起
        MimeMultipart mimeMultipart = new MimeMultipart();
        mimeMultipart.addBodyPart(img);
        mimeMultipart.addBodyPart(textBody);
        mimeMultipart.setSubType("related");
        //设置到邮件中保存修改
        mimeMessage.setContent(mimeMultipart);
        mimeMessage.saveChanges();
        //设置邮件标题主题
        mimeMessage.setSubject("困难邮件学习");
        //发件人
        mimeMessage.setFrom(new InternetAddress("3578144921@qq.com"));
        //收件人
        mimeMessage.setRecipient(Message.RecipientType.TO,new InternetAddress("1499476208@qq.com"));
//5、接收邮件----------------------------------------------------------------
        transport.sendMessage(mimeMessage,mimeMessage.getAllRecipients());
        transport.close();

    }
```

