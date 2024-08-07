"""
manage.py的脚本用于完成类似于hugo方面的管理工作
"""
import argparse
import os
import re
import shutil
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
            if len(com_args) == command.args_num:
                command.handle(com_args)
            elif len(com_args) == 0:
                if len(command.default_value) == 0:
                    raise ValueError(f'{command.get_command()}执行错误: 无默认参数, 应该有{command.args_num}个, '
                                     f'实际有{len(com_args) or len(command.default_value)}个')
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


def operate_md_file_pictures_folder(args: list[str], is_delete=False):
    # args[0] 是 Markdown 文件路径
    md_file_path = args[0]

    # 读取 Markdown 文件内容
    with open(md_file_path, 'r', encoding='utf-8') as md_file:
        content = md_file.read()

    # 使用正则表达式匹配 Markdown 文件中的图片路径
    # 匹配 ![alt text](url) 格式的图片链接
    image_urls = re.findall(r'!\[.*?\]\((.*?)\)', content)

    def delete_file():
        complete_count = 0
        # 使用正则表达式匹配 Markdown 文件中的图片路径, 匹配 ![alt text](url) 格式的图片链接
        for url in image_urls:
            img_name = url.replace('\\', '/').rsplit('/', 1)[-1]
            img_file_path = os.path.join(NEW_IMAGE_FILE_PATH, img_name)

            if os.path.exists(img_file_path):
                # 文件存在，将其删除
                os.remove(img_file_path)
                complete_count += 1
            else:
                # 文件不存在，打印提示
                print(f"File does not exist: {img_file_path}")
        print(f'图片总共{len(image_urls)}个，已完成{complete_count}个')

    def copy_file():
        complete_count = 0
        # 使用正则表达式匹配 Markdown 文件中的图片路径, 匹配 ![alt text](url) 格式的图片链接
        for url in image_urls:
            img_name = url.replace('\\', '/').rsplit('/', 1)[-1]
            img_file_path = os.path.join(OLD_IMAGE_FILE_PATH, img_name)

            if os.path.exists(img_file_path):
                # 文件存在，将其复制到指定文件夹
                new_img_file_path = os.path.join(NEW_IMAGE_FILE_PATH, img_name)
                os.makedirs(NEW_IMAGE_FILE_PATH, exist_ok=True)
                shutil.copy2(img_file_path, new_img_file_path)
                complete_count += 1
            else:
                # 文件不存在，打印提示
                print(f"File does not exist: {img_file_path}")
        print(f'图片总共{len(image_urls)}个，已完成{complete_count}个')

    if not is_delete:
        copy_file()
    else:
        delete_file()


def delete_md_file_pictures_folder(args: list[str]):
    operate_md_file_pictures_folder(args, True)


def copy_md_file_pictures_folder(args: list[str]):
    operate_md_file_pictures_folder(args)


if __name__ == '__main__':
    commands = [
        Command('-cm', '--create_md_file', '创建MD文件模板, 1.文件夹路径(有默认值) 2.文件名称', create_md_file,
                args_num=2),
        Command('-cd', '--copy_directory_contents',
                '把文件夹内容拷贝到另一个文件夹内容, 1.源文件夹(有默认值) 2.目标文件夹(有默认值)', None,
                default_value=[OLD_IMAGE_FILE_PATH, NEW_IMAGE_FILE_PATH], args_num=2),
        Command('-bp', '--batch_modify', '文件内容批量替换, 1.文件路径 2.匹配的字符串 3.替换的字符串', None,
                args_num=3),
        Command('-cym', '--copy_md_file_pictures_folder', '下载MD文件中的图片到指定文件夹, 1.MD文件路径',
                copy_md_file_pictures_folder, args_num=1),
        Command('-dm', '--delete_md_file_pictures_folder', '在指定文件夹删除MD文件中的图片, 1.MD文件路径',
                delete_md_file_pictures_folder, args_num=1),
    ]
    handle_command(commands)
    print('执行完成')
