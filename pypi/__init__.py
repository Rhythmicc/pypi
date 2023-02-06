# -*- coding: utf-8 -*-

name = "pypi"

from .__config__ import *

config: pypiConfig = None
if enable_config:
    config = pypiConfig()

import sys
from QuickProject import (
    user_pip,
    _ask,
    external_exec,
    QproDefaultStatus,
    QproErrorString,
)


def requirePackage(
    pname: str,
    module: str = "",
    real_name: str = "",
    not_exit: bool = True,
    not_ask: bool = False,
    set_pip: str = user_pip,
):
    """
    获取本机上的python第三方库

    :param pname: 库名
    :param module: 待引入的模块名，可缺省
    :param real_name: 用于 pip3 install 的名字
    :param not_exit: 安装后不退出
    :param not_ask: 不询问
    :param set_pip: pip3的路径
    :return: 库或模块的地址
    """
    try:
        exec(f"from {pname} import {module}" if module else f"import {pname}")
    except (ModuleNotFoundError, ImportError):
        if not_ask:
            return None
        if _ask(
            {
                "type": "confirm",
                "message": f"""{name} require {pname + (' -> ' + module if module else '')}, confirm to install?"""
                if user_lang != "zh"
                else f"""{name} 依赖 {pname + (' -> ' + module if module else '')}，确认安装吗？""",
                "default": True,
            }
        ):
            with QproDefaultStatus(
                f"Installing {pname if not real_name else real_name}"
                if user_lang != "zh"
                else f"正在安装 {pname if not real_name else real_name}"
            ):
                st, _ = external_exec(
                    f"{set_pip} install {pname if not real_name else real_name} -U",
                    True,
                )
            if st:
                QproDefaultConsole.print(
                    QproErrorString,
                    f"Install {pname + (' -> ' + module if module else '')} failed, please install it manually: "
                    if user_lang != "zh"
                    else f"安装 {pname + (' -> ' + module if module else '')} 失败，请手动安装: ",
                    f"'{set_pip} install {pname if not real_name else real_name} -U'",
                )
                exit(-1)
            if not_exit:
                exec(f"from {pname} import {module}" if module else f"import {pname}")
            else:
                QproDefaultConsole.print(
                    QproInfoString,
                    "Install complete! Run again:"
                    if user_lang != "zh"
                    else f"安装完成！再次运行:",
                    " ".join(sys.argv),
                )
                exit(0)
        else:
            exit(-1)
    return eval(f"{module if module else pname}")


def update_version(version_filepath: str):
    """
    自定义更新版本号函数: 读取版本号 -> 更新版本号 -> 写入版本号

    :param version_filepath: 版本文件路径
    :return:
    """
    with open(version_filepath, "r") as f:
        lines = f.readlines()
    with open(version_filepath, "w") as f:
        for line in lines:
            line = line.strip("\n")
            _line = line.strip()
            if _line.startswith("VERSION"):
                version = [
                    int(i)
                    for i in line.split("=")[1].strip().strip("'").strip('"').split(".")
                ]
                version[-1] += 1
                print(f'VERSION = "{".".join([str(i) for i in version])}"', file=f)
            else:
                print(line, file=f)


def get_version(version_filepath: str) -> str:
    """
    自定义获取版本号函数: 读取版本号

    :param version_filepath: 版本文件路径
    :return: 版本号
    """
    with open(version_filepath, "r") as f:
        lines = f.readlines()
    for line in lines:
        line = line.strip("\n").strip()
        if line.startswith("VERSION"):
            return line.split("=")[1].strip().strip("'").strip('"')
    return None
