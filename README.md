# pypi

## Install

1. Get this project
   ```sh
   pip3 install git+https://github.com/Rhythmicc/pypi.git -U
   pip3 install git+https://gitee.com/RhythmLian/pypi.git -U
   ```

## Usage

get help: `pypi --help`

### SubCommands

| Command  | Demo                           | Description        |
| -------- | ------------------------------ | ------------------ |
| upload   | `pypi upload -msg bala bala`   | 发布并提交到 git   |
| git-push | `pypi git-push -msg bala bala` | 提交到 git         |
| post     | `pypi post <path>`             | 在生产环境应用     |
| get      | `pypi get <path>`              | 获取生产环境的文件 |

### Call registered function (for Developers)

```python
app.real_call('<function name>', *args, **kwargs)
```
