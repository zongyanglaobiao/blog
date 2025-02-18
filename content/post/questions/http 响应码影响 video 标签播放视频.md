---
title: http 响应码影响 video 标签播放视频
description: 后端接口能正常下载但是前端 video 标签无法播放视频，原因可能是...
# 默认url路径是title如果不写slug
slug: http 响应码影响 video 标签播放视频
date: 2025-02-18 09:35:23+0000
toc: true
categories:
  - bug-category
tags:
  - video标签
  - 播放视频
  - html
keywords:
  - html
id: c2474a95-7483-49e2-99b3-807b88696be3
---
# 背景
使用后端给的文件下载接口地址实现视频播放，但是 video 标签一直无法播放视频如下图，把接口地址放到浏览器请求能直接下载。但就是不能播放

![img.png](img/questions/3/img.png)

# 原因
**http 响应码不正确**，返回201是无法播放视频200可以如下图

![img.png](img/questions/3/img_1.png)

**状态码的影响：**

- `200 OK`：浏览器正确识别并处理文件，能够进行播放。
- `404 Not Found`：文件未找到时会返回此状态，浏览器会提示文件未找到，不能播放。
- `403 Forbidden`：如果浏览器无法访问资源，通常会返回此状态，表示没有权限访问文件，视频不会播放。
- `500 Internal Server Error`：服务器错误时返回此状态，表示后端发生了错误，视频无法播放。
- `304 Not Modified`：如果文件未被修改，浏览器会从缓存加载文件，通常不会导致播放失败，但在某些情况下，可能会导致视频不被正确加载。
- `415 Unsupported Media Type`：如果返回的 Content-Type 不支持浏览器播放的格式，可能会导致视频无法播放。
