python_interpreter = 'python3'


def update_version(version_filepath: str):
    """
    自定义更新版本号函数: 读取版本号 -> 更新版本号 -> 写入版本号
    
    :param version_filepath: 版本文件路径
    :return:
    """
    with open(version_filepath, 'r') as f:
        version = f.read().strip().split('.')
        version = [int(i) for i in version]
        version[-1] += 1
    with open(version_filepath, 'w') as f:
        f.write('.'.join([str(i) for i in version]))
