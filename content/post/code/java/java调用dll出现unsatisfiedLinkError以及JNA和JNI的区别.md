---
title: Java调用dll出现unsatisfiedLinkError以及JNA和JNI的区别
description: JNA和JNI的区别
# 默认url路径是title如果不写slug
slug: jna & jni
date: 2025-06-10 13:57:10+0000
toc: true
categories:
  - java-category
tags:
  - jni
  - jna
  - java
  - dll
keywords:
  - jni
  - jna
  - java
  - dll
id: ade8c563-648d-4e61-97bc-0ef0721ce8af
---
## UnsatisfiedLinkError

在对接硬件设备中，我们会遇到使用 java 调用 dll文件 的情况，此时大概率出现`UnsatisfiedLinkError`链接错误，原因可能有如下几种
1. 类名错误
2. 包名错误
3. 方法名参数错误
4. 使用 JNI 协议调用，结果 dll 未实现 JNI 协议需要使用 JNA 调用

这里需要特地说一下 JNI 和 JNA 是什么以及区别

## JNI & JNA

### JNI(Java Native Interface)
> Java 原生接口：由 Java 官方提供的一种机制，用来调用 C/C++ 编写的函数。

特点在于 Java 和 C/C++ 也需要遵循这个规范,示例如下

**C++代码:** 其中JNIExport和JNICALL就是规范的一部分,其中方法命名格式如下`Java_<包名_类名>_<方法名>`对应的 Java 调用时也应该相同

```C++
extern "C" JNIEXPORT jint JNICALL
Java_com_example_JniDemo_add(JNIEnv* env, jobject obj, jint a, jint b) {
    return a + b;
}
```

**Java 代码:** 同样的在调用 dll 方法中你的类名和包名、方法名都需要和 dll 中一致

```java
package com.example; // 包名对应 dll 方法中的包名
public class JniDemo {
    static {
        System.loadLibrary("native_lib"); // 加载 DLL
    }

    public native int add(int a, int b); // 声明 native 方法

    public static void main(String[] args) {
        System.out.println(new JniDemo().add(3, 4)); // 输出 7
    }
}

```

### JNA(Java Native Access)
> Java 开发的工具库，无需 JNI 编码，即可调用 DLL/so 中的 C 函数。

示例如下：

**C++代码: 无需实现 JNI 规范**

```C++
extern "C" __declspec(dllexport)
int add(int a, int b) {
    return a + b;
}
```

**Java代码：使用 JNA 直接调用，需要导入 JNA 包**

```java
import com.sun.jna.Library;
import com.sun.jna.Native;

public interface NativeLib extends Library {
    NativeLib INSTANCE = Native.load("native_lib", NativeLib.class);
    int add(int a, int b);
}

public class JnaDemo {
    public static void main(String[] args) {
        System.out.println(NativeLib.INSTANCE.add(3, 4)); // 输出 7
    }
}
```

## 总结

- 如果厂商给你 普通 C/C++ DLL（非 JNI 风格）：✅ 首选 JNA
- 如果厂商只提供了带 JNI 的 DLL：✅ 只能用 JNI
- 如果你自己控制底层 DLL、同时关注性能：✅ JNI 更灵活
- 如果你要快速完成对接、项目周期紧：✅ JNA 开发效率极高