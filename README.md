# pypi

## Install

```sh
pip3 install Qpro -U
```

## Usage

get help: `qrun --help`

### SubCommands

1. `hello`: `qrun hello <yourname>` -> `hello <yourname>!`

### Call registered function

```python
app.real_call('<function name>', *args, **kwargs)
```

## Register as Global Command

1. Set `QproGlobalDir` in your environment variable, such as `/home/<user>/.local/QproGlobalDir`
2. Register this project to global: `Qpro register-global`
3. Generate Fig completion script: `Qpro gen-fig-script`
4. Generate zsh completion script: `Qpro gen-zsh-comp`
