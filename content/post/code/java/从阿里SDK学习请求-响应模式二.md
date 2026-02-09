---
title: 从阿里SDK学习请求-响应模式二
description: 基于此模式的封装
# 默认url路径是title如果不写slug
slug: 通用请求-响应模式
date: 2026-01-26 10:34:59+0000
# 是否生成目录
toc: true
categories:
  - java-category
tags:
  - 设计模式
keywords:
  - 阿里巴巴
  - 请求-响应模式
id: 8aa4e3c2-3c53-4568-898f-0acbfd65123d
# 是否可以添加评论
comments: true
---

## 场景

当对接第三方系统如果涉及到多种 API 的对接，每一个API请求、响应都需要处理，但是很多请求响应处理方式都是相同只是参数不一样，所以借鉴阿里源码中"请求响应模式"设计了如下通用请求 - 响应模型
此模式不处理具体请求逻辑

```java
/**
 * 客户端【请求响应模式】
 *
 * @author jamesaks
 * @since 2025/5/22
 */
public interface Client {
    /**
     * 执行请求
     *
     * @param request 请求参数
     * @return 指定的响应类
     */
    <T extends Response> T execute(Request<T> request);
}
```

```java
/**
 * 抽象客户端
 *
 * @author jamesaks
 * @since 2025/11/11
 */
@Slf4j
public abstract class AbstractClient<Req, Resp> implements Client {

    /**
     * 执行请求并获取结果
     *
     * @see #execute(Request, ClientHook)
     */
    @Override
    public <T extends Response> T execute(Request<T> request) {
        return execute(request, null);
    }

    /**
     * 执行请求并获取结果
     *
     * @param request 请求参数
     * @param hook    请求执行钩子
     * @param <T>     响应结果类型
     * @return 响应结果
     * @see #doExecute(Request, ClientHook)
     */
    public <T extends Response> T execute(Request<T> request, ClientHook<Req, Resp, T> hook) {
        T instance = getRespInstance(request);
        try {
            //实现hook防止为null
            return doExecute(request, new ClientHook<>() {
                @Override
                public void beforeExecute(Req request) {
                    if (Objects.nonNull(hook)) {
                        hook.beforeExecute(request);
                    }
                    log.info("execute request --> {}", request);
                }

                @Override
                public Optional<T> afterExecute(Resp response) {
                    log.info("execute response --> {}", response);
                    return Objects.nonNull(hook) ? hook.afterExecute(response) : Optional.empty();
                }
            });
        } catch (Exception e) {
            log.error("execute error: ", e);
            instance.setError(e);
        }
        log.info("response: {}", instance);
        return instance;
    }

    /**
     * 最终实现请求并返回解析结果，这里默认权限是{@code protected},子类实现后不建议重写权限，{@code doExecute}只实现请求逻辑，其余的不需要管，如日志...
     * <p>
     *
     * @param request 请求参数
     * @param hook    请求执行钩子
     * @param <T>     响应结果类型
     * @return 响应结果
     * @see #execute(Request, ClientHook)
     */
    protected abstract <T extends Response> T doExecute(Request<T> request, ClientHook<Req, Resp, T> hook);

    /**
     * 获取响应结果实例
     *
     * @param request 请求参数
     * @param <T>     响应结果类型
     * @return 响应结果实例
     */
    protected <T extends Response> T getRespInstance(Request<T> request) {
        Request<T> tRequest = Objects.requireNonNull(request, "Request cannot be null");

        Class<T> respCls = tRequest.getResponseClass();
        if (respCls == null) {
            throw new IllegalArgumentException("Response class cannot be null");
        }

        //创建响应实例
        T responseInstance;
        try {
            responseInstance = respCls.getDeclaredConstructor().newInstance();
        } catch (ReflectiveOperationException e) {
            throw new RuntimeException("Failed to instantiate response class: " + respCls.getName(), e);
        }
        return responseInstance;
    }

    /**
     * 请求执行钩子
     *
     * @param <Req>  请求对象
     * @param <Resp> 响应对象
     * @param <T>    转换对象
     */
    public interface ClientHook<Req, Resp, T extends Response> {

        /**
         * 执行请求前
         *
         * @param request 请求对象
         */
        default void beforeExecute(Req request) {
        }

        /**
         * 执行请求后
         *
         * @param response 响应对象
         * @return 响应结果
         */
        default Optional<T> afterExecute(Resp response) {
            return Optional.empty();
        }
    }
}
```

```java
/**
 * 请求参数类
 *
 * @author jamesaks
 * @since 2025/5/22
 */
@Data
public abstract class Request<T extends Response> implements Serializable {

    /**
     * 请求路径
     */
    private transient String url;

    /**
     * 请求头部信息
     */
    private transient Map<String, Object> headers;

    /**
     * 请求方法
     */
    private transient RequestMethod method;

    /**
     * 请求体
     */
    private transient String body;

    /**
     * 指定响应实体类
     */
    public abstract Class<T> getResponseClass();
}
```

```java
/**
 * 请求方法枚举
 *
 * @author jamesaks
 * @since 2025/5/22
 */
public enum RequestMethod {
    GET, POST, PUT, DELETE, PATCH, OPTIONS, HEAD
}
```

```java
/**
 * 响应抽象类
 *
 * @author jamesaks
 * @since 2025/5/22
 */
@Data
public abstract class Response implements Serializable {

    /**
     * 如果执行请求有错误则返回错误信息或者 status 不为 200
     */
    public Object error;

    /**
     * 判断是否请求成功
     */
    public abstract boolean hasSuccess();
}
```

```java
/**
 * 默认实现，核心使用 hutool 工具类
 *
 * @author jamesaks
 * @since 2025/5/22
 */
@Slf4j
public class HutoolHttpClient extends AbstractClient<HttpRequest,HttpResponse> {

    /**
     * hutool 工具类默认 -1 永不超时，注意这会拖死系统
     */
    @Setter
    private int defaultTimeout = 5000;

    @Override
    protected <T extends Response> T doExecute(Request<T> request, ClientHook<HttpRequest, HttpResponse,T> hook) {
        T instance = getRespInstance(request);

        // 改为同步执行
        HttpRequest httpRequest = buildRequest(request);
        hook.beforeExecute(httpRequest);
        try (HttpResponse resp = httpRequest.execute(true)) {
            //返回自定义的解析逻辑
            Optional<T> optional = hook.afterExecute(resp);
            if (optional.isPresent()) {
                return optional.get();
            }

            //请求体
            String body = resp.body();
            if (resp.isOk() && StrUtil.isNotBlank(body)) {
                return JSONUtil.toBean(body, request.getResponseClass());
            }
            instance.setError(body);
        }
        return instance;
    }

    /**
     * 构建请求
     */
    private HttpRequest buildRequest(Request<?> request) {
        String url = request.getUrl();
        Map<String, Object> headers = request.getHeaders();
        RequestMethod method = request.getMethod();
        String body = request.getBody();
        HttpRequest req;
        switch (method) {
            case GET -> req = HttpRequest.get(url);
            case POST -> req = HttpRequest.post(url);
            case DELETE -> req = HttpRequest.delete(url);
            case PUT -> req = HttpRequest.put(url);
            default -> throw new RuntimeException("Unsupported request methods");
        }
        req.timeout(defaultTimeout);
        if (Objects.nonNull(body)) {
            req.body(body);
        }
        if (Objects.nonNull(headers)) {
            req.addHeaders(headers.entrySet().stream().collect(Collectors.toMap(Map.Entry::getKey, t -> JSONUtil.toJsonStr(t.getValue()))));
        }
        return req;
    }
}
```