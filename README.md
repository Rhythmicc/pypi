# pypi

## Install

1. Get this project
    ```sh
    pip3 install Qpro -U
    git clone https://github.com/Rhythmicc/pypi.git
    cd pypi
    ```
2. edit `__init__.py` for your own use;
3. register as global Command
    ```sh
    Qpro register-global
    ```

## Usage

get help: `pypi --help`

### SubCommands

| Command  | Demo                           | Description        |
| -------- | ------------------------------ | ------------------ |
| upload   | `pypi upload -msg bala bala`   | 发布并提交到git    |
| git-push | `pypi git-push -msg bala bala` | 提交到git          |
| post     | `pypi post <path>`             | 在生产环境应用     |
| get      | `pypi get <path>`              | 获取生产环境的文件 |

### Call registered function (for Developers)

```python
app.real_call('<function name>', *args, **kwargs)
```

## Register as Global Command

1. Set `QproGlobalDir` in your environment variable, such as `/home/<user>/.local/QproGlobalDir`
2. Register this project to global: `Qpro register-global`
3. Generate Fig completion script: `Qpro gen-fig-script`
4. Generate zsh completion script: `Qpro gen-zsh-comp`

## Other Cautions

1. This project must be cloned as name `pypi`!
