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
    - Servlet
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

##### 验证码实现

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
  - 重定向：url地址栏会变化
  - 转发：url地址栏不会发生变化
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  

