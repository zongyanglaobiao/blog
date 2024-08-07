"""
manage.py的脚本用于完成类似于hugo方面的管理工作
"""
import argparse

OLD_IMAGE_FILE_PATH = '1'
NEW_IMAGE_FILE_PATH = '2'


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
        print(args)


def handle_command(command_list: list[Command]):
    parser = argparse.ArgumentParser()
    for com in command_list:
        parser.add_argument(com.shorthand_command, com.command, nargs="*", type=str, help=com.help)

    for command in command_list:
        com_args = getattr(parser.parse_args(), command.get_command())
        if com_args is not None:
            if len(com_args) == command.args_num:
                command.handle(com_args)
            elif len(com_args) != command.args_num and len(command.default_value) == command.args_num:
                command.handle(command.default_value)
            else:
                raise ValueError(
                    f'{command.get_command()}执行错误: 参数个数不对 , 应该有{command.args_num}个 , 实际有{len(com_args)}个'
                )


if __name__ == '__main__':
    commands = [
        Command('-cmf', '--create_md_file', '创建MD文件模板', None, args_num=1),
        Command('-cd', '--copy_directory', '把某个文件夹拷贝到另一个文件夹', None,
                default_value=[OLD_IMAGE_FILE_PATH, NEW_IMAGE_FILE_PATH], args_num=2),
        Command('-min', '--modify_image_name', '修改图片名字', None),
    ]
    handle_command(commands)
