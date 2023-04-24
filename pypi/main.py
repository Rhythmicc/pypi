import os
from QuickProject import QproErrorString
from QuickProject.Commander import Commander
from . import *

app = Commander(name, True, non_complete=True)


@app.command()
def upload(msg: list):
    """
    发布并提交到git

    :param msg: 更新简要
    :return:
    """
    requirePackage("QuickStart_Rhy", "remove")("dist")
    update_version("pyproject.toml")
    with QproDefaultConsole.status("正在打包") as st:
        _st, ct = external_exec("poetry build")
        if _st != 0:
            QproDefaultConsole.print(QproErrorString, ct)
            return
        st.update("正在上传")
        _st, ct = external_exec(
            f'{python_interpreter} -m twine upload {os.path.join("dist", "*")}',
            without_output=True,
        )
        if _st != 0:
            QproDefaultConsole.print(QproErrorString, ct)
            return
    app.real_call("git-push", msg)


@app.command()
def delete(package: str = os.path.basename(os.getcwd()), version: str = None):
    """
    删除版本

    :param version: 版本号, 默认为当前版本
    :return:
    """
    if not version:
        version = get_version("pyproject.toml")
    with QproDefaultStatus("正在删除"):
        _st, ct = external_exec(
            f"{python_interpreter} -m twine delete {package}=={version}",
            without_output=True,
        )
        if _st != 0:
            QproDefaultConsole.print(QproErrorString, ct)
            return


@app.command()
def git_push(msg: list, with_version_update: bool = False):
    """
    提交到git

    :param msg: 提交简要
    :param with_version_update: 是否更新版本号
    :return:
    """
    if with_version_update:
        update_version("pyproject.toml")
    cmds = {
        "保存": f"git add .",
        "提交": f'git commit -m "{" ".join(msg)}"',
        "上传": "git push",
        "Gitee": "git push gitee",
    }
    with QproDefaultConsole.status("正在提交") as st:
        for k, v in cmds.items():
            st.update(f"正在{k}")
            _st, ct = external_exec(v, without_output=True)
            if _st != 0:
                QproDefaultConsole.print(QproErrorString, ct)
                return


@app.command()
def post(path: str):
    """
    在开发环境应用

    :param path: 文件路径
    :return:
    """
    external_exec(f"Qpro scp {path}")


@app.command()
def get(path: str):
    """
    获取开发环境的文件

    :param path: 文件路径
    :return:
    """
    external_exec(f"Qpro get {path}")


@app.command()
def update():
    """
    更新QuickProject
    """
    external_exec(f"{user_pip} install -U Qpro")
    external_exec(f"{user_pip} install -U git+https://github.com/Rhythmicc/pypi.git")


def main():
    app()


if __name__ == "__main__":
    main()
