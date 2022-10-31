const completionSpec: Fig.Spec = {
    "name": "pypi",
    "description": "pypi",
    "subcommands": [
        {
            "name": "--help",
            "description": "获取帮助",
            "options": [
                {
                    "name": "--hidden",
                    "description": "显示隐藏命令"
                }
            ]
        },
        {
            "name": "complete",
            "description": "获取补全列表",
            "args": [],
            "options": [
                {
                    "name": "--team",
                    "description": "团队名",
                    "isOptional": true,
                    "args": {
                        "name": "team",
                        "description": "团队名"
                    }
                },
                {
                    "name": "--token",
                    "description": "团队token",
                    "isOptional": true,
                    "args": {
                        "name": "token",
                        "description": "团队token"
                    }
                },
                {
                    "name": "--is_script",
                    "description": "是否为脚本"
                }
            ]
        },
        {
            "name": "upload",
            "description": "发布并提交到git",
            "args": [],
            "options": [
                {
                    "name": "-msg",
                    "description": "更新简要",
                    "args": {
                        "name": "msg",
                        "description": "更新简要",
                        "isVariadic": true
                    }
                }
            ]
        },
        {
            "name": "git-push",
            "description": "提交到git",
            "args": [],
            "options": [
                {
                    "name": "-msg",
                    "description": "提交简要",
                    "args": {
                        "name": "msg",
                        "description": "提交简要",
                        "isVariadic": true
                    }
                },
                {
                    "name": "--with_version_update",
                    "description": "是否更新版本号"
                }
            ]
        },
        {
            "name": "post",
            "description": "在开发环境应用",
            "args": [
                {
                    "name": "path",
                    "description": "文件路径",
                    "template": [
                        "filepaths",
                        "folders"
                    ]
                }
            ],
            "options": []
        },
        {
            "name": "get",
            "description": "获取开发环境的文件",
            "args": [
                {
                    "name": "path",
                    "description": "文件路径",
                    "template": [
                        "filepaths",
                        "folders"
                    ]
                }
            ],
            "options": []
        },
        {
            "name": "update",
            "description": "更新QuickProject",
            "args": [],
            "options": []
        }
    ]
};
export default completionSpec;
