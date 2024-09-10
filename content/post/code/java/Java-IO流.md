---
title: Java IO
description: IO流用于处理数据传输，如读/写文件
# 默认url路径是title如果不写slug
slug: Java-IO流
date: 2024-08-28 16:06:47+0000
toc: true
categories:
  - java-category
tags:
  - IO
keywords:
  - IO
---

## 文件

- 保存数据的地方
- 文件流
    - **输入流就是把磁盘(文件，网络)的数据读入Java程序中**
    - **输出流就是把Java的内存上的数据读到磁盘(文件，网络)上**
    - 输入流用于从目标(文件，磁盘，网络)读取数据到Java程序，输出流是把Java程序写的数据向目标(文件，磁盘，网络)写入。

![image-20221210152954577](img/io/image-20221210152954577.png)

### 文件创建

#### 完整路径

```java
public void createFile1() throws IOException {
  String path = "D:\\Program Files (x86)\\idea\\IDEAproject\\HELLOWORLD_MYTEST\\src\\newknowledge\\iostream\\file1.txt";
  File file = new File(path);
  file.createNewFile();   //重点是这个方法createNewFile();
  System.out.println("文件创建成功");
}
```

#### 父目录子文件


```java
public void createFile2() throws IOException {
  String parent = "D:\\";   //父目录
  File file1 = new File(parent);   //就是创建个文件对象
  //子路径
  String path = "Program Files (x86)\\idea\\IDEAproject\\HELLOWORLD_MYTEST\\src\\newknowledge\\iostream\\file2.txt";
  File file = new File(file1,path);   //这个是创建文件对象-->在内存中
  file.createNewFile();   //这句才是生成文件----->生成在硬盘中
  System.out.println("文件创建成功");
}
```

### 文件操作

```java
//先创建文件对象
File file = new File("D:\\Program Files (x86)\\idea\\IDEAproject\\HELLOWORLD_MYTEST\\src\\newknowledge\\iostream\\file1.txt");
File file = new File(String path);
file.delete() //返回是boolean值，删除目录，文件都可以
file.mkdir()  //创建一级目录。返回boolean    
file.mkdirs()  //创建多级目录。返回boolean 
System.out.println("文件名字：" + file.getName());        
System.out.println("文件绝对路径：" + file.getAbsolutePath());        
System.out.println("目标文件文件的父目录：" + file.getParent());        
System.out.println("文件大小：" + file.length());        
System.out.println("文件是否存在：" + file.exists());        
System.out.println("文件是否是一个文件：" + file.isFile());        
System.out.println("文件是否是一个目录：" + file.isDirectory());        
```

## IO流分类

![image-20221226200113595](img/io/image-20221226200113595.png)


![image-20221219233927406](img/io/image-20221219233927406.png)


- **字节流**

    - 输入流（InputStream）
    - 输出流（OutputStream）

- **字符流(不要读取二进制文件(声音，视频.....)会损坏文件)**

    - 输入流(reader)
    - 输出流（writer）

- **节点流（底层）**

    - 从一个数据源(存放数据的地方)的地方**读写**数据流也就是，也就是说读写数据的过程
    - 它是一个大的方向

- **处理流/包装流**

    - 处理流>节点流>输入输出流(字符、数组、字节)
    - 建立在节点流之上，提供更为强大的读写能力，也更加灵活，其中用了修饰器模式
    - 各个处理流有一个父类的引用，也就是说它就可以包装这个父类的引用
    - 构造器需要一个节点流就是处理流

## 序列化(写)和反序列化(读)

- 主要用到的流：ObjectOutputStream和ObjectInputStream

- **序列化**：保存数据时是保存**数据的值**和**类型**

- **反序列化**：恢复数据时恢复**数据的值**和**数据类型**

- 让某个对象可以序列化就必须要实现两个接口的其中一个

    - Serializable：标记接口没有任何方法，推荐使用
    - Externalizable

- 反序列化时**注意顺序**一定要跟序列化顺序一样

- transient：防止变量被序列化只能用在**变量上**

    - 序列化时默认所有属性都能被序列化除了**static**和**transient**

  ```
  //这个代表版本号，也就是说假如这个类加了什么(比如属性)序列化时不会认为这是新的类，只会认为就是这个类升级了
  //网络传输的东西都需要序列化，因此需要一个唯一的标记号，序列化的serialVersionUID就是做这样的事
  private  static final long serialVersionUID = 1L;  //序列化版本可以自定义
  ```

- 序列化对象时，里面的**属性(自定义类也需要)** 也需要实现Serializable接口
- 序列化**可继承**，父类实现了Serializable接口，子类也就相当于实现了

## 标准输入输出流

- System.in标准输入、System.out标准输出
- 相关的流
    - InputStream   =  键盘
    - PrintStream   =  显示器

## 转换流

- 目的：把**字节流转换(包装)字符流**，解决不同的编码问题
- 相关的流：InputStreamReader和OutputStreamWriter他俩有一个共同的特点就是可以设置字符集
    - InputStreamReader是Reader子类
    - OutputStreamWriter是Writer的子类

## 打印流

- 相关的流：PrintStream和PrintWriter
    - PrintStream
      - setOut()切换输出位置(可以是文件)
- 打印流只有**输出（写）** 默认是输出到控制台(显示器)

## Properties

- `Properties`用于读写配置文件**.properties**文件
- 配置文件的格式：键=值，不能有空格，不用双引号默认类型是String

  ![image-20221227153900048](img/io/image-20221227153900048.png)




## IO小知识

### UTF-8编码下中英文大小

```text
1中文字符（word）= 3 byte（字节）  = 24bit（位）    2的24次方变化
1英文字符/1个数字(word)  = 1 byte（字节）  = 8bit（位）    0000000000000000--->1111111111111111 2的8次方变化
0/1就是一位
其他编码下中英文各占2和3个字符
```

### 内存的进制

```text
  8bit(位)=1Byte(字节)     36,864字节  byte
  1024Byte(字节)=1KB	   36,864/1024 = 36kb
  1024KB=1MB				36kd/1024 = 0.03m   
  1024MB=1GB 				
  1024GB=1TB  
  ```