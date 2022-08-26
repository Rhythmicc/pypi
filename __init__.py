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

