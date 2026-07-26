# PostDev Skills

面向真实产品开发者的开源 [Claude Code](https://claude.com/claude-code) 技能（skills）。

[![许可证: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](../../LICENSE)
[![Skills](https://img.shields.io/badge/skills-1-green.svg)](#技能列表)
[![欢迎 PR](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](../../CONTRIBUTING.md)
[![ko-fi](https://img.shields.io/badge/support-ko--fi-ff5e5b.svg)](https://ko-fi.com/postdev360)

**其他语言：** [English](../../README.md) · [Français](README.fr.md) · [Español](README.es.md)

---

## 技能列表

| 技能 | 作用 |
| --- | --- |
| [**app-blueprint**](../../skills/app-blueprint/) | 在为新应用、新产品或新功能提出任何代码或架构方案*之前*，先用简单易懂的语言进行一次简短的需求访谈，然后写出一份由你确认的 `PROJECT_BRIEF.md`。 |

## 安装

每个技能都是一个独立的文件夹。把你需要的复制到技能目录即可。

**仅用于单个项目** — 该技能只在这个项目中可用，可随项目一起提交到版本库：

```bash
mkdir -p .claude/skills
git clone --depth 1 https://github.com/PostDev360/postdev-skills.git /tmp/postdev-skills
cp -r /tmp/postdev-skills/skills/app-blueprint .claude/skills/
rm -rf /tmp/postdev-skills
```

**用于本机所有项目** — 该技能在任何地方都可用：

```bash
mkdir -p ~/.claude/skills
git clone --depth 1 https://github.com/PostDev360/postdev-skills.git /tmp/postdev-skills
cp -r /tmp/postdev-skills/skills/app-blueprint ~/.claude/skills/
rm -rf /tmp/postdev-skills
```

然后启动 Claude Code 并运行 `/skills` 确认已加载。当你的请求与技能描述匹配时，技能会自动触发；你也可以直接按名称调用。

## app-blueprint

### 存在的原因

非技术背景的创始人和早期项目发起人常常直接要求 AI 助手"帮我做一个应用"，却没意识到过程中有多少决策是被悄悄做出的：是否需要用户账号、数据是否需要持久保存、面向哪些平台、v1 版本的真正范围是什么。App Blueprint 会先把这些决策摆到台面上，以对话的形式明确下来，确保做决定的是产品负责人本人，而不是 AI。

### 触发时机

当你想要启动一个新应用/产品/功能，但需求尚不明确时（例如"我想做一个应用"、"帮我创建一个项目"、"我有一个工具的想法"），或你直接跳过范围界定、要求代码时，该技能会自动触发。如果你已经提供了清晰的需求说明，或明确要求跳过需求访谈，则该技能会让步。

### 工作方式

1. 用通俗语言提问，把技术性权衡转化为现实后果——例如用*"如果有人关闭应用后第二天再打开，他们的信息还应该保留吗？"*代替*"你需要持久化存储吗？"*
2. 每次只问 3-4 个相关问题，而不是一次性提出一长串问卷；当答案是具体选项时使用多选提示。
3. 按顺序覆盖七大类问题：目的与受众、人员与权限、信息与记忆、使用场景与方式、范围与优先级、实际约束、集成与外观——只有当你的回答已经明确覆盖某一类别时才会跳过。
4. 将 **Project Brief（项目简报）** 写入 `PROJECT_BRIEF.md`，并请你确认或修正，之后才会开始任何架构设计或代码编写。
5. 使用你所书写的语言进行对话。

### 简报确认之后

有两条原则会延续到实际构建过程中：

- **简明汇报** — 整个构建过程中的进度更新和总结都保持简短，以降低长期项目中的 token 消耗。
- **模块化分块构建** — 应用被拆分为相互独立、低耦合的模块，之后新增或删除某个功能时，只需改动对应的模块，而不必牵动整个代码库。

### 产出结果

一份经过确认的书面 Project Brief，作为后续所有实现工作的依据来源。

## 参与贡献

欢迎各种形式的贡献——新技能、对现有技能的改进、翻译以及缺陷报告。请先阅读 [CONTRIBUTING.md](../../CONTRIBUTING.md)，并参阅[行为准则](../../CODE_OF_CONDUCT.md)。

## 许可证

[MIT](../../LICENSE) © PostDev360

## 支持本项目

如果这些技能为你节省了时间，欢迎在 [Ko-fi](https://ko-fi.com/postdev360) 上支持它们的开发。
