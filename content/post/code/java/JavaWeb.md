---
title: JavaWeb
description: 一遍文章让你快速入门JavaWeb
slug: JavaWeb
date: 2024-08-08 00:00:00+0000
toc: true
categories:
    - db-category
    - java-category
tags:
    - JavaWeb
    - SQL
    - Tomcat
    - Maven
    - HTTP
    - Servlet
    - Cookie
    - Session
keywords:
  - Java
  - JavaWeb
  - SQL
  - Tomcat
  - Maven
  - HTTP
  - Servlet
  - Cookie
  - Session
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

  ![image-20221129140528956](img/javaweb/image-20221129140528956.png)

- 在bin文件内点startup.bat

  ![image-20221228120857316](img/javaweb/image-20221228120857316.png)

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

    ![image-20221129141843038](img/javaweb/image-20221129141843038.png)

    2. 没有：去dns服务器找，能找到就返回，找不到就返回找不到

    ![img](img/javaweb/L377CV890TBGA{904_F26.png)

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

  ![image-20221228164932271](img/javaweb/image-20221228164932271.png)

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

![image-20221228172129655](img/javaweb/image-20221228172129655.png)

在设置中设置自动下载源代码

![image-20221228182122799](img/javaweb/image-20221228182122799.png)

**Tip：** 以上配置如不想要每个项目都配置一次，则在在IDEA默认全局配置设置

### IDEA配置Tomcat

1. 点击当前文件进行配置

    ![image-20221228190143133](img/javaweb/image-20221228190143133.png)

2. 配置上下文路径映射，也就是url地址会显示

    ![image-20221228190810818](img/javaweb/image-20221228190810818.png)

    ![image-20221228191139999](img/javaweb/image-20221228191139999.png)

3.  启动Tomcat，默认首页是index.jsp

    ![image-20221228191236459](img/javaweb/image-20221228191236459.png)

4.  项目的结构

    ![微信图片_20221228191616](img/javaweb/微信图片_20221228191616.jpg)

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

### Maven子摸快

```xml
<modules>
    <!-- 子摸快,servlet01对应Pom文件中artifactId名字   -->
    <module>servlet01</module>
</modules>
 ```

子目录会有父目录的AGV

```xml
<parent>
    <artifactId>javaweb02-maven</artifactId>
    <groupId>com.xxl</groupId>
    <version>1.0-SNAPSHOT</version>
</parent>
 ```

**父模块可以用来管理依赖，子摸快可以直接使用**

## Servlet

1.  Servlet就是sun公司**开发动态Web的一门技术**
2. Sun公司在这些API提供了一个接口就做：Servlet，如果要开发一个Servlet程序，需要两个步骤
    - 编写一个类实现Servlet接口
    - 把开发好的Java类部署到web服务器中，实现了Servlet接口的程序叫做**Servlet**
3. **Servlet是单例模式**

### Servlet原理

- Servlet是由web服务器调用，web服务器在收到浏览器请求之后，会：

    ![image-20221229132501759](img/javaweb/image-20221229132501759.png)

- 简图

    ![image-20221229133758829](img/javaweb/image-20221229133758829.png)

### ServletContext

Web容器在启动的时候，他会为每个web程序都创建一个对应的ServletContext对象，他代表当前的web应用

#### 共享数据 

**共享数据：** 因为一个web应用只有一个上下文，所有的servlet都可以拿到这个上下文对象，所以数据可以共享


![img](img/javaweb/C9C66AC0E5979A71CD52AA77490DDD70.png)


1. **设置数据**

    ```java
    //设置数据
    String username = "xxl";  
    ServletContext servletContext = req.getServletContext();   
    servletContext.setAttribute("username",username);
    
    String text = "<h1>开始设置数据</h1>";
    //流不需要设置type和encoding
    ServletOutputStream outputStream = resp.getOutputStream();
    outputStream.write(text.getBytes(),0,text.getBytes().length);
    outputStream.close();
    ```

    ![image-20221229165933759](img/javaweb/image-20221229165933759.png)

2. **拿到数据**

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

    ![image-20221229165955253](img/javaweb/image-20221229165955253.png)

#### 获取初始化参数

```java
ServletContext servletContext = this.getServletContext();
String url = servletContext.getInitParameter("url");//这个就是获得web.xml中设置的context-param参数
String text = "<h1>" + url + "</h1>";
ServletOutputStream outputStream = resp.getOutputStream();
outputStream.write(text.getBytes(),0,text.getBytes().length);
outputStream.close();
```

![image-20221229172428454](img/javaweb/image-20221229172428454.png)

####  转发和重定向

##### 转发

**转发：当前文件地址，转发带参数**

```java
ServletContext servletContext = this.getServletContext();
RequestDispatcher requestDispatcher = servletContext.getRequestDispatcher("/demo01");  //还没开始转发
requestDispatcher.forward(req, resp);  //开始转发
```

##### 重定向

**重定向：得带上项目地址，相当于之前重新发起请求，不能携带之前的request中参数**

```java  
//getContextPath  项目地址不带/  
resp.sendRedirect(req.getServletContext().getContextPath()+"/success/success.jsp");   重定向  
```  



![image-20221229174355664](img/javaweb/image-20221229174355664.png)



#### 读取资源文件

- 发现问题在java目录下的properties文件识别不了，解决方案：在Maven篇章写了
- 相对路径：target\servlet-02\WEB-INF\classes，俗称classpath

**读取配置文件**

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

#### 路径问题

```java
this.getServletContext().getRealPath("/WEB-INF/upload")
// 等于tomcat服务器所在的位置的webapps中 E:\Program Files (x86)\TomcatAndMaven\apache-tomcat-10.0.27-windows-x64\apache-tomcat-10.0.27\webapps\servlet_09\WEB-INF\upload\
```

### HttpServletRequest

HttpServletRequest代表客户端的请求，用户通过http协议访问服务器，http请求中的所有信息都会被封装到HttpServletRequest对象中，通过这个对象的方法可以获得客户端的所有信息

#### 常用方法

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

#### 简单示例

简单模拟写一个登录页

**后端**

```JAVA
//处理请求
String username = req.getParameter("username");
String password = req.getParameter("password");
System.out.println("用户名：" + username + ",密码：" + password);

//登录成功之后，重定向
//重定向一定要记住，要当前的项目路径+页面路径
resp.sendRedirect("/servlet02/loginSuccess.jsp");
```

**前端**

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

##### 获取参数 & 请求转发

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
### HttpServletResponse

响应，web服务器接收端客户端的http请求，针对这个请求，分别创建一个代表请求的HttpServletRequest对象和一个代表响应的HttpServletResponse的对象。
    - HttpServletRequest可以获取请求过来的参数
    - HttpServletResponse可以在这个对象加一些响应的信息

#### 常用方法

- 负责向浏览器发送数据的方法

```java
public ServletOutputStream getOutputStream() throws IOException;   字节流
public PrintWriter getWriter() throws IOException;   字符流
```  

负责向浏览器发送的响应头的方法

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

#### 响应码

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

#### 简单示例

##### 下载文件

```java
//文件路径
String path = "D:\\Program Files (x86)\\idea\\IDEAproject\\javaweb02-maven\\servlet-02\\src\\main\\java\\com\\xxl\\servlet\\response\\女孩.jpeg";
//上下文拿到的真实路径:  E:\Program Files (x86)\TomcatAndMaven\apache-tomcat-10.0.27-windows-x64\apache-tomcat-10.0.27\webapps\servlet02\迪丽热巴.png
//图片不可能在tomcat下面
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

##### 验证码

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

##### **重定向**

```java
//路径要注意还要加上项目路径
resp.sendRedirect("/servlet02/code");  
```

#### 面试题

请你聊聊重定向和转发的区别: 
- 相同点
    - 页面都会跳转
- 不同点
  - 重定向：url地址栏会变化，不会携带原请求的请求参数
  - 转发：url地址栏不会发生变化，会携带原请求的请求参数

## Cookie

### 会话

- **重点：除了服务器创建的cookie，自己增加的cookie只会在你response回去的那个页面（详细信息见下面图解），也就是说转发会携带请求和cookie，而重定向不会**

- **cookie是有作用范围，范围的大小决定请求的时候能带哪些cookie所以有的时候明明设置了cookie却无法生效，看下图**

  ![image-20230404143945057](img/javaweb/image-20230404143945057.png)

- 用户打开浏览器，点击了很多链接，访问多个web资源，然后关闭浏览器，这个过程可以称之为会话

- 一次会话是指： 好比打电话，当A打给B，电话接通了 会话开始，持续到会话结束。 浏览器访问服务器，就如同打电话，浏览器A给服务器发送请求，访问web程序，该次会话就开始，其中不管浏览器发送了多少请求 ，都为一次会话，直到浏览器关闭，本次会话结束。

    ```java
    // 解决ajax跨域导致session不一致的问题，由于sessionId是存在cookie,而每次获取getSession()
    // 都会通过cookie中的sessionId来获取session,如果没有就会创建一个新的session，然后把sessionId存在cookie中
    // 把cookie中的sessionId给下一个请求，失败因为跨域原因导致cookie崩创建
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
    ```

### 有状态会话

- 第一次去某个网站然后登录，之后会给你标记，下次来的时候，网站识别到这个标记，知道你来过，所以就不用重新登录了

### 保存会话的两种技术

- **cookie**：客户端技术 ，存的数据比较少
- **session**：服务器技术，利用这个技术，可以保存用户的会话信息，可以把数据或者信息放在session中

### Cookie的使用方法

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

  ```java
    编码：URLEncoder.encode();
    解码： URLDecoder.decode();
    ```

## Session

- **每个人获取的session都不同，只要不是在同一个浏览器**

- **session是存在服务器上，cookie是存在浏览器(每次请求会携带当前页的所有cookie)，session对象在服务器默认存活时间未30分钟**

- 对session来说也是一样的，除非程序通知服务器删除一个session，否则服务器会一直保留。

  > 所以浏览器从来不会主动在关闭之前通知服务器它将要关闭，因此服务器根本不会有机会知道浏览器已经关闭，之所以会有这种错觉，是大部分session机制都使用会话cookie来保存session id，而关闭浏览器后这个session id就消失了，再次连接服务器时也就无法找到原来的session
  > 恰恰是由于关闭浏览器不会导致session被删除，迫使服务器为session设置了一个失效时间，一般是30分钟也就是说这个session可以一直存在，只要服务器不刷新，或者设置一个存话时间(这样浏览器关闭也会存在)，当距离客户端上一次使用session的时间超过这个失效时间时，服务器就可以认为客户端已经停止了活动，才会把session删除以节省存储空间

- 服务器刷新，浏览器关闭/刷新，session就没了，不适合存数据

- cookie可以存在浏览器，只要还在cookie存活期cookie就一直存在。

- **session和cookie关系**

  ```text
  场景：通过session里用户判断是否登录
      设置session时间(是这个session对象在服务器的存活时间，一般为30分钟)：如果关闭浏览页再打开Session中还是存着用户信息的.关闭浏览器再打开就要重新登录，
      （注意session是可以跨同个服务器的多个页面这就是保存用户信息的核心(它存在web上下文中)，cookie则不可以，只能在某一页，但是cookie
      是存在请求中的，也就是每次请求都会携带当前页的cookie）
      session是是通过cookie中存的sessionId获得的，但保存sessionId的cookie是服务器自己创建的，一旦关闭浏览器
      再次打开页面就会重新创建cookie同时session也会变化，(想要完成“记住我”这种功能，需要cookie和session一起合作)
      所以需要设置cookie存活期，浏览器默认创建的cookie存活期为一次会话，也就是浏览器不够就心
  ```

### 什么是Session

- 服务器会给，会给每一个用户(浏览器某个app)，创建一个Session对象
- 一个web应用只有一个session并且独占一个浏览器（**也就是session是唯一的**），也就是换了一个浏览器也有session只是不一样，但这个session独占这个浏览器。只要浏览器没有关闭，这个Session就存在。这一点跟cookie一样

### Session和Cookie的区别

- cookie：是把用户的数据写给用户的浏览器，浏览器保存(可以保存多个)
- session：把用户的数据写给用户独占的session中，服务端保存，**session对象由服务器创建**

### Session用法

**存数据**

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

//这个session是否是新创建的if (session.isNew()) {resp.getWriter().write("<h1>session是新创建的</h1>");
}else {
    //只会走这一步(根据浏览器来，chrome就会走上面的)，因为打开那个页面就自动会创建一个会话session,只要访问就会产生一个sessionresp.getWriter().write("<h1>session不是新创建的，id："+session.getId()+"</h1>");
}
//取数据
String name = (String)session.getAttribute("name");
System.out.println(name);
//session创建的时候做了什么
/*Cookie cookie = new Cookie("JSESSIONID", session.getId());
 resp.addCookie(cookie);*/
 ```

**servlet与servlet之间的通信用session**

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

**手动注销session以及session的存的数据**

```java
HttpSession session = req.getSession();
//注销session中所存的数据
session.removeAttribute("name");
//注销掉整个session
session.invalidate();
 ```

**自动注销session在配置文件(web.xml)中设置session存活时间**

```xml
<!--  session配置  -->
<session-config>
    <!--     设置存活时间，以分钟为单位 设置在服务器的存活时间  -->
    <session-timeout>1</session-timeout>
</session-config>
 ```

### 使用场景

- 保存一个登录用户的时间
- 购物车信息  


### 12：多个用户如何共享数据

##### 12.1、多个用户在同一个web应用如何共享数据

- **只能用ServletContext**，cookie不行，session也不行
    - session是因为每个用户都有自己的一个唯一的sessionId
    - cookie是因为无法做到，是因为需要提交cookie  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  

