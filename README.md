# LangChain 学习项目

这是一个系统性的 LangChain 学习笔记项目，包含从基础到高级的各种示例和实践。

## 项目结构

```
.
├── codes/
│   ├── chapter01-summary/           # LangChain框架初体验
│   ├── chapter02-model IO/          # 模型输入输出相关
│   ├── chapter03-chain/             # Chain 链式调用
│   ├── chapter04-memory/            # Memory 记忆模块
│   ├── chapter05-tools/             # Tools 工具模块
│   ├── chapter06-agents/            # Agents 智能代理
│   └── chapter07-RAG/               # RAG 检索增强生成
└── README.md
```

## 章节介绍

### 第一章：LangChain 框架初体验
初步演示LangChain各个模块（模型对话、提示词模板、输出解析器、向量存储、RAG及Agent）的基本使用

### 第二章：模型输入输出 (Model IO)

涵盖 LangChain 中模型的基础使用方法：

1. 环境变量配置和大模型调用
2. 不同方式调用模型（同步与异步）
3. 提示词模板 (PromptTemplate 和 ChatPromptTemplate)
4. 少量示例提示词模板 (Few-shot Prompt Template)
5. 从文档中加载提示词
6. 输出解析器的使用
7. 本地大模型调用

### 第三章：链式调用 (Chain)

介绍 LangChain 核心概念之一的 Chain：

1. LCEL (LangChain Expression Language) 语法
2. 传统 LangChain 使用方式
3. 基于 LCEL 语法的新式 Chain 构建

### 第四章：记忆模块 (Memory)

讲解如何在对话中保持上下文状态：

1. 自定义实现记忆功能
2. 基础 Memory 组件使用
3. Memory 模块其他组件详解

### 第五章：工具模块 (Tools)

介绍 LangChain 中的工具系统：

1. 工具概述
2. 工具定义及使用方法

### 第六章：智能代理 (Agents)

深入探讨 Agent 的工作机制：

1. Agent 概念理解
2. 工具调用的传统方式
3. 工具调用的通用方式
4. Agent 中集成记忆组件

### 第七章：检索增强生成 (RAG)

实现知识库问答系统：

1. Retrieval 模块使用
2. 完整项目：智能对话助手

## 使用说明

参考 [conda使用指南.md](./docs/conda使用指南.md)安装所需要的依赖环境

每个章节目录下包含多个 Jupyter Notebook (.ipynb) 文件和部分 Python 脚本，按照数字顺序学习效果更佳。

## 参考资料
官网地址：https://www.langchain.com/langchain

官网文档：https://python.langchain.com/docs/introduction/

API文档：https://python.langchain.com/api_reference/

github地址：https://github.com/langchain-ai/langchain
