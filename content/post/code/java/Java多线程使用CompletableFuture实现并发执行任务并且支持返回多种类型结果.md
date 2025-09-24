---
title: Java多线程使用CompletableFuture实现并发执行任务并且支持返回多种类型结果
description: 使用CompletableFuture并发执行任务并且支持返回多种类型结果
# 默认url路径是title如果不写slug
slug: 对线成
date: 2025-09-24 10:46:01+0000
toc: true
categories:
  - java-category
tags:
  - 多线程
  - 并发执行
  - CompletableFuture
keywords:
  - 多线程
  - 并发执行
  - CompletableFuture
id: d0283eb7-54b7-466d-9adb-b9def8fadab3
comments: true
---

## 多任务并发执行 & 返回多种类型结果

最近在写物料系统发现需要大量的计算，需要查很多表收集数据为了优化接口响应速度，初步使用多线程来解决，因为我发现很多计算前需要收集的数据是没有关联的可以并发查询，但是后面又发现返回的数据类型不一致
不能通过泛型直接统一返回所以封装如下工具类：可以多个任务并发执行并且返回**多种类型结果**也可以**同类型多任务**并发执行，并做了异常处理支持。可以复制直接使用
    
**多线程任务执行工具类**,注意最后需要等待所有任务结束才能继续走业务代码

```java
/**
 * 多线程任务工具类
 * @author jamesaks
 * @since 2025/9/13
 */
public final class TaskRunnerUtils {

    public static TaskResults runTasksAndCollect(List<Supplier<?>> tasks) {
        return runTasksAndCollect(tasks, true);
    }

    /**
     * 并行执行多类型任务
     *
     * @param tasks            任务列表
     * @param isThrowException 有异常时是否抛出异常 true抛出
     */
    public static TaskResults runTasksAndCollect(List<Supplier<?>> tasks, boolean isThrowException) {
        checkIsEmpty(tasks);

        //构建任务
        List<CompletableFuture<TaskResults.TaskResult>> taskFutureList = tasks
                .stream()
                .map(task -> CompletableFuture
                        .supplyAsync(task)
                        //以下两行代码可以使用 handle
                        .thenApply(TaskResults.TaskResult::success)
                        .exceptionally(throwable -> {
                            if (isThrowException) {
                                throw new CompletionException(throwable.getCause());
                            }
                            return TaskResults.TaskResult.failure(throwable);
                        })
                )
                .toList();

        try {
            //堵塞等待所有任务执行完成
            CompletableFuture.allOf(taskFutureList.toArray(new CompletableFuture[0])).join();
            //获取结果
            return new TaskResults(taskFutureList.stream().map(CompletableFuture::join).toList());
        } catch (Exception e) {
            Throwable cause = e.getCause();
            //运行时异常直接抛出
            if (cause instanceof RuntimeException runtimeException) {
                throw runtimeException;
            }
            //包装异常
            throw new RuntimeException(e.getCause());
        }
    }

    /**
     * 并行执行多个任务
     */
    public static <T> List<T> runTask(List<Supplier<T>> tasks) {
        checkIsEmpty(tasks);

        //构建任务
        List<CompletableFuture<T>> taskFutureList = tasks
                .stream()
                .map(CompletableFuture::supplyAsync)
                .toList();

        try {
            //堵塞等待所有任务执行完成
            CompletableFuture.allOf(taskFutureList.toArray(new CompletableFuture[0])).join();
            //获取结果
            return taskFutureList.stream().map(CompletableFuture::join).toList();
        } catch (CompletionException e) {
            Throwable cause = e.getCause();
            //运行时异常直接抛出
            if (cause instanceof RuntimeException runtimeException) {
                throw runtimeException;
            }
            //包装异常
            throw new RuntimeException(e.getCause());
        }
    }

    private static void checkIsEmpty(List<?> list) {
        if (list == null || list.isEmpty()) {
            throw new IllegalArgumentException("list is empty");
        }
    }
}
```

**任务结果**

```java
/**
 * 任务结果集合包装类
 * @author jamesaks
 * @since 2025/9/22
 */
public record TaskResults(List<TaskResult> results) {
    /**
     * 获取所有任务结果，包括失败
     */
    public List<TaskResult> all() {
        return results;
    }

    /**
     * 获取指定类型的任务结果, 不包括失败任务
     */
    public <T> List<T> getValues(Class<T> type) {
        return results.parallelStream()
                .filter(TaskResult::isSuccess)
                .flatMap(r -> {
                    Object value = r.value;
                    if (value == null) {
                        return Stream.empty();
                    }
                    // 如果本身就是 List
                    if (value instanceof Collection<?> list) {
                        return list.stream()
                                .filter(Objects::nonNull)
                                .filter(type::isInstance)
                                .map(type::cast);
                    }
                    // 单个值
                    if (type.isInstance(value)) {
                        return Stream.of(type.cast(value));
                    }
                    return Stream.empty();
                })
                .toList();
    }

    /**
     * 获取所有失败的任务
     */
    public List<TaskResult> failures() {
        return results.stream()
                .filter(r -> !r.isSuccess())
                .toList();
    }

    /**
     * 获取所有成功的任务
     */
    public List<TaskResult> successes() {
        return results.stream()
                .filter(r -> !r.isSuccess())
                .toList();
    }

    /**
     * 任务执行结果包装类
     *
     * @param value 任务结果
     * @param error 任务异常
     */
    public record TaskResult(Object value, Throwable error) {
        public static TaskResult success(Object value) {
            return new TaskResult(value, null);
        }

        public static TaskResult failure(Throwable error) {
            return new TaskResult(null, error);
        }

        public boolean isSuccess() {
            return error == null;
        }
    }
}
```

### 调用示例

**多任务同类型结果**

```java
public static void main(String[] args) throws InterruptedException {
        Supplier<String> task1 = ()  -> {
            System.out.println(Thread.currentThread().getName() + "task1");
            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                throw new RuntimeException(e);
            }
            return "task1";
        };

        Supplier<String> task2 = ()  -> {
            System.out.println(Thread.currentThread().getName() + "task2");
            return "task2";
        };

        List<String> strings = TaskRunnerUtils.runTask(List.of(task1, task2));
        System.out.println(strings);
}

//输出
//ForkJoinPool.commonPool-worker-2task2
//ForkJoinPool.commonPool-worker-1task1
//[task1, task2]
```

**多任务不同类型结果**

```java
public static void main(String[] args) throws InterruptedException {
        //字符串类型
        Supplier<String> task1 = ()  -> {
            System.out.println(Thread.currentThread().getName() + "task1");
            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                throw new RuntimeException(e);
            }
            return "task1";
        };
        
        //数值类型
        Supplier<Integer> task2 = ()  -> {
            System.out.println(Thread.currentThread().getName() + "task2");
            return 1;
        };
        
        //集合类型
        Supplier<List<String>> task3 = ()  -> {
            System.out.println(Thread.currentThread().getName() + "task3");
            return List.of("task3-multi-1", "task3-multi-2");
        };

        TaskResults taskResults = TaskRunnerUtils.runTasksAndCollect(List.of(task1, task2,task3));
        System.out.println(taskResults.getValues(String.class));
        System.out.println(taskResults.getValues(Integer.class));
}

//输出
//ForkJoinPool.commonPool-worker-1task1
//ForkJoinPool.commonPool-worker-2task2
//ForkJoinPool.commonPool-worker-3task3
//[task1, task3-multi-1, task3-multi-2]
//[1]
```

## CompletableFuture
以上工具类使用到CompletableFuture
> `CompletableFuture`，它针对`Future`做了改进，可以传入回调对象，当异步任务完成或者发生异常时，自动调用回调对象的回调方法。
> - `xxx()`：表示该方法将继续在已有的线程中执行；
> - `xxxAsync()`：表示将异步在线程池中执行

### 常用API

#### supplyAsync

创建一个异步任务，并返回一个`CompletableFuture`对象，该对象表示异步任务的结果。类似 Runnable

#### anyOf & allOf

处理多个异步任务的组合操作

- `anyOf`：当任意一个任务完成时即触发完成状态，返回最先完成任务的结果

- `allOf`：需要等待所有任务都完成才会触发完成状态，返回 `Void` 类型，不包含具体结果值

#### thenApply && thenApplyAsync

任务串行执行

- `thenApply` 表示当前任务执行完毕后，把结果交给下一个函数来处理（同步执行），它会在调用它的线程里继续执行（通常是前一个任务运行的线程）
- `thenApplyAsync` 表示当前任务执行完毕后，把结果交给下一个函数来处理（异步执行）。它会在线程池里调度新的线程来执行

```java
public static void main(String[] args) throws Exception {
    // 第一个任务:
    CompletableFuture<String> cfQuery = CompletableFuture.supplyAsync(() -> {
        return queryCode("中国石油");
    });
    // cfQuery成功后继续执行下一个任务:
    CompletableFuture<Double> cfFetch = cfQuery.thenApplyAsync((code) -> {
        return fetchPrice(code);
    });
    // cfFetch成功后打印结果:
    cfFetch.thenAccept((result) -> {
        System.out.println("price: " + result);
    });
    // 主线程不要立刻结束，否则CompletableFuture默认使用的线程池会立刻关闭:
    Thread.sleep(2000);
}

static String queryCode(String name) {
    try {
        Thread.sleep(100);
    } catch (InterruptedException e) {
    }
    return "601857";
}

static Double fetchPrice(String code) {
    try {
        Thread.sleep(100);
    } catch (InterruptedException e) {
    }
    return 5 + Math.random() * 20;
}
```

####  exceptionally & exceptionallyAsync

- `exceptionally`：表示当前任务执行过程中发生异常时，把异常信息交给下一个函数来处理（同步执行），它会在调用它的线程里继续执行（通常是前任务运行的线程）
- `exceptionallyAsync`：表示当前任务执行过程中发生异常时，把异常信息交给下一个函数来处理（异步执行）。它会在线程池里调度新的线程来执行

#### thenAcceptAsync 

- `thenAcceptAsync` 方法用于处理任务执行结果，但是不返回新的结果。

#### handle & handleAsync

- `handle` 方法用于处理任务执行结果，并且返回新的结果。(同步通常是前任务运行线程)
- `handleAsync` 方法用于处理任务执行结果，并且返回新的结果。 (异步是在线程池中调度新的线程来执行)

```java
CompletableFuture<String> f = CompletableFuture.supplyAsync(() -> {
    throw new RuntimeException("Boom");
}).handle((result, ex) -> {
    if (ex != null) return "Recovered";
    return result;
});

System.out.println(f.join()); // Recovered
``` 