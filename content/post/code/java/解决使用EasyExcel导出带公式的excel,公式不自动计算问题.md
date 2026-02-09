---
title: 使用EasyExcel导出带公式的excel
description: EasyExcel 导出带公式的excel，打开显示公式字符串而不是对应值
# 默认url路径是title如果不写slug
slug: export excel
date: 2025-11-06 16:45:01+0000
# 是否生成目录
toc: true
categories:
  - java-category
tags:
  - EasyExcel
keywords:
  - EasyExcel
  - FastExcel
  - 带公式导出excel
id: 0820f77b-5e9a-4733-b3bc-c870ee363f2f
# 是否可以添加评论
comments: true
---

## 解决使用EasyExcel导出带公式的Excel,公式不自动计算问题

使用EasyExcel导出带公式的 Excel 打开后发现显示的字符串而不是计算后的值，需要点击被引用的列，公式才会自动计算。说实话这不算是
Bug 更多是我写法有问题，原因就是封装Excel导出模板，`这个模板把每一格数据类型统一改为了String，导致公式无法自动计算、、计算。`
。所以当你遇到这种问题检查一下导出的数据格式是否正确

EasyExcel / FastExcel版本

```xml
<!-- fastExcel工具 -->
<dependency>
    <groupId>cn.idev.excel</groupId>
    <artifactId>fastexcel</artifactId>
    <version>1.2.0</version> <!-- Use the latest version -->
</dependency>
```

**特别说明:** 我不是基于 EasyExcel 的注解形式导出的，因为导出的数据以及布局比较定制化且复杂。想看注解的可以走了，以下内容不是基于注解的

**测试类:** 经过我实际使用测试发现带公式导出，只需要做**两步**，在官网或者github看到类似问题解决方法都是调用以下API，最终发现调没调用都不影响

1. `setForceFormulaRecalculation(true)`: 强行计算公式
2. `evaluateAll()`: 计算所有公式

### 第一步：实现CellWriteHandler接口

实现接口之后，并注册到`ExcelWriterBuilder`中详细代码在最后，这里只给出关键代码

```java
//表格格式设置为计算类型
cell.setCellFormula();
```

### 第二步：设置数值类型

```java
//这一步没有的话，导出的数据类型都是 String ，只有数值类型公式才会自动计算
//Tip: 其实FastExcel 支持输入 Object 但是业务需求常常需要对输出进行处理所以我这里统一使用 String
//但是我想说的时候如果公式没自动自动计算有可能是你的类型没识别成数值类型
cell.setCellValue(Integer.parseInt(cell.getStringCellValue()));
```

## 完整测试代码

```java
/**
 * 测试导出 excel
 * @author jamesaks
 * @since 2025/10/25
 */
@Slf4j
@SpringBootTest(classes = MaterialApplication.class)
public class TestExportExcelStyle {

    public void reportExport(ExcelTemplate template) {
        // 2. 文件路径
        String filePath = "/Users/jamesaks/Downloads/excel-test/" + System.currentTimeMillis() + ".xlsx";
        File file = new File(filePath);
        if (!file.getParentFile().exists()) {
            boolean mkdirSuccess = file.getParentFile().mkdirs();
            if (!mkdirSuccess) {
                throw new RuntimeException("创建目录失败");
            }
        }

        // 3. 写文件（注册样式）
        try (ExcelWriter writer = EasyExcel.write(file).build()) {
            // 1. 检查数据
            template.checkIsEmpty();

            //写入
            WriteSheet sheet = template
                    .getSheetBuilder(EasyExcel.writerSheet(template.sheetName()))
                    .useDefaultStyle(false)
                    .needHead(true)
                    .head(template.getHead())
                    .build();

            //区分 Table 和 sheet 概念
            writer.write(template.getBody(), sheet);
        }
    }

    @Test
    void exportExcel() {
        reportExport(new ExcelTemplate() {
            @Override
            public String sheetName() {
                return "测试";
            }

            @Override
            public List<List<ExcelCell>> rows() {
                //外层为一行
                //内层为每行的列数
                return List.of(
                        List.of(new ExcelCell(3), new ExcelCell(4), new ExcelCell("=SUM(A2:B2)"), new ExcelCell("=A2-B2")),
                        List.of(new ExcelCell(100), new ExcelCell(200), new ExcelCell("=SUM(A3:B3)"), new ExcelCell("=A3-B3"))
                );
            }

            @Override
            public List<List<ExcelCell>> head() {
                //外层表达每行列数
                //内层为有几行
                return List.of(
                        List.of(new ExcelCell("数值1")),
                        List.of(new ExcelCell("数值2")),
                        List.of(new ExcelCell("相加")),
                        List.of(new ExcelCell("相减"))
                );
            }

            @Override
            public ExcelWriterSheetBuilder getSheetBuilder(ExcelWriterSheetBuilder writerBuilder) {
                //实现公式自动相加的核心逻辑
                return writerBuilder.registerWriteHandler(new CellWriteHandler() {
                    @Override
                    public void afterCellDispose(WriteSheetHolder writeSheetHolder, WriteTableHolder writeTableHolder, List<WriteCellData<?>> cellDataList, Cell cell, Head head, Integer relativeRowIndex, Boolean isHead) {
                        if (!isHead && CellType.STRING.equals(cell.getCellType()) && cell.getStringCellValue().contains("=")) {
                            cell.setCellFormula(cell.getStringCellValue().substring(1));
                        }

                        if (StrUtil.isNumeric(cell.getStringCellValue())) {
                            //将字符串转为数值类型
                            cell.setCellValue(Integer.parseInt(cell.getStringCellValue()));
                        }
                    }
                });
            }
        });
        log.info("生成成功");
    }
}    
```

**Excel导出模板接口**

```java
/**
 * Excel 导出模板接口
 *
 * @author jamesaks
 * @see ExportServiceImpl#reportExport(String, ExcelTemplate)
 * @since 2025/10/9
 */
public interface ExcelTemplate {
    /**
     * 获取 sheet 名称
     *
     * @return sheet名称
     */
    String sheetName();

    /**
     * 除了head之外的数据 rows 外层的 List 代表一行数据，里面的List 代表每行的每列数据
     * {@link cn.idev.excel.ExcelWriter#write(Collection, WriteSheet)}
     *
     * @return 每行数据
     */
    List<List<ExcelCell>> rows();

    /**
     * Excel 标题，外层的 List 表达每一列，里面的List 代表有多少行，决定头有几行是里面的 List 决定的
     * {@link AbstractParameterBuilder#head(List)}
     *
     * @return 标题
     */
    List<List<ExcelCell>> head();

    /**
     * 获取除标题外数据
     */
    default List<List<String>> getBody() {
        //有序合并
        return rows().stream()
                .map(list -> list.stream().map(ExcelCell::getValue).toList())
                .toList();
    }

    /**
     * 获取excel头
     */
    default List<List<String>> getHead() {
        //有序合并
        return head().stream()
                .map(list -> list.stream().map(ExcelCell::getValue).toList())
                .toList();
    }

    /**
     * sheet 构建者，样式相关的可以在这设置，不是复杂样式使用excelStyle即可，不使用 easy excel 默认样式则需要重写这个
     */
    default ExcelWriterSheetBuilder getSheetBuilder(ExcelWriterSheetBuilder writerBuilder) {
        return writerBuilder.registerWriteHandler(getExcelStyle());
    }

    /**
     * 获取样式
     */
    default WriteHandler getExcelStyle() {
        if (excelStyle() != null) {
            return excelStyle();
        }
        return defaultStyle();
    }

    default void checkIsEmpty() {
        if (rows() == null || rows().isEmpty()) {
            throw new BusinessException(BusinessErrorCode.ERROR, "Excel列数据不存在");
        }

        if (head() == null || head().isEmpty()) {
            throw new BusinessException(BusinessErrorCode.ERROR, "Excel标题数据不存在");
        }
    }

    /**
     * 子类选择是否重写，不重写使用默认的样式
     */
    default WriteHandler excelStyle() {
        return null;
    }

    /**
     * 默认样式
     */
    private WriteHandler defaultStyle() {
        //创建 EasyExcel 写样式（头/内容：不换行，字体 12，居中）
        WriteCellStyle headStyle = new WriteCellStyle();
        WriteFont headFont = new WriteFont();
        headFont.setFontHeightInPoints((short) 12);
        headStyle.setWriteFont(headFont);
        headStyle.setWrapped(false);
        headStyle.setHorizontalAlignment(HorizontalAlignment.CENTER);
        headStyle.setVerticalAlignment(VerticalAlignment.CENTER);

        WriteCellStyle contentStyle = new WriteCellStyle();
        WriteFont contentFont = new WriteFont();
        contentFont.setFontHeightInPoints((short) 12);
        contentStyle.setWriteFont(contentFont);
        // 关键：不自动换行
        contentStyle.setWrapped(false);
        contentStyle.setHorizontalAlignment(HorizontalAlignment.CENTER);
        contentStyle.setVerticalAlignment(VerticalAlignment.CENTER);
        return new HorizontalCellStyleStrategy(headStyle, contentStyle);
    }

    /**
     * Excel 每一格
     */
    @Builder
    @NoArgsConstructor
    @AllArgsConstructor
    @Data
    class ExcelCell {

        private static final String EMPTY = "";

        /**
         * 一格的数据，为多个表示这一格有多行
         */
        private List<Object> cellValues;

        private boolean useSafeConvert = true;

        public ExcelCell(Object... values) {
            if (values.length == 0) {
                throw new BusinessException(BusinessErrorCode.ERROR, "Excel列数据不能为空");
            }
            this.cellValues = Arrays.stream(values).toList();
        }

        public ExcelCell(Object value, boolean useSafeConvert) {
            this(List.of(Objects.isNull(value) ? EMPTY : value), useSafeConvert);
        }

        /**
         * 转为字符串
         * 目前只考虑一格只有一行的情况
         */
        public String getValue() {
            //转为字符串
            return cellValues.stream().map(this::safeConvertString).findFirst().orElse(EMPTY);
        }

        public String safeConvertString(Object s) {
            if (!useSafeConvert) {
                return Objects.toString(s);
            }

            if (s == null) {
                return EMPTY;
            }

            if (s instanceof String str && StrUtil.isBlank(str)) {
                return EMPTY;
            }

            // 0 转为 "0"
            if (s instanceof Number num && num.intValue() == 0) {
                return "0";
            }

            //double去掉小数点
            if (s instanceof Double d && d.intValue() == d) {
                return String.valueOf(d.intValue());
            }

            // 把 NULL_STR 文本变为空
            if ("null".equals(s)) {
                return EMPTY;
            }
            return s.toString();
        }

        /**
         * 返回空格子在 excel 中就是这个格没有展示如何内容
         */
        public static ExcelCell empty() {
            return new ExcelCell(EMPTY);
        }
    }
}
```