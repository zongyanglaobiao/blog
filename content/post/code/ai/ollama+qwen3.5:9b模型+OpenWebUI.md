---
title: Ubuntu+Ollama+Qwen3.5:9b模型+OpenWebUI
description: 在 Ubuntu 系统上使用 ollama 运行qwen3.5:9b模型集成到OpenWebUI
slug: ollama+qwen3.5:9b模型+OpenWebUI
date: 2026-03-06 11:04:41+0000
# 是否生成目录
toc: true
categories:
  - ai-category
tags:
  - ollama
  - qwen3.5
  - open webui
keywords:
  - ollama
  - qwen3.5
  - open webui
  - ubuntu
  - docker
id: d1b6f336-7fbd-4d23-853a-06eed8994083
# 是否可以添加评论
comments: true
---

把旧的的 Windows 电脑，安装 Ubuntu 系统，有了环境就想试试本地大模型，便有本次博客

- `Ubuntu系统版本`: Ubuntu 24.04.4 LTS
- `运行内存`: 16G
- `硬盘`: 512G
- `CPU`: i5-1135G7

## 下载 Ollama

终端执行如下命令

```shell
curl -fsSL https://ollama.com/install.sh | sh
```

使用 `ollama --version` 命令时，出现如下错误，关闭当前终端，重新打开一个终端，在执行即可

```shell
bash: /snap/bin/ollama: 没有那个文件或目录
```

## Ollama 修改监听地址

默认只监听 127.0.0.1，需要修改服务配置

```shell
sudo systemctl edit ollama

# 在文件中增加以下内容，注意需要在 ### Edits below this comment will be discarded 之上
[Service]
Environment="OLLAMA_HOST=0.0.0.0"

# 可能使用的编辑器是 nano 而不是 vim，此时保存就是 
# 保存：Ctrl + O + Enter 
# 退出：Ctrl + X 

#重启 Ollama 服务
systemctl restart ollama
```

## Open WebUI
> [Open WebUI 是一个可扩展、功能丰富且用户友好的自托管 AI 平台，设计为完全离线运行。 它支持各种 LLM 运行器，如 Ollama 和 OpenAI 兼容 API，具有用于 RAG 的内置推理引擎，使其成为强大的 AI 部署解决方案。](https://openwebui-doc-zh.pages.dev/) 



### 使用 Docker Compose 启动

> [安装 Docker 文档](https://yeasy.gitbook.io/docker_practice/di-yi-bu-fen-ru-men-pian/03_install)

创建 `docker-compose.yml`文件,使用`docker compose up -d`启动，如果下载速度慢，可以使用 docker 镜像，

```yaml
services:
    open-webui:
        image: openwebui/open-webui
        container_name: open-webui
        ports:
            - "8080:8080"
        volumes:
            - ./data:/app/backend/data
        # 配置本地 ollama 的地址，注意网络 Open WebUI是容器运行，有网络问题，这里的 ip 换成自己的
        environment:
            - OLLAMA_BASE_URL=http://192.168.2.80:11434
        restart: unless-stopped
```

启动后，浏览器访问 127.0.0.1:8080 初始化用户就可以正常聊天了


