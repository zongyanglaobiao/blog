---
title: 使用github page部署hugo博客网站出现请求网站图标抛出404异常
description:  使用github page部署hugo博客网站出现请求网站图标抛出404异常
# 默认url路径是title如果不写slug
slug: questions1
date: 2024-08-14 12:06:05+0000
toc: true
categories:
  - BUG
tags:
  - HUGO搭建博客
draft: true
---

## 网站图标404问题

近期在使用hugo搭建自己的博客网站的时候出现如下问题：我给自己的博客网站加了一个网站图标本地启动测试是正常的，**所以就能排除是项目中配置问题**

![image-20240807121256876](img/questions/1/image-20240807121256876.png)

但是部署到github pages上就出现问题，如下图

![image-20240807121437791](img/questions/1/image-20240807121437791.png)

经过排查发现是在请求的时候出现了404

![image-20240807121543512](img/questions/1/image-20240807121543512.png)

于是我就下载了github  actions帮我打包构建好的前端项目，发现没有什么异常因为`index.html`和图标在一起并且打开图标文件也没有什么异常，请求`https://zongyanglaobiao.github.io/favicon.svg`路径本身没什么问题但是就是返回**404**问题

![image-20240807121919132](img/questions/1/image-20240807121919132.png)

## 解决方法

正在需找中...