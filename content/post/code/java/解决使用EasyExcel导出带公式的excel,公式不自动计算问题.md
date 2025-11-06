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
        // 1. 检查数据
        template.checkIsEmpty();

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
        try (ExcelWriter writer = template.getWriterBuilder(EasyExcel.write(file)).build()) {
            WriteSheet sheet = EasyExcel.writerSheet(template.sheetName()).build();
            writer.writeContext().writeWorkbookHolder().getWorkbook().setForceFormulaRecalculation(true);

            // 写 head + rows：使用 Table 的 head 仅用于表头，实际我们写的是原始行数据
            WriteTable table = EasyExcel.writerTable(0).needHead(true).head(template.getHead()).build();
            writer.write(template.getBody(), sheet, table);
            
            //TODO 这里写不写都无所谓，不影响
            //Workbook workbook = writer.writeContext().writeWorkbookHolder().getCachedWorkbook();
            // 设置强制计算公式：不然公式会以字符串的形式显示在excel中
            //workbook.setForceFormulaRecalculation(true);
            // 新增：预计算所有公式，缓存结果值到 cell（解决显示 0 问题）
            //FormulaEvaluator formulaEvaluator = workbook.getCreationHelper().createFormulaEvaluator();
            // 计算整个 workbook 的公式，并设置 cached value
            //formulaEvaluator.evaluateAll();
        }
    }


    @Test
    void testExcel() {
        //测试excel带公式导出
        reportExport(getTemplate());
        log.info("生成成功");
    }

    private ExcelTemplate getTemplate() {
        return new ExcelTemplate() {

            @Override
            public String sheetName() {
                return "测试EXCEL";
            }

            @Override
            public List<List<ExcelCell>> rows() {
                return List.of(
                        List.of(new ExcelCell("2025-11-03"), new ExcelCell(1.0), new ExcelCell(2.0), new ExcelCell("=B2+C2")),
                        List.of(new ExcelCell("2025-11-04"), new ExcelCell(1.0), new ExcelCell(2.0), new ExcelCell("=SUM(B2,C2)")),
                        List.of(new ExcelCell("2025-11-05"), new ExcelCell(1.0), new ExcelCell(2.0), new ExcelCell("=IFERROR(B2 / 7 + C2,0)"))
                );
            }

            @Override
            public List<List<ExcelCell>> head() {
                return List.of(
                        List.of(new ExcelCell("时间")),
                        List.of(new ExcelCell("常量1")),
                        List.of(new ExcelCell("常量2")),
                        List.of(new ExcelCell("SUM"))
                );
            }

            @Override
            public ExcelWriterBuilder getWriterBuilder(ExcelWriterBuilder writerBuilder) {
                return writerBuilder.registerWriteHandler(new ExcelFormulaHandler());
            }

            private record ExcelFormulaHandler() implements CellWriteHandler {
                @Override
                public void afterCellDispose(WriteSheetHolder writeSheetHolder, WriteTableHolder writeTableHolder, List<WriteCellData<?>> cellDataList, Cell cell, Head head, Integer relativeRowIndex, Boolean isHead) {
                    if (!isHead && CellType.STRING.equals(cell.getCellType()) && cell.getStringCellValue().contains("=")) {
                        //设置计算类型，去除=
                        cell.setCellFormula(cell.getStringCellValue().substring(1));
                    }
                    
                    //筛选出数值类型的 cell
                    if (StrUtil.isNumeric(cell.getStringCellValue())) {
                        cell.setCellValue(Integer.parseInt(cell.getStringCellValue()));
                    }
                }
            }
        };
    }

}
```

**Excel导出模板接口**

```java
/**
 * Excel 导出模板
 *
 * @author jamesaks
 * @since 2025/10/9
 */
public interface ExcelTemplate {
    /**
     * 页名称
     */
    String sheetName();

    /**
     * 除了head之外的数据 rows 外层的 List 代表一行数据，里面的List 代表每行的每列数据
     */
    List<List<ExcelCell>> rows();

    /**
     * Excel 标题，外层的 List 表达每一列，里面的List 代表有多少行，决定头有几行是里面的 List 决定的
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
     * excel 构建者，样式相关的可以在这设置，不是复杂样式使用excelStyle即可，不使用 easy excel 默认样式则需要重写这个
     */
    default ExcelWriterBuilder getWriterBuilder(ExcelWriterBuilder writerBuilder) {
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
         *  一格的数据，为多个表示这一格有多行
         */
        private final List<Object> cellValues;

        private final boolean useSafeConvert = true;

        public ExcelCell(Object... values) {
            if (values.length == 0) {
                throw new BusinessException(BusinessErrorCode.ERROR, "Excel列数据不能为空");
            }
            this.cellValues = Arrays.stream(values).toList();
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

            // 0 转为 "0"
            if (s instanceof Number num && num.intValue() == 0) {
                return "0";
            }

            //double去掉小数点
            if (s instanceof Double d && d.intValue() == d) {
                return String.valueOf(d.intValue());
            }

            // 把你的 NULL_STR 文本变为空
            if ("null".equals(s)) {
                return EMPTY;
            }
            return s.toString();
        }
    }
}
```