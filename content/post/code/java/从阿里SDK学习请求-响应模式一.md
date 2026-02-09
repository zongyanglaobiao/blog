---
title: 从阿里SDK学习请求-响应模式一
description: 最近在发现阿里SDK中调用请求有一些有趣的地方
# 默认url路径是title如果不写slug
slug: Request-Response-Pattern
date: 2025-05-14 10:18:02+0000
toc: true
categories:
  - java-category
tags:
  - 设计模式
keywords:
  - Java
  - 设计模式
  - 阿里巴巴
  - 请求-响应模式
  - 命令模式
  - 模板方法模式
  - 阿里SDK
id: a58c6f8e-0500-4bfd-8407-0ac260290cfb
---

## 请求响应模式

在阿里SDK中，很多调用接口都使用`类型安全的请求-响应模式`，[代码](https://www.alibabacloud.com/help/zh/sdk/developer-reference/initializing-1)。废话不多说，Show Code

```java

import cn.hutool.http.HttpRequest;
import cn.hutool.http.HttpResponse;
import cn.hutool.json.JSONUtil;
import lombok.*;
import lombok.extern.slf4j.Slf4j;
import java.lang.reflect.InvocationTargetException;

public class RequestResponsePattern {
    @Data
    static abstract class Response{
        private boolean success;
        private Object error;
    }

    @Data
    static abstract class Request<T extends Response> {
        private String url;
        public abstract Class<T> getResponseClass();
    }

    static class Client{
        private static final String BASE_URL = "https://www.baidu.com/";
        public <T extends Response> T execute(Request<T> request) throws NoSuchMethodException, InvocationTargetException, InstantiationException, IllegalAccessException {
            Class<T> responseClass = request.getResponseClass();
            try (HttpResponse response = HttpRequest.get(BASE_URL.concat(request.getUrl())).execute();) {
                T bean = JSONUtil.toBean(response.body(), responseClass);
                bean.setSuccess(true);
                return bean;
            } catch (Exception e) {
                T t = responseClass.getDeclaredConstructor().newInstance();
                t.setError(e);
                t.setSuccess(false);
                return t;
            }
        }
    }

    @EqualsAndHashCode(callSuper = true)
    @Data
    static class TestResponse extends Response{
        private String message;
    }

    @EqualsAndHashCode(callSuper = true)
    @AllArgsConstructor
    @Data
    @NoArgsConstructor
    static class TestRequest extends Request<TestResponse>{
        private String name;

        @Override
        public Class<TestResponse> getResponseClass() {
            return TestResponse.class;
        }
    }

    /**
     * test demo
     */
    public static void main(String[] args) throws InvocationTargetException, NoSuchMethodException, InstantiationException, IllegalAccessException {
        Client client = new Client();
        TestRequest testRequest = new TestRequest();
        testRequest.setUrl("get");
        TestResponse execute = client.execute(testRequest);
        System.out.println(execute.getError());
    }
}
```

以上比较粗糙，Request类没有那么灵活，感兴趣的可以拿自己的业务设计一下

## 场景 & 为什么

> 每个API请求对象在创建时，就明确地知道了它预期会接收到哪种类型的响应数据结构。通常与外部API交互时使用


**类型安全：** 通过指定 Response 类，编译器可以在编译期检查类型是否匹配，避免运行时类型转换错误。 
开发者可以直接操作强类型的对象，而无需手动解析 JSON 或处理原始数据。

**代码可读性：**
每个 API 有明确的 Request 和 Response 类，命名通常与 API 功能对应，开发者可以快速理解 API 的用途。
相比直接操作 Map 或 JSON 字符串，这种写法更直观，符合面向对象的设计理念。

**封装性：**
SDK 将底层的 HTTP 请求、签名生成、JSON 解析等复杂逻辑封装在内部，开发者只需关注业务参数和返回数据的处理。
Request 和 Response 类可以包含校验逻辑（例如必填参数检查），提高代码健壮性。

**易于维护和扩展：**
每个 API 的 Request 和 Response 类是独立的，新增或修改 API 时，只需添加新的类，不会影响现有代码。
如果 API 返回的数据结构发生变化，只需更新对应的 Response 类即可。

**错误处理统一：**
Response 类通常包含通用的错误字段（例如 error_code、error_msg），便于开发者统一处理异常情况。

