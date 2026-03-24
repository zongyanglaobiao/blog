---
title: "链接"
date: 2026-02-26
slug: "links"
menu:
    main:
        weight: 4
        name: 链接
        params: 
            icon:  link
toc: false
comments: false
---

<style>
.tools-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
}
.tools-container h2, .tools-container h3, .tools-container h4, .tools-container h5 {
  border-left: none !important;
  /* padding-left: 0 !important; */
}
.tools-container h2::before, .tools-container h3::before,
.tools-container h4::before, .tools-container h5::before {
  display: none !important;
}
.category-section { margin-bottom: 48px; }
.category-header {
  display: flex;
  align-items: center;
  flex-wrap: wrap;
  gap: 12px;
  margin-bottom: 20px;
  padding-bottom: 12px;
  border-bottom: 1px solid rgba(0,0,0,.08);
}
.category-icon { font-size: 28px; flex-shrink: 0; }
.category-title {
  font-size: 24px;
  font-weight: 600;
  color: #1d1d1f;
  margin: 0;
  flex: 1;
  min-width: 0;
}
.cards-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 16px;
}
.tool-card {
  display: flex;
  flex-direction: column;
  background: #fff;
  border-radius: 16px;
  padding: 20px;
  text-decoration: none;
  color: inherit;
  box-shadow: 0 2px 8px rgba(0,0,0,.04);
  border: 1px solid rgba(0,0,0,.06);
  transition: all .3s cubic-bezier(.4,0,.2,1);
  overflow: hidden;
}
.tool-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 12px 32px rgba(0,0,0,.12);
  border-color: transparent;
}
.tool-name {
  font-size: 16px;
  font-weight: 600;
  color: #1d1d1f;
  margin: 0 0 8px;
  line-height: 1.4;
  word-break: break-word;
}
.tool-desc {
  font-size: 14px;
  color: #86868b;
  line-height: 1.6;
  margin: 0 0 12px;
  flex: 1;
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
  word-break: break-word;
}
.tags {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
}
.tag {
  font-size: 11px;
  padding: 4px 10px;
  border-radius: 20px;
  font-weight: 500;
  flex-shrink: 0;
  background-color: #F2F2F7;
  color: #8E8E93;
  border: 1px solid #E5E5EA;
}
@media (max-width: 768px) {
  .cards-grid { grid-template-columns: 1fr; }
  .tools-container { padding: 12px; }
}
</style>

<div class="tools-container">

<section class="category-section">
  <div class="category-header">
    <span class="category-icon">📰</span>
    <h2 class="category-title">资讯发现</h2>
  </div>
  <div class="cards-grid">
    <a class="tool-card" href="https://github.com/ruanyf/weekly" target="_blank">
      <h3 class="tool-name">科技爱好者周刊</h3>
      <p class="tool-desc">科技爱好者周刊，每周更新技术资讯</p>
      <div class="tags"><span class="tag">开源</span></div>
    </a>
    <a class="tool-card" href="https://hellogithub.com" target="_blank">
      <h3 class="tool-name">HelloGitHub</h3>
      <p class="tool-desc">分享 GitHub 上有趣、入门级的开源项目</p>
      <div class="tags"><span class="tag">在线</span></div>
    </a>
    <a class="tool-card" href="https://github.com/521xueweihan/HelloGitHub" target="_blank">
      <h3 class="tool-name">HelloGitHub 仓库</h3>
      <p class="tool-desc">GitHub 上有趣、入门级开源项目分享</p>
      <div class="tags"><span class="tag">开源</span></div>
    </a>
    <a class="tool-card" href="https://github.com/GitHubDaily/GitHubDaily" target="_blank">
      <h3 class="tool-name">GitHubDaily</h3>
      <p class="tool-desc">坚持分享 GitHub 上高质量、有趣实用的开源技术教程、开发者工具</p>
      <div class="tags"><span class="tag">开源</span></div>
    </a>
  </div>
</section>

<section class="category-section">
  <div class="category-header">
    <span class="category-icon">🛠️</span>
    <h2 class="category-title">开发工具</h2>
  </div>
  <div class="cards-grid">
    <a class="tool-card" href="https://github.com/521xueweihan/git-tips" target="_blank">
      <h3 class="tool-name">Git的奇技淫巧</h3>
      <p class="tool-desc">Git 使用技巧集合，提升你的 Git 使用效率</p>
      <div class="tags"><span class="tag">Git</span></div>
    </a>
    <a class="tool-card" href="https://github.com/yuaotian/go-cursor-help" target="_blank">
      <h3 class="tool-name">Cursor 试用修复</h3>
      <p class="tool-desc">解决 Cursor 免费试用限制问题</p>
      <div class="tags"><span class="tag">JavaScript</span></div>
    </a>
    <a class="tool-card" href="https://wstool.js.org/" target="_blank">
      <h3 class="tool-name">WebSocket 在线测试</h3>
      <p class="tool-desc">在线 WebSocket 连接测试工具</p>
      <div class="tags"><span class="tag">WebSocket</span></div>
    </a>
    <a class="tool-card" href="https://www.sojson.com/encrypt.html" target="_blank">
      <h3 class="tool-name">加解密工具</h3>
      <p class="tool-desc">在线加密解密工具，支持多种算法</p>
      <div class="tags"><span class="tag">加解密</span></div>
    </a>
  </div>
</section>

<section class="category-section">
  <div class="category-header">
    <span class="category-icon">📚</span>
    <h2 class="category-title">学习资源</h2>
  </div>
  <div class="cards-grid">
    <a class="tool-card" href="https://github.com/CyC2018/CS-Notes" target="_blank">
      <h3 class="tool-name">CS-Notes</h3>
      <p class="tool-desc">技术面试必备基础知识、Leetcode、计算机操作系统、计算机网络、系统设计</p>
      <div class="tags"><span class="tag">面试刷题</span></div>
    </a>
    <a class="tool-card" href="https://pdai.tech/md/resource/tools.html" target="_blank">
      <h3 class="tool-name">Java 全栈知识体系</h3>
      <p class="tool-desc">Java 博客，涵盖 Java 基础到高级的完整知识体系</p>
      <div class="tags"><span class="tag">Java</span></div>
    </a>
    <a class="tool-card" href="https://github.com/itwanger/toBeBetterJavaer" target="_blank">
      <h3 class="tool-name">Java 进阶之路</h3>
      <p class="tool-desc">通俗易懂、风趣幽默的 Java 学习指南，涵盖基础、并发、JVM、企业级开发、面试</p>
      <div class="tags"><span class="tag">Java</span></div>
    </a>
    <a class="tool-card" href="https://github.com/krahets/hello-algo" target="_blank">
      <h3 class="tool-name">Hello 算法</h3>
      <p class="tool-desc">动画图解、一键运行的数据结构与算法教程，支持多种编程语言</p>
      <div class="tags"><span class="tag">算法</span></div>
    </a>
    <a class="tool-card" href="https://github.com/DocsHome/microservices" target="_blank">
      <h3 class="tool-name">微服务：从设计到部署</h3>
      <p class="tool-desc">Microservices from Design to Deployment 中文版</p>
      <div class="tags"><span class="tag">微服务</span></div>
    </a>
    <a class="tool-card" href="https://en.knowledgefxg.com/" target="_blank">
      <h3 class="tool-name">英语学习资源导航</h3>
      <p class="tool-desc">英语学习资源聚合导航</p>
      <div class="tags"><span class="tag">学习</span></div>
    </a>
    <a class="tool-card" href="https://github.com/RealKai42/qwerty-learner" target="_blank">
      <h3 class="tool-name">Qwerty Learner</h3>
      <p class="tool-desc">为键盘工作者设计的单词记忆与英语肌肉记忆锻炼软件</p>
      <div class="tags"><span class="tag">学习</span></div>
    </a>
    <a class="tool-card" href="https://github.com/codecrafters-io/build-your-own-x" target="_blank">
      <h3 class="tool-name">build-your-own-x</h3>
      <p class="tool-desc">通过从零开始重现你最喜欢的技术来掌握编程。</p>
      <div class="tags"><span class="tag">造轮子</span></div>
    </a>
  </div>
</section>

<section class="category-section">
  <div class="category-header">
    <span class="category-icon">🤖</span>
    <h2 class="category-title">AI 相关</h2>
  </div>
  <div class="cards-grid">
    <a class="tool-card" href="https://github.com/tukuaiai/vibe-coding-cn/tree/main" target="_blank">
      <h3 class="tool-name">Vibe Coding 工作站</h3>
      <p class="tool-desc">开发经验 + 提示词库，AI 辅助编程工作站</p>
      <div class="tags"><span class="tag">Python</span></div>
    </a>
    <a class="tool-card" href="https://github.com/browser-use/browser-use" target="_blank">
      <h3 class="tool-name">Browser Use</h3>
      <p class="tool-desc">使 AI 代理可以访问网站，让 AI 能够操作浏览器</p>
      <div class="tags"><span class="tag">Python</span></div>
    </a>
    <a class="tool-card" href="https://github.com/vercel/ai" target="_blank">
      <h3 class="tool-name">Vercel AI SDK</h3>
      <p class="tool-desc">TypeScript 工具包，帮助构建 AI 驱动的应用程序</p>
      <div class="tags"><span class="tag">TypeScript</span></div>
    </a>
    <a class="tool-card" href="https://github.com/Zeyi-Lin/HivisionIDPhotos" target="_blank">
      <h3 class="tool-name">HivisionIDPhotos</h3>
      <p class="tool-desc">轻量级的 AI 证件照制作算法</p>
      <div class="tags"><span class="tag">Python</span></div>
    </a>
    <a class="tool-card" href="https://github.com/anthropics/skills" target="_blank">
      <h3 class="tool-name">Skills 教程</h3>
      <p class="tool-desc">Claude 官方开源的 Skills 教程。该项目是 Anthropic 官方开源的 Agent Skills 仓库，介绍如何通过标准化的 SKILL.md 文件结构，将提示词和工具调用封装为插件形式，为 AI 助手提供可动态加载的技能包，以可复用的方式更好地完成特定任务。</p>
      <div class="tags"><span class="tag">Python</span><span class="tag">HTML</span></div>
    </a>
    <a class="tool-card" href="https://github.com/datawhalechina/hello-agents" target="_blank">
      <h3 class="tool-name">搭建 Agent 教程</h3>
      <p class="tool-desc">📚 《从零开始构建智能体》——从零开始的智能体原理与实践教程</p>
      <div class="tags"><span class="tag">Python</span><span class="tag">HTML</span><span class="tag">JavaScript</span></div>
    </a>
  </div>
</section>

<section class="category-section">
  <div class="category-header">
    <span class="category-icon">💻</span>
    <h2 class="category-title">前端开发</h2>
  </div>
  <div class="cards-grid">
    <a class="tool-card" href="https://github.com/eligrey/FileSaver.js" target="_blank">
      <h3 class="tool-name">FileSaver.js</h3>
      <p class="tool-desc">客户端保存文件的解决方案，适合在客户端生成文件的 Web 应用</p>
      <div class="tags"><span class="tag">JavaScript</span></div>
    </a>
    <a class="tool-card" href="https://github.com/lucide-icons/lucide" target="_blank">
      <h3 class="tool-name">Lucide Icons</h3>
      <p class="tool-desc">美观且一致的图标工具包，Feather Icons 的分支</p>
      <div class="tags"><span class="tag">JavaScript</span></div>
    </a>
    <a class="tool-card" href="https://github.com/chokcoco/CSS-Inspiration" target="_blank">
      <h3 class="tool-name">CSS Inspiration</h3>
      <p class="tool-desc">在这里找到写 CSS 的灵感</p>
      <div class="tags"><span class="tag">CSS</span></div>
    </a>
  </div>
</section>

<section class="category-section">
  <div class="category-header">
    <span class="category-icon">🖥️</span>
    <h2 class="category-title">桌面应用</h2>
  </div>
  <div class="cards-grid">
    <a class="tool-card" href="https://v2.tauri.app/" target="_blank">
      <h3 class="tool-name">Tauri</h3>
      <p class="tool-desc">用 Web 前端技术构建跨平台桌面和移动应用，比 Electron 更轻量</p>
      <div class="tags"><span class="tag">Rust</span><span class="tag">框架</span><span class="tag">跨平台</span></div>
    </a>
    <a class="tool-card" href="https://github.com/tw93/Pake" target="_blank">
      <h3 class="tool-name">Pake</h3>
      <p class="tool-desc">利用 Rust 轻松构建轻量级多端桌面应用，将网页打包成桌面应用</p>
      <div class="tags"><span class="tag">Rust</span><span class="tag">跨平台</span></div>
    </a>
    <a class="tool-card" href="https://github.com/beeware/toga" target="_blank">
      <h3 class="tool-name">Toga</h3>
      <p class="tool-desc">Python GUI 框架，构建跨平台原生桌面应用</p>
      <div class="tags"><span class="tag">Python</span><span class="tag">框架</span><span class="tag">跨平台</span></div>
    </a>
  </div>
</section>

<section class="category-section">
  <div class="category-header">
    <span class="category-icon">⚙️</span>
    <h2 class="category-title">运维部署</h2>
  </div>
  <div class="cards-grid">
    <a class="tool-card" href="https://github.com/SuperManito/LinuxMirrors" target="_blank">
      <h3 class="tool-name">LinuxMirrors</h3>
      <p class="tool-desc">一键切换 Linux 软件源为国内镜像，支持主流发行版</p>
      <div class="tags"><span class="tag">Shell</span><span class="tag">Linux</span></div>
    </a>
    <a class="tool-card" href="https://github.com/HQarroum/docker-android" target="_blank">
      <h3 class="tool-name">Docker Android</h3>
      <p class="tool-desc">运行 Android 模拟器作为服务的 Docker 镜像</p>
      <div class="tags"><span class="tag">Android</span><span class="tag">Docker</span></div>
    </a>
    <a class="tool-card" href="https://www.yourware.so/" target="_blank">
      <h3 class="tool-name">Yourware</h3>
      <p class="tool-desc">只要有 HTML 文件就能生成有域名公网可访问的网站</p>
      <div class="tags"><span class="tag">在线</span></div>
    </a>
  </div>
</section>

<section class="category-section">
  <div class="category-header">
    <span class="category-icon">📁</span>
    <h2 class="category-title">文件媒体</h2>
  </div>
  <div class="cards-grid">
    <a class="tool-card" href="https://github.com/schollz/croc" target="_blank">
      <h3 class="tool-name">Croc</h3>
      <p class="tool-desc">任意两台计算机之间轻松安全地传输文件和文件夹</p>
      <div class="tags"><span class="tag">Go</span><span class="tag">命令行</span><span class="tag">跨平台</span></div>
    </a>
    <a class="tool-card" href="https://github.com/microsoft/markitdown" target="_blank">
      <h3 class="tool-name">MarkItDown</h3>
      <p class="tool-desc">将文件和办公文档转换为 Markdown 的工具</p>
      <div class="tags"><span class="tag">Python</span></div>
    </a>
    <a class="tool-card" href="https://github.com/jianchang512/pyvideotrans" target="_blank">
      <h3 class="tool-name">视频翻译配音</h3>
      <p class="tool-desc">将视频翻译为另一种语言，支持语音识别、合成、字幕翻译</p>
      <div class="tags"><span class="tag">Python</span></div>
    </a>
    <a class="tool-card" href="https://github.com/yt-dlp/yt-dlp" target="_blank">
      <h3 class="tool-name">yt-dlp</h3>
      <p class="tool-desc">功能丰富的命令行音频/视频下载器</p>
      <div class="tags"><span class="tag">Python</span><span class="tag">命令行</span></div>
    </a>
  </div>
</section>

<section class="category-section">
  <div class="category-header">
    <span class="category-icon">🎨</span>
    <h2 class="category-title">设计绘图</h2>
  </div>
  <div class="cards-grid">
    <a class="tool-card" href="https://github.com/excalidraw/excalidraw" target="_blank">
      <h3 class="tool-name">Excalidraw</h3>
      <p class="tool-desc">画图神器，绘制类似手绘风格的虚拟白板图表</p>
      <div class="tags"><span class="tag">JavaScript</span><span class="tag">在线</span></div>
    </a>
    <a class="tool-card" href="https://xia8.top/" target="_blank">
      <h3 class="tool-name">Adobe 全家桶</h3>
      <p class="tool-desc">Adobe 全家桶软件资源 - 百度网盘</p>
      <div class="tags"><span class="tag">资源</span></div>
    </a>
  </div>
</section>

<section class="category-section">
  <div class="category-header">
    <span class="category-icon">🏃</span>
    <h2 class="category-title">生活工作</h2>
  </div>
  <div class="cards-grid">
    <a class="tool-card" href="https://github.com/loks666/get_jobs" target="_blank">
      <h3 class="tool-name">AI 找工作助手</h3>
      <p class="tool-desc">全平台自动投简历脚本：Boss、前程无忧、猎聘、拉勾、智联招聘</p>
      <div class="tags"><span class="tag">找工作</span></div>
    </a>
    <a class="tool-card" href="https://github.com/Snouzy/workout-cool" target="_blank">
      <h3 class="tool-name">Workout Cool</h3>
      <p class="tool-desc">现代开源健身教练平台，创建锻炼计划、追踪进度</p>
      <div class="tags"><span class="tag">健身</span></div>
    </a>
    <a class="tool-card" href="https://github.com/myhhub/stock" target="_blank">
      <h3 class="tool-name">Stock 股票分析</h3>
      <p class="tool-desc">获取股票数据、计算指标、识别形态、综合选股、回测验证</p>
      <div class="tags"><span class="tag">Python</span><span class="tag">股票</span></div>
    </a>
    <a class="tool-card" href="https://github.com/usememos/memos" target="_blank">
      <h3 class="tool-name">Memos</h3>
      <p class="tool-desc">开源、可自托管的笔记服务，无追踪、无广告、无订阅费</p>
      <div class="tags"><span class="tag">Go</span></div>
    </a>
    <a class="tool-card" href="https://tv.garden/comedy/HhYHpgeNR67LDQ" target="_blank">
      <h3 class="tool-name">TV Garden</h3>
      <p class="tool-desc">世界各地网上电视台直播</p>
      <div class="tags"><span class="tag">影视</span></div>
    </a>
    <a class="tool-card" href="https://github.com/ZhuLinsen/daily_stock_analysis" target="_blank">
      <h3 class="tool-name">AI 智能股票分析系统</h3>
      <p class="tool-desc">基于 LLM 的智能股票分析系统。这是一个由 LLM 驱动的智能股票分析工具，支持 A 股、港股和美股的每日自动分析与推送。它通过 AkShare、Tushare、YFinance 等数据源获取实时行情，并借助 DeepSeek 等大模型 API 服务，对自选股票进行多维度分析（技术面、筹码分布、舆情），生成决策仪表盘，支持 GitHub Actions 定时执行（无需服务器）或 Docker 一键部署。</p>
      <div class="tags"><span class="tag">Python</span><span class="tag">JavaScript</span></div>
    </a>
  </div>
</section>

</div>