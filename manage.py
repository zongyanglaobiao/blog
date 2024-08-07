"""
manage.py的脚本用于完成类似于hugo方面的管理工作
"""
import argparse
import os
import time

OLD_IMAGE_FILE_PATH = r"E:\Program Files (x86)\Typora\note\img"
NEW_IMAGE_FILE_PATH = r'D:\Program Files (x86)\idea\IDEAproject\github\hugo-blog\static\img'
ING_PATH = r'img/'

class Command:

    def __init__(self, shorthand_command,
                 command,
                 help_text,
                 processor=None,
                 default_value=None,
                 args_num=0):
        if default_value is None:
            default_value = []
        if default_value is None:
            default_value = []
        self.shorthand_command = shorthand_command
        self.command = command
        self.help = help_text
        self.processor = processor
        self.default_value = [] if default_value is None else default_value
        self.args_num = args_num

    def get_command(self):
        return self.command.replace('-', '')

    def handle(self, args: list[str]):
        if len(args) == 0 or self.processor is None:
            return
        self.processor(args)


def handle_command(command_list: list[Command]):
    parser = argparse.ArgumentParser(description='hugo搭建博客快速小工具, 参数顺序必须与命令描述参数顺序一致')
    for com in command_list:
        parser.add_argument(com.shorthand_command, com.command, nargs="*", type=str, help=com.help)
    parsed_args = parser.parse_args()
    for command in command_list:
        com_args = getattr(parsed_args, command.get_command())
        if com_args is not None:
            print(com_args)
            if len(com_args) == command.args_num:
                command.handle(com_args)
            elif len(com_args) == 0:
                command.handle(command.default_value)
            elif len(com_args) + len(command.default_value) == command.args_num:
                command.handle(command.default_value + com_args)
            else:
                raise ValueError(
                    f'{command.get_command()}执行错误: 参数个数不对, 应该有{command.args_num}个, '
                    f'实际有{len(com_args) or len(command.default_value)}个'
                )


def create_md_file(args: list[str]):
    # args[0]是文件夹路径 args[1]是文件名，创建文件名.md文件
    md_template = f"""
    ---
title: {args[1]}
description: 自动生成
slug: {args[1]}
date: {time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())}+0000
image: 自动生成.jpg
toc: true
categories:
  - 自动生成
tags:
  - 自动生成
weight: 1
---
# 自动生成标题
    """
    # 确保文件夹路径存在，如果不存在则创建
    os.makedirs(args[0], exist_ok=True)

    # 构造文件完整路径
    file_path = os.path.join(args[0], f"{args[1]}.md")

    # 检查文件是否存在
    if os.path.exists(file_path):
        print(f'{file_path}已经存在，无需创建')
        return

    # 写入文件
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(md_template.strip())  # 使用 .strip() 移除首尾多余的换行符
    print(f'{file_path}创建成功')


if __name__ == '__main__':
    commands = [
        Command('-cm', '--create_md_file', '创建MD文件模板, 1.文件夹路径(有默认值) 2.文件名称', create_md_file,
                args_num=2),
        Command('-cd', '--copy_directory_contents',
                '把文件夹内容拷贝到另一个文件夹内容, 1.源文件夹(有默认值) 2.目标文件夹(有默认值)', None,
                default_value=[OLD_IMAGE_FILE_PATH, NEW_IMAGE_FILE_PATH], args_num=2),
        Command('-bp', '--batch_modify', '文件内容批量替换,1.文件路径 2.匹配的字符串 3.替换的字符串', None, args_num=3),
    ]
    handle_command(commands)
    print('执行完成')
