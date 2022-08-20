import os
from QuickStart_Rhy import remove, dir_char
from QuickProject.Commander import Commander
from . import *

app = Commander(True)


@app.command()
def upload(msg: list):
    """
    发布并提交到git

    :param msg: 更新简要
    :return:
    """
    remove('dist')
    update_version('VERSION')
    os.system(f'{python_interpreter} setup.py sdist')
    os.system(f'twine upload dist{dir_char}*')
    app.real_call('git-push', msg)


@app.command()
def git_push(msg: list):
    """
    提交到git

    :param msg: 提交简要
    :return:
    """
    os.system('git add .')
    os.system(f'git commit -m "{" ".join(msg)}"')
    os.system('git push')
    os.system('git push gitee')


@app.command()
def post(path: str):
    """
    在开发环境应用

    :param path: 文件路径
    :return:
    """
    os.system(f'Qpro scp {path}')


@app.command()
def get(path: str):
    """
    获取开发环境的文件

    :param path: 文件路径
    :return:
    """
    os.system(f'Qpro get {path}')


if __name__ == '__main__':
    app()
