---
title: 参考Harness Engineering，使用 AI Agent 进行全栈开发反思
description: 反思在使用 AI Agent 协助开发的时候一些问题
# 默认url路径是title如果不写slug
slug: work-with-agent
date: 2026-04-23 09:58:15+0000
# 是否生成目录
toc: true
categories:
  - ai-category
tags:
  - 全栈开发
  - Harness Engineering
  - SDD
keywords:
  - Agent
  - Harness Engineering
  - SDD
  - TDD
  - SpringBoot
  - Vue
id: cacff4cb-be7b-4469-9685-dc2bb4ce27f6
# 是否可以添加评论
comments: true
---

## 背景

使用公司现有前后端脚手架，从公司提供的 PRD 文档开始进行完整开发。整个过程推进得比较麻烦，也花了不少时间在需求拆解、项目结构理解以及开发流程摸索上。结果就是能看就是如果要交付还是有一段距离的。但是还可以进行完善

- PRD 拆解与任务规划
- Agent 上下文管理
- AI 生成代码的校验与修正
- 前后端联调协作
- 基于 AI 的研发效率提升方式

## 项目难点

1. 按照项目约束开发
2. 在已有的脚手架上面开发
3. 前后端如何连接
4. 如何做回滚测试
5. 代码可维护

## 过程

### 技术栈 & 工具

- SpringBoot
- Vue
- MySQL
- Claude Code
- Codex CLI
- IDEA

### 后端

我的流程如下：

1. 将原始需求文档使用 AI Agent 进行精简出一份文档
2. 编写拆分任务文档[backend-plan-generation-specifications](static/img/ai/doc/backend-plan-generation-specifications.md)

#### 总结

PRD -> 和 AI 梳理需求，需求分析，清晰目标 -> 输出文档：业务架构 & 技术架构 & 权限设计 & 领域建模 & 功能设计 & 数据库表设计 -> 编写自己的工作流(HOOK、SKILLS、RULES、ECC、SUPERPOWERS)单个模块结合TDD整体结合 SDD -> 任务拆分 -> 最后进行 E2E 回归整体测试

### 前端

- 

## AI的漩涡

1. 反复的提问会导致 AI 一直回复：比如一个文档让他审核检查漏洞它会给出，但修完之后再同样话语去问还是给出漏洞，就是这种没有一个终点或者确定的回答，直到最后成为一个屎山或者超长篇文档。

## 对 Harness Engineering 的理解

当我接到这个任务的时候，其实是有点没头绪因为没有尝试根据企业项目级 PRD 文档生成整个企业项目代码，通过查找发现 [Harness Engineering](https://www.runoob.com/ai-agent/harness-engineering.html) 这个概念，其中的
这个概念中四个核心组件

1. 上下文工程（Context Engineering）
2. 架构约束（Architecture Constraints）
3. 反馈循环（Feedback Loop）
4. 熵管理（Entropy Management）

其实经过实际开发时发现，如果要按照你

## ECC(Everything-Calude-Code)

- 



