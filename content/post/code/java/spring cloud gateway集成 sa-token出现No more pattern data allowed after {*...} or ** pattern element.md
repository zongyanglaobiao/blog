---
title: 路径匹配问题
description: spring cloud gateway集成 sa-token出现No more pattern data allowed after {*...} or ** pattern element
# 默认url路径是title如果不写slug
date: 2025-05-20 09:55:02+0000
toc: true
categories:
  - java-category
tags:
  - 微服务
keywords:
  - Java
  - Spring Boot 3
  - Spring Cloud
  - 微服务
  - gateway
id: a89c6f83-0500-4bfd-8407-0ac260290cfb
---


## 版本

```xml
<spring-boot.version>3.2.12</spring-boot.version>
<spring-cloud-dependencies.version>2023.0.3</spring-cloud-dependencies.version>
<spring-cloud-alibaba-dependencies.version>2023.0.3.2</spring-cloud-alibaba-dependencies.version>
<sa-token-spring-boot3-starter.version>1.42.0</sa-token-spring-boot3-starter.version>
```
## 背景
使用 spring cloud 其中的 gateway 组件集成sa-token在增加全局过滤器抛出`No more pattern data allowed after {*...} or ** pattern element`
```java

private static final String[] WHITELIST = {
        "/**/doc.html",
        "/**/*.css",
        "/**/*.js",
        "/**/*.png",
        "/**/*.jpg",
        "/**/*.ico",
        "/**/v3/**",
        "/**/login/**",
};

/**
 * 注册 [Sa-Token全局过滤器]
 */
@Bean
public SaReactorFilter getSaReactorFilter() {
    return new SaReactorFilter()
            // 指定 [拦截路由]
            .addInclude("/**")
            // 指定 [放行路由]
            .addExclude(WHITELIST)
            // 指定[认证函数]: 每次请求执行
            .setAuth(obj -> StpUtil.checkLogin()).
            setBeforeAuth(obj -> {
                // ---------- 设置跨域响应头 ----------
                SaHolder.getResponse()
                        // 是否可以在iframe显示视图： DENY=不可以 | SAMEORIGIN=同域下可以 | ALLOW-FROM uri=指定域名下可以
                        // .setHeader("X-Frame-Options", "SAMEORIGIN")
                        // 是否启用浏览器默认XSS防护： 0=禁用 | 1=启用 | 1; mode=block 启用, 并在检查到XSS攻击时，停止渲染页面
                        .setHeader("X-XSS-Protection", "1; mode=block")
                        // 禁用浏览器内容嗅探
                        .setHeader("X-Content-Type-Options", "nosniff")
                        // 允许指定域访问跨域资源
                        .setHeader("Access-Control-Allow-Origin", "*")
                        // 允许所有请求方式
                        .setHeader("Access-Control-Allow-Methods", "*")
                        // 有效时间
                        .setHeader("Access-Control-Max-Age", "3600")
                        // 允许的header参数
                        .setHeader("Access-Control-Allow-Headers", "*");
                // 如果是预检请求，则立即返回到前端
                SaRouter.match(SaHttpMethod.OPTIONS)
                        // OPTIONS预检请求，不做处理
                        .free(r -> {})
                        .back();
            });
}
```
这不是 sa-token 问题，其中的错误出现在匹配路径的写法,其中不允许`/**`但是这在 spring boot 是正常使用的，修改成如下就能解决这个问题
```java
private static final String[] WHITELIST = {
        "/doc.html",
        "*.css",
        "*.js",
        "*.png",
        "*.jpg",
        "*.ico",
        "/v3/**",
        "/test/login/**",
};
```



