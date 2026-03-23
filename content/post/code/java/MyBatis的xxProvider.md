---
title: MyBatis的xxProvider
description: DeleteProvider、InsertProvider、SelectProvider、UpdateProvider
# 默认url路径是title如果不写slug
slug: MyBatis的xxProvider
date: 2026-03-18 15:00:45+0000
# 是否生成目录
toc: false
categories:
  - java-category
tags:
  - Mybatis-Plus
keywords:
  - Mybatis-Plus
  - DeleteProvider
  - InsertProvider
  - SelectProvider
  - UpdateProvider
id: db42fda5-e903-4aeb-b660-06152ed4d62e
# 是否可以添加评论
comments: true
---

## 使用 Mybatis 写 SQL 语句的三种方式

- XML 文件
- 注解
- 使用 xxxProvider

前两者常用也比较熟悉，最近突然看到可以通过 xxxProvider 来写 SQL 语句,之前想写一个通用的 SQL 方法需要借助原生的 template
或者 xml 来实现.现在有一种新的方式就是使用 xxxProvider。
`DeleteProvider、InsertProvider、SelectProvider、UpdateProvider`看着很多其实都是类似 XML 标签的效果，例如说被标注@SelectProvider的返回值是
int 则会报错

**注意点：**

1. **方法名：** 注解中method 方法名需要和Provider中一样
2. **传值：** Provider使用 Map 作为入参时，Mapper 层参数需要加上`@Param`，否则无法准确传值，使用普通参数则一一对应即可
3. **MetaObjectHandler：** 执行的 SQL 不再经过 MetaObjectHandler 的处理

```java

/**
 * 基础通用BaseMapper
 */
public interface IBaseMapper<E> extends BaseMapper<E> {

    default Class<E> getEntityClass() {
        return (Class<E>) ReflectionKit.getSuperClassGenericType(this.getClass(), BaseMapper.class, 0);
    }

    @DeleteProvider(type = Provider.class, method = "truncate")
    void truncate(String tableName);

    default void truncate() {
        truncate(getEntityClass().getAnnotation(TableName.class).value());
    }

    @SelectProvider(type = Provider.class, method = "select")
    List<E> select(String tableName);

    default List<E> select() {
        return select(getEntityClass().getAnnotation(TableName.class).value());
    }

    @InsertProvider(type = Provider.class, method = "insert")
    int insert(String tableName, String val);

    default int insert(String val) {
        return insert(getEntityClass().getAnnotation(TableName.class).value(), val);
    }

    /**
     * Provider 使用 Map 接收
     */
    @UpdateProvider(type = Provider.class, method = "update")
    int update(@Param("tableName") String tableName, @Param("col") String col, @Param("colValue") String colValue, @Param("id") String id);

    default int update(String col, String colValue, String id) {
        return update(getEntityClass().getAnnotation(TableName.class).value(), col, colValue, id);
    }

    class Provider {
        public String truncate(String tableName) {
            return "TRUNCATE TABLE %s".formatted(tableName);
        }

        public String select(String tableName) {
            return "select * from %s;".formatted(tableName);
        }

        public String insert(String tableName, String roleName) {
            return new SQL() {{
                INSERT_INTO(tableName);
                VALUES("id", "'%s'".formatted(IdWorker.getId()));
                VALUES("role_name", "'%s'".formatted(roleName));
            }}.toString();
        }

        /**
         * 特殊传参
         */
        public String update(Map<String, String> map) {
            return """
                    update %s set %s = '%s' where id = '%s' ;
                    """.formatted(map.get("tableName"), map.get("col"), map.get("colValue"), map.get("id"));
        }
    }
}
```

**测试方法**

```java

@Test
void truncate() {
    roleMapper.truncate();
    userMapper.truncate();
}

@Test
void select() {
    List<RoleEntity> select = roleMapper.select();
    System.out.println(select);
}

@Test
void insert() {
    int insert = roleMapper.insert("测试");
    System.out.println(insert);
}

@Test
void update() {
    int update = roleMapper.update("role_name", "测试111", "2036003703345229825");
    System.out.println(update);
}
```
