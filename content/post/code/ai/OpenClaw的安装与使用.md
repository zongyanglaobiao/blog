---
title: Telegram + OpenClaw 的安装与使用
description: 养殖🦞的第一步
slug: OpenClaw的安装与使用
date: 2026-03-09 17:49:18+0000
image: img/ai/ai2.png
toc: true
categories:
  - ai-category
tags:
  - OpenClaw
  - Agent
keywords:
  - OpenClaw
  - Agent
  - OpenClaw Agent 加入 Telegram 群组
id: 153fd817-8191-4255-9205-fbdfb3e2f5ae
comments: true
---

## 准备工作

- `NodeJS: `24.14.0
- `Git: `2.43.0
- `Telegram Bot Token`
- `Minmax API Key（或者其他家的 API Key）`

## OpenClaw 安装

[官方中文文档](https://docs.openclaw.ai/zh-CN)，按照步骤安装。安装引导中能跳过则跳过，因为后续都可以通过 Web UI 来配置，我建议就配置引导中模型 API Key 和勾上最后的 skills，到 `openclaw onboard --install-daemon` 结束可能出现如下错误
**Gateway: not detected (gateway closed (1006 abnormal closure (no close frame)): no close )**。

版本：当前安装的版本为：v2026.3.24

![错误](img/ai/ai3.png)

当前的 OpenClaw Gateway 没有启动成功

```shell
# 检查是否启动了
openclaw gateway status

# 检查端口是否占用
netstat -anp | grep "18789"

# 手动启动
openclaw gateway 
```

安装引导结束后会提供 Web UI 地址，该地址携带一个 token，请直接使用该网址访问，否则访问网关需要手动配置 token

## 配置 Telegram Bot Token

国内用户访问 Telegram 网页端需要走**代理**，代表你安装的 OpenClaw 使用 Telegram 通信也需要走**代理**。打开 http://127.0.0.1:18789?token=<你的token>，把 Telegram Bot Token 给 OpenClaw 让他配置，配置好在 Telegram 发送 `/start` 获取配对码，
获取之后把 Telegram Bot 的配对码发给 OpenClaw 让它配置

或者使用如下命令手动执行

```shell
openclaw pairing approve telegram [配对码]
```

## Agent Teams

复杂的任务给单个 Agent 处理会容易出现上下文爆炸，幻觉。模拟现实生活场景复杂任务需要拆解分发，借助 OpenClaw 的多 Agent 机制是否可以实现拆分并互相讨论？

### Telegram Group && Telegram Group Topic

Telegram 群组支持 Topic（话题）功能，类似于在一个大群内创建不同的讨论分区。

#### 创建 Bot

在 @BotFather 使用 `/newbot`，按提示输入 Bot 名称，复制 BotFather 给你的 Token，发给 OpenClaw 让他自己配置。发送 `/start` 到新的 Bot 获取配对码，再给 OpenClaw 让它进行配对

**Tip：** 每次 OpenClaw 自动重启都需要在终端开启代理，最好把这个规则告诉 OpenClaw 记下来

#### 创建 Agent

1. **创建新代理：** 执行 `openclaw agents add interviewer`，按照引导往下走。在选择 channel 时，选择上面已创建并配对的 Telegram 渠道。
    - Telegram DM policy -> pairing
    ![nwebot](img/ai/ai7.png)
2. **重启 OpenClaw：** `openclaw gateway restart`
3. **验证是否成功：** 在引导中，我没有直接从旧的 Agent 复制 Profile。因此需要在对应的 Workspace 中修改 `SOUL.md` 文件。比如我定义了角色是面试官，可以在 Telegram 中询问验证。
   ![interviewer](img/ai/ai8.png)


#### 加入群组

1. **开放接收群组信息权限：** 在 @BotFather 使用 `/mybots` 选择对应 Bot，Bot Settings → Group Privacy → Turn off
2. **获取群组 ID：** 先把机器人拉入群组，通过 `openclaw logs --follow` 查看日志，@我们的机器人日志就会看到对应的群组 ID
   ![group](img/ai/ai9.png)
3. **修改 OpenClaw 配置：** 修改完重启
```json
// 修改 channels.telegram 部分：
{
   "channels": {
      "telegram": {
         "groupPolicy": "allowlist",
         "groups": {
            "-1003512211919": {
              //  true 代表被@才回复  ,false 是所有都回复        
               "requireMention": true
            }
         }
      }
   }
}
```

然后在群里 @对应的 Bot，**注意点：** 如果先将 Bot 拉入群，再修改权限设置，修改可能不会立即生效。建议先完成权限配置，再将 Bot 拉入群。就可以了
![ok](img/ai/ai10.png)

