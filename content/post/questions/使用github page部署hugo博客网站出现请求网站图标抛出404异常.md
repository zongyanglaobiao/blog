---
title: 使用github page部署hugo博客请求网站图标抛出404异常
description:  使用github page部署hugo博客网站出现请求网站图标抛出404异常
# 默认url路径是title如果不写slug
slug: questions1
date: 2024-08-14 12:06:05+0000
toc: true
categories:
  - bug-category
tags:
  - HUGO搭建博客
keywords:
  - HUGO
  - 搭建博客
id: 10
---

## 网站图标404问题

近期在使用hugo搭建自己的博客网站的时候出现如下问题：我给自己的博客网站加了一个网站图标本地启动测试是正常的

![image-20240807121256876](img/questions/1/image-20240807121256876.png)

配置文件如下，我的图标文件在`static/favicon.svg

```toml
favicon = "/favicon.svg"
```

但是部署到github pages上就出现问题，如下图

![image-20240807121437791](img/questions/1/image-20240807121437791.png)

经过排查发现是在请求的时候出现了404

![image-20240807121543512](img/questions/1/image-20240807121543512.png)

于是我就下载了github  actions帮我打包构建好的前端项目，发现没有什么异常因为`index.html`和图标在一起并且打开图标文件也没有什么异常，请求`https://zongyanglaobiao.github.io/favicon.svg`路径本身没什么问题但是就是返回**404**问题

![image-20240807121919132](img/questions/1/image-20240807121919132.png)

## 解决方法

最后发现是配置文件写错了,hugo中图片是否带`/`会影响图片是否正常显示。去掉`/`就可以正常显示

```toml
favicon = "favicon.svg"
```