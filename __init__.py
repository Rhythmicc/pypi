python_interpreter = 'python3'


def update_version(version_filepath: str):
    """
    自定义更新版本号函数: 读取版本号 -> 更新版本号 -> 写入版本号
    
    :param version_filepath: 版本文件路径
    :return:
    """
    with open(version_filepath, 'r') as f:
        lines = f.readlines()
    with open(version_filepath, 'w') as f:
        for line in lines:
            line = line.strip('\n')
            _line = line.strip()
            if _line.startswith('VERSION'):
                version = [int(i) for i in line.split('=')[1].strip().strip("'").strip('"').split('.')]
                version[-1] += 1
                print(f'VERSION = "{".".join([str(i) for i in version])}"', file=f)
            else:
                print(line, file=f)


default_custom_command_template = \
    """const completionSpec: Fig.Spec = __CUSTOM_COMMAND_SPEC__;
export default completionSpec;
"""

zsh_comp_template = """#compdef __proj_name__

local cur prev
cur=${words[CURRENT]}
prev=${words[CURRENT-1]}

(( $+functions[___proj_name___args_comp] )) || 
___proj_name___args_comp() {
    local -a opt_args
    __sub_commands_args__
    _describe subcommand opt_args
}

(( $+functions[___proj_name___main] )) || 
___proj_name___main() {
    local -a args
    args=(
        __sub_commands__
    )

    _describe -t common-commands 'common commands' args && _ret=0
}

if (( ${#words} >= 3 )); then
    ___proj_name___args_comp
else
    ___proj_name___main
fi
"""

zsh_file_comp1 = """
else
    _arguments -S -s '*:filename:_files'
    return
fi
"""
zsh_file_comp2 = """
_arguments -S -s '*:filename:_files'
return
"""