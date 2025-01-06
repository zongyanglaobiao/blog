---
title: Java的Stream中的坑 - Peek
description: Stream API 的peek执行次数跟什么有关系？
# 默认url路径是title如果不写slug
slug: Java
date: 2025-01-06 10:31:36+0000
categories:
  - java-category
keywords:
  - Java
  - Stream
id: 9f4de719-7805-424f-995f-b684371e8d83
---

# Java的Stream中坑 - Peek

以下代码会输出什么结果？

```java
public static void main(String[] args) {
    Optional<Integer> first = Stream.of(1, 2, 3).filter(t -> t > 1).peek(System.out::println).findFirst();
    System.out.println(first.orElse(null));
}
```

我相信大部分人认为是如下结果
```text
2
3
2
```
**实际是**
```text
2
2
```

## 原因
peek 执行的次数取决于流的消费，而流的消费由终端操作（findFirst()）触发。具体来说：

**惰性求值和短路操作：**
findFirst() 是一个短路操作，它会找到第一个符合条件的元素后立即终止流的遍历。
因为流是惰性求值的，所以在执行 filter 和 peek 时，这些操作本身并不会立即执行，只有在遇到终端操作（如 findFirst()）时，流才会被实际消费。

**findFirst() 触发流消费：**
findFirst() 会找到第一个符合条件的元素 2，然后流停止遍历，这时 peek 才会执行。
由于 peek 是在元素通过 filter 后触发的，它会打印出第一个符合条件的元素 2，然后流被短路，停止处理后续元素，所以只打印了一次。

**peek 执行的次数取决于：** 

- peek 执行的次数取决于流中的元素个数和流是否被消费（由终端操作触发）。
- 如果流中有多个元素，而终端操作如 findFirst() 会在找到第一个符合条件的元素时停止，peek 只会执行一次，打印出第一个符合条件的元素。



